# MEETING: Product Progress Review - Strategic Planner, Mobile App, Vehicle Snapshot

**DATE:** 2025-09-25  
**DURATION:** 03:42:56  
**ATTENDEES:** Dan Khasis (CEO), Vova (UI/UX Design), Igor Skrynkovskyy (SVP Platform), Parker Woodward (Sales), Davron Usmonov (Frontend Engineer), Semeyon S (VP Platform), Artur Moskalenko (QA Director), Kateryna Shevchenko (QA Lead), Alexey Afanasiev (Frontend Lead), Igor Golovtsov (Senior Frontend Engineer), Alexey Gusentsov (Frontend Engineer), Serhii Kasainov (Frontend Tech Lead), Anton Zadyraka (Mobile QA Team Lead), Igor S., Oleg Pravyk (QA), Alex Yasko (Product Manager), Manar Kurmanov (Frontend Engineer), Eugene (Frontend Engineer), Vladimir Fedorov (Frontend Developer)  
**DAN_PRESENT:** yes  
**MEETING_TYPE:** Product Review  
**DATA_SOURCE:** full_transcript+summary  
**CONFIDENCE_LEVEL:** high

---

## TOPIC: Mobile App Login Screen Redesign
**TIME:** 00:06:09 - 00:08:37  
**PARTICIPANTS:** Vova, Kateryna Shevchenko, Igor Skrynkovskyy

### DISCUSSION

**[00:06:09] Vova:** We've drawn 150 versions of the login screen. I honestly lean towards this login screen being the best. This is for our mobile app. It's not finished, just a raw draft, but we have a million versions. The third option was best because you can log in with everything and you can reach it with your thumb holding the phone in one hand, instead of stretching for Google Login at the very top like on the first two images.

**[00:07:41] Kateryna Shevchenko:** Vova, did you simplify this based on some analytics showing how most people register, or on what basis?

**[00:07:51] Vova:** Based on empirical experience, nothing else. We don't collect, we don't have an analytics department to do that.

**[00:08:13] Igor Skrynkovskyy:** This is a very good observation. Because, for example, I know that we don't only use Google. We have two big usages and a third separate one. It's Google, Microsoft, and Apple. These are commonly used things.

**[00:08:38] Vova:** What are the proportions between them? We need to find out. I suggest we go to Artem and ask. Good idea. Just so we don't cut off what people use. If Microsoft is used by 10%, not 2% or 1%, then of course it's needed. Even if it's 2% or 1%, why take away the button from these people? They'll just have to find their button once, and then after that they'll always see theirs.

### DECISION: Authentication Options Analysis
**DECIDED_BY:** Igor Skrynkovskyy, Vova  
**DECISION:** Analyze authentication usage statistics (Google, Microsoft, Apple SSO) before finalizing login screen design  
**RATIONALE:** Need to understand actual user distribution across authentication providers to avoid cutting off significant user groups. Even small percentages represent real users who shouldn't be inconvenienced. [PENDING_DATA_ANALYSIS]

### ACTION_ITEMS
- **OWNER:** Artur Moskalenko | **TASK:** Provide authentication statistics breakdown (Google vs Microsoft vs Apple SSO usage) | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Vova | **TASK:** Finalize login screen design based on authentication statistics | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Mobile App Plan Route Flow Redesign
**TIME:** 00:13:00 - 00:28:43  
**PARTICIPANTS:** Vova, Alexey Afanasiev, Kateryna Shevchenko, Artur Moskalenko, Igor Golovtsov, Anton Zadyraka

### DISCUSSION

**[00:13:05] Vova:** I'll demo the new Plan Route process for the mobile app. It's not finished yet, we're figuring out an illustration here. You enter the app for the first time, it says let's plan a route. Still in Airframe. Or if you already have routes, you see this form. You have a big card for the route you need to drive. This is a new feature where the dispatcher can publish unassigned routes, and drivers in the company can see them under this button and accept them if they're in their region.

**[00:13:05] Vova:** Changes: We hid history. We show the next route with a big card. Then you click Plan New Route here, here, or here depending on Flow. You arrive here. This is your empty route. By default, the assumption is you start from where you are now. And you have a Destinations button or edit Start Location. Adding Destination is very similar to what we had. You search, it's inserted by distance, filtered for what's not on your continent. Then you see beautiful additional parameters where you can edit or add something.

**[00:15:05] Vova:** And the new Split feature to plan multiple routes at once. You turn it on - it's off by default. If you want multiple routes at once, turn it on and set limits. Maximum number of routes to plan. And a button to spread routes across following days if you're driving yourself, not handing off to someone.

**[00:15:19] Kateryna Shevchenko:** I have questions about buttons. Not about the logic. Visual is generally okay, main concept. But button labels I want shorter. Seems like extra information. For example, Save Route, Start Route. It's clear we're talking about a route. And in settings, there's also quite a bit. Where you have No Limits, it's too close together. You need to either build in line wrapping or shorten somehow.

**[00:16:39] Vova:** We took the parameters we already have implemented. This part. Added 4 options Dan requested plus one we thought of ourselves. And look, restrictions too - clearly we can select multiple. Then we'll also need examples when selected. So it will definitely be multiple lines or ellipsis.

**[00:17:34] Vova:** Actually this is Dan's text, I think he'll decide more. I tried to make short labels that are maximally unambiguous. So they can't be interpreted two ways.

**[00:18:22] Igor Golovtsov:** About this same thing. There were screens to the right. Where you have Play New Route, Play Route. There was My Route, something there, Start Route. 100% this was discussed. Well yeah, on the Play New Route screen you have action button 1.1 and it won't do anything. What do you suggest, take Plan, or what? What's the alternative?

**[00:19:04] Vova:** Where there's Save, remove Route everywhere. Here you can write Continue, but I think it's better to be specific.

**[00:19:18] Vova:** And this is the name, the default route name. The user will write what they want here.

**[00:21:11] Vova:** And we highlight the most likely action they should do next with a green button. In this case they have a route planned for today, so we know they probably don't need new routes today, so we don't highlight this button. It exists, they can press it, it will work, but we don't focus attention on it. Because apparently it's time for them to drive.

**[00:22:23] Vova:** I think it's better to separate to different screens because the use cases don't overlap. My Routes is my to-do list, what I need to work on. All Routes is not my to-do list, it's what my company is doing, it's an analytics screen. More like checking current status.

**[00:23:25] Vova:** Scan, import, choose on map, current location, enter with microphone. Did we forget something?

**[00:24:02] Vova:** I think here we can lay this out differently, make huge buttons here with pictures. Like ways to enter addresses.

**[00:24:19] Vova:** It will say Import, Photo, Choose Map. We'll definitely have recent addresses highlighted first.

**[00:25:14] Vova:** The path honestly doesn't shorten much, because opening a menu and choosing an option is two steps. In our version you click the search bar, click an additional option. Same two steps. We just visually spend fewer objects on the screen. Simplifying the exterior. With the same number of stages.

**[00:26:00] Vova:** Here actually we can add Voice. We can add it here. We can add additional options here.

**[00:26:15] Vova:** Dictate immediately or photograph immediately? From here. This is a good idea. I like it.

**[00:27:22] Vova:** When you choose depot, give the option to remember this depot forever. Good idea.

**[00:28:32] Vova:** Import source. Then you choose address book or something else. Or upload a file or connect Google Drive. There will be options.

### DECISION: Mobile Route Planning Wizard Approved
**DECIDED_BY:** Dan (implicit approval), Vova  
**DECISION:** Implement new step-by-step wizard flow for mobile route planning with simplified UI and multiple destination input methods  
**RATIONALE:** Current flow is too complex for mobile users. New wizard simplifies the process while maintaining flexibility. Includes new features: unassigned route acceptance, route splitting, multiple input methods (voice, photo, map, search, import). [CEO_APPROVED]

### ACTION_ITEMS
- **OWNER:** Vova | **TASK:** Shorten button labels (remove "Route" where context is clear) | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Vova | **TASK:** Add voice input and photo scan buttons directly in destination input | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Vova | **TASK:** Implement depot saving as default preference | **STATUS:** pending | **PRIORITY:** low
- **OWNER:** Frontend Team | **TASK:** Implement new mobile route planning wizard | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Customer Portal and Visit vs Destination Terminology
**TIME:** 00:37:50 - 00:40:26  
**PARTICIPANTS:** Vova, Dan Khasis, Team

### DISCUSSION

**[00:37:50] Vova:** Presenting the Customer Portal concept. The portal allows end customers to interact with the system: view their scheduled visits and request new ones.

**[00:38:15] Vova:** Key terminology decision: In the customer-facing interface, we should use the term "Visit" not "Destination". Destination is a physical place, but Visit is an event, a service at that place, which more accurately reflects what the customer is requesting.

**[00:39:30] Dan Khasis:** I agree with the proposed concept and terminology.

### DECISION: Customer Portal Terminology Standard
**DECIDED_BY:** Dan, Vova  
**DECISION:** Use term "Visit" in all customer-facing interfaces instead of "Destination"  
**RATIONALE:** Destination refers to physical location; Visit refers to the service event, which better matches customer mental model and request pattern. This improves customer understanding and creates more client-oriented product. [CEO_APPROVED]

### ACTION_ITEMS
- **OWNER:** Design Team | **TASK:** Continue developing Customer Portal concept for future implementation | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Update all customer-facing UI to use "Visit" terminology | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Strategic Planner Lifecycle and Status System
**TIME:** 00:40:26 - 00:55:36  
**PARTICIPANTS:** Igor Golovtsov, Semeyon S, Dan Khasis, Igor Skrynkovskyy, Vova

### DISCUSSION

**[00:40:26] Igor Golovtsov:** We need to define the lifecycle and status set for the new Strategic Plan entity.

**[00:41:15] Semeyon S:** Proposed lifecycle: Draft (initial setup), Syncing/Importing (data processing), In Progress (optimization running), Completed (optimization finished, results ready), Accepted (final status before publishing to real Master Routes or Ad-hoc Routes).

**[00:45:26] Igor Skrynkovskyy:** In the JSON, Juan specified the name schedulerName. If we write "scenario" here, users will never match this in their heads and will sit looking at an error. That's why it's chosen this way, so it works and doesn't confuse users.

**[00:45:45] Dan Khasis:** You're basically right, where for this scenario should somehow appear on this left side. And now you see why it's so convenient to have JSON. Okay, this already looks right, but here's another thing that's wrong. Cycles should be 2.

**[00:46:22] Dan Khasis:** I don't understand why he made it 4.

**[00:46:26] Igor Skrynkovskyy:** Because there was no cycle in the JSON and the default value is 4. Here's cycle 4, just copied the game. I don't know why he chose 4. I'm trying to tell you. I understand there's 4 there. 4 is the number of weeks. That's a month. So it's wrong. It should be 2, not 4.

**[00:47:01] Dan Khasis:** Or what does this mean?

**[00:47:05] Igor Skrynkovskyy:** This is the definition of a month. Number of days in the cycle.

**[00:47:16] Dan Khasis:** Because by default we need to output 7.

**[00:48:07] Dan Khasis:** Yes, but we need to... Don't do this now after defects, when you fix it. All headers are wrong. They're all headers... Machine headers, not human headers. These are just raw names. Without polish. This is an anti-pattern.

**[00:48:39] Dan Khasis:** This isn't a wizard. This is not a wizard. A wizard does... You click, you nicely insert everything. These are wizard steps, you're now on the third step of the wizard. Form is the wrong word then. I haven't thought of anything better. Why can't we just call it Scenarios? Because Scenarios is in all tabs. But it's not a form. Okay.

**[00:49:22] Dan Khasis:** Serhii, there will be Add Duplicate Scenario here, as we talked about the wizard. And in this wizard it will be by accumulation method. You'll be able to add any number of scenarios where some things change.

**[00:54:54] Dan Khasis:** Yes, here it's right. We just have a filter by number of stops in the route in routes. Sorry, go back one second to the previous topic. Here it's wrong. How can a location be routed inside a scenario? Routed can only be in an ad-hoc route or instead of a route. Here the status can only be Imported or Imported for Recurring or Imported for Ad-hoc. There can't be a routing status here.

**[00:55:45] Dan Khasis:** What does routed mean here, Igor? We have a funnel of work, right? You uploaded a file, you got optimization. In the optimization there are multiple scenarios. There are shared locations between all scenarios. Now inside a scenario you have global locations regardless of scenario. How can a location be routed in context, not in the context of a scenario? At best it can be imported, flag true/false within one individual scenario, not within the global list of locations. So it could end up in one scenario but not in another. So this is the wrong filter. It's meaningless. You could have everything routed, but some in one scenario, others in another. In the end you could have all scenarios that have unrouted, and this thing just misinforms you.

### DECISION: Strategic Plan Status Lifecycle Approved
**DECIDED_BY:** Dan, Igor Golovtsov, Semeyon S  
**DECISION:** Implement status lifecycle: Draft → Syncing/Importing → In Progress → Completed → Accepted  
**RATIONALE:** Clear status system allows users to understand where their work is in the process and provides controlled transition from hypothetical scenario to real executable routes. [CEO_APPROVED]

### DECISION: Scenario Duplication and Parameter Variation
**DECIDED_BY:** Dan, Semeyon S  
**DECISION:** Implement Add Duplicate Scenario feature allowing users to create multiple scenarios with varying parameters  
**RATIONALE:** Users need to test multiple hypothetical configurations quickly. Duplication with parameter changes enables rapid what-if analysis. [EXECUTING_CEO_DIRECTIVE]

### TECHNICAL_ISSUE: Location Routing Status Filter Logic Error
**[00:54:54] Dan Khasis:** Filter showing "routed" status for locations within Strategic Planner is fundamentally flawed. Locations exist at optimization level (shared across scenarios), but routing happens at scenario level. A location can be routed in one scenario but not another. Filter showing all locations as "routed" or "unrouted" is meaningless and misinforms users about actual scenario composition.

### ACTION_ITEMS
- **OWNER:** Igor Golovtsov | **TASK:** Implement full status lifecycle for Strategic Plans (Draft through Accepted) | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Fix default cycle parameter to 2 (not 4) for weekly scenarios | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Change all machine headers to human-readable labels in Strategic Planner | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Igor Skrynkovskyy | **TASK:** Remove or fix "routed" status filter for locations in Strategic Planner (filter is at wrong level - should be scenario-specific, not global) | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Implement Add Duplicate Scenario feature with parameter variation | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Strategic Planner Analytics Dashboard and Scenario Comparison
**TIME:** 00:48:32 - 00:59:02  
**PARTICIPANTS:** Vova, Dan Khasis, Semeyon S, Igor Skrynkovskyy

### DISCUSSION

**[00:48:45] Vova:** Presenting the design for strategic planning results screen. The goal is to create a powerful analytics tool, not just a route list. The dashboard aggregates key metrics from scenario results: number of routes, stops, total mileage, cost, etc. Includes various widgets for data visualization, including Polar Charts. Key feature is Comparison View allowing users to compare multiple scenarios side-by-side.

**[00:52:15] Dan Khasis:** I fully support the analytics dashboard concept. This is exactly what competitors lack. Need deep analytics including statistical distribution and bucketization - for example, "how many routes have between 10 and 20 stops". The scenario comparison function is one of the most important and powerful features of the new tool.

**[00:54:30] Dan Khasis:** This should be an analytical instrument for making informed business decisions, not just a route viewer.

### DECISION: Strategic Planner Results as Analytics Dashboard
**DECIDED_BY:** Dan, Vova  
**DECISION:** Strategic planning results will be a full analytics dashboard, not a simple route list, with deep statistical analysis and scenario comparison as central features  
**RATIONALE:** Dan emphasized this is what competitors don't have. Deep analytics including statistical distribution, bucketization (e.g., "how many routes have 10-20 stops"), and side-by-side scenario comparison are key competitive advantages. This tool enables data-driven business decisions, which is the core value proposition. [CEO_FINAL_DECISION]

### ACTION_ITEMS
- **OWNER:** Vova | **TASK:** Finalize dashboard design for Strategic Planner results with analytics widgets | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Implement calculation of all necessary aggregates and statistical metrics for dashboard | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Implement Comparison View as central UX element allowing side-by-side scenario analysis | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Implement statistical distribution and bucketization calculations (route stop counts, mileage ranges, etc.) | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Vehicle Snapshot Transformation to Operational Dashboard
**TIME:** 01:04:30 - 01:13:40  
**PARTICIPANTS:** Alexey Gusentsov, Vova, Dan Khasis, Davron Usmonov

### DISCUSSION

**[01:04:45] Vova:** Presenting concept mockups for Vehicle Snapshot page including real-time data widgets and historical data analysis charts.

**[01:05:20] Alexey Gusentsov:** Telemetry data display is already partially implemented.

**[01:06:15] Dan Khasis:** FlightAware analogy - the page should provide exhaustive information like flight tracking sites: beautiful large map, real-time data, historical tracks, and analytical graphs. At the top of the screen there should be a heads-up display with key real-time metrics: Current Speed, Odometer, Altitude, Fuel Level, Battery Level, Current Route.

**[01:08:45] Dan Khasis:** Need to add a new Telemetry or Tracking tab showing the complete log of all historical GPS points as a table with all accompanying data. This is critically important for investigations - for example, when suspecting fuel theft. Full telemetry history is essential for forensic analysis.

**[01:10:20] Dan Khasis:** Need to implement Plan vs Actual graphs comparing planned route metrics against actual data. For example, planned speed/altitude against actual. This allows users to see where execution deviated from plan and understand why.

### DECISION: Vehicle Snapshot Complete Redesign
**DECIDED_BY:** Dan, Vova  
**DECISION:** Transform Vehicle Snapshot from static information page to powerful operational dashboard combining real-time data, deep historical analytics, and Plan vs Actual comparison tools  
**RATIONALE:** Dan specified FlightAware-level detail: exhaustive information with beautiful large map, real-time heads-up display, complete historical telemetry log for investigations (fuel theft, route violations), and Plan vs Actual comparison graphs. This gives users complete fleet control and operational understanding. [CEO_FINAL_DECISION]

### ACTION_ITEMS
- **OWNER:** Vova | **TASK:** Redesign Vehicle Snapshot with heads-up display and Telemetry tab with historical log table | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Provide complete telemetry dataset through API (speed, altitude, fuel, battery, position, etc.) | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Implement new Vehicle Snapshot design with dynamic real-time updates | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Implement Plan vs Actual comparison graphs for route execution analysis | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Implement Telemetry tab with complete historical GPS track table for forensic analysis | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Telematics Fields and Vehicle PopOver Enhancement
**TIME:** 03:35:50 - 03:39:24  
**PARTICIPANTS:** Davron Usmonov, Dan Khasis, Alexey Gusentsov, Alexey Afanasiev

### DISCUSSION

**[03:35:50] Davron Usmonov:** We have LastUpdate information. We display it and show LastUpdate.

**[03:36:04] Dan Khasis:** It would be nice to display green, yellow, red here. For LastUpdate, it would be good to add another row for specific time, because here you have to calculate in your head how many seconds ago it was. Yes, just need to write how many minutes ago, or seconds ago, or hours ago. No, I would add another row, or in parentheses, or another row.

**[03:36:50] Davron Usmonov:** I would write how much time ago, and on Hover, on Tooltip just show the specific date and time. Look, in vehicles it's exactly this implementation, I wanted to ask. It says LastUpdate when it was, 7 days ago or 5 minutes ago. That's the info given.

**[03:37:10] Vova:** This is just much easier to perceive. Only it's incorrectly grouped and sorted here.

**[03:37:19] Davron Usmonov:** I understand, we'll pass a more informative text. But depending on how long ago it was. There should be either days, or hours, or minutes, or seconds. Yes, that's how it is now. If days - days, if it's about hours, hours are written, and if it's already too small, then in minutes.

**[03:37:43] Dan Khasis:** Is there a column in the vehicles list itself for this data?

**[03:37:51] Davron Usmonov:** Yes, but not all. There's odometer. So, we have battery health.

**[03:37:59] Dan Khasis:** But this isn't LastPosition, it's LastUpdate, more correctly said.

**[03:38:07] Dan Khasis:** This isn't LastPosition, this is LastUpdateReceived.

**[03:38:34] Dan Khasis:** Well here's the LastPosition address column, I don't understand something. It shouldn't be LastPosition, it should be LastUpdate, because this creates the illusion that you have a difference between location and position, which doesn't affect engine status or temperature at all. Yes, we'll ask backend, they'll rename it.

### DECISION: Relative Time Display Standard
**DECIDED_BY:** Dan, Davron Usmonov  
**DECISION:** Display time since last update in relative format (7 days ago, 5 minutes ago) everywhere in the system, with absolute timestamp on tooltip/hover  
**RATIONALE:** Dan emphasized relative time is much more informative for operational work than absolute timestamps. Users need to quickly assess data freshness without mental calculation. This improves usability across all real-time data displays. [CEO_APPROVED]

### DECISION: LastUpdate Terminology Correction
**DECIDED_BY:** Dan  
**DECISION:** Rename "LastPosition" field to "LastUpdate" or "LastUpdateReceived" throughout system  
**RATIONALE:** Current terminology creates false distinction between "location" and "position" that confuses users and doesn't reflect reality. LastUpdate accurately describes telemetry data freshness regardless of data type (location, temperature, status, etc.). [EXECUTING_CEO_DIRECTIVE]

### ACTION_ITEMS
- **OWNER:** Davron Usmonov | **TASK:** Implement relative time format (X days/hours/minutes/seconds ago) for all LastUpdate displays with absolute timestamp on hover | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Rename LastPosition field to LastUpdate or LastUpdateReceived in API and database | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Davron Usmonov | **TASK:** Add LastUpdate field with relative time to vehicle PopOver | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Standardize relative time display format across all system components | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Weather Layer Release Decision
**TIME:** 03:39:24 - 03:43:06  
**PARTICIPANTS:** Artur Moskalenko, Dan Khasis, Eugene

### DISCUSSION

**[03:39:24] Artur Moskalenko:** Short question, Dan. The weather layer is ready on staging, which we brought back. The question is whether to include it in the module that was before - I think it was called Predictive Weather.

**[03:40:06] Dan Khasis:** Roman Kozodoi made Predictive Weather a long time ago, then we abandoned that service, then we made a new service, but I don't remember if that new service was for Predictive Weather. I think it was more for something else.

**[03:40:38] Artur Moskalenko:** In this Predictive Weather there was a feature that added a weather layer to maps, and when we planned a route, weather was taken by location, and depending on if there was rain or snow, bad weather, it was proposed to increase service time and roll duration. But they really went to that API, that location, that day - if yes, then great. This was there, but it was a long time ago.

**[03:41:17] Dan Khasis:** I would enable weather layer for all people, but enable Predictive Weather only for people who have the Predictive Weather module.

**[03:41:43] Alexey Afanasiev:** Then we're all set.

**[03:41:46] Dan Khasis:** Okay. Eugene, let's stay with Artur. Eugene, will you stay? To discuss weather to the end. Okay. But actually about weather I still didn't understand. If we're enabling it for everyone now, this will just generate money because we pay per number of calls. Not many people use the map layer, this UI, but yes, we'll pay, but salespeople will sell this even more.

**[03:42:33] Artur Moskalenko:** Yes, but so it's not turned on by default, at least I mean in the checkbox.

**[03:42:56] Dan Khasis:** Bye. Bye.

### DECISION: Weather Layer Universal Release
**DECIDED_BY:** Dan  
**DECISION:** Enable weather layer for all users; enable Predictive Weather feature only for users with Predictive Weather module  
**RATIONALE:** Weather layer provides value to all users and creates sales opportunities. Cost will be incurred for API calls but sales team can leverage this for upselling. Predictive Weather (which adjusts service time based on forecast) remains premium module feature. [CEO_FINAL_DECISION]

### TECHNICAL_ISSUE: Weather Layer API Cost Management
**[03:41:46] Dan Khasis:** Enabling weather layer for all users will generate API costs since we pay per call. Need to balance cost against sales opportunity. Weather layer shouldn't be enabled by default in checkbox to control API usage.

### ACTION_ITEMS
- **OWNER:** Artur Moskalenko | **TASK:** Release weather layer universally (not default-enabled in checkbox) | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Artur Moskalenko | **TASK:** Keep Predictive Weather feature gated to users with Predictive Weather module | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Eugene | **TASK:** Review weather layer implementation details with Artur | **STATUS:** scheduled | **PRIORITY:** normal

---

## METADATA

**TOTAL_TOPICS:** 8  
**TOTAL_DECISIONS:** 9  
**TOTAL_ACTION_ITEMS:** 28  
**KEY_FEATURES_DISCUSSED:** Mobile App Login, Plan Route Wizard, Customer Portal, Visit Terminology, Strategic Planner Lifecycle, Strategic Planner Analytics Dashboard, Scenario Comparison, Vehicle Snapshot, Heads-Up Display, Telemetry Log, Plan vs Actual Graphs, Telematics Fields, Vehicle PopOver, Relative Time Display, Weather Layer, Predictive Weather  
**TECHNICAL_ISSUES:** Strategic Planner location routing status filter logic error, machine headers vs human headers, cycle parameter defaults, LastPosition vs LastUpdate terminology confusion, weather layer API cost management
