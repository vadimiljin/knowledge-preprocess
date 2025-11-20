#!/usr/bin/env python3
"""
Automated Bilingual Meeting Transcript Processor
Transforms raw Russian+English meeting transcripts into structured markdown and knowledge graph JSON

Author: Route4Me Team
Version: 1.0.0
"""

import os
import sys
import json
import re
import argparse
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import subprocess

try:
    from anthropic import Anthropic
except ImportError:
    print("Error: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)


class Colors:
    """Terminal colors for rich output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


class TranscriptProcessor:
    """Main processor for bilingual meeting transcripts"""
    
    def __init__(self, api_key: str, dry_run: bool = False, model: str = "claude-sonnet-4-20250514"):
        self.client = Anthropic(api_key=api_key)
        self.dry_run = dry_run
        self.model = model
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.start_time = None
        
    def print_stage(self, stage: str, message: str):
        """Print colored stage message"""
        print(f"\n{Colors.BOLD}{Colors.BLUE}[{stage}]{Colors.END} {message}")
        
    def print_success(self, message: str):
        """Print success message"""
        print(f"{Colors.GREEN}✓{Colors.END} {message}")
        
    def print_warning(self, message: str):
        """Print warning message"""
        print(f"{Colors.YELLOW}⚠{Colors.END} {message}")
        
    def print_error(self, message: str):
        """Print error message"""
        print(f"{Colors.RED}✗{Colors.END} {message}")
        
    def estimate_tokens(self, text: str) -> int:
        """Rough token estimation (1 token ≈ 4 chars for mixed language)"""
        return len(text) // 3
    
    def call_claude(self, prompt: str, system_prompt: str = "", max_tokens: int = 16000) -> Tuple[str, int, int]:
        """Call Claude API with retry logic"""
        if self.dry_run:
            estimated_output = max_tokens
            estimated_input = self.estimate_tokens(prompt + system_prompt)
            return "[DRY RUN - No actual API call]", estimated_input, estimated_output
        
        retries = 3
        for attempt in range(retries):
            try:
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=max_tokens,
                    system=system_prompt if system_prompt else None,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                
                input_tokens = response.usage.input_tokens
                output_tokens = response.usage.output_tokens
                self.total_input_tokens += input_tokens
                self.total_output_tokens += output_tokens
                
                return response.content[0].text, input_tokens, output_tokens
                
            except Exception as e:
                if attempt < retries - 1:
                    wait_time = (2 ** attempt) * 2
                    self.print_warning(f"API call failed: {e}. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    raise Exception(f"API call failed after {retries} attempts: {e}")
    
    def stage1_extract_glossary(self, raw_transcript: str) -> Dict[str, List[str]]:
        """Stage 1: Extract technical terms that should not be translated"""
        self.print_stage("STAGE 1", "Extracting technical glossary from transcript...")
        
        prompt = f"""You are analyzing a meeting transcript in Russian that contains English technical terms. Your task is to identify ALL technical terms, product names, code-related terminology, and proper nouns that should be preserved in English when translating.

Categories to identify:
1. **Technical Terms**: API names, code terms, technical concepts
2. **Product Names**: Software products, tools, services
3. **Code Elements**: Variable names, function names, file names
4. **Company/Project Terms**: Internal project names, company-specific terminology
5. **Acronyms**: Technical acronyms and abbreviations

Return your analysis as a JSON object with this EXACT structure:
{{
  "technical_terms": ["term1", "term2", ...],
  "product_names": ["product1", "product2", ...],
  "code_elements": ["element1", "element2", ...],
  "company_terms": ["term1", "term2", ...],
  "acronyms": ["ABBR1", "ABBR2", ...]
}}

CRITICAL: Output ONLY valid JSON, nothing else. No markdown, no explanations, no code blocks.

Transcript to analyze:
{raw_transcript}"""

        response, in_tokens, out_tokens = self.call_claude(prompt, max_tokens=8000)
        
        print(f"  Input tokens: {in_tokens:,} | Output tokens: {out_tokens:,}")
        
        if self.dry_run:
            return {
                "technical_terms": ["example_term"],
                "product_names": ["ExampleProduct"],
                "code_elements": ["example.file"],
                "company_terms": ["ExampleProject"],
                "acronyms": ["API"]
            }
        
        # Clean response - remove markdown code blocks if present
        response = response.strip()
        if response.startswith("```"):
            response = re.sub(r'^```json?\s*|\s*```$', '', response, flags=re.MULTILINE)
        
        try:
            glossary = json.loads(response)
            total_terms = sum(len(v) for v in glossary.values())
            self.print_success(f"Extracted {total_terms} technical terms across {len(glossary)} categories")
            return glossary
        except json.JSONDecodeError as e:
            self.print_error(f"Failed to parse glossary JSON: {e}")
            self.print_warning("Using empty glossary - review output carefully!")
            return {
                "technical_terms": [],
                "product_names": [],
                "code_elements": [],
                "company_terms": [],
                "acronyms": []
            }
    
    def save_glossary(self, glossary: Dict, output_path: Path) -> Path:
        """Save glossary to editable JSON file"""
        glossary_path = output_path / "technical_terms.json"
        with open(glossary_path, 'w', encoding='utf-8') as f:
            json.dump(glossary, f, indent=2, ensure_ascii=False)
        return glossary_path
    
    def load_glossary(self, glossary_path: Path) -> Dict:
        """Load glossary from JSON file"""
        with open(glossary_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def flatten_glossary(self, glossary: Dict) -> List[str]:
        """Flatten glossary dict to list of all terms"""
        terms = []
        for category_terms in glossary.values():
            terms.extend(category_terms)
        return sorted(set(terms))  # Deduplicate and sort
    
    def stage2_translate_to_english(self, raw_transcript: str, glossary: Dict) -> str:
        """Stage 2: Translate full transcript to English preserving technical terms"""
        self.print_stage("STAGE 2", "Translating transcript to English...")
        
        flat_glossary = self.flatten_glossary(glossary)
        glossary_str = "\n".join(f"- {term}" for term in flat_glossary)
        
        system_prompt = """You are a professional translator specializing in technical content. You translate Russian text to English while preserving technical terminology exactly as specified."""
        
        prompt = f"""Translate this meeting transcript from Russian to English. 

CRITICAL RULES:
1. Translate all natural language to clear, professional English
2. Keep ALL terms from the glossary below EXACTLY as-is (no translation)
3. Preserve all timestamps, speaker names, and formatting
4. Maintain the conversational flow and tone
5. Keep proper nouns (people names) in original form

TECHNICAL TERMS TO PRESERVE (DO NOT TRANSLATE):
{glossary_str}

TRANSCRIPT TO TRANSLATE:
{raw_transcript}"""

        response, in_tokens, out_tokens = self.call_claude(prompt, system_prompt, max_tokens=16000)
        
        print(f"  Input tokens: {in_tokens:,} | Output tokens: {out_tokens:,}")
        self.print_success("Translation complete")
        
        return response
    
    def stage3_structure_english(self, translated_en: str, glossary: Dict) -> str:
        """Stage 3: Structure English translation into formatted markdown"""
        self.print_stage("STAGE 3", "Structuring English version...")
        
        flat_glossary = self.flatten_glossary(glossary)
        glossary_str = "\n".join(f"- {term}" for term in flat_glossary)
        
        system_prompt = """You are a meeting transcript structuring expert. You transform raw conversational transcripts into perfectly structured markdown documents suitable for knowledge graph ingestion."""
        
        prompt = f"""Transform this translated meeting transcript into a perfectly structured markdown document.

TECHNICAL TERMS (already in English, keep exactly):
{glossary_str}

OUTPUT FORMAT (FOLLOW EXACTLY):

# MEETING: [Clear descriptive title]
**DATE:** YYYY-MM-DD
**DURATION:** HH:MM:SS
**ATTENDEES:** Name1, Name2, Name3, ...

---

## TOPIC: [Topic Name]
**TIME:** HH:MM:SS - HH:MM:SS
**PARTICIPANTS:** Name1, Name2, Name3

### DISCUSSION
**[HH:MM:SS] Speaker Name:** Statement text goes here.

**[HH:MM:SS] Speaker Name:** Another statement.

### DECISION: [Decision Label]
**DECIDED_BY:** Name(s)
**DECISION:** Clear description of what was decided
**RATIONALE:** Why this decision was made
**ALTERNATIVES_CONSIDERED:** ["Option 1", "Option 2"] (if discussed)

### TECHNICAL_ISSUE: [Issue Label]
**[HH:MM:SS] Speaker Name:** Description of technical issue discussed

### ACTION_ITEMS
- **OWNER:** Name | **TASK:** Task description | **STATUS:** pending/in_progress/done | **PRIORITY:** high/normal/low

---

(Repeat TOPIC sections for each distinct topic)

---

## METADATA
**TOTAL_TOPICS:** N
**TOTAL_DECISIONS:** N
**TOTAL_ACTION_ITEMS:** N
**KEY_FEATURES_DISCUSSED:** Feature1, Feature2, ...
**TECHNICAL_ISSUES:** Issue1, Issue2, ...

CRITICAL RULES:
1. Identify distinct topics by semantic clustering
2. Extract explicit decisions with who decided and why
3. Extract action items with clear owners
4. Preserve ALL timestamps exactly
5. Keep technical terms from glossary exactly as-is
6. Every statement must have timestamp and speaker
7. Group related statements under appropriate topics
8. Use proper markdown headers (##, ###)
9. Keep discussion statements concise but complete

TRANSLATED TRANSCRIPT:
{translated_en}"""

        response, in_tokens, out_tokens = self.call_claude(prompt, system_prompt, max_tokens=16000)
        
        print(f"  Input tokens: {in_tokens:,} | Output tokens: {out_tokens:,}")
        self.print_success("English structuring complete")
        
        return response
    
    def stage4_structure_russian(self, raw_transcript: str, glossary: Dict) -> str:
        """Stage 4: Structure original Russian transcript preserving technical terms"""
        self.print_stage("STAGE 4", "Structuring Russian version...")
        
        flat_glossary = self.flatten_glossary(glossary)
        glossary_str = "\n".join(f"- {term}" for term in flat_glossary)
        
        system_prompt = """Вы эксперт по структурированию транскриптов встреч. Вы преобразуете сырые разговорные транскрипты в идеально структурированные markdown документы для извлечения графа знаний."""
        
        prompt = f"""Преобразуйте этот транскрипт встречи в идеально структурированный markdown документ НА РУССКОМ ЯЗЫКЕ.

ТЕХНИЧЕСКИЕ ТЕРМИНЫ (оставить на английском, НЕ ПЕРЕВОДИТЬ):
{glossary_str}

ФОРМАТ ВЫВОДА (СТРОГО СЛЕДОВАТЬ):

# MEETING: [Ясное описательное название на русском]
**DATE:** YYYY-MM-DD
**DURATION:** HH:MM:SS
**ATTENDEES:** Имя1, Имя2, Имя3, ...

---

## TOPIC: [Название темы на русском]
**TIME:** HH:MM:SS - HH:MM:SS
**PARTICIPANTS:** Имя1, Имя2, Имя3

### DISCUSSION
**[HH:MM:SS] Имя Спикера:** Текст высказывания.

**[HH:MM:SS] Имя Спикера:** Другое высказывание.

### DECISION: [Метка решения на русском]
**DECIDED_BY:** Имя(имена)
**DECISION:** Четкое описание принятого решения
**RATIONALE:** Обоснование решения
**ALTERNATIVES_CONSIDERED:** ["Вариант 1", "Вариант 2"] (если обсуждались)

### TECHNICAL_ISSUE: [Метка проблемы на русском]
**[HH:MM:SS] Имя Спикера:** Описание обсуждаемой технической проблемы

### ACTION_ITEMS
- **OWNER:** Имя | **TASK:** Описание задачи | **STATUS:** pending/in_progress/done | **PRIORITY:** high/normal/low

---

(Повторить секции TOPIC для каждой темы)

---

## METADATA
**TOTAL_TOPICS:** N
**TOTAL_DECISIONS:** N
**TOTAL_ACTION_ITEMS:** N
**KEY_FEATURES_DISCUSSED:** Функция1, Функция2, ...
**TECHNICAL_ISSUES:** Проблема1, Проблема2, ...

КРИТИЧЕСКИЕ ПРАВИЛА:
1. Определите отдельные темы по семантическому кластеризации
2. Извлеките явные решения с указанием, кто решил и почему
3. Извлеките задачи с четкими владельцами
4. Сохраните ВСЕ временные метки точно
5. Оставьте технические термины из глоссария на английском ТОЧНО как есть
6. Каждое высказывание должно иметь временную метку и спикера
7. Группируйте связанные высказывания под соответствующими темами
8. Используйте правильные markdown заголовки (##, ###)
9. Держите высказывания краткими, но полными
10. ВЕСЬ ТЕКСТ кроме технических терминов должен быть НА РУССКОМ

ОРИГИНАЛЬНЫЙ ТРАНСКРИПТ:
{raw_transcript}"""

        response, in_tokens, out_tokens = self.call_claude(prompt, system_prompt, max_tokens=16000)
        
        print(f"  Input tokens: {in_tokens:,} | Output tokens: {out_tokens:,}")
        self.print_success("Russian structuring complete")
        
        return response
    
    def stage5_parse_and_validate(self, md_path: Path, output_path: Path, language: str) -> Tuple[Dict, Dict]:
        """Stage 5: Parse markdown with existing parser and perform full validation"""
        self.print_stage("STAGE 5", f"Parsing and validating {language.upper()} version...")
        
        # Import the parser from the existing script
        sys.path.insert(0, str(Path(__file__).parent))
        try:
            from parse_meeting import MeetingParser
        except ImportError:
            self.print_error("parse_meeting.py not found in current directory!")
            return {}, {}
        
        # Parse the markdown
        parser = MeetingParser()
        try:
            graph_data = parser.parse_file(str(md_path))
            self.print_success(f"Parsed {graph_data['statistics']['total_nodes']} nodes, "
                             f"{graph_data['statistics']['total_relationships']} relationships")
        except Exception as e:
            self.print_error(f"Parsing failed: {e}")
            return {}, {}
        
        # Full structural validation
        validation_results = self.full_validation(md_path, graph_data)
        
        # Print validation summary
        passed = sum(1 for v in validation_results.values() if v['passed'])
        total = len(validation_results)
        
        if passed == total:
            self.print_success(f"All {total} validation checks passed")
        else:
            self.print_warning(f"Validation: {passed}/{total} checks passed")
            for check, result in validation_results.items():
                if not result['passed']:
                    self.print_error(f"  {check}: {result['message']}")
        
        return graph_data, validation_results
    
    def full_validation(self, md_path: Path, graph_data: Dict) -> Dict:
        """Perform full structural validation"""
        results = {}
        
        # Read markdown for structural checks
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Check 1: Meeting header exists
        results['meeting_header'] = {
            'passed': bool(re.search(r'^# MEETING:', md_content, re.MULTILINE)),
            'message': 'Meeting header present'
        }
        
        # Check 2: Required metadata fields
        required_fields = ['DATE', 'DURATION', 'ATTENDEES']
        for field in required_fields:
            results[f'metadata_{field.lower()}'] = {
                'passed': bool(re.search(rf'\*\*{field}:\*\*', md_content)),
                'message': f'{field} field present'
            }
        
        # Check 3: At least one topic
        results['has_topics'] = {
            'passed': graph_data['statistics']['node_counts']['topics'] > 0,
            'message': f"Found {graph_data['statistics']['node_counts']['topics']} topics"
        }
        
        # Check 4: Topics have required structure
        topic_pattern = r'## TOPIC:.*?\n\*\*TIME:\*\*.*?\n\*\*PARTICIPANTS:\*\*'
        topic_matches = re.findall(topic_pattern, md_content, re.DOTALL)
        results['topic_structure'] = {
            'passed': len(topic_matches) > 0,
            'message': f'{len(topic_matches)} properly structured topics'
        }
        
        # Check 5: Statements have timestamps
        all_timestamps_valid = all(
            re.match(r'\d{2}:\d{2}:\d{2}', s['timestamp']) 
            for s in graph_data['nodes']['statements']
        )
        results['timestamp_format'] = {
            'passed': all_timestamps_valid,
            'message': 'All timestamps properly formatted'
        }
        
        # Check 6: Multiple speakers
        results['speaker_count'] = {
            'passed': len(graph_data['nodes']['people']) >= 2,
            'message': f"Found {len(graph_data['nodes']['people'])} speakers"
        }
        
        # Check 7: Decisions have required fields
        decisions_valid = True
        for decision in graph_data['nodes']['decisions']:
            if not all(key in decision for key in ['decided_by', 'description', 'rationale']):
                decisions_valid = False
                break
        results['decision_fields'] = {
            'passed': decisions_valid or len(graph_data['nodes']['decisions']) == 0,
            'message': 'All decisions have required fields'
        }
        
        # Check 8: Action items have owners
        actions_have_owners = all(
            'owner_id' in action for action in graph_data['nodes']['action_items']
        )
        results['action_owners'] = {
            'passed': actions_have_owners or len(graph_data['nodes']['action_items']) == 0,
            'message': 'All action items have assigned owners'
        }
        
        # Check 9: Relationships reference valid nodes
        node_ids = set()
        for node_type, nodes in graph_data['nodes'].items():
            if isinstance(nodes, list):
                node_ids.update(n['id'] for n in nodes)
        
        relationships_valid = all(
            rel['from'] in node_ids and rel['to'] in node_ids
            for rel in graph_data['relationships']
        )
        results['relationship_integrity'] = {
            'passed': relationships_valid,
            'message': 'All relationships reference valid nodes'
        }
        
        # Check 10: METADATA section exists
        results['metadata_section'] = {
            'passed': bool(re.search(r'## METADATA', md_content)),
            'message': 'Metadata section present'
        }
        
        return results
    
    def process(self, input_path: str, output_dir: str = "./output", skip_glossary_review: bool = False) -> Dict:
        """Main processing pipeline"""
        self.start_time = time.time()
        
        # Setup paths
        input_file = Path(input_path)
        if not input_file.exists():
            self.print_error(f"Input file not found: {input_path}")
            return {}
        
        # Read input
        self.print_stage("INIT", f"Processing: {input_file.name}")
        with open(input_file, 'r', encoding='utf-8') as f:
            raw_transcript = f.read()
        
        # Estimate initial cost
        input_tokens = self.estimate_tokens(raw_transcript)
        estimated_total_output = 16000 * 4  # 4 stages with output
        estimated_cost = (input_tokens * 4 * 0.003 / 1000) + (estimated_total_output * 0.015 / 1000)
        
        print(f"  Input size: {len(raw_transcript):,} chars (~{input_tokens:,} tokens)")
        print(f"  Estimated cost: ${estimated_cost:.2f}")
        
        if self.dry_run:
            self.print_warning("DRY RUN MODE - No actual API calls will be made")
        
        # Create output directory
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        meeting_name = input_file.stem
        output_path = Path(output_dir) / f"{timestamp}_{meeting_name}"
        output_path.mkdir(parents=True, exist_ok=True)
        
        print(f"  Output directory: {output_path}")
        
        # Stage 1: Extract glossary
        glossary = self.stage1_extract_glossary(raw_transcript)
        glossary_path = self.save_glossary(glossary, output_path)
        self.print_success(f"Glossary saved to: {glossary_path}")
        
        # User review checkpoint
        if not skip_glossary_review and not self.dry_run:
            print(f"\n{Colors.BOLD}{Colors.YELLOW}USER REVIEW REQUIRED{Colors.END}")
            print(f"Review and edit technical terms in: {Colors.CYAN}{glossary_path}{Colors.END}")
            print("Press ENTER when ready to continue, or Ctrl+C to abort...")
            try:
                input()
                # Reload glossary after user edit
                glossary = self.load_glossary(glossary_path)
                self.print_success("Glossary loaded, continuing processing...")
            except KeyboardInterrupt:
                self.print_warning("\nProcessing aborted by user")
                return {}
        
        # Stage 2: Translate to English
        translated_en = self.stage2_translate_to_english(raw_transcript, glossary)
        translated_path = output_path / "translated_full_en.md"
        with open(translated_path, 'w', encoding='utf-8') as f:
            f.write(translated_en)
        self.print_success(f"Translation saved to: {translated_path}")
        
        # Stage 3: Structure English
        structured_en = self.stage3_structure_english(translated_en, glossary)
        structured_en_path = output_path / "structured_en.md"
        with open(structured_en_path, 'w', encoding='utf-8') as f:
            f.write(structured_en)
        self.print_success(f"English structure saved to: {structured_en_path}")
        
        # Stage 4: Structure Russian
        structured_ru = self.stage4_structure_russian(raw_transcript, glossary)
        structured_ru_path = output_path / "structured_ru.md"
        with open(structured_ru_path, 'w', encoding='utf-8') as f:
            f.write(structured_ru)
        self.print_success(f"Russian structure saved to: {structured_ru_path}")
        
        # Stage 5: Parse and validate both versions
        parsed_en, validation_en = self.stage5_parse_and_validate(
            structured_en_path, output_path, "english"
        )
        parsed_en_path = output_path / "parsed_en.json"
        with open(parsed_en_path, 'w', encoding='utf-8') as f:
            json.dump(parsed_en, f, indent=2, ensure_ascii=False)
        self.print_success(f"English JSON saved to: {parsed_en_path}")
        
        parsed_ru, validation_ru = self.stage5_parse_and_validate(
            structured_ru_path, output_path, "russian"
        )
        parsed_ru_path = output_path / "parsed_ru.json"
        with open(parsed_ru_path, 'w', encoding='utf-8') as f:
            json.dump(parsed_ru, f, indent=2, ensure_ascii=False)
        self.print_success(f"Russian JSON saved to: {parsed_ru_path}")
        
        # Generate metadata
        elapsed_time = time.time() - self.start_time
        # Claude Sonnet 4.5 pricing: $3/1M input, $15/1M output
        input_cost = (self.total_input_tokens / 1_000_000) * 3.0
        output_cost = (self.total_output_tokens / 1_000_000) * 15.0
        total_cost = input_cost + output_cost
        
        metadata = {
            "processing_info": {
                "input_file": str(input_file),
                "timestamp": timestamp,
                "elapsed_seconds": round(elapsed_time, 2),
                "model": self.model,
                "dry_run": self.dry_run
            },
            "token_usage": {
                "total_input_tokens": self.total_input_tokens,
                "total_output_tokens": self.total_output_tokens,
                "input_cost_usd": round(input_cost, 4),
                "output_cost_usd": round(output_cost, 4),
                "total_cost_usd": round(total_cost, 4)
            },
            "glossary": {
                "total_terms": sum(len(v) for v in glossary.values()),
                "categories": {k: len(v) for k, v in glossary.items()}
            },
            "validation": {
                "english": {
                    "total_checks": len(validation_en),
                    "passed": sum(1 for v in validation_en.values() if v['passed']),
                    "details": validation_en
                },
                "russian": {
                    "total_checks": len(validation_ru),
                    "passed": sum(1 for v in validation_ru.values() if v['passed']),
                    "details": validation_ru
                }
            },
            "statistics": {
                "english": parsed_en.get('statistics', {}),
                "russian": parsed_ru.get('statistics', {})
            }
        }
        
        metadata_path = output_path / "metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        # Print final summary
        print(f"\n{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}PROCESSING COMPLETE{Colors.END}")
        print(f"{Colors.GREEN}{'='*60}{Colors.END}")
        print(f"\n📁 Output directory: {Colors.CYAN}{output_path}{Colors.END}")
        print(f"\n📄 Generated files:")
        print(f"  ├─ technical_terms.json       (Editable glossary)")
        print(f"  ├─ translated_full_en.md      (Full English translation)")
        print(f"  ├─ structured_en.md           (Structured English)")
        print(f"  ├─ structured_ru.md           (Structured Russian)")
        print(f"  ├─ parsed_en.json             (Knowledge graph JSON)")
        print(f"  ├─ parsed_ru.json             (Knowledge graph JSON)")
        print(f"  └─ metadata.json              (Processing metadata)")
        
        if not self.dry_run:
            print(f"\n💰 Cost: ${total_cost:.4f}")
            print(f"  ├─ Input tokens: {self.total_input_tokens:,} (${input_cost:.4f})")
            print(f"  └─ Output tokens: {self.total_output_tokens:,} (${output_cost:.4f})")
        
        print(f"\n⏱️  Time: {elapsed_time:.1f}s")
        
        en_stats = parsed_en.get('statistics', {}).get('node_counts', {})
        ru_stats = parsed_ru.get('statistics', {}).get('node_counts', {})
        
        print(f"\n📊 Statistics:")
        print(f"  English: {en_stats.get('topics', 0)} topics, {en_stats.get('decisions', 0)} decisions, {en_stats.get('action_items', 0)} actions")
        print(f"  Russian: {ru_stats.get('topics', 0)} topics, {ru_stats.get('decisions', 0)} decisions, {ru_stats.get('action_items', 0)} actions")
        
        return metadata


def main():
    parser = argparse.ArgumentParser(
        description='Automated Bilingual Meeting Transcript Processor',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  python transcript_processor.py meeting.md
  
  # Dry run to estimate cost
  python transcript_processor.py meeting.md --dry-run
  
  # Skip glossary review (auto-continue)
  python transcript_processor.py meeting.md --skip-review
  
  # Custom output directory
  python transcript_processor.py meeting.md -o ./processed_meetings
  
  # Use GPT-4 instead of Claude
  python transcript_processor.py meeting.md --model gpt-4-turbo-preview
        """
    )
    
    parser.add_argument('input', help='Path to raw meeting transcript (markdown)')
    parser.add_argument('-o', '--output', default='./output', 
                       help='Output directory (default: ./output)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Estimate cost without making API calls')
    parser.add_argument('--skip-review', action='store_true',
                       help='Skip glossary review checkpoint')
    parser.add_argument('--model', default='claude-sonnet-4-20250514',
                       help='Model to use (default: claude-sonnet-4-20250514)')
    parser.add_argument('--api-key', help='API key (or set ANTHROPIC_API_KEY env var)')
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print(f"{Colors.RED}Error:{Colors.END} No API key provided. Set ANTHROPIC_API_KEY environment variable or use --api-key")
        return 1
    
    # Check if parse_meeting.py exists
    if not Path('parse_meeting.py').exists():
        print(f"{Colors.RED}Error:{Colors.END} parse_meeting.py not found in current directory")
        print("Please ensure parse_meeting.py is in the same directory as this script")
        return 1
    
    # Process transcript
    try:
        processor = TranscriptProcessor(api_key, dry_run=args.dry_run, model=args.model)
        processor.process(args.input, args.output, args.skip_review)
        return 0
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Processing interrupted by user{Colors.END}")
        return 130
    except Exception as e:
        print(f"\n{Colors.RED}Error:{Colors.END} {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
