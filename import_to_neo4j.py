#!/usr/bin/env python3
"""
Unified import script for meeting data and business context into Neo4j.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any
from neo4j import GraphDatabase


class Neo4jMeetingImporter:
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.person_mapping = {}  # Track persons across meetings
        
    def close(self):
        self.driver.close()
    
    def clear_database(self):
        """Clear all existing data."""
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
            print("✓ Database cleared")
    
    def import_meeting_data(self, graph_json_path: str):
        """Import a single meeting's graph JSON."""
        with open(graph_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        with self.driver.session() as session:
            # Import Meeting nodes
            for meeting in data['nodes']['meetings']:
                session.run("""
                    MERGE (m:Meeting {id: $id})
                    SET m.title = $title,
                        m.date = date($date),
                        m.duration = $duration,
                        m.attendees = $attendees,
                        m.purpose = $purpose
                """, **meeting)
            
            # Import Person nodes with merge strategy
            for person in data['nodes']['people']:
                session.run("""
                    MERGE (p:Person {name: $name})
                    ON CREATE SET p.id = $id,
                                  p.first_seen = date($first_seen),
                                  p.meetings_attended = 1,
                                  p.total_statements = $statements_count
                    ON MATCH SET p.meetings_attended = p.meetings_attended + 1,
                                 p.total_statements = p.total_statements + $statements_count
                """, name=person['name'], id=person['id'], 
                     first_seen=data['nodes']['meetings'][0]['date'],
                     statements_count=person['statements_count'])
            
            # Import Topic nodes
            for topic in data['nodes']['topics']:
                session.run("""
                    CREATE (t:Topic {
                        id: $id,
                        label: $label,
                        time_range: $time_range,
                        participants: $participants,
                        keywords: $keywords
                    })
                """, **topic)
            
            # Import Statement nodes
            for statement in data['nodes']['statements']:
                session.run("""
                    CREATE (s:Statement {
                        id: $id,
                        speaker_id: $speaker_id,
                        timestamp: $timestamp,
                        text: $text,
                        sequence: $sequence,
                        topic_id: $topic_id
                    })
                """, **statement)
            
            # Import Decision nodes
            for decision in data['nodes']['decisions']:
                session.run("""
                    CREATE (d:Decision {
                        id: $id,
                        description: $description,
                        decided_by: $decided_by,
                        rationale: $rationale,
                        alternatives: $alternatives,
                        topic_id: $topic_id
                    })
                """, **decision)
            
            # Import ActionItem nodes
            for action in data['nodes']['action_items']:
                session.run("""
                    CREATE (a:ActionItem {
                        id: $id,
                        description: $description,
                        owner_id: $owner_id,
                        status: $status,
                        priority: $priority,
                        deadline: $deadline,
                        topic_id: $topic_id
                    })
                """, **action)
            
            # Import Relationships
            for rel in data['relationships']:
                session.run("""
                    MATCH (from {id: $from_id})
                    MATCH (to {id: $to_id})
                    CALL apoc.create.relationship(from, $type, $props, to) YIELD rel
                    RETURN rel
                """, from_id=rel['from'], to_id=rel['to'],
                     type=rel['type'], props=rel.get('properties', {}))
            
        print(f"✓ Imported meeting from: {graph_json_path}")
    
    def import_business_context(self, context_json_path: str, meeting_id: str):
        """Import business context data."""
        with open(context_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        with self.driver.session() as session:
            # Import Directive nodes
            for directive in data['nodes']['directives']:
                session.run("""
                    CREATE (d:Directive {
                        id: $id,
                        number: $number,
                        title: $title,
                        timestamp: $timestamp,
                        directive_type: $directive_type,
                        authority_level: $authority_level,
                        urgency: $urgency,
                        assigned_to: $assigned_to,
                        deadline: $deadline,
                        issue: $issue,
                        business_impact: $business_impact,
                        impact_severity: $impact_severity,
                        emotion: $emotion,
                        quotes: $quotes,
                        meeting_date: date($meeting_date)
                    })
                """, **directive)
                
                # Link directive to meeting
                session.run("""
                    MATCH (m:Meeting {id: $meeting_id})
                    MATCH (d:Directive {id: $directive_id})
                    CREATE (m)-[:ISSUED_DIRECTIVE]->(d)
                """, meeting_id=meeting_id, directive_id=directive['id'])
                
                # Link directive to assigned person if exists
                if directive['assigned_to']:
                    for person_name in directive['assigned_to'].split(','):
                        person_name = person_name.strip()
                        session.run("""
                            MATCH (p:Person {name: $person_name})
                            MATCH (d:Directive {id: $directive_id})
                            MERGE (d)-[:DIRECTIVE_ASSIGNED_TO]->(p)
                        """, person_name=person_name, directive_id=directive['id'])
            
            # Import LeadershipPattern nodes
            for pattern in data['nodes']['leadership_patterns']:
                session.run("""
                    MERGE (p:Person {name: $name})
                    ON MATCH SET p.role = $role,
                                 p.takes_initiative = $takes_initiative,
                                 p.seeks_approval = $seeks_approval,
                                 p.authority_scope = $authority_scope
                """, **pattern)
        
        print(f"✓ Imported business context from: {context_json_path}")
    
    def create_cross_meeting_relationships(self):
        """Create relationships between entities across meetings."""
        with self.driver.session() as session:
            # Link topics with similar labels across meetings
            session.run("""
                MATCH (t1:Topic)
                MATCH (t2:Topic)
                WHERE t1.label = t2.label AND id(t1) < id(t2)
                MERGE (t1)-[:RELATED_TOPIC]->(t2)
            """)
            
            print("✓ Created cross-meeting relationships")
    
    def get_statistics(self) -> Dict[str, int]:
        """Get import statistics."""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (n)
                RETURN labels(n)[0] as label, count(n) as count
                ORDER BY count DESC
            """)
            
            stats = {record['label']: record['count'] for record in result}
            
            rel_result = session.run("""
                MATCH ()-[r]->()
                RETURN type(r) as type, count(r) as count
                ORDER BY count DESC
            """)
            
            rel_stats = {record['type']: record['count'] for record in rel_result}
            
            return {"nodes": stats, "relationships": rel_stats}


def main():
    # Configuration
    NEO4J_URI = "bolt://localhost:7687"
    NEO4J_USER = "neo4j"
    NEO4J_PASSWORD = "YourPassword123"  # Change this to your password
    
    BASE_DIR = Path("/home/vadim/Projects/route4me.com/knowledge_preprocess")
    
    # Initialize importer
    importer = Neo4jMeetingImporter(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
    
    try:
        # Clear existing data
        print("\n=== Clearing existing data ===")
        importer.clear_database()
        
        # Find all meeting directories
        meeting_dirs = sorted([d for d in BASE_DIR.iterdir() 
                              if d.is_dir() and d.name.startswith('26-') or 
                                 d.is_dir() and d.name.startswith('3') or
                                 d.is_dir() and d.name.startswith('4')])
        
        print(f"\n=== Found {len(meeting_dirs)} meeting directories ===\n")
        
        # Import each meeting
        for meeting_dir in meeting_dirs:
            print(f"\nProcessing: {meeting_dir.name}")
            
            # Import graph JSON
            graph_json = meeting_dir / "graph.json"
            if graph_json.exists():
                importer.import_meeting_data(str(graph_json))
            else:
                print(f"  ⚠ Warning: graph.json not found in {meeting_dir.name}")
            
            # Import business context if available
            context_json = meeting_dir / "business_context.json"
            if context_json.exists():
                # Extract meeting ID from graph.json
                with open(graph_json, 'r') as f:
                    graph_data = json.load(f)
                    meeting_id = graph_data['nodes']['meetings'][0]['id']
                
                importer.import_business_context(str(context_json), meeting_id)
            else:
                print(f"  ℹ Info: business_context.json not found (optional)")
        
        # Create cross-meeting relationships
        print("\n=== Creating cross-meeting relationships ===")
        importer.create_cross_meeting_relationships()
        
        # Print statistics
        print("\n=== Import Statistics ===")
        stats = importer.get_statistics()
        
        print("\nNodes:")
        for label, count in stats['nodes'].items():
            print(f"  {label}: {count}")
        
        print("\nRelationships:")
        for rel_type, count in stats['relationships'].items():
            print(f"  {rel_type}: {count}")
        
        print("\n✓ Import complete! Access Neo4j Browser at http://localhost:7474")
        
    finally:
        importer.close()


if __name__ == "__main__":
    main()