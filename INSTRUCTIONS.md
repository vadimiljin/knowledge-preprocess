# COMPLETE PROJECT INSTRUCTIONS - FINAL VERSION

**Version:** 3.0 (Parser-Compatible + Maximum Business Intelligence)
 **Date:** 2025-11-22
 **Status:** Production Ready

------

## MISSION

Transform Russian+English meeting transcripts into Neo4j-ready knowledge graphs while preserving maximum organizational intelligence about Dan's (CEO) decision-making authority.

------

## CORE PRINCIPLES

1. **Parser Compatibility = NON-NEGOTIABLE** - structured_en.md MUST pass parse_meeting.py
2. **Dan's Authority Always Tracked** - CEO controls everything, mark his involvement explicitly
3. **Zero Information Loss** - Use business_context.md for what parser can't handle
4. **Raw Transcript = Truth** - Verify everything against source
5. **Never Fabricate** - Mark uncertainty explicitly

------

## ORGANIZATIONAL CONTEXT

- **Dan Khasis = CEO** - Final decision maker on everything
- **Decision Hierarchy:** Dan's decisions > Leadership decisions > Team decisions
- **Meeting Reality:** Nothing goes to production without Dan's approval
- **Authority Tracking:** Critical for understanding what's approved vs. proposed

------

## INPUT TYPES

### Type 1: Full Transcript + Summary (IDEAL - HIGH confidence)

- PRIMARY: Raw transcript (.md)
- SECONDARY: Alexey's summary
- Strategy: Verify transcript, enrich with summary context

### Type 2: Full Transcript Only (GOOD - MEDIUM-HIGH confidence)

- SOLE SOURCE: Raw transcript (.md)
- Strategy: Extract everything, infer business context

### Type 3: Summary Only (ACCEPTABLE - MEDIUM-LOW confidence)

- SOLE SOURCE: Alexey's summary
- Strategy: Mark ALL data `[SUMMARY_ONLY - not verified]`
- Add disclaimer in headers

### Type 4: Neither (REJECT)

- Action: Request at least one source

------

## OUTPUT: 4 ARTIFACTS (ALL REQUIRED)

### ARTIFACT 1: technical_glossary.json

```json
{
  "metadata": {
    "source_quality": "full_transcript|transcript_only|summary_only",
    "verification_status": "verified|partial|unverified",
    "processed_date": "YYYY-MM-DD",
    "meeting_date": "YYYY-MM-DD"
  },
  "technical_terms": ["term1", "term2"],
  "product_names": ["Product1"],
  "code_elements": ["element.js"],
  "company_terms": ["strategic optimization"],
  "acronyms": ["API", "UI"]
}
```

**Categories:**

- technical_terms: APIs, core.next, snapshots, tracking_number, pushers, feature flags
- product_names: Route4Me, AZUGA, Neo4j, Slack, SAP
- code_elements: routes.list, facility_view, DestinationDriver
- company_terms: strategic optimization, white label, assignment board
- acronyms: API, UI, ERP, ASAP

**Rules:**

- Translate Russian technical terms → English
- Preserve exact casing
- Include variations

------

### ARTIFACT 2: translated_full_en.md

```markdown
[TRANSLATION METADATA]
- Source: full_transcript|summary_only
- Original Language: Russian + English technical terms
- Translation Date: YYYY-MM-DD
- Transcript Accuracy: XX.X%
- Confidence Level: high|medium|low

---

**[HH:MM:SS] Speaker Name**: Translated statement preserving technical_terms.
```

**Rules:**

- Translate ALL Russian → clear English
- PRESERVE technical terms from glossary
- Keep timestamps HH:MM:SS format
- Keep speaker names original
- If summary-only: Mark `[~HH:MM:SS from summary]`

------

### ARTIFACT 3: structured_en.md (PARSER-COMPATIBLE)

**CRITICAL: This file MUST pass parse_meeting.py validation**

#### ALLOWED SECTIONS ONLY:

✅ `### DISCUSSION`
 ✅ `### DECISION: [Label]`
 ✅ `### ACTION_ITEMS`
 ✅ `### TECHNICAL_ISSUE: [Label]`

#### FORBIDDEN (breaks parser):

❌ `### DAN'S DIRECTIVES`
 ❌ `### LEADERSHIP INPUTS`
 ❌ `### TEAM DISCUSSION`
 ❌ `### BUSINESS_IMPACT`
 ❌ Roles in brackets after names
 ❌ Priority prefixes `[CRITICAL_URGENT]`
 ❌ Extra DECISION fields (AUTHORITY_LEVEL, CONFIDENCE)

#### EXACT FORMAT:

```markdown
# MEETING: [Clear Descriptive Title]

**DATE:** YYYY-MM-DD  
**DURATION:** HH:MM:SS  
**ATTENDEES:** Name1 (Short Role), Name2 (Short Role), Name3, ...  
**DAN_PRESENT:** yes|no  
**MEETING_TYPE:** Product Review|Ad-Hoc|Technical|Strategic Planning  
**DATA_SOURCE:** full_transcript|summary_only|transcript+summary  
**CONFIDENCE_LEVEL:** high|medium|low

---

## TOPIC: [Topic Name]
**TIME:** HH:MM:SS - HH:MM:SS  
**PARTICIPANTS:** Name1, Name2, Name3

### DISCUSSION

**[HH:MM:SS] Speaker Name**: Statement text.

**[HH:MM:SS] Speaker Name**: Another statement.

### DECISION: [Decision Label]

**DECIDED_BY:** Dan, Name1, Name2  
**DECISION:** Clear one-sentence description  
**RATIONALE:** Why this decision. Include Dan's approval status and business reasoning. [EXECUTING_CEO_DIRECTIVE] or [PENDING_CEO_APPROVAL] or [CEO_APPROVED] markers as needed.  
**ALTERNATIVES_CONSIDERED:** ["Option 1", "Option 2"]

### TECHNICAL_ISSUE: [Issue Label]

**[HH:MM:SS] Speaker Name**: Description of technical issue.

### ACTION_ITEMS

- **OWNER:** Person Name | **TASK:** Description | **STATUS:** pending|in_progress|done | **PRIORITY:** high|normal|low | **DEADLINE:** YYYY-MM-DD
- **OWNER:** Backend Team | **TASK:** Description | **STATUS:** pending | **PRIORITY:** normal

---

## METADATA

**TOTAL_TOPICS:** N  
**TOTAL_DECISIONS:** N  
**TOTAL_ACTION_ITEMS:** N  
**KEY_FEATURES_DISCUSSED:** Feature1, Feature2, ...  
**TECHNICAL_ISSUES:** Issue1, Issue2, ...
```

#### EMPLOYEE ROLES - CRITICAL RULES

**Source:** Employees CSV (document 11)

**Role Format - SHORT essence only:**

- "FrontEnd Product & Corporate Websites Lead" → "Frontend Lead"
- "Front End Engineer" → "Frontend Engineer"
- "Senior Front End Engineer" → "Senior Frontend Engineer"
- "VP Platform" → "VP Platform"
- "Global SVP Platform" → "SVP Platform"

**Known Employees:**

- Semeyon S: VP Platform
- Serhii Kasainov: Front-End Tech Lead
- Igor Skrynkovskyy: SVP Platform
- Igor Golovtsov: Senior Frontend Engineer
- Manar Kurmanov: Frontend Engineer
- Dmitry Smaliak: Frontend Engineer
- Eugene (Bondarenko): Frontend Engineer
- Alexey Afanasiev: Frontend Lead
- Alexey Gusentsov: Frontend Engineer
- Dan (Khasis): CEO

**Usage Rules:**

1. Check Employees file FIRST for every participant
2. Use SHORT form in ATTENDEES metadata ONLY
3. NEVER show roles in:
   - DISCUSSION speaker names: `**[00:00:00] Name**` ← Correct
   - ACTION_ITEMS owner: `**OWNER:** Name` ← Correct
   - DECISION decided_by: `**DECIDED_BY:** Name` ← Correct
4. If no role in file: Use short inferred role or leave blank

#### DAN'S AUTHORITY ENCODING (Option C)

**Rule:** Always include Dan in DECIDED_BY when he approved/involved

**Status Markers for RATIONALE:**

- `[EXECUTING_CEO_DIRECTIVE]` - Team implementing Dan's prior request
- `[PENDING_CEO_APPROVAL]` - Decision made, awaiting Dan's approval
- `[CEO_APPROVED]` - Dan explicitly approved
- `[CEO_REJECTED]` - Dan rejected proposal

**Examples:**

```markdown
### DECISION: Deploy Feature X
**DECIDED_BY:** Dan
**DECISION:** Approved immediate deployment
**RATIONALE:** Customer impact critical, technical validation complete. CEO green light given.

### DECISION: Add Distance Columns
**DECIDED_BY:** Dmitry Smaliak
**DECISION:** Add two new columns to routes view
**RATIONALE:** Implementing distance/drive time columns as Dan specifically requested in previous demo. [EXECUTING_CEO_DIRECTIVE]

### DECISION: Fix Tracking Bug
**DECIDED_BY:** Serhii Kasainov
**DECISION:** Deploy backend fix to production
**RATIONALE:** Critical bug on AZUGA accounts. Technical fix validated, requires Dan's approval before deployment. [PENDING_CEO_APPROVAL]
```

#### TEAM OWNERSHIP (Option B + Migration Path)

**Current Format:**

```markdown
- **OWNER:** Backend Team | **TASK:** Implement pusher support | **STATUS:** pending
- **OWNER:** Design Team | **TASK:** Review mockups | **STATUS:** in_progress
```

**Neo4j Today:**

- Creates Person nodes: "Backend Team", "Design Team"
- Fully backward compatible

**Future Migration (when individual names available):**

```cypher
// Option A: Replace team with individual
MATCH (a:ActionItem)-[r:ASSIGNED_TO]->(team:Person {name: "Backend Team"})
WHERE a.description CONTAINS "pusher support"
MATCH (person:Person {name: "Mihail Krivulya"})
DELETE r
CREATE (a)-[:ASSIGNED_TO]->(person)

// Option B: Add team membership
MATCH (team:Person {name: "Backend Team"})
SET team.type = "team"
WITH team
MATCH (p1:Person {name: "Mihail Krivulya"})
MATCH (p2:Person {name: "Dmitryl Lyubetsky"})
CREATE (team)-[:HAS_MEMBER]->(p1)
CREATE (team)-[:HAS_MEMBER]->(p2)

// Query: Tasks for team OR its members
MATCH (a:ActionItem)-[:ASSIGNED_TO]->(owner)
WHERE owner.name = "Backend Team" 
   OR (owner)<-[:HAS_MEMBER]-(:Person {name: "Backend Team"})
RETURN a
```

**Common Team Names:** Backend Team, Frontend Team, Design Team, QA Team, Mobile Team

------

### ARTIFACT 4: business_context.md

**Purpose:** Preserve ALL business intelligence that parser can't handle

```markdown
# Business Context Analysis: [Meeting Title]

**Meeting Date:** YYYY-MM-DD  
**Analysis Date:** YYYY-MM-DD  
**Dan Present:** yes|no  
**Data Source:** full_transcript|summary_only|transcript+summary

---

## EXECUTIVE SUMMARY

**Dan's Involvement:**
- Directives given: N
- Decisions approved: N
- Strategic guidance: [Key themes]
- Overall sentiment: [Pleased|Neutral|Concerned|Frustrated|Angry]
- Emotional intensity: [Low|Medium|High]

**Critical Decisions:** [Top 3 most important with business impact]

**Urgent Action Items:** [Tasks Dan flagged as immediate]

**Business Priorities:** [What Dan emphasized]

---

## DAN'S DIRECTIVES & AUTHORITY

### Directive 1: [Title]
**Timestamp:** [HH:MM:SS] or [Referenced from prior meeting]  
**Type:** CRITICAL_DIRECTIVE|STRATEGIC_DIRECTIVE|FEATURE_REQUEST|APPROVAL|REJECTION|PHILOSOPHY  
**Exact Quote/Key Points:** "Direct quote" or [Key points if paraphrased]  
**Issue:** What problem/opportunity Dan identified  
**Business Impact:** Revenue|Reputation|Technical Debt|User Experience|Operational  
**Impact Severity:** Critical|High|Medium|Low  
**Urgency:** IMMEDIATE|THIS_WEEK|THIS_SPRINT|LONG_TERM  
**Assigned To:** [Names if Dan assigned]  
**Deadline:** [Specific date/timeframe if stated]  
**Emotion:** [Frustrated|Angry|Concerned|Pleased|Neutral|Passionate]  
**Emotional Context:** [Why this tone - what it reveals about priorities]  
**Status:** Executed|In Progress|Pending|Blocked  
**Authority Level:** CEO_FINAL_DECISION

**Organizational Implications:**
- What this reveals about Dan's priorities
- How team should interpret/execute
- What gets deprioritized as result

---

## DECISION HIERARCHY & AUTHORITY ANALYSIS

### Decision: [Decision Label from structured.md]

**Reference:** See structured.md DECISION block for formal details

**Authority Analysis:**
- **Authority Level:** CEO_FINAL|CEO_APPROVED|LEADERSHIP_APPROVED|TEAM_LEVEL|TEAM_PROPOSAL
- **Decision Maker(s):** Dan (primary role), Others (execution role)
- **Dan's Role:** Direct decision|Approved team proposal|Guided approach|Not involved|Approval pending
- **Approval Status:** Approved by Dan|Pending Dan review|Implicit approval|No approval needed

**Business Impact Assessment:**
- **Category:** Revenue|Reputation|Technical Debt|User Experience|Operational|Compliance
- **Severity:** Critical|High|Medium|Low
- **Stakeholders Affected:** Customers|Partners|Internal team|All
- **Customer Impact:** [Specific user/customer consequences]
- **Revenue Impact:** [If applicable]
- **Reputation Impact:** [If applicable]
- **Cost of Inaction:** [What happens if not done]
- **Expected Benefit:** [Value if successfully executed]
- **Timeline Impact:** [Effect on roadmap/deadlines]

**Emotional Context:**
- Dan's sentiment about this decision
- Team's sentiment
- Urgency indicators from discussion tone
- Stress/pressure levels

**Strategic Alignment:**
- How this fits Dan's long-term vision
- What it reveals about priorities
- Implications for future decisions

---

## TECHNICAL ISSUES - BUSINESS TRANSLATION

### Issue: [Issue Label from structured.md]

**Reference:** See structured.md TECHNICAL_ISSUE block for technical details

**Business Translation:**
- **User Impact:** How customers experience this
- **User Scenarios Affected:** [Specific use cases broken]
- **Business Cost:** Time/money/reputation/productivity
- **Customer Complaints:** [If mentioned]
- **Support Burden:** [If discussed]
- **Competitive Impact:** [How this affects market position]
- **Root Cause (Business Terms):** [Why this happened from org perspective]
- **Prevention Strategy:** [How to avoid similar issues]

**Dan's Assessment:**
- Did Dan weigh in on severity?
- Dan's priority level for fix
- Dan's concern level (emotion)
- Dan's deadline expectations

---

## LEADERSHIP DECISION PATTERNS

### [Leader Name] - [Role]

**Decision-Making Style:**
- Takes initiative on: [Types of decisions]
- Seeks approval for: [What needs escalation]
- Authority scope: [What they can decide autonomously]

**Decisions This Meeting:**
1. [Decision] - [Authority level] - [Dan's response]
2. [Decision] - [Authority level] - [Dan's response]

**Proposals This Meeting:**
1. [Proposal] - [Status: Approved/Pending/Rejected]

**Technical Inputs:**
- Key contributions to discussion
- Areas of expertise demonstrated

---

## ORGANIZATIONAL INSIGHTS

### Meeting Dynamics
- **Primary Drivers:** [Who pushed agenda]
- **Decision Style:** Collaborative|Directive|Mixed
- **Dan's Engagement:** Heavy|Moderate|Light|Not present
- **Bottlenecks:** [What slowed progress]
- **Clarity Level:** [How clear were outcomes]

### Team Sentiment
- **Morale:** Positive|Neutral|Strained
- **Confidence:** High|Medium|Low
- **Urgency Level:** Calm|Moderate|High pressure|Crisis mode
- **Notable Tensions:** [If any conflicts/friction]
- **Team Energy:** Energized|Steady|Fatigued

### Communication Patterns
- **Dan → Team:** [Directive|Collaborative|Hands-off]
- **Team → Dan:** [Seeking guidance|Presenting solutions|Reporting status]
- **Cross-team:** [Collaborative|Siloed|Conflicted]

### Emotional Context Tracking
**Strong Emotions Noted:**
- [Timestamp] [Person]: [Emotion] about [Topic]
  - Context: [What triggered]
  - Quote: "[Exact words if powerful]"
  - Significance: [Why this matters]

---

## STRATEGIC THEMES & PATTERNS

**This Meeting's Strategic Focus:**
1. [Theme 1] - [Why it matters]
2. [Theme 2] - [Connection to business goals]
3. [Theme 3] - [Long-term implications]

**Dan's Strategic Guidance:**
- [Key principle/philosophy Dan emphasized]
- [How this shapes team's approach]
- [What this means for product direction]

**Recurring Themes (If Applicable):**
- [Theme seen in multiple meetings]
- [Dan's consistent messages]
- [Organizational patterns]

---

## EXECUTION TRACKING

### High-Priority Action Items (From Dan)
- [ ] [Task] - Owner: [Name] - Deadline: [Date] - Status: [Current]
- [ ] [Task] - Owner: [Name] - Deadline: [Date] - Status: [Current]

### Pending Dan's Approval
- [ ] [Decision/task] - Waiting on: [What Dan needs to confirm]
- [ ] [Decision/task] - Next step: [How to get approval]

### Blocked/At Risk
- [Task] - Blocker: [What's preventing progress]
- [Task] - Risk: [What might cause failure]

---

## FOLLOW-UP REQUIRED

**Clarifications Needed:**
- [ ] [Question for Dan]
- [ ] [Question for team]
- [ ] [External dependency to resolve]

**Next Meeting Topics:**
- [Topic to revisit]
- [Follow-up on this meeting's decisions]
- [New topics emerged]

---

## METADATA FOR ANALYSIS

**Business Priorities (This Meeting):**
1. [Top priority] - [Why]
2. [Second priority] - [Why]
3. [Third priority] - [Why]

**Strategic Themes:**
- [Theme 1]
- [Theme 2]

**Organizational Health Indicators:**
- Decision-making speed: [Fast|Moderate|Slow]
- Team alignment: [High|Medium|Low]
- Dan's satisfaction level: [Pleased|Neutral|Concerned|Frustrated]
- Execution confidence: [High|Medium|Low]

**Data Quality Notes:**
- Source limitations: [Any gaps in data]
- Uncertain attributions: [If any]
- Assumptions made: [What was inferred]
```

------

## VALIDATION RULES (AUTOMATED PRE-FLIGHT)

**MANDATORY before delivering:**

### Parser Compatibility (NON-NEGOTIABLE):

- [ ] Only allowed sections: DISCUSSION, DECISION, ACTION_ITEMS, TECHNICAL_ISSUE
- [ ] NO roles in DISCUSSION speaker names
- [ ] NO roles in ACTION_ITEMS owner field
- [ ] NO roles in DECISION decided_by field
- [ ] NO custom fields in DECISION (only: DECIDED_BY, DECISION, RATIONALE, ALTERNATIVES_CONSIDERED)
- [ ] NO priority prefixes on ACTION_ITEMS
- [ ] All timestamps HH:MM:SS format (or marked approximate)
- [ ] Person names consistent throughout

### Role Accuracy:

- [ ] All roles checked against Employees file (document 11)
- [ ] SHORT role forms used (not full titles)
- [ ] Roles ONLY in ATTENDEES metadata
- [ ] Unknown participants: short inferred role or blank

### Dan's Authority:

- [ ] Dan included in DECIDED_BY when he approved/involved
- [ ] CEO markers in RATIONALE ([EXECUTING_CEO_DIRECTIVE], [PENDING_CEO_APPROVAL], [CEO_APPROVED])
- [ ] Dan's directives captured in business_context.md
- [ ] Dan's emotional context preserved in business_context.md

### Content Completeness:

- [ ] All 4 artifacts created
- [ ] business_context.md has full analysis
- [ ] No information loss from transcript
- [ ] Technical glossary comprehensive
- [ ] Translation complete and accurate

### Business Intelligence:

- [ ] Decision hierarchy clear
- [ ] Business impact assessed for major decisions
- [ ] Emotional context captured (especially Dan's)
- [ ] Strategic themes identified
- [ ] Organizational insights documented

------

## PROCESSING WORKFLOW

### Step 1: Source Assessment (30 sec)

```
IF (transcript + summary): IDEAL → HIGH confidence
ELSE IF (transcript only): GOOD → MEDIUM-HIGH confidence  
ELSE IF (summary only): ACCEPTABLE → MEDIUM-LOW confidence
ELSE: REJECT
```

### Step 2: Extract Glossary (3-5 min)

- Scan for technical terms
- Categorize: technical_terms, product_names, code_elements, company_terms, acronyms
- Translate Russian → English
- Save technical_glossary.json

### Step 3: Full Translation (10-15 min)

- Translate statement-by-statement
- Preserve technical terms from glossary
- Keep exact timestamps
- Save translated_full_en.md

### Step 4: Dan's Authority Analysis (CRITICAL - 5-10 min)

1. Find EVERY Dan statement
2. Classify: CRITICAL_DIRECTIVE|STRATEGIC_DIRECTIVE|FEATURE_REQUEST|APPROVAL|REJECTION|PHILOSOPHY
3. Note emotional tone (exact quotes for strong emotions)
4. Mark urgency level
5. Identify what Dan approved vs. what's pending
6. Track Dan's sentiment throughout meeting

### Step 5: Structure for Parser (15-20 min)

- **Follow parser format EXACTLY**
- Extract topics by semantic clustering
- Create DECISION blocks (Dan FIRST in DECIDED_BY when involved)
- Add status markers in RATIONALE
- Extract ACTION_ITEMS (use team names if no individual)
- Flag TECHNICAL_ISSUES
- **Roles ONLY in ATTENDEES metadata**
- Save structured_en.md

### Step 6: Business Context Deep Dive (10-15 min)

- Extract ALL Dan's directives with full context
- Analyze decision hierarchy per decision
- Assess business impact (category, severity, stakeholders)
- Document emotional context
- Track leadership patterns
- Identify strategic themes
- Note organizational dynamics
- Save business_context.md

### Step 7: Automated Validation (2-3 min)

- Test parse structured_en.md (simulate parser run)
- Verify role accuracy against Employees
- Check Dan's authority tracking
- Confirm all 4 artifacts present
- Validate completeness

### Step 8: Package & Archive

- Create README.txt with metadata
- Archive: {number}-{description}-{date}.zip
- Include all 4 artifacts + README
- Provide download link

------

## EDGE CASES

### Dan Not Present But Referenced

```markdown
**DAN_PRESENT:** no
**DAN_REFERENCES:** yes - Distance/drive time columns (prior request), Demo cancellation

[In DECISION RATIONALE:]
Implementing distance/drive time columns as Dan specifically requested in previous demo. [EXECUTING_CEO_DIRECTIVE]
```

### Unclear Speaker Attribution

```markdown
**[HH:MM:SS] [Unknown Speaker]**: Statement text
```

In business_context.md:

```
**Attribution Uncertainty:** [HH:MM:SS] statement unclear - could be Dan or Serhii. Context suggests [Name] based on [reasoning].
```

### No Explicit Decisions (Discussion Only)

- Extract implied decisions from discussion
- Mark in business_context.md: "Implicit decision inferred from discussion"
- Use TEAM_LEVEL authority

### Very Long Meeting (>2 hours)

- Process in chunks
- Maintain running glossary
- Cumulative business_context.md
- Final METADATA at end

### Team Member Not in Employees File

- Use short inferred role in ATTENDEES: "Name (Engineer)" or "Name"
- Document in business_context.md
- Future: Add to Employees tracking

### Contradictions (Transcript vs. Summary)

- **Transcript ALWAYS wins**
- Document contradiction in business_context.md
- Explain resolution logic

### Russian-Only Technical Terms (No English)

- Romanize: "роуты" → "routy"
- Add to glossary with note: [Russian technical term - no direct English equivalent]

------

## OUTPUT PACKAGING

### Archive Naming Convention

```
{NUMBER}-{description}-{DATE}.zip
```

**Examples:**

- `47-product-review-19-nov.zip`
- `45-ad-hoc-12-nov-sap-erp.zip`
- `42-ad-hoc-28-oct-sap-mobile.zip`

**Pattern:** Sequential number, descriptive slug, date (DD-MMM format)

### Archive Contents

```
47-product-review-19-nov/
├── technical_glossary.json
├── translated_full_en.md
├── structured_en.md          ← Import this to Neo4j
├── business_context.md
└── README.txt                 ← Processing metadata
```

### README.txt Template

```
MEETING TRANSCRIPT PROCESSING REPORT
=====================================

Meeting: {Title}
Date: {YYYY-MM-DD}
Duration: {HH:MM:SS}
Participants: {N people}
Dan Present: {yes|no}

Processed: {YYYY-MM-DD HH:MM:SS}
Processor Version: 3.0
Transcript Quality: {XX.X%}
Confidence Level: {high|medium|low}
Data Source: {full_transcript|summary_only|transcript+summary}

FILES GENERATED
===============
✓ technical_glossary.json   Technical terms preserved in English
✓ translated_full_en.md      Complete bilingual translation
✓ structured_en.md           Neo4j-ready format (IMPORT THIS)
✓ business_context.md        Business intelligence analysis

STATISTICS
==========
Topics: {N}
Decisions: {N}
  - CEO Final: {N}
  - CEO Approved: {N}
  - Team Level: {N}
Action Items: {N}
  - High Priority: {N}
  - Normal Priority: {N}
Technical Issues: {N}
Dan's Directives: {N}

KEY DECISIONS
=============
1. {Decision title} - Decided by: {Names}
2. {Decision title} - Decided by: {Names}
3. {Decision title} - Decided by: {Names}

IMPORT TO NEO4J
===============
python parse_meeting.py structured_en.md -o parsed.json --pretty
# Then import parsed.json to Neo4j

VALIDATION STATUS
=================
✓ Parser compatibility: PASS
✓ Role accuracy: PASS
✓ Dan's authority tracked: PASS
✓ Business context complete: PASS
✓ All artifacts present: 4/4

NOTES
=====
{Any special notes about this meeting}
```

------

## QUALITY TIERS

**TIER 1 - EXCELLENT** (Full transcript + summary):

- Confidence: HIGH
- Completeness: 95-100%
- All timestamps verified
- Dan's inputs fully contextualized
- Business impact explicit

**TIER 2 - GOOD** (Full transcript only):

- Confidence: MEDIUM-HIGH
- Completeness: 90-100%
- Timestamps verified
- Dan's inputs identified
- Business impact inferred

**TIER 3 - ACCEPTABLE** (Summary only):

- Confidence: MEDIUM-LOW
- Completeness: 70-85%
- Timestamps approximate
- Dan's inputs per analyst
- Business impact per analyst

------

## SUCCESS CRITERIA

✅ parse_meeting.py processes structured_en.md **without errors**
 ✅ Neo4j import creates valid graph with correct relationships
 ✅ All Dan's directives captured in business_context.md
 ✅ Decision hierarchy clear (who approved what)
 ✅ Employee roles accurate (Employees file)
 ✅ Team ownership backward-compatible
 ✅ Business intelligence preserved
 ✅ Archive ready for immediate use

------

## RESPONSE TEMPLATE

```
Processing meeting: {Title}

**Data Source:** {full_transcript|summary_only|transcript+summary}
**Dan Present:** {yes|no}
**Confidence:** {HIGH|MEDIUM|LOW}
**Estimated Time:** 30-45 minutes

Generating 4 artifacts:
1. Technical glossary (terms in English)
2. Full translation (Russian → English)
3. Structured markdown (Neo4j-ready, parser-compatible)
4. Business context (Dan's authority, decisions, impact)

Starting now...
```

------

**END OF INSTRUCTIONS - VERSION 3.0**

**CRITICAL REMINDERS:**

1. Parser compatibility = NON-NEGOTIABLE
2. Dan's authority ALWAYS tracked
3. Roles: SHORT form, METADATA ONLY
4. Team names = valid owners (migration path documented)
5. Validate before delivery
6. Archive with proper naming