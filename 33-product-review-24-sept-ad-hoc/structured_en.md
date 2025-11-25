# MEETING: Product Review Ad Hoc - Asset Management Architecture Design

**DATE:** 2024-09-24
**DURATION:** 01:26:13
**ATTENDEES:** Dan Khasis (CEO), Igor Skrynkovskyy (SVP Platform), Serhii Kasainov (Front-End Tech Lead)
**DAN_PRESENT:** yes
**MEETING_TYPE:** Ad-Hoc Technical Design Session
**DATA_SOURCE:** full_transcript+summary
**CONFIDENCE_LEVEL:** high

---

## TOPIC: Asset Management Schema Architecture Design
**TIME:** 00:00:25 - 00:35:27
**PARTICIPANTS:** Dan Khasis, Igor Skrynkovskyy

### DISCUSSION

**[00:00:25] Dan Khasis**: Starting with the type of thing. We currently have attributes incorrectly fixed at vehicle level. Although it's not only a vehicle, can be any thing - generator, excavator and so on. If we look at the diagram, we have asset. Asset saved in asset master list, where there's some unique physical thing. This physical thing has attributes in Entity Attribute Value pattern, where such asset has such attribute with such value. This attribute type from Attribute Types table - instead of fixed columns in Vehicles table for hardcoded attributes, this saves by rows, so you can have 0 or unlimited attributes per asset. If you need to add attribute types, don't need to modify columns and constantly modify code base for elastic indexing.

**[00:06:20] Igor Skrynkovskyy**: But then shouldn't this be an operational metric?

**[00:06:24] Dan Khasis**: No, because this is more like weight of machine, it's a constant. We want 6000 revolutions per minute limit there, and how many specific revolutions we save in another place. This describes attribute for saving acceptable deviations or ranges.

**[00:06:56] Igor Skrynkovskyy**: Shouldn't we then select some other group or class for this attribute, so it's clear these are limits or limitation?

**[00:07:14] Dan Khasis**: Good point, we can do that. This opens second topic - there's third table, attribute type categories. Very elementary table. Category of attribute types so you can dynamically output grouped attribute types from backend on frontend, don't need to hardcode columns. If we have these columns, we can make new category - fifth one, operating guidelines and specifications.

**[00:08:29] Igor Skrynkovskyy**: Dan, shouldn't we make these IDs UUID or something else right away? Because customer might come and say I want to create my own categories.

**[00:08:55] Dan Khasis**: We can, but I don't want to do this now. I want to do most primitive thing - we classify categories, and this is quite fixed. Then this will be another thing later. Customer has ability to categorize other things.

**[00:12:22] Igor Skrynkovskyy**: We have table route for me asset groups with field bin 16, asset group type id. What is this field responsible for?

**[00:13:18] Dan Khasis**: Asset groups allows each user to classify their assets into groups they personally want. You have master asset list, asset has attributes, N number of attributes. This asset simultaneously has type - one type. And asset can be in arbitrarily created groups. Then there's linking between asset and groups. Like search groups, arbitrarily generated, like semantics of some word. For example, Minsk region - you took all assets, threw in generators of nuclear power plant into Minsk region. Now you have Minsk region group. Like arbitrary grouping. Assets and groups links this ID with this group.

**[00:15:22] Igor Skrynkovskyy**: Returning to this table - this group type ID field. What value should be here?

**[00:16:22] Dan Khasis**: I need to think. Probably there was reason why I did this. Maybe initially I wanted to make if this is logical group or physical group, maybe I forgot to delete this. I did this in middle of night. I'll comment it out for now.

**[00:17:35] Igor Skrynkovskyy**: Physical group, logical group - why these two values? They can't be both physical and logical simultaneously.

**[00:17:46] Dan Khasis**: I was thinking about this. I don't have good answer, but I have gut feeling it can be both at same time. In hospital there is equipment - ventilators, monitors, pumps. They are all physically in same department where surgical procedures performed. And logically they are all grouped on same vertical.

### DECISION: Entity Attribute Value Pattern for Assets

**DECIDED_BY:** Dan Khasis
**DECISION:** Implement Entity Attribute Value pattern for asset management instead of fixed columns approach used in vehicles table
**RATIONALE:** CEO-level architectural decision for maximum flexibility. EAV pattern allows unlimited attributes per asset without schema modifications, eliminating constant code base changes for elastic indexing. Enables support for diverse asset types across new market verticals without database restructuring. [CEO_APPROVED]
**ALTERNATIVES_CONSIDERED:** ["Continue with fixed columns in vehicles table", "Create separate tables for each asset type"]

### DECISION: Asset Categorization Hierarchy

**DECIDED_BY:** Dan Khasis  
**DECISION:** Implement three-level hierarchy: asset master list, asset types with categories, and user-defined groups
**RATIONALE:** CEO dictating data model architecture. Three-level approach provides both system-level classification and user flexibility. System maintains type taxonomy while allowing arbitrary user grouping for operational needs. [CEO_APPROVED]
**ALTERNATIVES_CONSIDERED:** ["Single-level flat structure", "Two-level type/instance only"]

### DECISION: Attribute Type Categories

**DECIDED_BY:** Dan Khasis, Igor Skrynkovskyy
**DECISION:** Create attribute type categories table for dynamic frontend grouping. Initially fixed categories, future customer-defined categories
**RATIONALE:** Enables dynamic frontend rendering without hardcoded columns. Dan approved phased approach - fixed categories in version 1, customer categories as future enhancement. [CEO_APPROVED]
**ALTERNATIVES_CONSIDERED:** ["UUID-based extensible system from start", "Hardcoded attribute groups"]

### DECISION: Physical and Logical Group Support

**DECIDED_BY:** Dan Khasis
**DECISION:** Support both physical and logical group classifications simultaneously
**RATIONALE:** CEO's gut instinct that assets can be in both physical location grouping and logical operational grouping simultaneously. Hospital equipment example - physically in surgery department, logically on mobile cart. [CEO_APPROVED]

### ACTION_ITEMS

- **OWNER:** Igor Skrynkovskyy | **TASK:** Implement EAV pattern schema for asset management | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Create asset master list, asset attributes, asset attribute values tables | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Create asset types, asset type categories, asset groups tables | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Implement versioning mechanism with is_current, effective_from, effective_to fields | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Create polymorphic relationship for asset-to-facility linking | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Dan Khasis | **TASK:** Finalize DDL and provide to team | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Strategic Planner Snapshot UI Requirements
**TIME:** 00:35:27 - 00:58:46
**PARTICIPANTS:** Dan Khasis, Serhii Kasainov, Igor Skrynkovskyy

### DISCUSSION

**[00:35:27] Dan Khasis**: Moving to Strategic Planner. Read-only snapshot must be stylistically and functionally identical to Route List. User should see familiar table with routes and fully interactive map. This is critical sales blocker.

**[00:40:15] Serhii Kasainov**: New developer already working on read-only version of snapshot. We discussed performance issues with hundreds of routes on map.

**[00:42:30] Dan Khasis**: Map in separate tab - I support Vova's idea to put map in separate tab so it takes maximum space and is convenient for analysis. This is exactly what we need.

**[00:45:22] Dan Khasis**: Snapshot critically missing filters by day and week. User must be able to click on cell in matrix results and immediately see on map and in table all routes for that specific day. This is fundamental requirement.

**[00:50:18] Dan Khasis**: Need to implement ability to select multiple routes - for example, same route for different weeks - and compare them on one map. Like in e-commerce when you compare cameras, you click "add to compare" and it shows side-by-side comparison.

**[00:55:30] Serhii Kasainov**: We do this in routes view. In locations. In routes simply, where Vova's mockup, he made map as separate tab, and he specifically explained why to me. Because there's timeline, and you rotate this map by days.

**[00:56:06] Dan Khasis**: That's obvious. This is one view, but this is completely different thing when I want to look at specific thing, I click on it. I can't just take and select and compare two things after filtering. I must have ability to check them side-by-side. Map that he drew will never allow to do first route, second route. Because clients want to see how route looks first day second week, first day 23rd week, first day 24th week. They don't believe, they want to see with their own eyes side-by-side.

**[01:00:04] Serhii Kasainov**: But this is on one map with different routes. Or how is this?

**[01:00:04] Dan Khasis**: I see that if you click on each route, like in scope, it instantly shows you high-level overview, or you can, like when you buy, for example, you went, you want to buy digital camera, and now I click add to compare, I click compare and instantly it compares them. That's what this is about. We don't have this. I can't turn this on now. I can do it here, but route comparison is still legacy but nevertheless it works.

### DECISION: Strategic Planner Snapshot UI Design

**DECIDED_BY:** Dan Khasis
**DECISION:** Read-only snapshot must copy Route List UI/UX exactly - table view, interactive map in separate tab, full filtering capabilities
**RATIONALE:** CEO dictating critical sales blocker resolution. Current snapshot is uninformative and prevents demos. Copying proven Route List design ensures usability and leverages existing user familiarity. [CRITICAL_DIRECTIVE]
**ALTERNATIVES_CONSIDERED:** ["Custom snapshot-specific UI", "Simplified report view"]

### DECISION: Day and Week Filtering

**DECIDED_BY:** Dan Khasis
**DECISION:** Add filters by day and week that activate when user clicks matrix results cells
**RATIONALE:** CEO identifying fundamental missing requirement. Users must click matrix cell and immediately see filtered routes for that day/week on map and table. This is baseline functionality for scenario analysis. [CRITICAL_DIRECTIVE]

### DECISION: Route Comparison Feature

**DECIDED_BY:** Dan Khasis
**DECISION:** Implement multi-route selection and side-by-side comparison on single map, similar to e-commerce product comparison
**RATIONALE:** CEO demanding competitive feature. Clients don't believe optimization results without visual proof. Need ability to select multiple instances of same route across different time periods and visually compare side-by-side. Legacy route comparison exists but needs modernization. [CEO_APPROVED]

### ACTION_ITEMS

- **OWNER:** Frontend Team | **TASK:** Implement snapshot UI copying Route List design | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Add interactive map in separate tab for snapshot | **STATUS:** in_progress | **PRIORITY:** high  
- **OWNER:** Frontend Team | **TASK:** Implement day/week filtering activated by matrix cell clicks | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Create multi-route selection and side-by-side comparison feature | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Optimize map rendering for hundreds of routes using existing approaches | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: GPS Data Quality Issues and BigQuery Integration
**TIME:** 00:58:46 - 01:03:24  
**PARTICIPANTS:** Dan Khasis, Semeyon (referenced), Igor Skrynkovskyy

### DISCUSSION

**[00:58:46] Dan Khasis**: Semeyon presented analysis confirming low quality GPS tracks from Amwaste client. iOS mobile app not working in background mode, which breaks analytics and product functionality. Most data from mobile devices very sparse, points come mainly on arrival at location, indicating users closing app.

**[01:00:30] Dan Khasis**: Must immediately restore Foreground Service for iOS that was previously disabled. Without it, tracking data is useless. Need to start collecting metrics on mobile app session duration. This will prove to client that problem is their drivers closing app.

**[01:02:15] Dan Khasis**: Critical directive - all GPS data must immediately start being recorded to BigQuery. This will unlock huge possibilities for advanced analytics that are currently blocked. This is priority.

### DECISION: Restore iOS Foreground Service

**DECIDED_BY:** Dan Khasis
**DECISION:** Immediately restore Foreground Service functionality in iOS app to enable background GPS tracking
**RATIONALE:** CEO directive to fix critical data quality issue. Foreground Service was previously disabled but is essential for continuous tracking. Current sparse data from Amwaste proves background tracking failure. Without this, product analytics are broken. [CRITICAL_DIRECTIVE]

### DECISION: Mobile Session Analytics

**DECIDED_BY:** Dan Khasis
**DECISION:** Implement collection and analysis of mobile app active session duration metrics
**RATIONALE:** CEO ordering proof mechanism. Need data to demonstrate to clients that problem is driver behavior closing app, not system malfunction. Session metrics provide objective evidence. [CEO_APPROVED]

### DECISION: BigQuery GPS Data Integration

**DECIDED_BY:** Dan Khasis
**DECISION:** Prioritize and implement export of all GPS data to BigQuery
**RATIONALE:** CEO strategic directive for analytics infrastructure. BigQuery integration unlocks advanced analytics capabilities currently impossible. This is foundational for future data science initiatives. [CRITICAL_DIRECTIVE]

### ACTION_ITEMS

- **OWNER:** Mobile Team | **TASK:** Restore Foreground Service implementation in iOS app | **STATUS:** pending | **PRIORITY:** high | **DEADLINE:** immediate
- **OWNER:** Backend Team | **TASK:** Implement mobile app session duration tracking and analytics | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Design and implement GPS data export pipeline to BigQuery | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Flexible Service Time and Time Window Logic
**TIME:** 01:03:24 - 01:15:30
**PARTICIPANTS:** Dan Khasis, Serhii Kasainov, Igor Skrynkovskyy

### DISCUSSION

**[01:03:24] Dan Khasis**: New critical business requirement discovered in client meeting. System must support scenarios where service time significantly exceeds time window duration. For many operations - unloading 10 tons of sand, servicing complex equipment - important thing is arriving on site within time window, for example 13:00 to 14:00 while gate is open. Actual work can take 3-5 hours and go far beyond this window.

**[01:06:45] Dan Khasis**: Competitive advantage - none of competitors support this logic. Their systems will throw error if service time exceeds time window duration. Implementing this "small thing" gives huge advantage. Opens doors to clients in heavy logistics, construction, service industries.

**[01:10:20] Serhii Kasainov**: So we need to modify validation logic to only check arrival time within window, not service completion time?

**[01:11:15] Dan Khasis**: Exactly. Need to add option at constraint level that allows system to validate only arrival time in time window, ignoring service end time. When calculating overall route, service time - for example 5 hours - must be correctly accounted for planning subsequent stops.

### DECISION: Flexible Time Window Validation

**DECIDED_BY:** Dan Khasis
**DECISION:** Modify optimization and validation logic to support service time exceeding time window duration, validating only arrival time
**RATIONALE:** CEO identifying unique competitive advantage from client discussion. Real-world scenarios require arrival during restricted access window but service extending beyond. Current competitor systems fail this use case. Implementing this unlocks heavy logistics, construction, and service maintenance verticals. [CEO_APPROVED]
**ALTERNATIVES_CONSIDERED:** ["Maintain current strict time window validation", "Split long services into multiple stops"]

### ACTION_ITEMS

- **OWNER:** Backend Team | **TASK:** Add constraint-level option for flexible time window validation | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Modify validation logic to check only arrival time within time window | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Ensure service time properly accounts in route calculation for subsequent stops | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Route Comparison Legacy System Issues  
**TIME:** 01:15:30 - 01:23:49
**PARTICIPANTS:** Dan Khasis, Serhii Kasainov, Igor Skrynkovskyy

### DISCUSSION

**[01:15:30] Serhii Kasainov**: We have route comparison somewhere but interface broken. Something we broke today.

**[01:16:45] Dan Khasis**: Here grouping should also be by facility type. Open console please. Feels like one API call died.

**[01:18:00] Dan Khasis**: Look at customers view. Here need to output number of locations, number of assets will appear. Then I open customer locations. I'll group not just by customer but also, for example, number of assets will appear. Then I'll open new thing that will have assets, and it will be almost copy of vehicles.

**[01:20:15] Dan Khasis**: I'll open telematics connections, there will be new tab, now sync assets. GPS Inside PS should be capital letters Samsara. Sync customer data appears. Should appear sync routes, and then needed, mute is on, and should be sync assets. I would make another section, when we do sync HOS, I'll make model for this too. HOS - this is all when people worked, when driver sat at wheel, tracks this, because this will affect everything.

**[01:21:23] Dan Khasis**: Here everything crashed too. Here grouping should also be by facility type.

**[01:23:49] Dan Khasis**: I need to make small break, then find out who's picking up child, then marketing call will be, and other things.

### TECHNICAL_ISSUE: Route Comparison UI Broken

**[01:15:30] Serhii Kasainov**: Route comparison interface broken. Something broke during today's deployment. List that should have 25 elements not appearing. No output, nothing else.

**[01:16:45] Dan Khasis**: Console shows possible API call failure. Grouping by facility type also missing. Multiple UI elements not rendering properly.

### ACTION_ITEMS

- **OWNER:** Frontend Team | **TASK:** Debug and fix route comparison UI broken in today's deployment | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Add sync assets tab to telematics connections interface | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Add number of assets field to customers and customer locations views | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Plan HOS sync model and implementation | **STATUS:** pending | **PRIORITY:** low

---

## TOPIC: Meeting Wrap-up and Next Steps
**TIME:** 01:23:49 - 01:26:13
**PARTICIPANTS:** Dan Khasis, Igor Skrynkovskyy, Serhii Kasainov

### DISCUSSION

**[01:23:54] Igor Skrynkovskyy**: I understood everything except comparison of scenarios, how to fit this in one screen.

**[01:24:00] Serhii Kasainov**: You showed example in online store, they specifically do this with separate pages, and you have up to five columns there.

**[01:24:07] Dan Khasis**: Yes, absolutely right, you select up to five, and then you click view, and then fullscreen comparison opens that has all metrics, pivot, same as old one always had. So it's clear that from first click something will open. Okay, I need to make small break, then find out who's picking up child, then marketing call, and other things.

**[01:25:06] Igor Skrynkovskyy**: Okay, thanks for interview. Igor, anything else, any questions?

**[01:25:12] Dan Khasis**: No look, no more questions, I must, I think, one more table for invoicing and SQLite for invoicing. I think invoicing first version ready.

**[01:25:23] Igor Skrynkovskyy**: Good, but then send final DDL with these values and so on, so we don't lose it anywhere. So we finally finalize and say we're ready to work.

**[01:25:42] Dan Khasis**: You're ready to work, just there might be one more table needed for something.

**[01:25:56] Igor Skrynkovskyy**: Good, but we started work anyway. If everything works out, I'll tell you tomorrow. We have very interesting things related to AI. If it works out, I'll tell you tomorrow. Thanks, bye.

### ACTION_ITEMS

- **OWNER:** Dan Khasis | **TASK:** Send final DDL for asset management schema | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Dan Khasis | **TASK:** Add invoicing table to schema if needed | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Igor Skrynkovskyy | **TASK:** Report on AI-related developments tomorrow | **STATUS:** pending | **PRIORITY:** normal

---

## METADATA

**TOTAL_TOPICS:** 6
**TOTAL_DECISIONS:** 10
**TOTAL_ACTION_ITEMS:** 22
**KEY_FEATURES_DISCUSSED:** Asset Management EAV Pattern, Strategic Planner Snapshot UI, Route Comparison, GPS Data Quality, BigQuery Integration, Flexible Time Windows, Telematics Sync
**TECHNICAL_ISSUES:** Route comparison UI broken, iOS background tracking disabled, sparse GPS data from Amwaste
**CRITICAL_CEO_DIRECTIVES:** BigQuery integration, Foreground Service restoration, Snapshot UI redesign, Flexible time window logic
