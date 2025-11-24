# MEETING: Product Progress Review - November 2025

**DATE:** 2025-11-03  
**DURATION:** 03:45:56  
**ATTENDEES:** Dan Khasis (CEO), Semeyon S (VP Platform), Serhii Kasainov (Front-End Tech Lead), Igor Skrynkovskyy (SVP Platform), Igor Golovtsov (Senior Frontend Engineer), Manar Kurmanov (Frontend Engineer), Alexey Gusentsov (Frontend Engineer), Vladimir Fedorov (Frontend Engineer), Davron Usmonov (Frontend Engineer), Alexey Afanasiev (Frontend Lead), Vova (UI/UX/Design), Artur Moskalenko (QA Director & Product Ops), Mihail Krivulya (Backend Engineer), Vladyslav Feshchenko (QA), Volodymyr Ishchenko (QA), Alex Shulga (QA), Artem Klopov (Backend Engineer), Alex Yasko (Product Manager), Anna  
**DAN_PRESENT:** yes  
**MEETING_TYPE:** Product Review  
**DATA_SOURCE:** full_transcript+summary  
**CONFIDENCE_LEVEL:** high

---

## TOPIC: Service Time Heatmap Visualization

**TIME:** 00:06:28 - 00:18:48  
**PARTICIPANTS:** Alexey Gusentsov, Dan Khasis, Semeyon S, Igor Skrynkovskyy, Artur Moskalenko

### DISCUSSION

**[00:06:28] Alexey Gusentsov:** Showing Customer Location Snapshot. New Service Time tab with heatmap on mock data. API already in testing. Shows legend and heatmap with tooltips. Data will be ranged from max to min values from backend, color-coded accordingly. Can display all 24 hours if data available.

**[00:07:46] Semeyon S:** What date range are we showing for this data?

**[00:07:56] Igor Skrynkovskyy:** No date range. This is historical data for all time for specific location.

**[00:08:06] Semeyon S:** Then we need to indicate in text that it's for entire period.

**[00:08:24] Dan Khasis:** Wait please. Serious problems here. Screen is impossible to use for customers.

**[00:08:47] Dan Khasis:** Need numbers displayed. Need tooltips with numbers too. Or need toggle switch to show all values, especially time. So people don't have to hover everywhere. If people don't want to see time by default, let them turn it off. Unclear if this is actual or planned time.

**[00:10:26] Dan Khasis:** Don't make me guess what they did. Let me say what we expect. We have planned - what they ordered. We have actual with different sources: actual detected, actual marked, actual telematics, actual merged. If Artem can't do everything at once, do at least one. Priority order: marked first, detected second, telematics third, merged fourth. No good indicators here. Where's planned versus actual? If expected 10 minutes but spent 5 minutes, that's good right? Why no green or blue? Only bad shown?

**[00:11:34] Dan Khasis:** Need indicators for good results. Green if actual is better than planned.

**[00:12:44] Dan Khasis:** Should add matrix for scheduled service time in Customer Locations in Address Book.

**[00:14:12] Dan Khasis:** Everything I'm trying to say - we don't need to do everything at once, but we must label everything clearly so it's understandable. Right now unclear what person is looking at - Planned or Actual? If Actual, from which source? If Actual, for what range - last 30 days, 90 days, 1000 days? Plus would be good to switch to our hash ID instead of integer.

**[00:14:25] Dan Khasis:** Proposed adding Hash ID for Customer Location for better addressing.

### DECISION: Heatmap Required Features

**DECIDED_BY:** Dan  
**DECISION:** Implement toggle switch for showing/hiding numerical values in heatmap cells, add indicators for good results (green when actual better than planned), clearly label data source (Planned/Actual) and time period  
**RATIONALE:** Screen is unusable without numerical values visible. Users need to understand what data they're viewing and whether performance is good or bad. Critical for customer usability. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** ["Always show numbers", "Only tooltips", "Different color schemes"]

### ACTION_ITEMS

- **OWNER:** UI Team | **TASK:** Implement toggle switch for showing/hiding numerical values in heatmap | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Add logic for displaying good results indicators (green color) | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** UI Team | **TASK:** Add clear labels for data source (Planned/Actual) and time period | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Igor Skrynkovskyy | **TASK:** Discuss adding Hash ID for Customer Location entity | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Scatter Plot Financial Metrics Missing

**TIME:** 00:18:52 - 00:22:33  
**PARTICIPANTS:** Manar Kurmanov, Dan Khasis, Vova

### DISCUSSION

**[00:18:52] Manar Kurmanov:** Showing Scatter Plot visualization for comparing scenarios. Tool requires more data; current mock data insufficient. UI width too narrow.

**[00:20:29] Dan Khasis:** David Pelli confused between visits and customer locations. Recommends adding another axis describing customer locations. Missing total visits here even though it's inside scenario. Still no dollars shown.

**[00:21:16] Dan Khasis:** Missing basic details: difference between Visit and Customer Location, no Total Visits, no number separators (commas) for large numbers.

**[00:21:50] Dan Khasis:** Tool is useless if key financial metrics (dollars/euros) are not included. Financial indicators (Revenue, Cost in currency) must always be included according to account settings.

**[00:22:35] Dan Khasis:** Criticized overly narrow UI elements.

### DECISION: Financial Metrics Mandatory

**DECIDED_BY:** Dan  
**DECISION:** Make financial indicators (dollars/euros based on account settings) mandatory to display in Scatter Plot and all similar tools  
**RATIONALE:** Tool is worthless without key financial metrics that drive business decisions. We repeat this hundreds of times on every call - financial data must always be displayed. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS

- **OWNER:** Manar Kurmanov | **TASK:** Fix UI/UX issues including narrow elements | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Make financial indicators (in dollars/euros) mandatory to display | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** UI Team | **TASK:** Add missing metrics including Total Visits and clear headers | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Route Map Editor Critical Usability Defects

**TIME:** 00:23:00 - 00:32:44  
**PARTICIPANTS:** Dan Khasis, Serhii Kasainov, Vova

### DISCUSSION

**[00:23:17] Dan Khasis:** Very unpleasant to look at. Very unpleasant to look at.

**[00:28:16] Dan Khasis:** Showing how simple features we made 13 years ago with Roman Kozodoi in Route Map. Remember ETA toggle? Will show difference between what client wants versus forcing people to suffer with what they don't want.

**[00:30:11] Dan Khasis:** Planning route while right hand refreshes page in another tab because pusher still doesn't work. Watch how addresses move in timeline. I drag-and-drop and it doesn't move. This is a car without a steering wheel. Why can't I move? I click, nothing fucking moves. Click three, doesn't move. Click two, doesn't move. What's happening? Must I click this thing?

**[00:30:23] Dan Khasis:** This is huge defect. If someone taught me this, maybe I'd accept this flaw. But as a person... People do video editing for example. Let's pretend they're right for a second, Vova. That it's easier technologically for them. Now I zoom out. Want to show how flexible system is. I can move number 3 of green route to any position in orange route. I click on three and drag, nothing fucking moves. First defect. I move, tooltip appears, disappears. Watch what happens. I click, now they say must click this to move, to engage. I click and map fucking disappeared. Don't know where to move anything now. Zoom out again to move it again. Why torture users? Why are you even making these decisions independently?

**[00:32:07] Dan Khasis:** I selected, I see on map green route, second stop. Want to click and move. I click, lost everything. I click, want to move unit one to red route. Everything is lost. You're torturing me, you're scalding me. Ignore dates. What are these words? Don't even know what this means.

### DECISION: Fix Route Editor Drag and Drop

**DECIDED_BY:** Dan  
**DECISION:** Restore intuitive drag-and-drop functionality in Route Editor without requiring special mode activation  
**RATIONALE:** Current implementation is a car without steering wheel. Users expect to click and drag stops directly without toggling modes or losing map view. Fundamental usability broken. [CRITICAL_DIRECTIVE]  
**ALTERNATIVES_CONSIDERED:** []

### TECHNICAL_ISSUE: Pusher Not Working

**[00:30:11] Dan Khasis:** Pusher still doesn't work - users must manually refresh page to see route updates.

### ACTION_ITEMS

- **OWNER:** Frontend Team | **TASK:** Fix drag-and-drop to work without mode toggling, maintain map visibility | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Fix pusher to enable real-time updates without page refresh | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Team and Crew Management with Terminology Customization

**TIME:** 00:40:00 - 01:05:00  
**PARTICIPANTS:** Dan Khasis, Serhii Kasainov, Vova, Semeyon S

### DISCUSSION

**[00:43:10] Dan Khasis:** Need to introduce concept of Team with Primary Member for reporting purposes.

**[00:45:00] Dan Khasis:** Critically important to add section in Organization Settings for customizing terminology (aliases). For example: Visits to Shops.

**[00:46:08] Dan Khasis:** Must allow customers to define their own aliases for terminology because every industry uses different terms.

**[00:55:00] Dan Khasis:** First priority: implement Service Time calculation by summing time spent on each Service Type.

**[00:56:16] Vova:** Will develop model for dynamic Service Time calculation by summing times for various Service Types.

**[00:57:02] Dan Khasis:** Emphasized all data (Service Time, Time Windows, Customer Location address) must be saved with history (over time) for reporting. If we don't do this, all history is lost forever.

**[01:03:50] Vova:** Will continue design development for configuring seasonal schedules/prices.

### DECISION: Customizable Terminology System

**DECIDED_BY:** Dan  
**DECISION:** Add mechanism for customizable terminology (Aliases) in Organization Settings allowing customers to rename system terms to match their industry  
**RATIONALE:** Every industry uses different terminology. Critical for new large customers who have established vocabularies. Examples: Visits becomes Shops, Stops becomes Deliveries, etc. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** ["Hard-coded industry templates", "Post-processing label changes"]

### DECISION: Dynamic Service Time Calculation

**DECIDED_BY:** Dan  
**DECISION:** Develop model for dynamically calculating Service Time by summing time for different Service Types linked to location and season  
**RATIONALE:** Critical for new customers. Service time varies by what services are performed, time of day, and season. Must be calculated from catalog of services, not static value. [EXECUTING_CEO_DIRECTIVE]  
**ALTERNATIVES_CONSIDERED:** []

### DECISION: Historical Data Preservation

**DECIDED_BY:** Dan  
**DECISION:** Ensure all data changes (Service Time, Time Windows, addresses) are saved with complete history timestamps  
**RATIONALE:** If we don't preserve history, all historical data is lost forever. Critical for reporting and analysis. Cannot reconstruct past performance without this. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS

- **OWNER:** Backend Team | **TASK:** Add customizable terminology (Aliases) mechanism in Organization Settings | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Vova | **TASK:** Develop model for dynamic Service Time calculation from Service Types catalog | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Vova | **TASK:** Continue design for seasonal schedules/pricing configuration | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Ensure historicity of data (Service Time, Time Windows, etc) with timestamps | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Route List and Assign Board Sub-totals Missing

**TIME:** 01:55:00 - 02:04:17  
**PARTICIPANTS:** Dan Khasis, Igor Skrynkovskyy, Serhii Kasainov

### DISCUSSION

**[01:54:48] Dan Khasis:** Assign Board completely useless without Service Time, Stop Count and Sub-totals.

**[01:56:56] Dan Khasis:** Interfaces missing critically important information: time and distance to next stop, total sums (Sub-totals) per route.

**[01:57:04] Dan Khasis:** Need to add route totals: Total distance, total time, total service time, stop count.

**[01:59:44] Dan Khasis:** Must add ability to filter Route List by time/duration (for example: show all routes longer than 8 hours).

**[02:03:00] Dan Khasis:** Need to add Raw Data field for Man-hours to Route Data.

**[02:03:29] Igor Skrynkovskyy:** Will add separate Raw Data field for Man-hours to Route Data.

### DECISION: Sub-totals Mandatory in Lists

**DECIDED_BY:** Dan  
**DECISION:** Add Sub-totals (total time, distance, Service Time, stop count) to Route List and Assign Board  
**RATIONALE:** Assign Board is completely useless without these aggregated metrics. Users need to quickly assess and compare routes. Fundamental data missing. [CRITICAL_DIRECTIVE]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS

- **OWNER:** Backend Team | **TASK:** Add Sub-totals (total time, distance, Service Time) to Route List and Assign Board | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Igor Skrynkovskyy | **TASK:** Add Raw Data field for Man-hours to Route Data | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** UI Team | **TASK:** Implement filtering by time/duration in Route List | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: SAP ERP Integration - Invoicing, Item Master, Price List

**TIME:** 02:19:00 - 03:10:00  
**PARTICIPANTS:** Dan Khasis, Serhii Kasainov, Mihail Krivulya, Vova

### DISCUSSION

**[02:33:52] Serhii Kasainov:** Showing Invoices table where statuses (Paid) come from external system, Pending generated internally.

**[02:37:00] Dan Khasis:** Invoices table must contain: Customer, Due Date, Status, Dollar Amount, with filters.

**[02:39:04] Dan Khasis:** For Invoices generated in external system, must create button/link that redirects user to original URL in SAP/ERP.

**[02:54:24] Dan Khasis:** First version should generate Invoices in Read-Only mode (draft). Editing not allowed yet.

**[02:55:00] Dan Khasis:** Need full view for Item Master (products) showing all attributes including various ID types (UPC, ISBN) and their history.

**[03:00:00] Dan Khasis:** Price List should be separate entity reflecting default prices, with ability to view history and prices for specific Customer.

**[03:01:08] Dan Khasis:** Price List is complex entity. Prices change depending on Customer/Contract/Season.

**[03:04:17] Serhii Kasainov:** Will discuss detailed design for Item Master and Price List pages with Vova.

**[03:09:43] Dan Khasis:** Goal is to create authoritative automatic draft of what happened in field.

### DECISION: SAP Integration Read-Only View

**DECIDED_BY:** Dan  
**DECISION:** Create separate menu section for SAP/ERP integration containing Read-Only views of Invoices, Item Master, and Price List  
**RATIONALE:** Need to generate authoritative draft of field activities. First version is Read-Only to establish data flow. Editing comes later. Focus on financial data display and linking to original ERP records. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** ["Editable from start", "Single unified view"]

### ACTION_ITEMS

- **OWNER:** Serhii Kasainov | **TASK:** Create new menu section for SAP/ERP integration (Invoices, Item Master, Price List) | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Serhii Kasainov | **TASK:** Implement Read-Only Invoices display with key fields and filters | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Mihail Krivulya | **TASK:** Implement logic for external link to original Invoice in ERP system | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Serhii Kasainov | **TASK:** Discuss detailed design for Item Master and Price List pages with Vova | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Timezone Management Implementation

**TIME:** 03:10:37 - 03:20:00  
**PARTICIPANTS:** Dan Khasis, Serhii Kasainov, Vova

### DISCUSSION

**[03:10:37] Serhii Kasainov:** Many tickets for implementing Time Zone logic across all pages. Need to define default behavior (use Facility/Depot/Departure Address timezone) and who can override.

**[03:11:37] Dan Khasis:** Priority: Time Zone must be implemented first in Route List, Route Editor, and Route Snapshot (90% of all actions).

**[03:18:04] Dan Khasis:** Default Time Zone behavior (e.g., using Facility timezone) should be set by Administrator in Organization Settings.

**[03:19:34] Dan Khasis:** Administrator should have ability to enable/disable timezone override capability for different user types.

**[03:20:00] Dan Khasis:** Settings for default timezone and override rights must be in Organization Settings.

### DECISION: Timezone Priority Screens

**DECIDED_BY:** Dan  
**DECISION:** Prioritize Time Zone implementation in Route List, Route Editor, Route Snapshot (covers 90% of user actions). Default timezone and override permissions managed through Organization Settings  
**RATIONALE:** Focus on screens where users spend most time. Administrator controls timezone behavior centrally to maintain consistency while allowing flexibility where needed. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** ["Implement everywhere at once", "User-level timezone preferences"]

### ACTION_ITEMS

- **OWNER:** Serhii Kasainov | **TASK:** Prioritize Time Zone implementation in Route List, Route Editor, Route Snapshot | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Vova | **TASK:** Design settings for default timezone and override permissions in Organization Settings | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Critical Optimization Routes Missing Bug

**TIME:** 03:23:09 - 03:32:00  
**PARTICIPANTS:** Dan Khasis, Igor Skrynkovskyy, Volodymyr Ishchenko

### DISCUSSION

**[03:23:09] Igor Skrynkovskyy:** After optimization, not all generated routes appear in list. Example: 4 out of 8 routes missing.

**[03:24:23] Igor Skrynkovskyy:** Previously released fix for similar problem to staging.

**[03:25:55] Igor Skrynkovskyy:** Need to debug route synchronization and map display mechanism - currently too slow.

**[03:28:26] Dan Khasis:** Expressed disbelief how such defect could appear and pass by team.

**[03:31:00] Dan Khasis:** Emphasized enormous losses (money, time, reputation) from releases that break key functionality.

**[03:37:35] Volodymyr Ishchenko:** Routes take first 5 random values because Unix timestamp identical.

**[03:37:40] Igor Skrynkovskyy:** Where's next page? Why random?

**[03:38:19] Igor Skrynkovskyy:** Will immediately investigate and fix cause of missing routes in optimization results.

### TECHNICAL_ISSUE: Missing Routes After Optimization

**[03:23:09] Igor Skrynkovskyy:** Critical defect where after optimization, routes don't fully display in system. Appears to be event message loss between services causing incomplete final result. Example: optimization generates 8 routes but only 4 appear in Route Snapshot. Limit parameter set to 5 when total is 8, causing pagination issues.

### DECISION: Critical Bug Investigation

**DECIDED_BY:** Igor Skrynkovskyy  
**DECISION:** URGENT investigation and fix for missing routes after optimization  
**RATIONALE:** Critical defect affecting core functionality. Data loss in optimization results is unacceptable. Huge losses in money, time, and reputation from such releases. [PENDING_CEO_APPROVAL]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS

- **OWNER:** Igor Skrynkovskyy | **TASK:** URGENT - Investigate and fix missing routes in optimization results | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Igor Skrynkovskyy | **TASK:** Debug route synchronization mechanism (currently too slow) | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: SSO Registration and BlueNet Integration Issues

**TIME:** 03:34:20 - 03:46:22  
**PARTICIPANTS:** Dan Khasis, Artur Moskalenko, Igor Skrynkovskyy

### DISCUSSION

**[03:34:34] Artur Moskalenko:** Dan wrote third time about SSO registration still allowing new account creation. Checked admin tunnel - don't see accounts created outside admin tunnel.

**[03:35:11] Dan Khasis:** How do you explain people creating these accounts?

**[03:35:17] Artur Moskalenko:** Many sources: BlueNet creates, Partner Channel, admin tunnel. Found no accounts in last two weeks made directly through SSO.

**[03:35:40] Dan Khasis:** You said important thing about BlueNet. We need to tell BlueNet how to properly parametrize their registration URL so they switch to Marketplace. They're still sending old way.

**[03:36:13] Igor Skrynkovskyy:** Already told them everything. They have detailed description of which parameters to use. Default automatically sets correct package and Marketplace account type.

**[03:36:39] Dan Khasis:** I don't think that's true. I know it's not true.

**[03:36:43] Igor Skrynkovskyy:** I can prove it.

**[03:36:46] Dan Khasis:** I can prove it too. Max Pirogov writes me that he now manually changes their accounts every few days that are still created under Enterprise plan. Last week he did this seven times.

**[03:37:06] Igor Skrynkovskyy:** Will write to Max now.

**[03:38:37] Dan Khasis:** We must provide them example of how to create Marketplace accounts properly. System creates Marketplace accounts automatically for them specifically - they send advertising code to us.

**[03:39:02] Igor Skrynkovskyy:** In new organization they have specific package that automatically assigns when they register new account. Specifically made so on their side when switched to new API with old values it automatically sets them to correct one.

**[03:39:33] Dan Khasis:** How long does this auto-transition take?

**[03:39:38] Igor Skrynkovskyy:** What do you mean time? I said they automatically transition new accounts they create, automatically get correct Marketplace attributes.

**[03:40:02] Dan Khasis:** To Enterprise. And you're trying to say after this you ignore everything and do what you want anyway.

**[03:40:08] Artur Moskalenko:** They continue creating accounts in old organization. That's the problem.

**[03:40:16] Igor Skrynkovskyy:** We must tell them. Will send request I sent you three months ago for account setup, one endpoint for everything, everything in ideal state, they just need to use it.

**[03:41:34] Dan Khasis:** Another point about this - their callbacks should work at facility level, not just account level.

**[03:41:39] Igor Skrynkovskyy:** What does this mean - they will collect or receive at specific endpoint registered in facility or some event created with specific facility attribute?

**[03:42:14] Dan Khasis:** They will write topid and other fixed attributes at facility level with UI editor, then system will check and say this order linked to this facility, so we make callback not to global URL but to this facility's specific URL. Will explain separately.

**[03:43:08] Igor Skrynkovskyy:** Dan wait, don't understand what you mean by callback. This is BlueNet/Deliver Hero notification or webhooks? Different things. If talking only BlueNet and Deliver Hero, no problem, we can do with custom data at facility level now.

**[03:43:44] Dan Khasis:** Talking about BlueNet, not global webhooks. BlueNet, Deliver Hero, etc.

**[03:43:56] Igor Skrynkovskyy:** Good. How high priority?

**[03:44:00] Dan Khasis:** From your vacation we'll discuss separately to make it faster, very transparent.

**[03:44:16] Igor Skrynkovskyy:** Can propose solution then discuss if you want.

**[03:44:22] Dan Khasis:** They want us through Frontend to let people change these parameters too, so administrator can login and change. Will answer separately, can't do it now.

**[03:44:46] Igor Skrynkovskyy:** If done properly it will be complex because they don't use Facility right? If they start using Facility we need to give them immediately ability in one account, in one Primary organizational account to work with Facility, this Select we gave at top with Facility selection, preparation of all these things etc, and we need immediately all screens everything else to adapt so everything works ideally.

**[03:45:26] Dan Khasis:** Except Orders and Destinations nothing worries much.

**[03:45:35] Igor Skrynkovskyy:** Either way it must all work, just need to recheck everything.

**[03:45:42] Dan Khasis:** Again we must start with something. They're ready to receive some minimal prototype.

**[03:45:50] Igor Skrynkovskyy:** OK.

**[03:45:54] Dan Khasis:** Their patience is running out. I must call Josh about AT&T release they want to make. Must disconnect. OK everyone bye.

### DECISION: BlueNet Registration Fix

**DECIDED_BY:** Dan, Igor Skrynkovskyy  
**DECISION:** Provide BlueNet with proper v5 registration endpoint documentation and parameters to create Marketplace accounts correctly. Implement facility-level callbacks for BlueNet/Deliver Hero integration  
**RATIONALE:** BlueNet continues creating Enterprise accounts in old organization instead of Marketplace accounts in new organization. Max Pirogov manually fixes these accounts multiple times per week. Their patience running out. Must provide clear documentation and minimal prototype for facility-level callbacks. [EXECUTING_CEO_DIRECTIVE]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS

- **OWNER:** Igor Skrynkovskyy | **TASK:** Send BlueNet v5 registration documentation with correct Marketplace parameters | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Igor Skrynkovskyy | **TASK:** Design facility-level callback system for BlueNet/Deliver Hero | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Igor Skrynkovskyy | **TASK:** Coordinate with Max Pirogov on current account creation issues | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Create UI for facility-level callback parameter editing | **STATUS:** pending | **PRIORITY:** normal

---

## METADATA

**TOTAL_TOPICS:** 8  
**TOTAL_DECISIONS:** 10  
**TOTAL_ACTION_ITEMS:** 32  
**KEY_FEATURES_DISCUSSED:** Service Time Heatmap, Scatter Plot, Route Editor, Team/Crew Management, Sub-totals, SAP Integration, Timezone, Optimization Stability, SSO Registration, BlueNet Integration  
**TECHNICAL_ISSUES:** Route Editor drag-and-drop broken, Pusher not working, Missing routes after optimization, SSO registration parameters, BlueNet creating wrong account types  
**DAN_SPEAKING_TIME:** 02:24:57 (64.2%)  
**DAN_DIRECTIVE_COUNT:** 15+ major directives  
**CRITICAL_ISSUES:** 3 (Route Editor usability, Missing optimization routes, BlueNet integration)
