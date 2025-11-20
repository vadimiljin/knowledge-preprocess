#!/usr/bin/env python3
"""
Meeting Transcript to Knowledge Graph Parser
Parses structured markdown meeting transcripts into JSON format for knowledge graph ingestion.
"""

import re
import json
from datetime import datetime
from typing import Dict, List, Any
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class Node:
    """Base class for all node types"""
    id: str
    type: str


@dataclass
class Meeting(Node):
    title: str
    date: str
    duration: str
    attendees: List[str]
    purpose: str = ""


@dataclass
class Person(Node):
    name: str
    statements_count: int = 0


@dataclass
class Topic(Node):
    label: str
    time_range: str
    participants: List[str]
    keywords: List[str]


@dataclass
class Statement(Node):
    speaker_id: str
    timestamp: str
    text: str
    sequence: int
    topic_id: str


@dataclass
class Decision(Node):
    description: str
    decided_by: str
    rationale: str
    alternatives: List[str]
    topic_id: str


@dataclass
class ActionItem(Node):
    description: str
    owner_id: str
    status: str
    priority: str
    deadline: str
    topic_id: str


@dataclass
class Relationship:
    """Represents a relationship between two nodes"""
    type: str
    from_id: str
    to_id: str
    properties: Dict[str, Any]


class MeetingParser:
    """Parses structured markdown meeting transcripts into knowledge graph JSON"""
    
    def __init__(self):
        self.nodes = {
            "meetings": [],
            "people": {},
            "topics": [],
            "statements": [],
            "decisions": [],
            "action_items": []
        }
        self.relationships = []
        self.sequence_counter = 0
        self.current_topic_id = None
        self.meeting_id = None
        
    def generate_id(self, prefix: str, identifier: str = None) -> str:
        """Generate a unique ID for a node"""
        if identifier:
            # Clean identifier for ID usage
            clean_id = re.sub(r'[^a-zA-Z0-9_]', '_', identifier.lower())
            return f"{prefix}_{clean_id}"
        return f"{prefix}_{datetime.now().timestamp()}_{self.sequence_counter}"
    
    def parse_file(self, filepath: str) -> Dict[str, Any]:
        """Parse markdown file and return knowledge graph JSON"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse meeting header
        self._parse_meeting_header(content)
        
        # Parse topics and their content
        self._parse_topics(content)
        
        # Build output structure
        return self._build_output()
    
    def _parse_meeting_header(self, content: str):
        """Extract meeting metadata from header"""
        # Extract meeting title
        title_match = re.search(r'^# MEETING: (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Untitled Meeting"
        
        # Extract date
        date_match = re.search(r'\*\*DATE:\*\* (.+)$', content, re.MULTILINE)
        date = date_match.group(1).strip() if date_match else ""
        
        # Extract duration
        duration_match = re.search(r'\*\*DURATION:\*\* (.+)$', content, re.MULTILINE)
        duration = duration_match.group(1).strip() if duration_match else ""
        
        # Extract attendees
        attendees_match = re.search(r'\*\*ATTENDEES:\*\* (.+)$', content, re.MULTILINE)
        attendees = []
        if attendees_match:
            attendees = [name.strip() for name in attendees_match.group(1).split(',')]
        
        # Create meeting node
        self.meeting_id = self.generate_id("meeting", f"{date}_{title}")
        meeting = Meeting(
            id=self.meeting_id,
            type="Meeting",
            title=title,
            date=date,
            duration=duration,
            attendees=attendees
        )
        self.nodes["meetings"].append(meeting)
        
        # Create person nodes and relationships
        for attendee in attendees:
            person_id = self.generate_id("person", attendee)
            if person_id not in self.nodes["people"]:
                self.nodes["people"][person_id] = Person(
                    id=person_id,
                    type="Person",
                    name=attendee
                )
                # Create HAS_ATTENDEE relationship
                self.relationships.append(Relationship(
                    type="HAS_ATTENDEE",
                    from_id=self.meeting_id,
                    to_id=person_id,
                    properties={}
                ))
    
    def _parse_topics(self, content: str):
        """Parse all topics and their subsections"""
        # Split by topic headers - capture everything up to next topic or end
        topic_pattern = r'## TOPIC: (.+?)\n\*\*TIME:\*\* (.+?)\n\*\*PARTICIPANTS:\*\* (.+?)\n(.*?)(?=\n## TOPIC:|\n## METADATA|\Z)'
        topic_matches = re.finditer(topic_pattern, content, re.DOTALL)
        
        for topic_match in topic_matches:
            topic_label = topic_match.group(1).strip()
            time_range = topic_match.group(2).strip()
            participants_str = topic_match.group(3).strip()
            
            # Extract full topic content (group 4)
            topic_content = topic_match.group(4)
            
            # Create topic ID
            topic_id = self.generate_id("topic", topic_label)
            
            # Parse participants
            participants = [p.strip() for p in participants_str.split(',')]
            
            # Extract keywords from topic label
            keywords = self._extract_keywords(topic_label)
            
            # Create topic node
            topic = Topic(
                id=topic_id,
                type="Topic",
                label=topic_label,
                time_range=time_range,
                participants=participants,
                keywords=keywords
            )
            self.nodes["topics"].append(topic)
            
            # Create CONTAINS relationship
            self.relationships.append(Relationship(
                type="CONTAINS_TOPIC",
                from_id=self.meeting_id,
                to_id=topic_id,
                properties={"time_range": time_range}
            ))
            
            # Store current topic for statements
            self.current_topic_id = topic_id
            
            # Parse discussion statements
            self._parse_discussion(topic_content, topic_id)
            
            # Parse decisions
            self._parse_decisions(topic_content, topic_id)
            
            # Parse action items
            self._parse_action_items(topic_content, topic_id)
            
            # Parse technical issues
            self._parse_technical_issues(topic_content, topic_id)
    
    def _parse_discussion(self, content: str, topic_id: str):
        """Parse discussion statements"""
        # First find DISCUSSION section
        discussion_pattern = r'### DISCUSSION\n(.+?)(?=\n###|\n---|\Z)'
        discussion_match = re.search(discussion_pattern, content, re.DOTALL)
        
        if not discussion_match:
            return
        
        discussion_content = discussion_match.group(1)
        
        # Pattern: **[timestamp] Speaker:** text
        statement_pattern = r'\*\*\[(.+?)\] (.+?):\*\* (.+?)(?=\n\n|\n\*\*\[|\Z)'
        
        for match in re.finditer(statement_pattern, discussion_content, re.DOTALL):
            timestamp = match.group(1).strip()
            speaker_name = match.group(2).strip()
            text = match.group(3).strip()
            
            # Create person if not exists
            speaker_id = self.generate_id("person", speaker_name)
            if speaker_id not in self.nodes["people"]:
                self.nodes["people"][speaker_id] = Person(
                    id=speaker_id,
                    type="Person",
                    name=speaker_name
                )
            
            # Update statement count
            self.nodes["people"][speaker_id].statements_count += 1
            
            # Create statement node
            statement_id = self.generate_id("statement", f"{speaker_name}_{timestamp}")
            self.sequence_counter += 1
            
            statement = Statement(
                id=statement_id,
                type="Statement",
                speaker_id=speaker_id,
                timestamp=timestamp,
                text=text,
                sequence=self.sequence_counter,
                topic_id=topic_id
            )
            self.nodes["statements"].append(statement)
            
            # Create relationships
            self.relationships.extend([
                Relationship(
                    type="SPOKEN_BY",
                    from_id=statement_id,
                    to_id=speaker_id,
                    properties={"timestamp": timestamp}
                ),
                Relationship(
                    type="DISCUSSES",
                    from_id=statement_id,
                    to_id=topic_id,
                    properties={"sequence": self.sequence_counter}
                )
            ])
            
            # Create NEXT relationship with previous statement if exists
            if len(self.nodes["statements"]) > 1:
                prev_statement = self.nodes["statements"][-2]
                if prev_statement.topic_id == topic_id:
                    self.relationships.append(Relationship(
                        type="NEXT",
                        from_id=prev_statement.id,
                        to_id=statement_id,
                        properties={}
                    ))
    
    def _parse_decisions(self, content: str, topic_id: str):
        """Parse decision blocks"""
        decision_pattern = r'### DECISION: (.+?)\n\*\*DECIDED_BY:\*\* (.+?)\n\*\*DECISION:\*\* (.+?)\n\*\*RATIONALE:\*\* (.+?)(?:\n\*\*ALTERNATIVES_CONSIDERED:\*\* (.+?))?(?=\n###|\n---|\Z)'
        
        for match in re.finditer(decision_pattern, content, re.DOTALL):
            label = match.group(1).strip()
            decided_by = match.group(2).strip()
            description = match.group(3).strip()
            rationale = match.group(4).strip()
            alternatives_str = match.group(5).strip() if match.group(5) else ""
            
            # Parse alternatives
            alternatives = []
            if alternatives_str:
                # Extract from list format like ["option1", "option2"]
                alt_match = re.findall(r'"([^"]+)"', alternatives_str)
                alternatives = alt_match if alt_match else []
            
            # Create decision node
            decision_id = self.generate_id("decision", label)
            decision = Decision(
                id=decision_id,
                type="Decision",
                description=description,
                decided_by=decided_by,
                rationale=rationale,
                alternatives=alternatives,
                topic_id=topic_id
            )
            self.nodes["decisions"].append(decision)
            
            # Create relationships
            self.relationships.extend([
                Relationship(
                    type="HAS_DECISION",
                    from_id=topic_id,
                    to_id=decision_id,
                    properties={"label": label}
                ),
                Relationship(
                    type="DECIDED_BY",
                    from_id=decision_id,
                    to_id=self.generate_id("person", decided_by),
                    properties={}
                )
            ])
    
    def _parse_action_items(self, content: str, topic_id: str):
        """Parse action items"""
        # First find ACTION_ITEMS section
        action_section_pattern = r'### ACTION_ITEMS\n(.+?)(?=\n---|\n##|\Z)'
        action_section_match = re.search(action_section_pattern, content, re.DOTALL)
        
        if not action_section_match:
            return
        
        action_content = action_section_match.group(1)
        
        # Pattern: - **OWNER:** name | **TASK:** description | **STATUS:** status | **PRIORITY:** priority
        action_pattern = r'- \*\*OWNER:\*\* (.+?) \| \*\*TASK:\*\* (.+?)(?: \| \*\*STATUS:\*\* (.+?))?(?: \| \*\*PRIORITY:\*\* (.+?))?(?: \| \*\*DEADLINE:\*\* (.+?))?(?=\n-|\n\n|\Z)'
        
        for match in re.finditer(action_pattern, action_content, re.DOTALL):
            owner = match.group(1).strip()
            task = match.group(2).strip()
            status = match.group(3).strip() if match.group(3) else "pending"
            priority = match.group(4).strip() if match.group(4) else "normal"
            deadline = match.group(5).strip() if match.group(5) else ""
            
            # Create action item node
            action_id = self.generate_id("action", task[:30])
            action_item = ActionItem(
                id=action_id,
                type="ActionItem",
                description=task,
                owner_id=self.generate_id("person", owner),
                status=status,
                priority=priority,
                deadline=deadline,
                topic_id=topic_id
            )
            self.nodes["action_items"].append(action_item)
            
            # Create relationships
            self.relationships.extend([
                Relationship(
                    type="HAS_ACTION_ITEM",
                    from_id=topic_id,
                    to_id=action_id,
                    properties={}
                ),
                Relationship(
                    type="ASSIGNED_TO",
                    from_id=action_id,
                    to_id=self.generate_id("person", owner),
                    properties={"status": status, "priority": priority}
                )
            ])
    
    def _parse_technical_issues(self, content: str, topic_id: str):
        """Parse technical issue blocks as special decision type"""
        issue_pattern = r'### TECHNICAL_ISSUE: (.+?)\n(.+?)(?=\n###|\n##|\Z)'
        
        for match in re.finditer(issue_pattern, content, re.DOTALL):
            label = match.group(1).strip()
            description = match.group(2).strip()
            
            # Create as decision node with special type
            issue_id = self.generate_id("issue", label)
            issue = Decision(
                id=issue_id,
                type="TechnicalIssue",
                description=description,
                decided_by="Team",
                rationale="Technical constraint identified during discussion",
                alternatives=[],
                topic_id=topic_id
            )
            self.nodes["decisions"].append(issue)
            
            # Create relationship
            self.relationships.append(Relationship(
                type="HAS_TECHNICAL_ISSUE",
                from_id=topic_id,
                to_id=issue_id,
                properties={"label": label}
            ))
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract keywords from text"""
        # Simple keyword extraction - split on common separators
        words = re.split(r'[&,\-\s]+', text.lower())
        # Filter out common words and short words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
        keywords = [w.strip() for w in words if len(w) > 2 and w not in stop_words]
        return keywords[:5]  # Limit to 5 keywords
    
    def _build_output(self) -> Dict[str, Any]:
        """Build final JSON output structure"""
        return {
            "metadata": {
                "processed_at": datetime.now().isoformat(),
                "schema_version": "1.0",
                "parser_version": "1.0.0"
            },
            "nodes": {
                "meetings": [asdict(m) for m in self.nodes["meetings"]],
                "people": [asdict(p) for p in self.nodes["people"].values()],
                "topics": [asdict(t) for t in self.nodes["topics"]],
                "statements": [asdict(s) for s in self.nodes["statements"]],
                "decisions": [asdict(d) for d in self.nodes["decisions"]],
                "action_items": [asdict(a) for a in self.nodes["action_items"]]
            },
            "relationships": [
                {
                    "type": r.type,
                    "from": r.from_id,
                    "to": r.to_id,
                    "properties": r.properties
                }
                for r in self.relationships
            ],
            "statistics": {
                "total_nodes": sum(len(nodes) if isinstance(nodes, list) else len(nodes) 
                                 for nodes in self.nodes.values()),
                "total_relationships": len(self.relationships),
                "node_counts": {
                    "meetings": len(self.nodes["meetings"]),
                    "people": len(self.nodes["people"]),
                    "topics": len(self.nodes["topics"]),
                    "statements": len(self.nodes["statements"]),
                    "decisions": len(self.nodes["decisions"]),
                    "action_items": len(self.nodes["action_items"])
                }
            }
        }


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Parse structured meeting transcript to knowledge graph JSON'
    )
    parser.add_argument(
        'input_file',
        help='Path to structured markdown file'
    )
    parser.add_argument(
        '-o', '--output',
        default='meeting_graph.json',
        help='Output JSON file path (default: meeting_graph.json)'
    )
    parser.add_argument(
        '--pretty',
        action='store_true',
        help='Pretty print JSON output'
    )
    
    args = parser.parse_args()
    
    # Parse the meeting transcript
    print(f"Parsing meeting transcript: {args.input_file}")
    meeting_parser = MeetingParser()
    
    try:
        graph_data = meeting_parser.parse_file(args.input_file)
        
        # Write output
        with open(args.output, 'w', encoding='utf-8') as f:
            if args.pretty:
                json.dump(graph_data, f, indent=2, ensure_ascii=False)
            else:
                json.dump(graph_data, f, ensure_ascii=False)
        
        print(f"\n✓ Successfully parsed meeting transcript")
        print(f"✓ Output written to: {args.output}")
        print(f"\nStatistics:")
        print(f"  - Total nodes: {graph_data['statistics']['total_nodes']}")
        print(f"  - Total relationships: {graph_data['statistics']['total_relationships']}")
        print(f"\nNode breakdown:")
        for node_type, count in graph_data['statistics']['node_counts'].items():
            print(f"  - {node_type}: {count}")
        
    except Exception as e:
        print(f"✗ Error parsing file: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
