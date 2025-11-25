// ========================================
// Neo4j Meeting Insight Queries
// ========================================

// QUERY 1: Dan's Critical Directives Tracker
// Shows all CEO_FINAL_DECISION directives across meetings
MATCH (m:Meeting)-[:ISSUED_DIRECTIVE]->(d:Directive)
WHERE d.authority_level = 'CEO_FINAL_DECISION'
RETURN m.date, d.title, d.urgency, d.assigned_to, d.deadline
ORDER BY m.date;

// QUERY 2: Topic Evolution Across Meetings  
// Track how Strategic Optimization topic evolved
MATCH (t:Topic)<-[:CONTAINS_TOPIC]-(m:Meeting)
WHERE t.label CONTAINS 'Strategic Optimization'
OPTIONAL MATCH (t)-[:HAS_DECISION]->(d:Decision)
RETURN m.date, t.label, count(d) as decisions
ORDER BY m.date;

// QUERY 3: Action Item Load by Person
// Find who has the most action items and which are pending
MATCH (p:Person)<-[:ASSIGNED_TO]-(a:ActionItem)
RETURN p.name, 
       count(a) as total_items,
       sum(CASE WHEN a.status = 'pending' THEN 1 ELSE 0 END) as pending,
       sum(CASE WHEN a.status = 'in_progress' THEN 1 ELSE 0 END) as in_progress,
       sum(CASE WHEN a.status = 'completed' THEN 1 ELSE 0 END) as completed
ORDER BY pending DESC;

// QUERY 4: Decision Authority Distribution
// See who makes the most decisions
MATCH (d:Decision)-[:DECIDED_BY]->(p:Person)
RETURN p.name, count(d) as decisions_made
ORDER BY decisions_made DESC;

// QUERY 5: Meeting Productivity Trend
// Track decisions and action items per meeting over time
MATCH (m:Meeting)
OPTIONAL MATCH (m)-[:CONTAINS_TOPIC]->(t:Topic)
OPTIONAL MATCH (t)-[:HAS_DECISION]->(d:Decision)
OPTIONAL MATCH (t)-[:HAS_ACTION_ITEM]->(a:ActionItem)
RETURN m.date, m.title,
       count(DISTINCT t) as topics,
       count(DISTINCT d) as decisions,
       count(DISTINCT a) as action_items
ORDER BY m.date;

// QUERY 6: People Collaboration Network
// See who works with whom most often
MATCH (p1:Person)<-[:SPOKEN_BY]-(s:Statement)-[:DISCUSSES]->(t:Topic)
MATCH (p2:Person)<-[:SPOKEN_BY]-(s2:Statement)-[:DISCUSSES]->(t)
WHERE p1.name < p2.name
RETURN p1.name, p2.name, count(DISTINCT t) as shared_topics
ORDER BY shared_topics DESC
LIMIT 20;

// QUERY 7: Urgent Directives Status
// Show all IMMEDIATE urgency items and their assignments
MATCH (d:Directive)
WHERE d.urgency = 'IMMEDIATE'
OPTIONAL MATCH (d)-[:DIRECTIVE_ASSIGNED_TO]->(p:Person)
RETURN d.title, d.issue, d.business_impact, p.name as assigned_to, d.deadline
ORDER BY d.meeting_date DESC;

// QUERY 8: Topic Discussion Intensity
// Find which topics generate the most discussion
MATCH (t:Topic)<-[:DISCUSSES]-(s:Statement)
RETURN t.label, count(s) as statement_count, t.time_range
ORDER BY statement_count DESC
LIMIT 15;

// QUERY 9: Person Activity Over Time
// Track each person's participation across meetings
MATCH (p:Person)<-[:HAS_ATTENDEE]-(m:Meeting)
RETURN p.name, 
       count(m) as meetings_attended,
       p.total_statements as total_statements,
       p.first_seen as first_meeting
ORDER BY meetings_attended DESC;

// QUERY 10: Critical Path - From Directive to Action
// Trace directives to the actions they spawned
MATCH (m:Meeting)-[:ISSUED_DIRECTIVE]->(d:Directive)
MATCH (d)-[:DIRECTIVE_ASSIGNED_TO]->(p:Person)
OPTIONAL MATCH (p)<-[:ASSIGNED_TO]-(a:ActionItem)
WHERE a.topic_id CONTAINS toLower(replace(d.title, ' ', '_'))
RETURN m.date, d.title, p.name, collect(a.description) as related_actions
ORDER BY m.date
LIMIT 20;