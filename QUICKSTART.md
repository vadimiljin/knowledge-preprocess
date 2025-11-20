# Quick Start Guide

## 5-Minute Setup

### Step 1: Install Dependencies

```bash
pip install anthropic
```

### Step 2: Set API Key

Get your key from: https://console.anthropic.com/

```bash
export ANTHROPIC_API_KEY='sk-ant-...'
```

### Step 3: Place Required Files

Ensure these files are in the same directory:
- `transcript_processor.py`
- `parse_meeting.py` (from previous deliverable)
- Your raw meeting transcript (e.g., `meeting.md`)

### Step 4: Run!

```bash
# Estimate cost first
python transcript_processor.py meeting.md --dry-run

# Process for real
python transcript_processor.py meeting.md
```

### Step 5: Review Glossary

When prompted:
1. Open `output/TIMESTAMP_meeting/technical_terms.json`
2. Review and edit technical terms
3. Press ENTER in terminal to continue

### Step 6: Access Results

Check `output/TIMESTAMP_meeting/` for:
- ✅ `structured_en.md` - English structured version
- ✅ `structured_ru.md` - Russian structured version  
- ✅ `parsed_en.json` - English knowledge graph
- ✅ `parsed_ru.json` - Russian knowledge graph
- ℹ️ `metadata.json` - Processing details & costs

## Expected Output

```
[STAGE 1] Extracting technical glossary from transcript...
  Input tokens: 20,124 | Output tokens: 4,532
✓ Extracted 47 technical terms across 5 categories
✓ Glossary saved to: output/2025-11-20_143022_meeting/technical_terms.json

USER REVIEW REQUIRED
Review and edit technical terms in: output/2025-11-20_143022_meeting/technical_terms.json
Press ENTER when ready to continue, or Ctrl+C to abort...

[STAGE 2] Translating transcript to English...
  Input tokens: 20,124 | Output tokens: 38,456
✓ Translation complete

[STAGE 3] Structuring English version...
  Input tokens: 38,456 | Output tokens: 40,123
✓ English structuring complete

[STAGE 4] Structuring Russian version...
  Input tokens: 20,124 | Output tokens: 38,890
✓ Russian structuring complete

[STAGE 5] Parsing and validating ENGLISH version...
✓ Parsed 81 nodes, 179 relationships
✓ All 10 validation checks passed

[STAGE 5] Parsing and validating RUSSIAN version...
✓ Parsed 81 nodes, 179 relationships
✓ All 10 validation checks passed

============================================================
PROCESSING COMPLETE
============================================================

📁 Output directory: output/2025-11-20_143022_meeting

📄 Generated files:
  ├─ technical_terms.json       (Editable glossary)
  ├─ translated_full_en.md      (Full English translation)
  ├─ structured_en.md           (Structured English)
  ├─ structured_ru.md           (Structured Russian)
  ├─ parsed_en.json             (Knowledge graph JSON)
  ├─ parsed_ru.json             (Knowledge graph JSON)
  └─ metadata.json              (Processing metadata)

💰 Cost: $2.18
  ├─ Input tokens: 98,828 ($0.30)
  └─ Output tokens: 122,001 ($1.88)

⏱️  Time: 127.5s

📊 Statistics:
  English: 7 topics, 6 decisions, 15 actions
  Russian: 7 topics, 6 decisions, 15 actions
```

## Common First-Time Issues

### "ModuleNotFoundError: No module named 'anthropic'"
```bash
pip install anthropic
```

### "Error: No API key provided"
```bash
export ANTHROPIC_API_KEY='your-key-here'
```

### "parse_meeting.py not found"
Copy `parse_meeting.py` to the same directory as `transcript_processor.py`

## Pro Tips

💡 **Always dry-run first**: See estimated cost before processing
```bash
python transcript_processor.py meeting.md --dry-run
```

💡 **Skip review for batch processing**: Use `--skip-review` flag
```bash
python transcript_processor.py meeting.md --skip-review
```

💡 **Keep glossaries**: Save edited glossaries for similar meetings
```bash
cp output/*/technical_terms.json templates/glossary_team_sync.json
```

## What's Next?

1. ✅ Review structured markdown files
2. ✅ Import JSON to Neo4j (see main README)
3. ✅ Query your knowledge graph
4. 🔄 Process more transcripts (batch script in README)

## Need Help?

Check the main README for:
- Detailed usage examples
- Troubleshooting guide
- Validation explanations
- Neo4j integration
- Batch processing scripts

## Example Input Format

Your transcript should look like this (Russian + English terms):

```markdown
# Транскрипт встречи

**Дата:** 2025-11-19
**Длительность:** 00:25:28
**Участники:** Person1, Person2, Person3

---

**Person1** [00:00:00 - 00:00:23]: По DestinationDriver есть что-то интересное?

**Person2** [00:00:23 - 00:00:40]: Я сейчас занимаюсь справками в Destinations...
```

The script handles:
- Mixed Russian/English
- Technical terminology
- Timestamps
- Speaker attribution
- Informal conversation style

That's it! Start processing your first transcript now! 🚀
