# Automated Bilingual Meeting Transcript Processor

Transforms raw Russian+English meeting transcripts into structured markdown and knowledge graph JSON using Claude AI.

## Features

- **Bilingual Processing**: Generates both English and Russian structured outputs
- **Smart Technical Term Extraction**: AI identifies technical terms to preserve
- **Editable Glossary**: Review and edit technical terms before final processing
- **Full Validation**: Comprehensive structural validation of outputs
- **Knowledge Graph Ready**: Outputs optimized for Neo4j/graph database ingestion
- **Cost Estimation**: Dry-run mode shows estimated API costs
- **Rich Progress Tracking**: Color-coded terminal output with detailed progress

## Architecture

```
Raw Transcript (Russian + English terms)
         ↓
[Stage 1] Extract Technical Glossary
         ↓ (USER REVIEW CHECKPOINT)
[Stage 2] Translate Full Transcript to English
         ↓
[Stage 3] Structure English Version
         ↓
[Stage 4] Structure Russian Version
         ↓
[Stage 5] Parse & Validate Both Versions
         ↓
Output: 7 files (2 markdown, 2 JSON, glossary, translation, metadata)
```

## Installation

### Requirements

```bash
pip install anthropic
```

Or from requirements.txt:

```bash
pip install -r requirements.txt
```

### Files Required

Place these files in the same directory:
- `transcript_processor.py` (main script)
- `parse_meeting.py` (parser from previous deliverable)

### API Key Setup

Get your Anthropic API key from: https://console.anthropic.com/

Set as environment variable:

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or pass directly with `--api-key` flag.

## Usage

### Basic Usage

```bash
python transcript_processor.py meeting_transcript.md
```

This will:
1. Extract technical glossary
2. **Pause for your review** - edit `technical_terms.json`
3. Process both English and Russian versions
4. Generate all output files in `./output/TIMESTAMP_filename/`

### Dry Run (Estimate Cost)

```bash
python transcript_processor.py meeting_transcript.md --dry-run
```

Shows estimated token usage and cost without making API calls.

### Skip Glossary Review

```bash
python transcript_processor.py meeting_transcript.md --skip-review
```

Auto-continues without waiting for glossary review (useful for batch processing).

### Custom Output Directory

```bash
python transcript_processor.py meeting_transcript.md -o ./processed_meetings
```

### Full Example

```bash
# Dry run first to see estimated cost
python transcript_processor.py team_sync.md --dry-run

# Process with glossary review
python transcript_processor.py team_sync.md -o ./output

# Review technical_terms.json and edit as needed
# Press ENTER to continue

# Script completes processing and generates all files
```

## Output Structure

```
output/
└── 2025-11-20_143022_team_sync/
    ├── technical_terms.json       # Editable glossary (5 categories)
    ├── translated_full_en.md      # Full English translation
    ├── structured_en.md           # Structured English (ready for parsing)
    ├── structured_ru.md           # Structured Russian (ready for parsing)
    ├── parsed_en.json             # English knowledge graph JSON
    ├── parsed_ru.json             # Russian knowledge graph JSON
    └── metadata.json              # Processing info, costs, validation
```

### File Descriptions

**technical_terms.json** - Extracted technical terminology organized by category:
```json
{
  "technical_terms": ["DestinationDriver", "core.next", "snapshots"],
  "product_names": ["AZUGA", "Neo4j"],
  "code_elements": ["routes.list", "tracking_number"],
  "company_terms": ["strategic optimization", "white label"],
  "acronyms": ["API", "UI", "ERP"]
}
```

**translated_full_en.md** - Complete English translation preserving technical terms

**structured_en.md** - English version formatted for knowledge graph:
- Organized by topics
- Timestamped statements
- Explicit decisions with rationale
- Action items with owners
- Metadata section

**structured_ru.md** - Russian version with same structure, technical terms in English

**parsed_en.json / parsed_ru.json** - Knowledge graph JSON with:
- Nodes: Meeting, Person, Topic, Statement, Decision, ActionItem
- Relationships: SPOKEN_BY, DISCUSSES, HAS_DECISION, ASSIGNED_TO, etc.
- Full statistics

**metadata.json** - Processing information:
```json
{
  "processing_info": {
    "timestamp": "2025-11-20_143022",
    "elapsed_seconds": 127.5,
    "model": "claude-sonnet-4-20250514"
  },
  "token_usage": {
    "total_input_tokens": 85000,
    "total_output_tokens": 64000,
    "total_cost_usd": 1.215
  },
  "glossary": {
    "total_terms": 47,
    "categories": {...}
  },
  "validation": {
    "english": {"passed": 10, "total_checks": 10},
    "russian": {"passed": 10, "total_checks": 10}
  }
}
```

## Cost Estimation

Based on typical 25-minute meeting transcript:

| Stage | Input Tokens | Output Tokens | Cost |
|-------|-------------|---------------|------|
| Stage 1: Glossary | 20,000 | 5,000 | $0.14 |
| Stage 2: Translation | 20,000 | 40,000 | $0.66 |
| Stage 3: English Structure | 40,000 | 40,000 | $0.72 |
| Stage 4: Russian Structure | 20,000 | 40,000 | $0.66 |
| **Total** | **100,000** | **125,000** | **$2.18** |

*Note: Actual costs vary by transcript length and complexity*

**Cost per token:**
- Input: $0.003 / 1K tokens
- Output: $0.015 / 1K tokens

## Validation Checks

The script performs 10 comprehensive validation checks on each output:

1. ✓ Meeting header exists
2. ✓ All required metadata fields present (DATE, DURATION, ATTENDEES)
3. ✓ At least one topic identified
4. ✓ Topics have proper structure (TIME, PARTICIPANTS)
5. ✓ All timestamps properly formatted (HH:MM:SS)
6. ✓ Multiple speakers detected
7. ✓ Decisions have required fields (DECIDED_BY, DECISION, RATIONALE)
8. ✓ Action items have assigned owners
9. ✓ All relationships reference valid nodes
10. ✓ Metadata section present

Failed checks are highlighted in red with specific error messages.

## Glossary Review Process

After Stage 1, the script pauses and displays:

```
[STAGE 1] ✓ Extracted 47 technical terms across 5 categories
✓ Glossary saved to: output/2025-11-20_143022_meeting/technical_terms.json

USER REVIEW REQUIRED
Review and edit technical terms in: output/2025-11-20_143022_meeting/technical_terms.json
Press ENTER when ready to continue, or Ctrl+C to abort...
```

**What to review:**

1. **False Positives**: Remove common words mistakenly flagged as technical
2. **Missing Terms**: Add important technical terms the AI missed
3. **Categorization**: Move terms to correct categories
4. **Spelling**: Fix any typos in technical terms

**Example edits:**

```json
{
  "technical_terms": [
    "DestinationDriver",
    "core.next",
    "snapshots",
    "tracking_number"  // Added - was missed
  ],
  "product_names": [
    "AZUGA",
    "Neo4j",
    "Route4Me"  // Added
  ],
  "code_elements": [
    "routes.list",
    "facility_view",
    "stash@{n}"  // Added Git term
  ],
  "company_terms": [
    "strategic optimization",
    "white label"
    // Removed "team sync" - too generic
  ],
  "acronyms": [
    "API",
    "UI",
    "ERP",
    "ASAP"  // Added
  ]
}
```

Save your edits, then press ENTER to continue.

## Batch Processing

Process multiple transcripts:

```bash
#!/bin/bash
for file in transcripts/*.md; do
    echo "Processing $file..."
    python transcript_processor.py "$file" --skip-review -o ./batch_output
    echo "---"
done
```

## Troubleshooting

### "No API key provided"

Set environment variable:
```bash
export ANTHROPIC_API_KEY='your-key-here'
```

Or pass directly:
```bash
python transcript_processor.py meeting.md --api-key 'your-key-here'
```

### "parse_meeting.py not found"

Ensure `parse_meeting.py` is in the same directory as `transcript_processor.py`.

### "API call failed"

The script automatically retries with exponential backoff. If all retries fail:
- Check your API key is valid
- Verify you have API credits
- Check internet connection
- Try again in a few minutes (rate limit)

### Validation failures

Review the specific validation errors in the output. Common issues:
- Missing timestamps in original transcript
- Ambiguous speaker attribution
- No clear decisions/action items in discussion

Check `metadata.json` for detailed validation results.

### JSON parsing errors

If glossary extraction fails:
- The script continues with empty glossary
- Review warning messages
- Manually create/edit `technical_terms.json`

### Cost concerns

Use `--dry-run` first to estimate costs before processing.

For very long transcripts (>1 hour):
- Consider splitting into multiple files
- Use `--dry-run` to see estimated cost first
- Expected cost: ~$2-5 per hour of meeting

## Advanced Usage

### Using Different Models

```bash
# Use Claude Opus (slower, more expensive, highest quality)
python transcript_processor.py meeting.md --model claude-opus-4-20250514

# Use Claude Haiku (faster, cheaper, good for simple transcripts)
python transcript_processor.py meeting.md --model claude-haiku-4-20250514
```

### Re-processing with Edited Glossary

If you want to re-run after editing glossary:

1. Copy edited `technical_terms.json` to a safe location
2. Re-run the script
3. When glossary is generated, replace it with your edited version
4. Press ENTER to continue

### Custom Validation

Edit the `full_validation()` method in `transcript_processor.py` to add custom checks.

## Integration with Knowledge Graph

### Import to Neo4j

```bash
# After processing
cd output/2025-11-20_143022_meeting

# Import English version
python -c "
from neo4j import GraphDatabase
import json

driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'password'))

with open('parsed_en.json') as f:
    data = json.load(f)

with driver.session() as session:
    # Create Meeting
    for meeting in data['nodes']['meetings']:
        session.run('CREATE (m:Meeting $props)', props=meeting)
    
    # Create People
    for person in data['nodes']['people']:
        session.run('CREATE (p:Person $props)', props=person)
    
    # Create relationships
    for rel in data['relationships']:
        session.run('''
            MATCH (from {id: $from_id})
            MATCH (to {id: $to_id})
            CREATE (from)-[r:\`' + rel['type'] + '\`]->(to)
            SET r = $props
        ''', from_id=rel['from'], to_id=rel['to'], props=rel['properties'])

print('Imported to Neo4j!')
"
```

### Query Examples

```cypher
// Find all action items for a person
MATCH (p:Person {name: "Dmitry Smaliak"})<-[:ASSIGNED_TO]-(a:ActionItem)
RETURN a.description, a.status, a.priority

// Get conversation flow for a topic
MATCH (t:Topic {label: "Strategic Optimization UI Development"})
MATCH (t)<-[:DISCUSSES]-(s:Statement)
RETURN s ORDER BY s.sequence

// Find decisions by topic
MATCH (t:Topic)-[:HAS_DECISION]->(d:Decision)
RETURN t.label, d.description, d.decided_by
```

## Performance

Typical processing times (25-minute meeting, ~20k chars):

| Stage | Time | Tokens |
|-------|------|--------|
| Stage 1: Glossary | 8s | 25k |
| Stage 2: Translation | 45s | 60k |
| Stage 3: English Structure | 35s | 80k |
| Stage 4: Russian Structure | 30s | 60k |
| Stage 5: Parsing | 2s | - |
| **Total** | **~2 minutes** | **225k** |

## Limitations

1. **Context Window**: Very long transcripts (>200k tokens) may need manual splitting
2. **Language Mixing**: Works best with Russian + English; other language pairs not tested
3. **Speaker Attribution**: Requires clear speaker labels in original transcript
4. **Technical Accuracy**: Review glossary carefully for domain-specific terms
5. **API Dependency**: Requires internet connection and valid API key

## Support

For issues or questions:
1. Check validation output in `metadata.json`
2. Review error messages in terminal
3. Use `--dry-run` to diagnose before processing
4. Examine intermediate files (translation, glossary)

## License

See LICENSE file for details.

## Changelog

### v1.0.0 (2025-11-20)
- Initial release
- Bilingual processing (EN/RU)
- Editable glossary extraction
- Full structural validation
- Knowledge graph JSON output
- Dry-run cost estimation
