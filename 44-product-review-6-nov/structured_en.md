# MEETING: Product Review - Strategic Planning & Feature Releases

**DATE:** 2025-11-06  
**DURATION:** 03:01:25  
**ATTENDEES:** Dan Khasis (CEO), Serhii Kasainov (Frontend Lead), Igor Skrynkovskyy (SVP Platform), Semeyon S (VP Platform), Vova (UI/UX), Alexey Gusentsov (Frontend Engineer), Igor Golovtsov (Senior Frontend Engineer), Manar Kurmanov (Frontend Engineer), Alexey Afanasiev (Frontend Lead), Artur Moskalenko (QA Director), Davron Usmonov (Frontend Engineer), Alex Shulga (QA), Mihail Krivulya (Backend Engineer), Volodymyr Ishchenko (QA), Maksym Silman (QA), Oleg Pravyk (QA)  
**DAN_PRESENT:** yes  
**MEETING_TYPE:** Product Review  
**DATA_SOURCE:** full_transcript+summary  
**CONFIDENCE_LEVEL:** high

---

## TOPIC: Destination Snapshot Release Review
**TIME:** 00:03:14 - 00:25:59  
**PARTICIPANTS:** Dan Khasis, Serhii Kasainov, Vova, Alexey Gusentsov, Semeyon S

### DISCUSSION

**[00:03:15] Serhii Kasainov**: Update on snapshots. We finally reached the goal we were working toward for a long time. We've pulled in the tables from routes-list into almost all snapshots. I'll finish today, and all will be complete. Thanks to this, each snapshot, at least for routes and destination, now has all the functionality that wasn't available before. Specifically, full list of filters with search and groupings, actual table groupings. Column groupings, particularly for timezone. The None option - when None is selected, nothing should be written here.

**[00:04:11] Vova**: It should say group by if none is selected. Here it changes to none, and here it disappears completely when none is selected. Group by - let's at least use a dash.

**[00:04:42] Serhii Kasainov**: Grouping disabled, nothing selected. I understand, no questions. Agreed. Where was I? Yes, this menu is available. For now only those three items that were here, now in QA they'll approve this iteration and I'll pull in basically all menu items that exist on routes-list. So on any snapshot with routes table you can work almost the same as on routes. Same for destination. Metrics also became automatically available here. And further on snapshots this same table will be reused everywhere with small adjustments, like on user-snapshot we won't allow filtering by user. Or on facility-snapshot we won't do grouping by facility. These improvements are ready, I think we'll deploy them Monday on routes. And I had a question, Dan, why didn't we release destination-snapshot? I know why we didn't release it. Why? Maybe you'll approve it? There are small fixes of course, but it looks better to me than many other snapshots we already released.

**[00:06:18] Dan Khasis**: Need to look. There was probably a reason, I don't remember the reason. Maybe you remember incorrectly, I remember incorrectly. And now just misunderstanding.

**[00:06:31] Serhii Kasainov**: There's a list of tickets, but again, we'll review them. I just don't remember anything critical there. Is it ideal? No, it's not ideal.

**[00:06:39] Alexey Gusentsov**: There definitely aren't any showstoppers, I remember, there aren't any.

**[00:06:43] Serhii Kasainov**: In any case it looks better than budget optimization. Sorry, internet cut out. Yes, Alexey, happens. It looks better than optimization-snapshot, than user-snapshot and than digital-snapshot. The map adds plus 50%, no plus 70% to attractiveness. Let's maybe release it. If something is really bad, I would quickly fix it today and release tomorrow.

**[00:07:24] Semeyon S**: Let's look at the tickets diagonally after the call.

**[00:07:34] Dan Khasis**: I'm not against releasing anything early or often. I'm just more curious if there's some level of minimal usefulness of this release. For example, we've been trying to launch this unfortunate service time for 6 months. We spent at least an hour on last Monday's meeting about historical service time and all the options associated with it. Pros and cons and how this needs to be considered and how this needs to be done. Okay, so we'll make a destination release. If this destination doesn't have full graphical linking, full link to order, full link to destination, full link to customer, to customer location, to strategic route where all this came from. Then what's the point if we don't show any high-level attributes and so on. For example, in this case you're showing, as I understand, this is a fake order ID, this isn't real?

**[00:09:26] Serhii Kasainov**: I think this is external order ID, these definitely aren't our IDs.

**[00:09:30] Dan Khasis**: And where is our order object?

**[00:09:34] Serhii Kasainov**: We agreed not to show our internal IDs.

**[00:09:38] Dan Khasis**: Not IDs, but our object.

**[00:09:45] Vova**: There should be a transition here.

**[00:09:51] Serhii Kasainov**: That's clear, there should be a link here.

**[00:09:54] Alexey Gusentsov**: Yes, we made links, they should be on order and on customer. I don't know why they're not here, need to investigate, but they definitely should be. Maybe there's such a base, I don't remember.

**[00:10:03] Serhii Kasainov**: On this account there's no order snapshot. Same with customer. This is clear, we can do this very quickly now. There's just already a large volume of work done here. I just remember this wasn't finally approved. Is the layout in order? If there are no obvious comments besides the transition, let's finish it. A large volume of work was done that's just hanging.

**[00:10:27] Dan Khasis**: I'm not arguing, I'm not arguing, but I'm just trying to tell you, imagine you're a user, what's the benefit of this? For example, you're showing a route. I don't know if this is good or bad. Geofence, if this came from Customer Location, and Customer Location came from Geotab, and we don't understand this is from Geotab. First, need to draw the Geotab polygon here. When I talk about graphics, I constantly mean that all these interconnected relationships... What worries me more, what's the point of all this if we tied people's hands behind their back anyway. And by the way, here's this defect. We tied their hands behind their back. If this was an order RouteFormation, we don't link to it. If this was Customer Location, we don't show this. If this was Customer Location with Geotab, we also don't show this. If it had a Geofence, we also don't show it. So what does this screen help people with? Attachments, okay, I agree. Activities, okay, if the filter works, I agree. History, what does History show, I don't understand. What does History show?

**[00:12:22] Artur Moskalenko**: Delivery Attempts.

**[00:12:27] Dan Khasis**: I don't understand what Delivery Attempts means. Is this a copy of Activities?

**[00:12:36] Artur Moskalenko**: Essentially, yes.

**[00:12:41] Dan Khasis**: What's the point of having this then?

**[00:12:42] Serhii Kasainov**: And Activity, including Activity on route.

**[00:12:50] Dan Khasis**: I don't understand how this relates to anything.

**[00:12:52] Maksym Silman**: As far as I remember, History is the historically renamed Notes.

**[00:12:58] Alexey Gusentsov**: No, History is actually Activities, and Activities is Notes, I think.

**[00:13:05] Serhii Kasainov**: I understand. It's just that in any case, to view Destination in this expanded view, we don't have any interface. I have to go to some Editor, open this second sidebar, scroll down, find these same Visit Details. So that I can look at one specific stop in one place, we don't have that. I see.

**[00:13:35] Dan Khasis**: So what are you looking at? We're making a completely new page to see Custom Data?

**[00:13:44] Serhii Kasainov**: We're making snapshots for everything?

**[00:13:48] Dan Khasis**: This is why we make snapshots, to see things in isolation in some summary format? And for what purpose? Is this really to see Custom Data? And for that we need to make a whole snapshot? Wait, I thought... I thought we make snapshots, one, to watch the progression of different iterations. Two, to see how, for example, customer location changed and what it came from, and maybe compare what it was and what it is now. So for example, to see a geofence. Because before they uploaded some crappy polygon, and now we improved it, and we want to see how it improved and why it improved. We're not doing this either yet. But this, I thought, was for these kinds of things. Or for example that we integrated Geotab import, and we want to see the list of polygons or trips that came from Geotab, and what we did with them. And this we don't do. Then what are we doing? I don't understand.

**[00:15:02] Vova**: For example, yes, History tab should show all previous historical visits to this address.

**[00:15:14] Dan Khasis**: Correct. This I understand.

**[00:15:17] Vova**: And Activities - driver notes, proof of visit, and such things.

**[00:15:29] Dan Khasis**: I think in the future there should also be, for example, related invoices, scanned assets, notification history sent to this customer. All this contextual information. But at minimum should be links. To customer, customer location, these things.

**[00:16:02] Serhii Kasainov**: Customer, customer location, order, route - we'll add these links.

**[00:16:15] Dan Khasis**: And by the way geofence. If this destination, for example, this is Customer Location. And this customer location has geofence. And geofence is polygon. So the polygon should be drawn.

**[00:16:44] Vova**: Yes, then some customers have hundreds of geofences on one location. Then we'll overload the map, but okay.

**[00:16:53] Dan Khasis**: Then we'll figure out how to show it best, but it should be shown. Because right now you won't understand anything, you won't see the context. This geofence is one meter or ten meters or hundred meters - you won't know.

### DECISION: Block Destination Snapshot Release

**DECIDED_BY:** Dan  
**DECISION:** Block destination snapshot release until critical contextual links and proper History tab are implemented  
**RATIONALE:** Without links to Order, Customer, Customer Location, Strategic Route, and proper geofence visualization, the snapshot has no practical value to users. The History tab must show historical visits to the address, not activity feed. [CEO_REJECTED current implementation]  
**ALTERNATIVES_CONSIDERED:** ["Release as-is with minor fixes", "Delay indefinitely"]

### ACTION_ITEMS

- **OWNER:** Serhii Kasainov | **TASK:** Add clickable links to Customer and Customer Location on destination snapshot | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Serhii Kasainov | **TASK:** Rework History tab to show all previous visits to address (not activity feed) | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Vova | **TASK:** Redesign Activities tab to show driver notes and proof of visit | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Alexey Gusentsov | **TASK:** Add geofence polygon visualization on map when available | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: SAP Connection Interface Review
**TIME:** 00:26:22 - 00:46:44  
**PARTICIPANTS:** Dan Khasis, Davron Usmonov, Serhii Kasainov, Igor Skrynkovskyy

### DISCUSSION

**[00:26:22] Davron Usmonov**: Showing version zero of new telematics connection type for SAP. This is table showing Atoms entities, not standard Vehicles.

**[00:28:45] Serhii Kasainov**: Previously discussed formatting issues like date format weren't fixed.

**[00:29:15] Dan Khasis**: All technical timestamp fields - created_at, updated_at - must be displayed strictly in UTC to avoid confusion when analyzing logs and transactions. This should be indicated directly in the column header.

**[00:31:42] Dan Khasis**: Multiple deficiencies - wrong date format, missing column selector, no export capability.

**[00:33:28] Dan Khasis**: Need to add archive flag similar to active/inactive for vehicles for atoms. This allows hiding obsolete or incorrect data that can't be deleted from source system SAP from drivers and users in interface.

**[00:35:51] Dan Khasis**: Commission renaming of Telematics section to Connections, and in future possibly to Asset Tracking.

**[00:38:15] Dan Khasis**: Let me give you a lecture about the difference between sync table - table with raw data received from external system - and normalized table - table with processed data brought to our model. System should be able to link these entities and do deduplication and data enrichment. For example, extract from trips in telematics unique addresses and create Customer Locations from them.

### DECISION: UTC Display for Technical Fields

**DECIDED_BY:** Dan  
**DECISION:** All technical timestamp fields (created_at, updated_at) must display in UTC format with explicit indication in column headers  
**RATIONALE:** Prevents confusion during log analysis and transaction troubleshooting. Technical fields are for debugging, not user time visualization. [CEO_FINAL_DECISION on technical standards]

### DECISION: Archive Mechanism for Atoms

**DECIDED_BY:** Dan  
**DECISION:** Implement archive flag for atoms similar to active/inactive for vehicles  
**RATIONALE:** Allows hiding obsolete or incorrect data from SAP that cannot be deleted from source system, keeping interface clean for drivers and users. [CEO_APPROVED]

### DECISION: Rebrand Telematics to Connections

**DECIDED_BY:** Dan  
**DECISION:** Rename Telematics section to Connections, with future evolution to Asset Tracking  
**RATIONALE:** Better reflects actual functionality and future direction of integration capabilities. [CEO_DIRECTIVE]

### ACTION_ITEMS

- **OWNER:** Davron Usmonov | **TASK:** Fix all formatting issues - date format, add column selector and export | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Davron Usmonov | **TASK:** Display technical time fields in UTC with explicit labeling in headers | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Igor Skrynkovskyy | **TASK:** Implement backend mechanism for archive flags on atoms | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Implement frontend support for atom archive flags | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Davron Usmonov | **TASK:** Rename Telematics section to Connections across interface | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Igor Skrynkovskyy | **TASK:** Configure permanent redirect from old Telematics URL to new Connections URL | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Visit Details Interface & Time Window Violations
**TIME:** 00:47:02 - 01:01:22  
**PARTICIPANTS:** Dan Khasis, Alexey Gusentsov, Vova, Serhii Kasainov, Igor Skrynkovskyy

### DISCUSSION

**[00:47:02] Alexey Gusentsov**: Updated Visit Details interface with planned, actual, and predicted data separated into sections for better readability.

**[00:49:15] Vova**: Raised complexity of determining visit status (early/late) as there are 6 possible states when comparing two time intervals (plan and actual).

**[00:51:28] Dan Khasis**: Critical requirement - system must detect and visually highlight time window violations even if route was built without optimization. Backend must provide this information.

**[00:52:45] Dan Khasis**: Violations should display as indicator icon - yellow or red triangle - next to time window.

**[00:53:20] Dan Khasis**: Route optimizer must respect time windows during optimization. If not, it's completely useless to customers.

**[00:55:10] Igor Skrynkovskyy**: Time window validation during optimization is already implemented in backend.

**[00:56:35] Dan Khasis**: If we have constraint parameters in optimization request but still violate time windows in result, this is bug and needs fixing immediately.

**[00:58:42] Vova**: Suggested showing actual violation in minutes rather than just red/yellow indicator.

**[00:59:15] Dan Khasis**: Good idea. Show both indicator and specific minutes early or late. This gives users concrete data for decision making.

### DECISION: Time Window Violation Detection

**DECIDED_BY:** Dan  
**DECISION:** System must detect and visually indicate time window violations with icon (yellow/red triangle) plus specific minutes early/late, regardless of whether route used optimization  
**RATIONALE:** Critical for customer operations planning. Backend must calculate violations for all routes. Specific minutes give actionable data. [CEO_CRITICAL_DIRECTIVE - customer-facing feature]

### ACTION_ITEMS

- **OWNER:** Backend Team | **TASK:** Implement time window violation detection for all routes regardless of optimization method | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Alexey Gusentsov | **TASK:** Add visual indicator (yellow/red triangle) for time window violations | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Alexey Gusentsov | **TASK:** Display specific minutes early/late alongside violation indicator | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Igor Skrynkovskyy | **TASK:** Verify time window constraints are respected during route optimization | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Service Time Analytics Widget Redesign
**TIME:** 01:01:22 - 01:32:11  
**PARTICIPANTS:** Dan Khasis, Alexey Gusentsov, Vova, Serhii Kasainov

### DISCUSSION

**[01:05:30] Alexey Gusentsov**: Demonstrated service time analytics widget comparing different data across customer addresses.

**[01:07:15] Dan Khasis**: This widget is completely uninformative. What is this showing? The main logic should be comparison of planned versus actual service time. This is what customers want to understand - do their time estimates match reality?

**[01:09:42] Dan Khasis**: Regarding color coding - cannot use red-yellow-green gradient for service time until we know the direction. For some businesses longer service time is good (billable hours), for others shorter is better (delivery efficiency). Colors imply good/bad which is incorrect without context.

**[01:12:25] Dan Khasis**: Until we implement configurable metric direction per service type or customer location, use neutral color palette - single color gradient.

**[01:14:50] Dan Khasis**: Required controls - user must select what data they're viewing (Reported vs Detected) and what they're comparing against (vs Planned). Also must have Date Range Picker for analysis time period.

**[01:16:35] Dan Khasis**: In tooltip for each cell must show count of visits that average is based on. This is critical context.

**[01:18:20] Dan Khasis**: Future - metric direction (bigger is better or smaller is better) should be configurable at service type or customer address level.

### DECISION: Service Time Widget Logic Redesign

**DECIDED_BY:** Dan  
**DECISION:** Complete redesign of service time analytics widget to focus on plan versus actual comparison with neutral color palette and required user controls (data type selector, date range picker)  
**RATIONALE:** Current widget provides no actionable insights. Plan vs actual comparison is what customers need. Colors are misleading without configurable metric direction. [CEO_REJECTED current implementation, CRITICAL_DIRECTIVE for redesign]

### ACTION_ITEMS

- **OWNER:** Alexey Gusentsov | **TASK:** Implement plan vs actual as primary widget logic | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Provide plan vs actual comparison data via API | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Vova | **TASK:** Change color palette to neutral single-color gradient until metric direction is configurable | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Alexey Gusentsov | **TASK:** Add data type selector (Reported/Detected vs Planned) to UI | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Alexey Gusentsov | **TASK:** Add Date Range Picker for time period selection | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Alexey Gusentsov | **TASK:** Add visit count to tooltip for each cell | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Strategic Optimizations - Scatter Plot, Radar Chart, AI Generator
**TIME:** 01:32:11 - 02:03:01  
**PARTICIPANTS:** Dan Khasis, Manar Kurmanov, Igor Golovtsov, Semeyon S, Vova, Igor Skrynkovskyy

### DISCUSSION

**[01:32:11] Manar Kurmanov**: Scatter Plot has been visually improved with formatted units and hovers.

**[01:34:25] Igor Golovtsov**: Demonstrated AI generator prototype where user describes desired optimization scenario in natural language (e.g., "create 5 cycles with lunch breaks...") and AI generates corresponding JSON for the form.

**[01:37:40] Semeyon S**: Suggested developing AI generator into chat format for iterative scenario refinement.

**[01:40:15] Dan Khasis**: Radar Chart looks terrible and scares people. Must hide it in first release version.

**[01:42:30] Dan Khasis**: Scatter Plot is useless without two key elements - filters (e.g., show only Monday routes) and interactivity - points on graph must be clickable to drill into specific scenario or route details.

**[01:45:50] Dan Khasis**: Global requirement - need to add Man-Hours concept (Service Time multiplied by Worker Count). This is critically important metric for all service businesses that affects cost and efficiency calculations.

**[01:48:20] Dan Khasis**: AI generator is perfectly correct, exactly right approach. Action - immediately record video demo for partner presentations.

**[01:50:35] Dan Khasis**: Strategy - expand this AI functionality to other parts of system, like regular route planning.

**[01:52:45] Dan Khasis**: Development - AI should be able to generate multiple scenarios from single request (e.g., "generate 10 scenarios with sliding 1-hour window").

**[01:55:10] Dan Khasis**: Results table missing critical metric - route consistency or repeatability from scenario to scenario.

### DECISION: Hide Radar Chart

**DECIDED_BY:** Dan  
**DECISION:** Remove Radar Chart from interface until complete redesign  
**RATIONALE:** Current visualization looks terrible and scares users. Not ready for release. [CEO_REJECTED current implementation]

### DECISION: Man-Hours Global Metric

**DECIDED_BY:** Dan  
**DECISION:** Add Man-Hours concept (Service Time × Worker Count) to data model and begin tracking throughout system  
**RATIONALE:** Critically important metric for service businesses affecting cost calculations and efficiency metrics. Currently missing from entire platform. [CEO_CRITICAL_DIRECTIVE - platform-wide change]

### DECISION: AI Generator Immediate Deployment

**DECIDED_BY:** Dan  
**DECISION:** Prioritize AI scenario generator for immediate video demo and partnership presentations  
**RATIONALE:** Prototype is perfectly correct and represents major competitive advantage. Must showcase to partners immediately. [CEO_APPROVED with HIGHEST_PRIORITY]

### ACTION_ITEMS

- **OWNER:** Manar Kurmanov | **TASK:** Hide Radar Chart from interface until redesign | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Manar Kurmanov | **TASK:** Add filters to Scatter Plot for route selection | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Vova | **TASK:** Make Scatter Plot points clickable to drill into details | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Igor Skrynkovskyy | **TASK:** Add Man-Hours concept to data model | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Implement Man-Hours calculations across system | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Igor Golovtsov | **TASK:** Record video demo of AI generator for partners | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Semeyon S | **TASK:** Continue AI generator development in chat format | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Igor Golovtsov | **TASK:** Expand AI generator to support multiple scenario generation from single request | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Route Balancing & Noodle Routes Problem
**TIME:** 02:11:31 - 02:24:15  
**PARTICIPANTS:** Dan Khasis, Igor Skrynkovskyy, Semeyon S

### DISCUSSION

**[02:11:31] Igor Skrynkovskyy**: According to Juan, major client problem isn't creating extra routes, but system creates fewer routes that are longer and suboptimal.

**[02:13:45] Igor Skrynkovskyy**: Main hypothesis - special clustering algorithm developed for FedEx to solve noodle routes and create more human-like routes is not enabled for this client.

**[02:15:20] Igor Skrynkovskyy**: Team concerned they don't have access to data and problem details that Juan and sales team are working with.

**[02:17:35] Dan Khasis**: Expressed extreme dissatisfaction with communication failure. Sales team and Juan have been working in isolation for weeks trying to manually solve client problems while main algorithm development team is unaware.

**[02:19:50] Dan Khasis**: Need to clearly distinguish two problems - noodle routes (incorrect geometry) versus unbalanced routes (uneven load distribution).

**[02:21:45] Dan Khasis**: Juan must immediately provide Igor's team with all data, datasets, examples, and client correspondence so problem can be solved systematically, not manually.

### DECISION: Communication Protocol for Client Issues

**DECIDED_BY:** Dan  
**DECISION:** Juan must immediately share all client data, datasets, examples, and correspondence with Igor's algorithm team for systematic problem solving  
**RATIONALE:** Critical communication failure - sales team working in isolation for weeks while development team unaware of major client issues. Problems must be solved systematically through algorithm improvements, not manual intervention. [CEO_FRUSTRATED - organizational dysfunction]

### TECHNICAL_ISSUE: Route Balancing for Major Client

**[02:11:31] Igor Skrynkovskyy**: Major client experiencing suboptimal routes - fewer routes created but they are longer and inefficient. Hypothesis is FedEx clustering algorithm not enabled for this client, which solves noodle routes and creates human-like geometry.

### ACTION_ITEMS

- **OWNER:** Igor Skrynkovskyy | **TASK:** Urgently contact Juan and obtain all client data for problem analysis | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Igor Skrynkovskyy | **TASK:** Test with clustering algorithm enabled for this client | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Administrative Items & Quick Decisions
**TIME:** 02:24:15 - 03:04:21  
**PARTICIPANTS:** Dan Khasis, Serhii Kasainov, Igor Skrynkovskyy, Alex Shulga, Vova

### DISCUSSION

**[02:24:15] Serhii Kasainov**: Thanks to cache optimization, deployment time to staging reduced from 15-20 minutes to 6.5 minutes.

**[02:26:40] Alex Shulga**: Stop limits feature for Azuga is ready but configured via API. To avoid overloading Juan, decided to train Alex Shulga or QA team to configure these limits via Postman until admin panel UI is available.

**[02:59:10] Alex Shulga**: Custom data for facilities - API complete. Question whether to display custom data in interface and whether all custom data is public.

**[03:00:18] Dan Khasis**: Not exactly. There's custom override advanced data where mobile team can ignore some custom data keys if I remember correctly.

**[03:00:44] Dan Khasis**: Custom connection ID is different thing, will be full-fledged object, more complex discussion. Custom data will appear here.

**[03:00:55] Dan Khasis**: In locations custom data will be visible somewhere bottom left. In customers there's no editor for some reason, I don't know as always. Why I must edit from here, I can't edit from here, but okay.

**[03:02:23] Artur Moskalenko**: Dan, while there's no UI for facility custom data, is there point in sending announcement to everyone?

**[03:02:34] Dan Khasis**: No, only internal people I think.

**[03:02:42] Dan Khasis**: Here everything except what's needed. For example, order is wrong. Need to think what people will most often do. By facility for example, or by start point, or by vehicle type, by vehicle profile, optimization profile, routing profile. We still haven't discussed after assignment, and we still haven't discussed trips. And someone invented this status again. I must go.

**[03:03:33] Vova**: Dan, when will you have time to discuss after assignment and things that need approval for mobile team?

**[03:03:43] Dan Khasis**: I don't know, maybe tomorrow morning. Everything depends on what Igor and Juan report today about strategic balancing for these clients. Because if Juan hasn't moved, I'll be forced to deal with this myself. And then everything tomorrow is cancelled.

### DECISION: Stop Limits Configuration Delegation

**DECIDED_BY:** Dan (implicit approval)  
**DECISION:** Train QA team (Alex Shulga) to configure client stop limits via Postman until admin panel UI is available  
**RATIONALE:** Feature ready but API-only. Delegation prevents overloading Juan with manual configuration tasks. [CEO_APPROVED delegation approach]

### DECISION: Facility Custom Data Announcement Scope

**DECIDED_BY:** Dan  
**DECISION:** Announce facility custom data API only to internal people, not external clients  
**RATIONALE:** No UI available yet for end users. Premature external announcement would create support burden. [CEO_FINAL_DECISION]

### ACTION_ITEMS

- **OWNER:** QA Team | **TASK:** Train Alex Shulga to configure stop limits via Postman | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Artur Moskalenko | **TASK:** Send facility custom data announcement to internal team only | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Vova | **TASK:** Schedule morning discussion with Dan about after assignment and mobile designs (conditional on balancing progress) | **STATUS:** pending | **PRIORITY:** normal

---

## METADATA

**TOTAL_TOPICS:** 7  
**TOTAL_DECISIONS:** 11  
**TOTAL_ACTION_ITEMS:** 37  
**KEY_FEATURES_DISCUSSED:** Destination Snapshot, SAP Connection, Visit Details, Time Window Violations, Service Time Analytics, Strategic Optimizations, Scatter Plot, Radar Chart, AI Generator, Man-Hours, Route Balancing, Custom Data, Stop Limits  
**TECHNICAL_ISSUES:** Route balancing for major client, Noodle routes, Communication failure between sales and development
