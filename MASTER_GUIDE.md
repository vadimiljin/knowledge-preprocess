# Complete Meeting Transcript Knowledge Graph System

## 🎯 What You Have

This package contains a complete pipeline for transforming meeting transcripts into knowledge graphs:

### Solution 1: Manual Processing (First Deliverable)
**Use when:** You already have structured transcripts or want full manual control

**Files:**
- `parse_meeting.py` - Parser for structured markdown
- `README.md` - Documentation for parser
- `meeting_structured.md` - Example structured format
- `meeting_graph_example.json` - Example output

**Process:** Manually structure transcript → Run parser → Get JSON

### Solution 2: Automated Bilingual Processing (Second Deliverable)
**Use when:** You have raw transcripts and want automated bilingual output

**Files:**
- `transcript_processor.py` - Automated AI-powered processor
- `TRANSCRIPT_PROCESSOR_README.md` - Full documentation
- `QUICKSTART.md` - 5-minute setup guide
- `requirements.txt` - Dependencies

**Process:** Raw transcript → AI processing → 4 structured files + 4 JSONs

---

## 📊 Comparison: Manual vs Automated

| Feature | Manual (parse_meeting.py) | Automated (transcript_processor.py) |
|---------|---------------------------|-------------------------------------|
| **Input** | Pre-structured markdown | Raw unstructured transcript |
| **Languages** | Any (single language) | Russian + English → Both outputs |
| **Processing** | Regex parsing | AI-powered structuring |
| **Cost** | Free | ~$2.18 per meeting |
| **Time** | <1 second | ~2 minutes |
| **Technical Term Handling** | Manual | AI extraction + editable |
| **Output Files** | 1 JSON | 7 files (2 markdown, 2 JSON, glossary, translation, metadata) |
| **Quality Control** | You structure it | 10-point validation |
| **Best For** | Clean structured input | Raw conversational transcripts |

---

## 🚀 Quick Start Paths

### Path A: You Have Raw Russian Transcripts

**Recommendation:** Use automated processor

```bash
# 1. Install
pip install anthropic
export ANTHROPIC_API_KEY='your-key'

# 2. Process
python transcript_processor.py raw_meeting.md

# 3. Review glossary when prompted
# 4. Get 4 outputs: EN + RU markdown + JSON
```

**Deliverables:**
- ✅ English structured markdown
- ✅ Russian structured markdown  
- ✅ English knowledge graph JSON
- ✅ Russian knowledge graph JSON
- ✅ Technical glossary
- ✅ Full translation
- ✅ Processing metadata

### Path B: You Have Pre-Structured Markdown

**Recommendation:** Use manual parser

```bash
# Parse existing structured markdown
python parse_meeting.py structured_meeting.md -o output.json --pretty
```

**Deliverables:**
- ✅ Knowledge graph JSON

### Path C: You Want Both (Recommended!)

```bash
# 1. Auto-process raw transcript
python transcript_processor.py raw_meeting.md

# 2. Outputs include pre-parsed JSONs
# 3. If needed, re-parse with manual parser for different options
python parse_meeting.py output/*/structured_en.md -o custom.json
```

---

## 📁 Complete File Reference

### Core Scripts

**parse_meeting.py** (19 KB)
- Manual parser for structured markdown
- Zero dependencies beyond Python stdlib
- Fast (<1 second)
- Command: `python parse_meeting.py input.md -o output.json`

**transcript_processor.py** (31 KB)
- AI-powered automated processor
- Requires: `anthropic` package
- Bilingual output
- Command: `python transcript_processor.py raw.md`

### Documentation

**README.md** (6.2 KB)
- Parser documentation
- Neo4j import examples
- Query examples
- Structured format specification

**TRANSCRIPT_PROCESSOR_README.md** (13 KB)
- Automated processor docs
- Architecture overview
- Cost estimation
- Validation details
- Troubleshooting

**QUICKSTART.md** (4.7 KB)
- 5-minute setup
- First-run walkthrough
- Common issues
- Pro tips

**requirements.txt** (339 B)
- Python dependencies
- Installation instructions

### Examples

**meeting_structured.md** (13 KB)
- Example structured transcript (Russian)
- Shows proper format for manual parser
- 7 topics, 43 statements, 6 decisions, 15 actions

**meeting_graph_example.json** (65 KB)
- Example parsed output
- 81 nodes, 179 relationships
- Ready for Neo4j import

---

## 🔄 Complete Workflow

### End-to-End Example

```bash
# STEP 1: Automated Processing
python transcript_processor.py team_meeting_2025-11-19.md

# Output directory created:
# output/2025-11-19_143022_team_meeting/
#   ├─ technical_terms.json           [AI extracted - review this!]
#   ├─ translated_full_en.md          [Full translation]
#   ├─ structured_en.md               [Structured English]
#   ├─ structured_ru.md               [Structured Russian]
#   ├─ parsed_en.json                 [KG JSON ready]
#   ├─ parsed_ru.json                 [KG JSON ready]
#   └─ metadata.json                  [Cost & validation]

# STEP 2: Review Technical Terms
vi output/2025-11-19_143022_team_meeting/technical_terms.json
# Edit, save, press ENTER in terminal

# STEP 3: Processing completes automatically

# STEP 4: Import to Neo4j (choose language)
cd output/2025-11-19_143022_team_meeting

# English version
neo4j-admin import \
  --database=meetings_en \
  --nodes=parsed_en.json

# Russian version  
neo4j-admin import \
  --database=meetings_ru \
  --nodes=parsed_ru.json

# STEP 5: Query Your Knowledge Graph
cypher-shell -d meetings_en
# Run queries from README.md
```

---

## 💰 Cost Analysis

### Automated Processing Costs

**Typical 25-minute meeting:**
- Input: ~20,000 chars → ~6,600 tokens
- Processing: 4 AI stages
- Total tokens: ~100k input + ~125k output
- **Cost: $2.18**

**Cost breakdown:**
- Stage 1 (Glossary): $0.14
- Stage 2 (Translation): $0.66
- Stage 3 (English Structure): $0.72
- Stage 4 (Russian Structure): $0.66

**Manual parsing:** $0.00 (but requires pre-structured input)

### Monthly Cost Estimates

| Meeting Frequency | Automated Cost | Manual Cost |
|------------------|----------------|-------------|
| Daily (20/month) | $43.60 | $0 |
| Weekly (4/month) | $8.72 | $0 |
| Bi-weekly (2/month) | $4.36 | $0 |

**ROI Consideration:**
- Manual structuring time: ~30-45 minutes per meeting
- Automated processing: ~2 minutes + 1 minute review
- Time saved: ~40 minutes × $hourly_rate vs $2.18 cost

---

## 🎓 Understanding the Output

### Structured Markdown Format

Both processors output this format:

```markdown
# MEETING: [Title]
**DATE:** 2025-11-19
**DURATION:** 00:25:28
**ATTENDEES:** Alice, Bob, Charlie

## TOPIC: Feature Development
**TIME:** 00:05:00 - 00:15:00
**PARTICIPANTS:** Alice, Bob

### DISCUSSION
**[00:05:15] Alice:** We need to implement the new API endpoint.

**[00:06:30] Bob:** I can handle the backend integration.

### DECISION: API Implementation Plan
**DECIDED_BY:** Alice, Bob
**DECISION:** Implement REST API with OAuth2 authentication
**RATIONALE:** Industry standard, better security
**ALTERNATIVES_CONSIDERED:** ["Basic Auth", "API Keys only"]

### ACTION_ITEMS
- **OWNER:** Bob | **TASK:** Implement OAuth2 backend | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Alice | **TASK:** Write API documentation | **STATUS:** pending | **PRIORITY:** normal
```

### Knowledge Graph JSON Structure

```json
{
  "nodes": {
    "meetings": [{"id": "meeting_123", "title": "...", ...}],
    "people": [{"id": "person_alice", "name": "Alice", ...}],
    "topics": [{"id": "topic_feature", "label": "...", ...}],
    "statements": [{"id": "stmt_1", "speaker_id": "person_alice", ...}],
    "decisions": [{"id": "decision_1", "description": "...", ...}],
    "action_items": [{"id": "action_1", "owner_id": "person_bob", ...}]
  },
  "relationships": [
    {"type": "SPOKEN_BY", "from": "stmt_1", "to": "person_alice"},
    {"type": "HAS_DECISION", "from": "topic_feature", "to": "decision_1"},
    ...
  ]
}
```

---

## 🔍 Quality Assurance

### Validation Checklist

Both tools validate:
- ✅ Meeting header structure
- ✅ Required metadata fields
- ✅ Timestamp formatting (HH:MM:SS)
- ✅ Speaker attribution
- ✅ Topic organization
- ✅ Decision completeness
- ✅ Action item ownership
- ✅ Relationship integrity

### Automated Processor Additional Checks

- ✅ Technical term preservation
- ✅ Translation quality (EN/RU consistency)
- ✅ Bilingual structure alignment
- ✅ Glossary completeness

---

## 🛠️ Advanced Usage

### Batch Processing Multiple Transcripts

```bash
#!/bin/bash
# batch_process.sh

for transcript in transcripts/*.md; do
    echo "Processing: $transcript"
    
    # Use automated processor
    python transcript_processor.py "$transcript" \
        --skip-review \
        -o ./batch_output
    
    echo "---"
done

echo "Batch processing complete!"
echo "Check ./batch_output/ for results"
```

### Custom Glossary Templates

```bash
# 1. Process first meeting with similar content
python transcript_processor.py meeting1.md

# 2. Save the reviewed glossary as template
cp output/2025-11-19_*/technical_terms.json templates/engineering_glossary.json

# 3. For subsequent meetings, pre-populate
cp templates/engineering_glossary.json output/next_meeting/technical_terms.json
python transcript_processor.py meeting2.md
# (glossary will already have your terms)
```

### Combining EN + RU in Same Graph

```cypher
// Import both to same Neo4j database with language labels

// English nodes
LOAD JSON FROM 'parsed_en.json' AS data
UNWIND data.nodes.statements AS stmt
CREATE (s:Statement:English)
SET s = stmt

// Russian nodes  
LOAD JSON FROM 'parsed_ru.json' AS data
UNWIND data.nodes.statements AS stmt
CREATE (s:Statement:Russian)
SET s = stmt

// Link equivalent statements
MATCH (en:Statement:English), (ru:Statement:Russian)
WHERE en.sequence = ru.sequence AND en.topic_id = ru.topic_id
CREATE (en)-[:TRANSLATION_OF]->(ru)
```

---

## 📚 Learning Resources

### Understanding Knowledge Graphs
- Neo4j Graph Academy: https://graphacademy.neo4j.com/
- Cypher Query Language: https://neo4j.com/docs/cypher-manual/

### Anthropic Claude API
- Documentation: https://docs.anthropic.com/
- Pricing: https://www.anthropic.com/pricing

### Meeting Analysis Use Cases
- Action item tracking dashboards
- Decision history and rationale
- Team communication patterns
- Topic evolution over time
- Cross-meeting entity resolution

---

## 🐛 Troubleshooting

### "Can't find parse_meeting.py"

Both files must be in same directory:
```bash
ls -l
# Should show both:
# parse_meeting.py
# transcript_processor.py
```

### Parsing Fails

**For manual parser:**
- Check markdown follows exact format in `meeting_structured.md`
- Verify timestamps are HH:MM:SS format
- Ensure speaker names are consistent

**For automated processor:**
- Check `metadata.json` for validation failures
- Review specific error messages
- Re-run with `--dry-run` to test without cost

### High Costs

- Use `--dry-run` first to estimate
- Split very long transcripts
- Consider manual parsing for simple meetings

### Technical Terms Mistranslated

- Review and edit `technical_terms.json` during checkpoint
- Add missing terms
- Remove false positives
- Save glossary as template for future meetings

---

## 🎯 Best Practices

### For Raw Transcripts
1. ✅ Always run `--dry-run` first
2. ✅ Review glossary carefully (critical!)
3. ✅ Save edited glossaries as templates
4. ✅ Check validation results in metadata.json
5. ✅ Keep consistent speaker names in source

### For Manual Structuring
1. ✅ Use example file as template
2. ✅ Keep timestamps consistent (HH:MM:SS)
3. ✅ One topic per major discussion theme
4. ✅ Explicit decisions with rationale
5. ✅ Clear action item owners

### General
1. ✅ Process meetings soon after they occur (fresh context)
2. ✅ Use consistent naming conventions
3. ✅ Archive raw transcripts separately
4. ✅ Regular Neo4j backups
5. ✅ Document custom glossary terms

---

## 📞 Support

### Check These First
1. Error messages in terminal
2. `metadata.json` validation section
3. This MASTER_GUIDE.md troubleshooting section
4. Individual README files

### Common Solutions
- API issues → Check key and credits
- Parsing errors → Verify input format
- Cost concerns → Use dry-run mode
- Quality issues → Review glossary

---

## 🎉 You're Ready!

You now have:
- ✅ Manual parser for quick processing
- ✅ AI-powered processor for automation
- ✅ Bilingual support (EN + RU)
- ✅ Knowledge graph ready outputs
- ✅ Complete documentation
- ✅ Working examples

Choose your path and start transforming your meeting transcripts into queryable knowledge graphs!

---

**Created:** 2025-11-20  
**Version:** 1.0.0  
**For:** Route4Me Team
