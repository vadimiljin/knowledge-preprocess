<!-- cadbfa70-214a-48b9-b213-ac695cbc90bb e792e168-5640-4cd9-9cda-8e90deaab456 -->
# Neo4j Meeting Knowledge Graph - Implementation Plan

## Phase 1: Install Neo4j on Ubuntu (20 min)

Install Neo4j Community Edition via apt package manager:

```bash
# Add Neo4j repository
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/neo4j.gpg
echo "deb [signed-by=/etc/apt/keyrings/neo4j.gpg] https://debian.neo4j.com stable latest" | sudo tee /etc/apt/sources.list.d/neo4j.list
sudo apt update

# Install Neo4j and APOC plugin
sudo apt install neo4j
sudo systemctl enable neo4j
sudo systemctl start neo4j
```

Configure APOC plugin for JSON loading:

- Download APOC JAR to `/var/lib/neo4j/plugins/`
- Edit `/etc/neo4j/neo4j.conf` to enable APOC procedures
- Set initial password via `neo4j-admin dbms set-initial-password`

Access Neo4j Browser at `http://localhost:7474`

---

## Phase 2: Parse All Meeting Transcripts (15 min)

Run existing `parse_meeting.py` on all 11 meeting folders:

```bash
cd /home/vadim/Projects/route4me.com/knowledge_preprocess

# Parse each meeting's structured_en.md into graph JSON
for dir in */; do
  if [[ -f "${dir}structured_en.md" ]]; then
    python3 parse_meeting.py "${dir}structured_en.md" -o "${dir}graph.json" --pretty
    echo "Parsed: ${dir}"
  fi
done
```

This will create `graph.json` in each of the 11 meeting folders.

---

## Phase 3: Create Business Context Parser (30 min)

Create new script `parse_business_context.py` to extract structured data from `business_context.md` files:

**New nodes to extract:**

- `Directive` - Dan's specific mandates with authority level, urgency, deadline
- `BusinessImpact` - Revenue, reputation, competitive impacts
- `LeadershipPattern` - Decision-making styles per person

**Key sections to parse from business_context.md:**

- `### Directive N:` blocks → Directive nodes
- `**Business Impact:**` → BusinessImpact properties
- `**Authority Level:**` → CEO_FINAL_DECISION, CEO_APPROVED, TEAM_LEVEL
- `**Urgency:**` → IMMEDIATE, THIS_SPRINT, LONG_TERM

**Relationships to create:**

- `ISSUED_DIRECTIVE`: Meeting → Directive
- `DIRECTIVE_ASSIGNED_TO`: Directive → Person
- `HAS_BUSINESS_IMPACT`: Directive → BusinessImpact

---

## Phase 4: Unified Import Script (20 min)

Create `import_to_neo4j.py` that:

1. Reads all `graph.json` files from meeting folders
2. Reads all business context JSON (from Phase 3)
3. Merges duplicate Person nodes across meetings
4. Connects cross-meeting entities (same person, same topic names)
5. Executes Cypher LOAD statements via neo4j Python driver

Key merge strategy for cross-meeting analysis:

```cypher
MERGE (p:Person {name: $name})
ON CREATE SET p.first_seen = $meeting_date
ON MATCH SET p.meetings_attended = p.meetings_attended + 1
```

---

## Phase 5: Run Insight Queries (30 min)

Pre-built queries to run immediately after import:

**Query 1: Dan's Directive Tracker**

```cypher
MATCH (d:Directive)-[:ISSUED_IN]->(m:Meeting)
WHERE d.authority_level = 'CEO_FINAL_DECISION'
RETURN m.date, d.description, d.urgency, d.assigned_to
ORDER BY m.date
```

**Query 2: Topic Evolution Across Meetings**

```cypher
MATCH (t:Topic)<-[:CONTAINS_TOPIC]-(m:Meeting)
WHERE t.label CONTAINS 'Strategic Optimization'
RETURN m.date, t.label, size((t)-[:HAS_DECISION]->()) as decisions
ORDER BY m.date
```

**Query 3: Action Item Load by Person**

```cypher
MATCH (p:Person)<-[:ASSIGNED_TO]-(a:ActionItem)
RETURN p.name, count(a) as total_items, 
       sum(CASE WHEN a.status = 'pending' THEN 1 ELSE 0 END) as pending
ORDER BY pending DESC
```

**Query 4: Decision Authority Distribution**

```cypher
MATCH (d:Decision)-[:DECIDED_BY]->(p:Person)
RETURN p.name, count(d) as decisions_made
ORDER BY decisions_made DESC
```

**Query 5: Meeting Productivity Trend**

```cypher
MATCH (m:Meeting)
OPTIONAL MATCH (m)-[:CONTAINS_TOPIC]->(t:Topic)
OPTIONAL MATCH (t)-[:HAS_DECISION]->(d:Decision)
OPTIONAL MATCH (t)-[:HAS_ACTION_ITEM]->(a:ActionItem)
RETURN m.date, m.title, 
       count(DISTINCT t) as topics,
       count(DISTINCT d) as decisions,
       count(DISTINCT a) as action_items
ORDER BY m.date
```

---

## Deliverables

After completing this plan, you will have:

1. **Neo4j running natively** on Ubuntu with APOC enabled
2. **11 meetings imported** as interconnected graph data
3. **Business context enrichment** with Dan's directives as first-class nodes
4. **5 ready-to-run insight queries** for immediate results
5. **Cross-meeting analysis** showing topic evolution and person patterns

---

## Files to Create

| File | Purpose |

|------|---------|

| `parse_business_context.py` | Extract directives from business_context.md |

| `import_to_neo4j.py` | Unified import script for all data |

| `insight_queries.cypher` | Collection of analysis queries |

## Files to Modify

| File | Change |

|------|--------|

| `/etc/neo4j/neo4j.conf` | Enable APOC procedures |

### To-dos

- [ ] Install Neo4j Community Edition via apt on Ubuntu
- [ ] Download and configure APOC plugin for JSON loading
- [ ] Run parse_meeting.py on all 11 meeting structured_en.md files
- [ ] Create parse_business_context.py to extract directives from business_context.md
- [ ] Create import_to_neo4j.py for unified data import with person merging
- [ ] Execute import script to load all meetings into Neo4j
- [ ] Run 5 pre-built Cypher queries and capture results for boss