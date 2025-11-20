# Meeting Transcript to Knowledge Graph Parser

## Overview
This package contains tools to restructure meeting transcripts into a format optimized for knowledge graph ingestion.

## Files Included

1. **meeting_structured.md** - Restructured transcript with proper sections, headers, and labels
2. **parse_meeting.py** - Python script to parse the structured markdown into JSON
3. **meeting_graph_example.json** - Example output from parsing the provided transcript

## Structured Markdown Format

The restructured markdown uses the following sections:

### Meeting Header
```markdown
# MEETING: [Title]
**DATE:** YYYY-MM-DD
**DURATION:** HH:MM:SS
**ATTENDEES:** Person1, Person2, ...
```

### Topic Sections
```markdown
## TOPIC: [Topic Name]
**TIME:** HH:MM:SS - HH:MM:SS
**PARTICIPANTS:** Person1, Person2, ...

### DISCUSSION
**[timestamp] Speaker:** Statement text

### DECISION: [Decision Label]
**DECIDED_BY:** Person(s)
**DECISION:** Description
**RATIONALE:** Reasoning
**ALTERNATIVES_CONSIDERED:** ["Option 1", "Option 2"]

### ACTION_ITEMS
- **OWNER:** Person | **TASK:** Description | **STATUS:** status | **PRIORITY:** priority

### TECHNICAL_ISSUE: [Issue Label]
Description and discussion
```

## Usage

### Basic Usage
```bash
python3 parse_meeting.py meeting_structured.md
```

This will generate `meeting_graph.json` in the current directory.

### Custom Output Path
```bash
python3 parse_meeting.py meeting_structured.md -o custom_output.json
```

### Pretty-Print JSON
```bash
python3 parse_meeting.py meeting_structured.md --pretty
```

### Full Example
```bash
python3 parse_meeting.py meeting_structured.md -o knowledge_graph.json --pretty
```

## Output JSON Structure

The generated JSON contains:

```json
{
  "metadata": {
    "processed_at": "ISO8601 timestamp",
    "schema_version": "1.0",
    "parser_version": "1.0.0"
  },
  "nodes": {
    "meetings": [...],
    "people": [...],
    "topics": [...],
    "statements": [...],
    "decisions": [...],
    "action_items": [...]
  },
  "relationships": [
    {
      "type": "RELATIONSHIP_TYPE",
      "from": "node_id",
      "to": "node_id",
      "properties": {...}
    }
  ],
  "statistics": {
    "total_nodes": 81,
    "total_relationships": 179,
    "node_counts": {...}
  }
}
```

## Knowledge Graph Schema

### Nodes
- **Meeting**: Meeting metadata (date, duration, attendees, purpose)
- **Person**: Individual participants (name, statement count)
- **Topic**: Discussion topics (label, time range, participants, keywords)
- **Statement**: Individual spoken statements (speaker, timestamp, text, sequence)
- **Decision**: Decisions made (description, decided_by, rationale, alternatives)
- **ActionItem**: Tasks assigned (description, owner, status, priority, deadline)

### Relationships
- **HAS_ATTENDEE**: Meeting → Person
- **CONTAINS_TOPIC**: Meeting → Topic
- **SPOKEN_BY**: Statement → Person
- **DISCUSSES**: Statement → Topic
- **NEXT**: Statement → Statement (conversation flow)
- **HAS_DECISION**: Topic → Decision
- **DECIDED_BY**: Decision → Person
- **HAS_ACTION_ITEM**: Topic → ActionItem
- **ASSIGNED_TO**: ActionItem → Person

## Import to Neo4j

### Using Cypher
```cypher
// Load the JSON file
CALL apoc.load.json("file:///path/to/meeting_graph.json") YIELD value

// Create Meeting nodes
UNWIND value.nodes.meetings AS meeting
CREATE (m:Meeting {
  id: meeting.id,
  title: meeting.title,
  date: meeting.date,
  duration: meeting.duration
})

// Create Person nodes
UNWIND value.nodes.people AS person
CREATE (p:Person {
  id: person.id,
  name: person.name,
  statements_count: person.statements_count
})

// Create relationships
UNWIND value.relationships AS rel
MATCH (from {id: rel.from})
MATCH (to {id: rel.to})
CALL apoc.create.relationship(from, rel.type, rel.properties, to) YIELD rel as r
RETURN count(r)
```

### Using Python neo4j Driver
```python
from neo4j import GraphDatabase
import json

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

with open("meeting_graph.json") as f:
    data = json.load(f)

with driver.session() as session:
    # Create nodes
    for meeting in data["nodes"]["meetings"]:
        session.run("""
            CREATE (m:Meeting {
                id: $id, title: $title, date: $date, duration: $duration
            })
        """, **meeting)
    
    # Create relationships
    for rel in data["relationships"]:
        session.run("""
            MATCH (from {id: $from_id})
            MATCH (to {id: $to_id})
            CALL apoc.create.relationship(from, $type, $props, to) YIELD rel
            RETURN rel
        """, from_id=rel["from"], to_id=rel["to"], 
            type=rel["type"], props=rel["properties"])
```

## Example Queries

### Find all action items assigned to a person
```cypher
MATCH (p:Person {name: "Dmitry Smaliak"})<-[:ASSIGNED_TO]-(a:ActionItem)
RETURN a.description, a.status, a.priority
```

### Get conversation flow for a topic
```cypher
MATCH path = (s:Statement)-[:NEXT*]->(end:Statement)
WHERE s.topic_id = "topic_strategic_optimization_ui_development"
RETURN path
ORDER BY s.sequence
```

### Find all decisions made by a person
```cypher
MATCH (p:Person {name: "Serhii Kasainov"})<-[:DECIDED_BY]-(d:Decision)
RETURN d.description, d.rationale
```

### Get meeting statistics
```cypher
MATCH (m:Meeting)-[:CONTAINS_TOPIC]->(t:Topic)
MATCH (t)-[:HAS_DECISION]->(d:Decision)
MATCH (t)-[:HAS_ACTION_ITEM]->(a:ActionItem)
RETURN m.title, 
       count(DISTINCT t) as topics,
       count(DISTINCT d) as decisions,
       count(DISTINCT a) as action_items
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Customization

To modify the parser for your specific needs:

1. Edit the regex patterns in `parse_meeting.py`
2. Add new node types by creating new dataclasses
3. Modify the `_build_output()` method to change output structure
4. Add custom relationship types in parsing methods

## Notes

- IDs are automatically generated based on content
- Timestamps are preserved from original transcript
- Conversation flow is maintained through NEXT relationships
- Topic keywords are automatically extracted
- Supports multiple attendees, participants, and action item owners
