#!/usr/bin/env python3
"""
Parse business_context.md files to extract Dan's directives and business impact data.
"""

import re
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


class BusinessContextParser:
    def __init__(self, business_context_path: str, meeting_date: str):
        self.business_context_path = Path(business_context_path)
        self.meeting_date = meeting_date
        self.content = ""
        
    def parse(self) -> Dict[str, Any]:
        """Parse business_context.md and return structured JSON."""
        with open(self.business_context_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
        
        directives = self._parse_directives()
        leadership_patterns = self._parse_leadership_patterns()
        
        return {
            "metadata": {
                "processed_at": datetime.now().isoformat(),
                "source_file": str(self.business_context_path),
                "meeting_date": self.meeting_date
            },
            "nodes": {
                "directives": directives,
                "leadership_patterns": leadership_patterns
            }
        }
    
    def _parse_directives(self) -> List[Dict[str, Any]]:
        """Extract directive nodes from business context."""
        directives = []
        
        # Match directive sections: ### Directive N: Title
        directive_pattern = r'### Directive (\d+): (.+?)\n\n\*\*Timestamp:\*\* (.+?)\n\*\*Type:\*\* (.+?)\n'
        
        for match in re.finditer(directive_pattern, self.content):
            directive_num = match.group(1)
            title = match.group(2).strip()
            timestamp = match.group(3).strip()
            directive_type = match.group(4).strip()
            
            # Extract the full directive section
            start_pos = match.start()
            next_directive = re.search(r'\n### (Directive \d+|Decision Hierarchy)', self.content[start_pos + 1:])
            end_pos = start_pos + next_directive.start() if next_directive else len(self.content)
            directive_text = self.content[start_pos:end_pos]
            
            # Extract key fields
            authority_level = self._extract_field(directive_text, r'\*\*Authority Level:\*\* (.+?)$')
            urgency = self._extract_field(directive_text, r'\*\*Urgency:\*\* (.+?)$')
            assigned_to = self._extract_field(directive_text, r'\*\*Assigned To:\*\* (.+?)$')
            deadline = self._extract_field(directive_text, r'\*\*Deadline:\*\* (.+?)$')
            business_impact = self._extract_field(directive_text, r'\*\*Business Impact:\*\* (.+?)$')
            impact_severity = self._extract_field(directive_text, r'\*\*Impact Severity:\*\* (.+?)$')
            emotion = self._extract_field(directive_text, r'\*\*Emotion:\*\* (.+?)$')
            
            # Extract issue and exact quotes
            issue_match = re.search(r'\*\*Issue:\*\* (.+?)(?=\n\n\*\*Business Impact)', directive_text, re.DOTALL)
            issue = issue_match.group(1).strip() if issue_match else ""
            
            quotes = self._extract_quotes(directive_text)
            
            directive_id = f"directive_{self.meeting_date}_{directive_num}"
            
            directives.append({
                "id": directive_id,
                "type": "Directive",
                "number": int(directive_num),
                "title": title,
                "timestamp": timestamp,
                "directive_type": directive_type,
                "authority_level": authority_level,
                "urgency": urgency,
                "assigned_to": assigned_to,
                "deadline": deadline,
                "issue": issue,
                "business_impact": business_impact,
                "impact_severity": impact_severity,
                "emotion": emotion,
                "quotes": quotes,
                "meeting_date": self.meeting_date
            })
        
        return directives
    
    def _parse_leadership_patterns(self) -> List[Dict[str, Any]]:
        """Extract leadership decision-making patterns."""
        patterns = []
        
        # Match leadership sections: ### Name - Role
        leadership_pattern = r'### (.+?) - (.+?)\n\n\*\*Decision-Making Style:\*\*'
        
        for match in re.finditer(leadership_pattern, self.content):
            name = match.group(1).strip()
            role = match.group(2).strip()
            
            # Extract the full section
            start_pos = match.start()
            next_section = re.search(r'\n### ', self.content[start_pos + 1:])
            end_pos = start_pos + next_section.start() if next_section else len(self.content)
            section_text = self.content[start_pos:end_pos]
            
            # Extract decision-making details
            takes_initiative = self._extract_list_field(section_text, r'- Takes initiative on: (.+?)$')
            seeks_approval = self._extract_list_field(section_text, r'- Seeks approval for: (.+?)$')
            authority_scope = self._extract_field(section_text, r'- Authority scope: (.+?)$')
            
            pattern_id = f"leadership_{self._normalize_id(name)}_{self.meeting_date}"
            
            patterns.append({
                "id": pattern_id,
                "type": "LeadershipPattern",
                "name": name,
                "role": role,
                "takes_initiative": takes_initiative,
                "seeks_approval": seeks_approval,
                "authority_scope": authority_scope,
                "meeting_date": self.meeting_date
            })
        
        return patterns
    
    def _extract_field(self, text: str, pattern: str) -> str:
        """Extract a single field value using regex."""
        match = re.search(pattern, text, re.MULTILINE)
        return match.group(1).strip() if match else ""
    
    def _extract_list_field(self, text: str, pattern: str) -> str:
        """Extract a list field value."""
        match = re.search(pattern, text, re.MULTILINE)
        return match.group(1).strip() if match else ""
    
    def _extract_quotes(self, text: str) -> List[str]:
        """Extract exact quotes from directive text."""
        quotes = []
        quote_pattern = r'\*\*Exact (?:Quote|Key Points):\*\*\s*\n(.+?)(?=\n\n\*\*|\Z)'
        
        match = re.search(quote_pattern, text, re.DOTALL)
        if match:
            quote_text = match.group(1).strip()
            # Extract individual quote lines
            for line in quote_text.split('\n'):
                if line.strip().startswith('- "'):
                    quote = line.strip()[3:].rstrip('"')
                    quotes.append(quote)
        
        return quotes
    
    def _normalize_id(self, text: str) -> str:
        """Normalize text for use in IDs."""
        return re.sub(r'[^a-z0-9]+', '_', text.lower()).strip('_')


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 parse_business_context.py <business_context.md> <meeting_date> [-o output.json] [--pretty]")
        print("\nExample:")
        print("  python3 parse_business_context.py 46-product-review-13-nov/business_context.md 2025-11-13 -o output.json --pretty")
        sys.exit(1)
    
    input_file = sys.argv[1]
    meeting_date = sys.argv[2]
    output_file = None
    pretty = False
    
    # Parse arguments
    i = 3
    while i < len(sys.argv):
        if sys.argv[i] == '-o' and i + 1 < len(sys.argv):
            output_file = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == '--pretty':
            pretty = True
            i += 1
        else:
            i += 1
    
    # Default output filename
    if not output_file:
        input_path = Path(input_file)
        output_file = input_path.parent / "business_context.json"
    
    # Parse the file
    parser = BusinessContextParser(input_file, meeting_date)
    result = parser.parse()
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        if pretty:
            json.dump(result, f, indent=2, ensure_ascii=False)
        else:
            json.dump(result, f, ensure_ascii=False)
    
    print(f"✓ Parsed {len(result['nodes']['directives'])} directives")
    print(f"✓ Parsed {len(result['nodes']['leadership_patterns'])} leadership patterns")
    print(f"✓ Output written to: {output_file}")


if __name__ == "__main__":
    main()