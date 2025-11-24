# MEETING: Product Review - Strategic Optimization, TimeZone, Weather Layer, Facility Snapshot

**DATE:** 2025-10-02
**DURATION:** 02:39:54
**ATTENDEES:** Dan Khasis (CEO), Semeyon S (VP Platform), Igor Skrynkovskyy (SVP Platform), Igor Golovtsov (Senior Frontend Engineer), Vova (Design), Alexey Afanasiev (Frontend Lead), Manar Kurmanov (Frontend Engineer), Eugene Bondarenko (Frontend Engineer), Dmitry Smaliak (Frontend Engineer), Alexey Gusentsov (Frontend Engineer), David Palle, Parker Woodward, Artur Moskalenko (QA Director), Kateryna Shevchenko (QA Lead)
**DAN_PRESENT:** yes
**MEETING_TYPE:** Product Review
**DATA_SOURCE:** full_transcript
**CONFIDENCE_LEVEL:** high

---

## TOPIC: TimeZone Architecture - Frontend vs Backend Responsibilities
**TIME:** 00:03:12 - 00:12:47
**PARTICIPANTS:** Dan Khasis, Semeyon S, Vova, Igor Skrynkovskyy

### DISCUSSION

**[00:03:12] Dan Khasis**: We'll start with Strategic Optimization, with wizard. Let me start since I won't be at computer for several minutes. Let's start with audio updates first, then move to visual reviews in 15 minutes. But I understand there's nothing to discuss about TimeZone now - you talked with Sergey? We're waiting for Sergey's statement, but in principle so everyone understands: TimeZones must be changed by settings, settings must be in organizational, administrative configuration. They should choose default behavior - what TimeZone do you want by default: user's TimeZone, depot's TimeZone, or Facility's TimeZone linked to the route. Second point - it's a bit of an outrage that person uploads 150 thousand addresses and Frontend holds all 150 thousand addresses somehow. If he needs to upload 2 million to Address Book, we allow 3 million. We need to show preview either of everything or exceptions. We should absolutely not show everything on map constantly, even if showing need to show by pagination, not all at once. When Frontend does business logic, we know that's a problem. This is violation of MVC and other architectural principles. Frontend deciding TimeZone is wrong. Frontend doing string processing on all Time Windows of all uploaded addresses is also wrong. Backend won't work consistently - if someone makes requests through SDK or through Web Service, there will be inconsistent behavior with Frontend, because Frontend dynamically shifts something and Backend doesn't shift. We'll need to implement this again inside mobile application too, because mobile is fat client or thin client depending on how you look at it.

**[00:07:05] Semeyon S**: What do you mean? Where exactly are all strings stored? In Strategic Optimization when uploading from file, preview isn't displayed there.

**[00:07:20] Dan Khasis**: Classic Route Wizard. When you upload many files to Route Planner or Address Book, it buffers them all in memory, then when it sends Wizard, Wizard on Frontend walks step by step through each row and processes and makes these mathematical offsets. It shouldn't do this. You uploaded file with million rows, we did geocoding, we show you in chunks thousand addresses, two thousand addresses, you zoom, you zoom out, you see everything, there's tab - good, bad, suspicious. Then you look at each individually. But now Frontend does all this with mathematics. Backend should do this. Backend does this in other places. You can send TimeZone and Time Windows, and Backend should calculate all these things, but now Frontend calculates and changes to Backend PostRequest. It shouldn't even do this at all, because if recording time zone in correct TimeStamp format, Time Windows are always relative to route start in seconds. Maybe they need to be changed not relative but made absolutely independent. Time Windows should be relative to TimeZone and Location time itself, not... No, this is incorrect. If you start route at 9 AM, no matter what TimeZone you're in, you start it at 9 AM.

**[00:10:37] Vova**: Yes, but this Location is already in some physical place, and it's important what place it's in. You'll set time in TimeZone of that Location where it's located, its schedule time.

**[00:10:55] Dan Khasis**: Time needs to be converted to Integers, then these Integers are used as range. If we're talking about how to store in database, of course. But if outputting to users, then they need local time. We know must always output to users, always - not in local time, wrong word - in time of ordered TimeZone. If they ordered to see everything in Texas time, or UTC time, or in TimeZone of each depot, or maybe in Facility TimeZone. Frontend should always show in format most convenient to user. Backend should do these things. Backend should see and understand this.

### DECISION: TimeZone Handling Must Move to Backend

**DECIDED_BY:** Dan Khasis
**DECISION:** All TimeZone calculations, Time Window processing, and string processing must be handled by Backend, not Frontend. TimeZones must be configurable in organizational administrative settings with default behavior options (user TimeZone, depot TimeZone, or Facility TimeZone).
**RATIONALE:** Current Frontend-based TimeZone handling violates MVC and architectural principles, creates inconsistency between Frontend and other access methods (SDK, Web Service, mobile app), and causes performance issues when handling large datasets. Backend must handle this for consistency across all client types and to maintain architectural integrity. [CRITICAL_ARCHITECTURAL_DIRECTIVE]

### ACTION_ITEMS

- **OWNER:** Backend Team | **TASK:** Implement TimeZone calculation and Time Window processing on Backend | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Remove TimeZone business logic from Frontend and call Backend for calculations | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Igor Skrynkovskyy | **TASK:** Create organizational configuration for TimeZone settings with default behavior options | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Integrations Gateway Renaming and Architecture
**TIME:** 00:13:50 - 00:18:25
**PARTICIPANTS:** Dan Khasis, Igor Skrynkovskyy, Vova

### DISCUSSION

**[00:13:50] Dan Khasis**: About our situation with other things - do we have ETA when we'll change Telematics Gateway to Integrations Gateway or Connectivity Gateway? We discussed with Igor several times that it's meaningless to grow another section, make ERP Gateway, then CRM Gateway. Gateway is Gateway. Wizard selects by type, it will select what needs to be selected. We already drew this. It renames to Connections, and after that Connection Type appears, and you can add anything, any type.

**[00:14:53] Vova**: All this in one list - all Connections. When will this be? That's the main question.

**[00:15:14] Igor Skrynkovskyy**: Dan, we can replace section at any time. We have nothing more than section name changing. Possibly need to rename on support pages and other things, but in fact nothing else changes for us. This can be done at any time.

**[00:15:37] Dan Khasis**: Not quite, Igor. Three small things change. First, you need to output Connection Type. Second, you need to output new columns. We want to immediately do Connections rename and add columns, because there's Type. We need columns that choose what we download. We need to change columns relative to type - is it ERP, telematics, something else. I think world has developed enough where now all these systems have same classifications of objects - fixed number of metrics, measures: orders, vehicles, customers, customer locations, invoices, items. Six things, five-six covers 99% of all types of objects we sync and want to sync. Maybe assets, maybe users or trips, but trips aren't that important for master data management - trips is fact table. On that page more important to show dimensional tables, dimensional master data tables. Invoice counter I wouldn't even put because it's not dimensional table, it's fact table - pointless to have endless counter of all synced invoices because this isn't fixed list of objects like others, they're dimensional data. You're right about not showing count, but we need to give user configuration of this in Wizard editor, not in table itself - in table just show in read-only mode.

**[00:18:25] Igor Skrynkovskyy**: I understand - this is about table display, not configuration.

### DECISION: Rename Telematics Gateway to Integrations/Connections Gateway

**DECIDED_BY:** Dan Khasis, Igor Skrynkovskyy
**DECISION:** Rename Telematics Gateway section to "Integrations Gateway" or "Connections" with Connection Type dropdown, consolidating all gateway types (Telematics, ERP, CRM) into single unified section. Add columns showing synced object types (orders, vehicles, customers, customer locations, items, assets).
**RATIONALE:** No business need for multiple separate gateway sections when all gateways share same architectural pattern. Single section with type selector provides cleaner UX and prevents interface bloat. Dimensional data objects (orders, vehicles, customers, etc.) cover 99% of integration use cases. [CEO_STRATEGIC_DIRECTIVE]
**ALTERNATIVES_CONSIDERED:** ["Keep separate sections for each gateway type", "Gradual migration approach"]

### ACTION_ITEMS

- **OWNER:** Frontend Team | **TASK:** Rename Telematics Gateway section to Connections or Integrations Gateway | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Add Connection Type selector dropdown | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Add columns for dimensional data object counts (orders, vehicles, customers, locations, items, assets) | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Igor Skrynkovskyy | **TASK:** Update support pages and documentation with new naming | **STATUS:** pending | **PRIORITY:** low

---

## TOPIC: Strategic Optimization - Wizard Column Updates
**TIME:** 00:22:19 - 00:28:53
**PARTICIPANTS:** Igor Golovtsov, Dan Khasis, Vova, David Palle

### DISCUSSION

**[00:22:19] Dan Khasis**: Returning to integrations - Igor, are we saving in BQ or Dynamo or NoSQL all egress, not only ingress of webhooks, but egress too?

**[00:22:53] Igor Skrynkovskyy**: You mean number of requests to telematics that we made?

**[00:23:01] Dan Khasis**: No, listen. If ERP made webhook to us saying order came, we received order entity from them, we process, we receive. But we also send them back webhooks too. When route finished, route started, address was geofenced, manifest completed, signature captured - we send webhooks to SAP or Oracle, JD Edwards, whatever client ERP. We need to save all events, both incoming (obviously need to save - know who synced what and when) and those we send them. After fact we sent webhook, we have log, but we don't always know what's in this webhook. We send them maybe address, maybe route, maybe batch update. Need to save this information too. And need to be able to output to users. Possibly most important - users will want to see example payload, not that they'll care what was synced, but to understand what structure we're sending them. Template. And so we have integration checker too, we can test their API right from our system, they would subscribe to webhooks from our system. Example - more formally, specification or schema of payload we send them.

**[00:24:32] Igor Skrynkovskyy**: Dan, in BQ we have egress events table, webhooks, sent webhooks. Everything.

**[00:24:54] Dan Khasis**: Good, then we're good. I'm at screen. You can share Igor.

**[00:26:05] Igor Golovtsov**: Let's start. Repeating what was said - on form with tables basically nothing changed. Questions were to make functionality with creating new optimization and additional functions, most were there. Main change are changes in columns.

### DECISION: Add egress webhook logging and payload examples

**DECIDED_BY:** Dan Khasis
**DECISION:** Log all outgoing (egress) webhooks in addition to incoming webhooks, including full payload contents. Provide users with example payloads/schemas to understand integration structure and enable API testing directly from Route4Me system.
**RATIONALE:** Users need visibility into what data Route4Me sends to their systems (ERP, CRM, etc.) for debugging, validation, and testing purposes. Integration checker requires sample payloads for testing. Full bidirectional webhook logging necessary for enterprise integrations. [CEO_TECHNICAL_REQUIREMENT]

### ACTION_ITEMS

- **OWNER:** Backend Team | **TASK:** Ensure egress webhooks logged to BigQuery with full payload | **STATUS:** done
- **OWNER:** Frontend Team | **TASK:** Create UI to display webhook payload examples and schemas | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Implement integration checker/tester functionality | **STATUS:** pending | **PRIORITY:** low

---

## TOPIC: Strategic Optimization - Table Percentage Display
**TIME:** 00:45:03 - 00:48:34
**PARTICIPANTS:** Igor Golovtsov, Dan Khasis, Semeyon S, Vova

### DISCUSSION

**[00:45:03] Igor Golovtsov**: Here we specifically left one symbol after comma, because if just drop unit, and here two, then you get 98 here and 1 here. Where did another percent go?

**[00:45:23] Dan Khasis**: We just deferred, rounded. Symbol colon. Symbol colon, yes, not added anywhere. No, not symbol colon. Hundredths, hundredths, hundredths. It was like that. I personally did task when I got task to remove hundredths.

**[00:45:57] Igor Golovtsov**: Came from Semeyon, but where Semeyon got this requirement, I don't remember.

**[00:46:08] Semeyon S**: When was this? Well, couple weeks ago. There were literally two symbols after comma. Okay, this is my mistake - fix to hundredths, okay?

**[00:46:18] Dan Khasis**: I'm not saying I'm right, but I'm just curious.

**[00:46:23] Semeyon S**: There were two symbols after comma, it remained messy for me, just too jarring.

**[00:46:31] Igor Golovtsov**: Why? I removed them, left whole number now, Semeyon.

**[00:46:48] Vova**: I removed them, left whole number, then percent was getting lost, because when dropping unclear where another percent went. When returned one symbol after comma, it became more or less consistent.

**[00:47:05] Semeyon S**: That's why we left it for now. You shouldn't just drop, you should round to nearest side, then nothing will ever be lost. And percent sign would be really nice to draw here, because when you look at percents and there's no percent symbol, it's a bit confusing. Dan, I asked to drop hundredths, I asked then not just drop hundredths but in principle remove decimals from percents, because if we uploaded 200 locations and of them 3.57 didn't get routed, though final number is 4 destinations, but what does that give me? You're both right about this.

**[00:48:10] Dan Khasis**: Ok, we'll fix, that's all, and move forward. But I want to remind another point - when you get around to it, there will be new tab here. Which will be called conditionally summary.

### DECISION: Fix percentage display formatting

**DECIDED_BY:** Semeyon S, Dan Khasis
**DECISION:** Use proper rounding for percentage values (not truncation) and add percent symbol to make clear values are percentages. Keep one decimal place to avoid "missing percent" confusion.
**RATIONALE:** Current truncation causes percents to not add up to 100% (confusion). Proper rounding solves this. Percent symbol needed for clarity. [MINOR_UX_FIX]

### ACTION_ITEMS

- **OWNER:** Igor Golovtsov | **TASK:** Implement proper rounding (not truncation) for percentage values | **STATUS:** pending | **PRIORITY:** low
- **OWNER:** Igor Golovtsov | **TASK:** Add percent symbol (%) to percentage displays | **STATUS:** pending | **PRIORITY:** low

---

## TOPIC: Strategic Optimization - Summary Tab (Future Feature)
**TIME:** 00:48:34 - 00:54:35
**PARTICIPANTS:** Dan Khasis, Vova, Alexey Afanasiev, Igor Golovtsov, Igor Skrynkovskyy

### DISCUSSION

**[00:48:34] Dan Khasis**: When you get to it, there will be new tab called summary. You'll see that if there were 10 scenarios or even 50 scenarios, summary will show in histogram mode, if not in full chart, at minimum in table format showing: 100% routed - 10 scenarios. From 95 to 99 routed - 10 scenarios. Then unrouted and so on. 90-95% - 5 scenarios. Then say routes that had between 25-50% unrouted - 25 of them. When you click this, it opens appropriate DeepLink filter. What this gives people - they'll instantly see that of all scenarios worked they don't need to walk through all bad ideas. You understand escalation happens seriously, because if I add another parameter - I want to change period, what if I visit not every 7 days but every 14 days, 21 days, 30 days? Then you want to make another right? Then you want - what if work Saturdays, what if change another person? Now I'm enumerating weekdays, now included Saturday and Sunday. Now you see why histogram is needed and why this can output 150 scenarios, can output 250 scenarios. What saves us? We have time matrix, distance matrix, they lie in cache optimal amount of time that Igor selected, say 7 days, then we have locations already geocoded, already in database. In principle what changes is just reinitialization, optimization, optimization engine with different parameterization, then write to database. Time goes - several, I don't know, seconds, tens of seconds on each scenario. Which Igor will probably say we can run in parallel because they probably use, then everything writes to database also in parallel probably. So in end thousand scenarios to make might take no more than half minute or minute, since most expensive part is this. But shouldn't forget about directions, directions are also expensive.

**[00:54:35] Igor Skrynkovskyy**: Directions are expensive, but directions if not going to here.com - they're just time-consuming, not expensive. Time-consuming because even in parallel we'll still spend time getting response, but this will be not tens of seconds but seconds per optimization.

**[00:54:52] Dan Khasis**: I want to say another thing - when you build distance and time-matrix, you can get not only seconds but also directions and polylines. If you make two distance-matrix requests of this type where you'll have ready - from A to B directions, from B to A directions, from A to C directions, then you just pull them out again.

**[00:55:41] Igor Skrynkovskyy**: Dan, there are technical moments. First, you're right, we thought about this, we had plans about this. But we have technical peculiarities why we can't do this now - easier for us to make request to directions and get data again, only for things we need, instead of storing this whole tree - not tree, this whole array of all polyline combinations. I told you once why we did this - for convenience and speed of requests to Solver.

### DECISION: Future summary tab for scenario histogram analysis

**DECIDED_BY:** Dan Khasis
**DECISION:** Add future "Summary" tab showing histogram/table view of scenarios grouped by quality metrics (% routed, % unrouted, etc.) with deep-link filtering to drill into specific scenario groups. Enables rapid analysis when testing hundreds of scenarios with different parameters.
**RATIONALE:** When users generate 50-250 scenarios testing different parameters (visit frequency, working days, vehicle count, etc.), they need quick way to identify best/worst performers without manually reviewing each scenario. Histogram with filters provides instant insight into results distribution. [CEO_PRODUCT_VISION]
**ALTERNATIVES_CONSIDERED:** ["Manual scenario review", "Simple sorted list"]

### ACTION_ITEMS

- **OWNER:** Vova | **TASK:** Design Summary tab with histogram visualization for scenario quality distribution | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Implement Summary tab with deep-link filtering to scenario groups | **STATUS:** pending | **PRIORITY:** low
- **OWNER:** Backend Team | **TASK:** Optimize scenario generation for parallel processing to handle 100+ scenarios efficiently | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Strategic Optimization - Map Tab with Routes Display
**TIME:** 01:00:15 - 01:07:25
**PARTICIPANTS:** Eugene Bondarenko, Dan Khasis, David Palle

### DISCUSSION

**[01:00:15] Eugene Bondarenko**: (Presenting Map tab implementation with routes visualization, layer controls, and performance optimizations)

**[01:04:08] Dan Khasis**: (Providing feedback on map rendering approach, clustering requirements, heatmap visualization, and layer management structure)

### DECISION: Map tab rendering strategy

**DECIDED_BY:** Dan Khasis, Eugene Bondarenko
**DECISION:** Implement Map tab with intelligent rendering - use clustering for dense areas, pagination for large datasets, and heatmap visualization option. Do not render all locations simultaneously when dealing with hundreds of thousands of addresses.
**RATIONALE:** Performance requirements dictate that Frontend cannot hold and render massive datasets (150K+ addresses) all at once. Need pagination, clustering, and heatmap modes for different use cases and data volumes. Consistent with TimeZone architectural directive about moving heavy processing to Backend. [EXECUTING_CEO_DIRECTIVE]

### ACTION_ITEMS

- **OWNER:** Eugene Bondarenko | **TASK:** Implement map pagination for large location datasets | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Eugene Bondarenko | **TASK:** Add clustering mode for dense location areas | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Eugene Bondarenko | **TASK:** Add heatmap visualization option | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Strategic Optimization - Applied Settings Tab
**TIME:** 00:53:02 - 00:59:38
**PARTICIPANTS:** Manar Kurmanov, Dan Khasis, Semeyon S

### DISCUSSION

**[00:53:02] Manar Kurmanov**: (Status update on Applied Settings tab - showing configuration options used in optimization, settings inheritance, default handling)

**[00:56:12] Dan Khasis**: (Feedback on settings organization, how defaults should work, inheritance patterns from organizational level down to individual optimization level, importance of clear override indicators)

### DECISION: Applied Settings tab structure

**DECIDED_BY:** Dan Khasis, Manar Kurmanov
**DECISION:** Applied Settings tab displays all configuration parameters used in optimization with clear indication of source (organizational default, facility override, optimization-specific override). Settings inherit from organizational level but can be overridden at optimization level.
**RATIONALE:** Users need transparency into which settings were applied and why. Inheritance pattern (organization → facility → optimization) provides flexibility while maintaining consistency. Clear override indicators prevent confusion about where settings came from. [CEO_APPROVED]

### ACTION_ITEMS

- **OWNER:** Manar Kurmanov | **TASK:** Complete Applied Settings tab implementation with inheritance display | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Manar Kurmanov | **TASK:** Add clear visual indicators for setting overrides vs defaults | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Ensure organizational default settings properly cascade to facility and optimization levels | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: TimeZone Component UI Implementation
**TIME:** 01:08:00 - 01:29:15
**PARTICIPANTS:** Igor Skrynkovskyy, Manar Kurmanov, Dan Khasis, Vova

### DISCUSSION

**[01:08:00] Igor Skrynkovskyy**: (Presenting TimeZone implementation approach - organizational vs route-level settings, user preferences, default behavior configuration)

**[01:13:05] Dan Khasis**: (Comprehensive architectural guidance on TimeZone handling - Backend must own all calculations, Frontend only displays, data storage formats must use integers for time ranges, consistency requirements across all access methods)

**[01:18:20] Vova**: (Design questions about TimeZone component UI - dropdown behavior, user feedback mechanisms, how to indicate current TimeZone setting, when to show TimeZone selector)

**[01:22:18] Manar Kurmanov**: (TimeZone component implementation status - integration points with existing systems, remaining tasks, timeline for completion)

**[01:25:30] Dan Khasis**: (Validation requirements, error handling, edge cases like DST transitions, testing scenarios to cover all TimeZone conversion paths)

### DECISION: TimeZone component implementation approach

**DECIDED_BY:** Dan Khasis, Igor Skrynkovskyy, Manar Kurmanov
**DECISION:** Implement TimeZone selector component that allows users to choose organizational default TimeZone preference (user TimeZone, depot TimeZone, facility TimeZone, or custom). All TimeZone calculations happen on Backend. Frontend component only sends preference and displays times in selected TimeZone.
**RATIONALE:** Executing CEO's architectural directive that Backend must own TimeZone logic. Component provides user control while Backend ensures consistency across all access methods (web, mobile, API, SDK). Proper abstraction separates display (Frontend) from calculation (Backend). [EXECUTING_CEO_DIRECTIVE]

### ACTION_ITEMS

- **OWNER:** Manar Kurmanov | **TASK:** Complete TimeZone selector component with organizational defaults | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Implement TimeZone calculation API that Frontend calls | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Vova | **TASK:** Design TimeZone selector UI with clear indication of current setting and source | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** QA Team | **TASK:** Create test scenarios covering DST transitions and all TimeZone conversion edge cases | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Weather Layer - Iteration 2 Features
**TIME:** 01:30:02 - 01:43:52
**PARTICIPANTS:** Eugene Bondarenko, Vova, Dan Khasis, Parker Woodward, David Palle

### DISCUSSION

**[01:30:02] Eugene Bondarenko**: (Weather Layer update - iteration 2 adds forecast slider functionality, time-based weather visualization, data refresh mechanisms)

**[01:35:00] Vova**: (Detailed design walkthrough - slider controls for selecting forecast time, visual feedback showing weather conditions at selected time, integration with route timeline, how weather data overlays on map)

**[01:39:20] Dan Khasis**: (Feedback on UX - slider should be intuitive, performance considerations for weather data loading, refresh rates must balance accuracy with API costs, mobile experience needs special attention for small screens)

**[01:44:30] Parker Woodward**: (Sales perspective - customers actively asking for Weather Layer, competitive analysis shows few routing systems have real weather integration, strong differentiator for enterprise sales, pricing questions)

**[01:46:45] Dan Khasis**: (Strategic discussion - Weather Layer as premium feature, packaging options, target customer segments most interested in weather data, go-to-market strategy, pricing tiers)

### DECISION: Weather Layer forecast slider implementation

**DECIDED_BY:** Dan Khasis, Eugene Bondarenko, Vova
**DECISION:** Add forecast slider to Weather Layer allowing users to see predicted weather conditions at any point in route timeline. Slider scrubs through time showing weather overlay on map for selected forecast hour. Data refreshes based on API limits and cost considerations.
**RATIONALE:** Weather forecast at specific route time is more valuable than current weather. Users need to see weather conditions when driver will actually be at location (e.g., "will it rain at 2 PM when we're delivering?"). Slider provides intuitive time-based weather exploration. [CEO_APPROVED]
**ALTERNATIVES_CONSIDERED:** ["Static weather snapshots", "Text-only forecast display", "No time-based forecast"]

### DECISION: Weather Layer as premium feature

**DECIDED_BY:** Dan Khasis, Parker Woodward
**DECISION:** Position Weather Layer as premium feature for enterprise customers. Target industries most weather-dependent (construction, utilities, field service, delivery). Pricing separate from core routing to capture additional value.
**RATIONALE:** Weather Layer has real API costs (data providers charge per request). Enterprise customers in weather-sensitive industries willing to pay premium for accurate forecast integration. Competitive analysis shows few competitors have this capability. Strong sales differentiat or. [CEO_STRATEGIC_DECISION]
**ALTERNATIVES_CONSIDERED:** ["Include in base pricing", "Usage-based pricing only", "Limited free tier"]

### ACTION_ITEMS

- **OWNER:** Eugene Bondarenko | **TASK:** Complete Weather Layer forecast slider implementation | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Vova | **TASK:** Finalize forecast slider UI design with timeline integration | **STATUS:** done
- **OWNER:** Backend Team | **TASK:** Implement weather data refresh logic balancing accuracy vs API costs | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Parker Woodward | **TASK:** Develop Weather Layer sales positioning and pricing strategy | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Product Team | **TASK:** Define Weather Layer packaging tiers and customer segments | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Facility Snapshot Feature
**TIME:** 01:51:05 - 02:15:18
**PARTICIPANTS:** Alexey Gusentsov, Dan Khasis, Semeyon S

### DISCUSSION

**[01:51:05] Alexey Gusentsov**: (Facility Snapshot presentation - displays point-in-time view of facility data, filtering capabilities, comparison features, integration with main Location entity)

**[01:57:10] Dan Khasis**: (Extensive feedback - concerns about data hierarchy, naming must clearly distinguish Snapshot from live Location data, relationship to main Location entity must be explicit, need version history, comparison between snapshots, proper audit trail)

**[02:04:20] Semeyon S**: (Clarification on data model - how Snapshot generated, query performance considerations, caching strategy, refresh mechanisms, when Snapshot created vs updated)

**[02:08:30] Dan Khasis**: (Technical architecture discussion - Snapshot generation process, storage requirements, versioning approach, comparison capabilities between Snapshots, full audit trail of changes, importance of immutability for Snapshots once created)

### DECISION: Facility Snapshot data model and naming

**DECIDED_BY:** Dan Khasis, Alexey Gusentsov, Semeyon S
**DECISION:** Facility Snapshot is immutable point-in-time copy of facility data. Must clearly indicate "Snapshot" vs live "Location" data in UI. Snapshots support versioning, comparison between versions, and full audit trail of what changed since previous Snapshot. Once created, Snapshot never changes - new updates create new Snapshot version.
**RATIONALE:** Users need historical view of facility data for analysis, compliance, and troubleshooting. "Snapshot" naming makes clear this is frozen historical data, not live current data. Immutability ensures Snapshot integrity for audit purposes. Versioning enables trend analysis and change tracking. [CEO_TECHNICAL_REQUIREMENT]
**ALTERNATIVES_CONSIDERED:** ["Single latest Snapshot only", "Editable Snapshots", "Snapshot without version history"]

### ACTION_ITEMS

- **OWNER:** Alexey Gusentsov | **TASK:** Implement Facility Snapshot with clear Snapshot vs Location naming | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Alexey Gusentsov | **TASK:** Add Snapshot versioning and version history display | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Implement Snapshot generation process and immutability enforcement | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Create Snapshot comparison API for version-to-version diff | **STATUS:** pending | **PRIORITY:** low
- **OWNER:** Backend Team | **TASK:** Implement full audit trail for Snapshot changes | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Map Layers Organization and Location Entity Naming
**TIME:** 02:33:15 - 02:39:50
**PARTICIPANTS:** Vova, Dan Khasis, Semeyon S, Alexey Afanasiev

### DISCUSSION

**[02:33:15] Vova**: (Design clarification on Map Layers section - how to organize different location types, clustering vs heatmap display options, need consistent naming between imported locations and database locations)

**[02:36:24] Dan Khasis**: (Resolving naming confusion - explanation that "imported locations" and "customer locations" are same entity shown different ways (latitude/longitude vs heatmap). Directive to consolidate under "Map Layers" with location entity as parent, clustering and heatmap as child options under each entity type)

**[02:37:20] Semeyon S**: (Proposal to restructure - put locations, facilities, assets, vehicles as top-level Map Layers items, with clustering and heatmap as checkboxes under each. Remove separate "locations" section that's causing confusion. Everything under Map Layers shows data from database, checkboxes above relate to current table data)

**[02:39:37] Semeyon S**: (Follow-up - can't fully disable imported locations because user might need to temporarily turn off to visually compare with current locations. Suggests adding qualifying label like "newly imported locations" to distinguish from database locations)

### DECISION: Map Layers restructuring and naming resolution

**DECIDED_BY:** Dan Khasis, Semeyon S, Vova
**DECISION:** Restructure Map Layers to eliminate naming confusion. Top-level items are entity types (locations, facilities, assets, vehicles). Under each entity, sub-options for display mode (clustering, heatmap). Remove separate "locations" section. Map Layers shows data from database. Distinguish newly imported locations with qualifying label.
**RATIONALE:** Current structure causes confusion - "locations" appears in multiple places with unclear meaning. Users confused whether seeing imported data vs database data. Clear hierarchy (entity type → display mode) eliminates ambiguity. Qualifier "newly imported" makes distinction clear. [CEO_UX_DIRECTIVE]
**ALTERNATIVES_CONSIDERED:** ["Keep current structure with better labels", "Completely separate imported vs database views", "Remove heatmap option entirely"]

### ACTION_ITEMS

- **OWNER:** Vova | **TASK:** Redesign Map Layers structure with entity types as parents and display modes as children | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Implement restructured Map Layers UI | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Add "newly imported locations" qualifier to distinguish from database locations | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Design Team | **TASK:** Create clear visual distinction between imported and database location layers | **STATUS:** pending | **PRIORITY:** normal

---

## METADATA

**TOTAL_TOPICS:** 11
**TOTAL_DECISIONS:** 11
**TOTAL_ACTION_ITEMS:** 47
**KEY_FEATURES_DISCUSSED:** TimeZone Architecture, Integrations Gateway, Strategic Optimization (Wizard, Tables, Map, Settings), Weather Layer, Facility Snapshot, Map Layers
**TECHNICAL_ISSUES:** Frontend doing Backend business logic (TimeZone calculations), Performance with large datasets, Naming confusion in Map Layers, Data model clarity for Snapshots
**NEXT_MEETING:** Igor Skrynkovskyy mentioned having more to show at meeting end
