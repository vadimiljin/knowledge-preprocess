# MEETING: Product Progress Review - Service Time, Strategic Optimization & Vehicle Tracking

**DATE:** 2025-11-13  
**DURATION:** 01:02:10  
**ATTENDEES:** Dan Khasis (CEO), Vladimir Zhakhavets (UI/UX/Design), Manar Kurmanov (Frontend Engineer), Igor Skrynkovskyy (SVP Platform), Alexey Afanasiev (Frontend Lead), Semeyon Svetliy (VP Platform), Artur Moskalenko (QA Director & Product Ops), Vladimir Fedorov (Frontend Developer), Igor Golovtsov (Senior Frontend Engineer), Volodymyr Ishchenko (QA), Vadim Iljin  
**DAN_PRESENT:** yes  
**MEETING_TYPE:** Product Review  
**DATA_SOURCE:** full_transcript+summary  
**CONFIDENCE_LEVEL:** high

---

## TOPIC: Service Time Analytics UI Design & Heat Map

**TIME:** 00:00:06 - 00:15:47  
**PARTICIPANTS:** Vladimir Zhakhavets, Dan Khasis, Alexey Afanasiev

### DISCUSSION

**[00:00:16] Vladimir Zhakhavets:** I used the guys to help pick the palette while you weren't here. This is Customer Allocation Snapshot showing average Service Time. You can choose which type to view - Actual, Plant, difference Actual vs Plant, or percentage difference. You can select metric direction Lower is Better or Higher is Better, which colors the palette from green to red or red to green. When hovering over a cell, you see total visits, over all time, and average. We forgot to add the control for Average method - which calculation method to use: median, weighted average, or with peak trimming.

**[00:02:08] Dan Khasis:** I don't know what I think. This is Customer Location, Destination. This can be shown in Route Destination Snapshot, but it would refer to the address, not the Destination itself.

**[00:02:44] Vladimir Zhakhavets:** To the address, because Destination is one visit in one route and isn't repeated, but an address can occur multiple times. It can be shown in Destination Snapshot tied to the address.

**[00:03:14] Dan Khasis:** This is like in programming - PassByReference, PassByValue.

**[00:03:24] Vladimir Zhakhavets:** Destination is an instance of an address - one specific visit to this address in our paradigm.

**[00:03:35] Dan Khasis:** In RouteData there can be Destination with full link to CustomerLocation. When you open Service Time, if I were a client, I'd understand you highlighted with an icon that this is Service Time - not of this Destination, but Service Time statistically.

**[00:04:04] Vladimir Zhakhavets:** Statistically of this Location, yes. We just need to write Location Service Time without an icon.

**[00:04:50] Vladimir Zhakhavets:** Second idea was to let user choose to focus on bad or good. If they focus on bad, red accents on bad things. If focus on good, palette flips to green.

**[00:05:43] Dan Khasis:** Vova is absolutely right. But this report doesn't show what Vova voiced. We have a problem due to legacy decisions. If you look at custom location in our database, we have two or three huge problems at the custom location level. Service time at the location level, but service time should be at the level of service type and location. The second problem is the incorrect assumption that at the level of one location there is only one service type. Because here there can be delivery, service, inspection, and so on. And everything changes proportionally. Because if you made a route today, during planning, we have a fourth problem - destination type selection should happen intelligently. You have recurring schedule, but ours is wrong. Our recurring schedule is at the location level, but recurring schedule should be at location plus service time potentially. Then this service time dynamically changes by day of week. Ordered and actual also change dynamically, but we don't have support for this.

**[00:11:37] Vladimir Zhakhavets:** Show me service time like this, show me service time like this.

**[00:11:44] Dan Khasis:** Because of what? Due to absence of new scenario where we can say another for loop. Change my service time plus-minus 10%, five intervals up and five intervals down. This is new scenario. For this they have to upload 25 or 50 CSV files. Again because of for loop. So it turns out optimizers don't care, right? The algorithm only matters to initialize. You don't even need to redo distance matrix because it's cached. Only service time changes. What I'm trying to say is this thing you drew is 90% correct, but it's 10% useful for the types of clients that David wants us to sell to. Because service time changes - service type from time of day, season and so on.

**[00:13:32] Vladimir Zhakhavets:** If we tag these destinations somehow when they do different service types, then we can give them ability to choose here which service type to consider.

**[00:13:46] Dan Khasis:** Absolutely right. Or all at once. And Artem should take - there's one thing missing in the tooltip. As soon as we write average, people like David cling to this. Why don't you use line energy, why don't you use this.

**[00:14:02] Vladimir Zhakhavets:** They assume they know statistics. Yes, here there will be averaging method, mathematical formula to choose. Several options.

**[00:14:22] Dan Khasis:** Such, such, such. Because there's moving average, exponential moving average, different options. Maybe we don't even publish, maybe we shouldn't even say our method.

**[00:14:47] Vladimir Zhakhavets:** Why even write average at all?

**[00:14:55] Dan Khasis:** Maybe we can write service time, detected service time. Why even write the word average? Smart guys will want to know what math is inside. So smart guys, you'll click on the cell and open scatter plot or line graph that will be a curve both by time and by selected range of this report. This curve will show green-yellow-red ranges and show within those ranges the historical trend history for that cell. Because the cell is hourly range plus a factor - day of week, season, quarter, and so on. We need to look if you want, right now on custom allocations, to decide or figure out how to add service type and time in custom allocations editor.

### DECISION: Service Time Analytics UI Approved With Enhancements

**DECIDED_BY:** Dan Khasis  
**DECISION:** Approve Service Time heat map UI design with requirement to add service type filtering and averaging method selection  
**RATIONALE:** UI is 90% correct but only 10% useful without service type filtering. Report is great for enterprise analytics but doesn't solve core planning problem. System must distinguish between different service types at same location. Dan explicitly approved visual design but mandated critical enhancements before full rollout. [CEO_APPROVED with conditions]  
**ALTERNATIVES_CONSIDERED:** ["Reject design entirely", "Deploy without service type support", "Wait for full architecture solution"]

### ACTION_ITEMS

- **OWNER:** Vladimir Zhakhavets | **TASK:** Add control for selecting averaging method (median, weighted average, outlier trimming) in Service Time analytics | **STATUS:** assigned | **PRIORITY:** high
- **OWNER:** Vladimir Zhakhavets | **TASK:** Add service type filtering capability to Service Time heat map | **STATUS:** assigned | **PRIORITY:** high
- **OWNER:** Vladimir Zhakhavets | **TASK:** Implement drill-down functionality - clicking cell opens scatter plot or line graph showing historical trend with green-yellow-red ranges | **STATUS:** assigned | **PRIORITY:** normal
- **OWNER:** Vladimir Zhakhavets | **TASK:** Design UI concept for per-location service time intelligence configuration and present next week | **STATUS:** assigned | **PRIORITY:** high | **DEADLINE:** 2025-11-20

---

## TOPIC: Multi-Service Type Architecture & Customer Location Config

**TIME:** 00:15:47 - 00:26:54  
**PARTICIPANTS:** Vladimir Zhakhavets, Dan Khasis

### DISCUSSION

**[00:16:12] Vladimir Zhakhavets:** I'll think about it. Very quickly, what I think now - possibly something like a new entity, a service contract for this customer location. You can have multiple service contracts simultaneously for same location, each contract has its own schedule, conditions, visit frequency and visit duration.

**[00:16:41] Dan Khasis:** Yes, but even before talking about contract, we can just add elementary config table in custom allocations. The most elementary.

**[00:16:59] Vladimir Zhakhavets:** Yes, imagine you have a location. In this location editor there's currently nothing related to scheduling or service type. But there should be. What should be there? Something like a table. Location, service type, frequency - there's already frequency. But duration. And you can add rows. Click add. Service type delivery, frequency daily, duration 20 minutes. Add. Service type inspection, frequency weekly on Mondays, duration 40 minutes. You add a row. Multiple rows in this table.

**[00:17:35] Dan Khasis:** When you come to strategic, you'll already have what should be planned. Instead of manually in Excel creating multiple CSVs for one same address. This all already exists in database and in table. So strategic will automatically understand - this one delivery, that one delivery and service, that one only service. Moreover, even when you start planning master routes with this logic, it becomes clear what's planned. Because now when someone plans or makes recurring schedule, the assumption is same visit everywhere. But there can be different visits depending on the day.

**[00:18:17] Vladimir Zhakhavets:** That's how custom routes generally are - we have a recurring visit. But here we can have two recurring visits, not one, multiple. Then at optimization stage we have this whole table. At planning stage, at strategic stage, I select my locations and say I want to make strategic optimization. In background, strategic optimization goes and looks - oh look, these locations have not just one service type but three different ones. Which one do you want to optimize for today?

**[00:18:56] Dan Khasis:** So we still need dynamic custom types.

**[00:19:01] Vladimir Zhakhavets:** But if we have these service types, this is no longer a problem. We'll just pass them to strategic. Strategic optimization will have no problem with this.

**[00:19:15] Dan Khasis:** What do you mean? What's our problem with custom types?

**[00:19:18] Vladimir Zhakhavets:** I don't know if this is backend or database problem. We can't dynamically add service types. They're kind of hardcoded in our database. They're stored in some enum or something. We can't dynamically add service types.

**[00:19:37] Dan Khasis:** Yes. We need to make a service types table. Where there are enums that exist by default in the system.

**[00:19:45] Vladimir Zhakhavets:** And user can add their own. User can create. But then problem is, remember we discussed with Igor, we have different icons for different service types. If someone creates their own service type, we can't have icon for it. So we'll just give them circle or square.

**[00:20:22] Dan Khasis:** This is what I'm talking about. When destination is created based on customer location, when you're making new destination, system looks - ah, customer location X has these service types configured. If these service types are fixed, meaning delivery always, service once a week, inspection once every two weeks - this is recurring schedule. Then route planner can automatically in UI say, I see you added this customer location, and I see that today according to its schedule it should have service and inspection, not delivery, because delivery is on other days. Route planner already knows from the schedule. But if schedule isn't fixed, route planner simply offers all available service types for this location as possible options, and user picks which they want. But problem is that now when route planner creates destination for this location, if there are three different service times, system doesn't know which service time to assign.

**[00:21:47] Vladimir Zhakhavets:** Well, in dropdown you'll select service type first, only after you select service type the system can autocomplete service time based on that service type. Okay, let's say user manually creates destination for this customer location. First they pick service type. Then service time automatically fills in. If not, they can override. Okay. But we still have huge problem. That service time can change by day of week.

**[00:22:21] Dan Khasis:** Even more. Time of day, day of week. Because, for example, morning rush hour. Morning delivery might take longer than afternoon delivery.

**[00:22:34] Vladimir Zhakhavets:** So service time becomes not a number anymore. Service time becomes a function. A formula. Service time equals if day of week equals Monday and if time of day between 8 and 10 AM, then 30 minutes, else if... Or maybe it's a table. Like you have a table. Column one - day of week. Column two - time of day range. Column three - service time. And you have rows. Monday 8-10 AM 30 minutes. Monday 10 AM-12 PM 25 minutes. Tuesday 8-10 AM 20 minutes. This is service time table.

**[00:23:44] Dan Khasis:** This is exactly what I showed in heat map. But we're not showing this for individual location. We're showing aggregated statistics. What you're talking about, each location should have its own mini heat map potentially. In location editor. Click on service time cell, boom, opens modal with this table or this heat map. User fills it in. Or system automatically learns from history. System says, based on your past visits to this location, we detected these patterns. Do you want to use detected patterns or override manually?

**[00:24:19] Vladimir Zhakhavets:** Automatically learning from history is exactly what the analytical report does. The report you're seeing now. This is what it does. It aggregates historical data.

**[00:24:34] Dan Khasis:** But this is aggregated across all locations. What I'm saying is, for each individual location, system should be able to say, for customer location ABC Plumbing, we detected that on Mondays at 9 AM service time is usually 45 minutes, but on Fridays at 3 PM it's 20 minutes. And this is specific to ABC Plumbing, not averaged across all customers. That's the difference. This report is useful for enterprise analytics. But for route planning and optimization, we need per-location intelligence.

**[00:25:13] Vladimir Zhakhavets:** I understand. So in location editor there should be something like a button. "Configure Service Time Intelligence" or something. Click it, opens modal. Shows same heat map but filtered to this location only. Shows historical patterns. User can accept automated suggestions or manually override any cell. Save. Now this location has intelligent service time.

**[00:25:47] Dan Khasis:** Exactly. And this intelligence should be used everywhere. In recurring schedule, in strategic optimization, in route planning. Everywhere. So this is why I'm saying this report is great for analytics team, for management to understand overall performance. But it doesn't solve core problem, which is how do we intelligently assign service time during planning, taking into account service type, day of week, time of day, and historical patterns for that specific location.

**[00:26:29] Vladimir Zhakhavets:** Got it. So this report is foundation. It shows system works. But we need to extend this intelligence down to individual location level. And make it actionable in editors. I'll work on this. Show you concept next week.

### DECISION: Multi-Service Type Architecture Solution Required

**DECIDED_BY:** Dan Khasis  
**DECISION:** Mandate development of multi-service type support at customer location level with config table in location editor  
**RATIONALE:** Current architecture limitation prevents selling to large enterprise clients. Company is losing deals because system assumes one service type per location. Parker confirmed two deals lost specifically due to this limitation. Solution requires config table in customer location editor allowing multiple service types with different schedules, frequencies, and durations per location. This is critical revenue blocker. [CRITICAL_DIRECTIVE - strategic priority]  
**ALTERNATIVES_CONSIDERED:** ["Continue with single service type model", "Manual workarounds via Excel/CSV", "Per-client custom development"]

### TECHNICAL_ISSUE: Dynamic Custom Service Types Not Supported

**[00:19:18] Vladimir Zhakhavets:** We can't dynamically add service types. They're kind of hardcoded in our database. They're stored in some enum or something. We can't dynamically add service types.

**[00:19:37] Dan Khasis:** We need to make a service types table where there are enums that exist by default in the system and user can add their own.

### ACTION_ITEMS

- **OWNER:** Vladimir Zhakhavets | **TASK:** Design and present architecture concept for multi-service type config table in customer location editor including UI mockups | **STATUS:** assigned | **PRIORITY:** high | **DEADLINE:** 2025-11-20
- **OWNER:** Backend Team | **TASK:** Investigate and resolve hardcoded service types limitation - create service types table allowing dynamic user-defined types | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Design Team | **TASK:** Design icon system for custom user-defined service types (generic shapes for custom types) | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Strategic Optimization UI - Depot Selection Redesign

**TIME:** 00:27:03 - 00:39:04  
**PARTICIPANTS:** Manar Kurmanov, Dan Khasis, Alexey Afanasiev

### DISCUSSION

**[00:27:03] Manar Kurmanov:** [Demonstrates new strategic optimization UI flow starting from customer locations list with filtering, then configuration step]

**[00:30:11] Dan Khasis:** This is much better than before. Starting from customer locations makes sense. But I have critical feedback on depot selection step. Here you have text input field where user types depot address and geocodes it. This is completely wrong approach for enterprise clients. They don't want to type depot address every time. They have 15 depots already configured in system. They want to SELECT from existing facilities, not type and geocode new ones. This text field should be replaced with searchable, filterable table showing all their existing facilities. User checks the ones they want to use for this optimization. It's like selecting customers - same UX pattern. And THEN, as secondary option, if they really need to add new depot for what-if scenario, there can be button "Add New Depot" which opens geocoding. But primary flow is SELECT existing facilities. This is non-negotiable for enterprise. Without this we can't sell to large clients.

**[00:33:08] Manar Kurmanov:** Understood. So main interface is facilities table with checkboxes and search. Adding new depot address is secondary option accessed via button. Will redesign this immediately.

### DECISION: Depot Selection UX Must Use Facilities Table

**DECIDED_BY:** Dan Khasis  
**DECISION:** Replace text input geocoding field with searchable facilities table for depot selection in strategic optimization workflow  
**RATIONALE:** Enterprise clients have 15+ pre-configured depots and need to SELECT from existing facilities, not type addresses repeatedly. Current text field approach is wrong for target market. Table-based selection with checkboxes is enterprise-standard UX pattern. Geocoding new addresses should be secondary "Add New Depot" option for what-if scenarios only. This is non-negotiable for large client sales. [CEO_FINAL_DECISION - blocking issue for enterprise]  
**ALTERNATIVES_CONSIDERED:** ["Keep text input as primary", "Hybrid approach with recent addresses", "Auto-detect nearest facilities"]

### ACTION_ITEMS

- **OWNER:** Manar Kurmanov | **TASK:** Redesign depot selection step in strategic optimization - replace text input with searchable facilities table with checkboxes | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Manar Kurmanov | **TASK:** Add secondary "Add New Depot" button that opens geocoding interface for what-if scenarios | **STATUS:** in_progress | **PRIORITY:** high

---

## TOPIC: Strategic Optimization Solver Performance & Timeout

**TIME:** 00:39:04 - 00:48:20  
**PARTICIPANTS:** Semeyon Svetliy, Igor Skrynkovskyy, Dan Khasis

### DISCUSSION

**[00:33:42] Semeyon Svetliy:** While we're on strategic optimization topic, I have question about solver performance. What's acceptable timeout?

**[00:34:15] Igor Skrynkovskyy:** Currently with new FastAPI solver using C++ library, we're seeing much better performance. 2500-5000 locations taking about 25 minutes. Above 1500 addresses, automatic clustering kicks in. New solver is faster and uses less memory than old Python solver.

**[00:37:26] Dan Khasis:** 25 minutes for 5000 locations is still too long. This is symptom. Root cause is inefficient clustering. No single cluster should have more than 2000 addresses. Long-term goal should be 5-10 minutes maximum for any optimization. But as interim solution, while we optimize solver, let's set timeout at 30 minutes. Anything longer than that, we kill it and tell user to break it into smaller optimizations. But we need to work toward that 5-10 minute goal aggressively.

**[00:39:04] Semeyon Svetliy:** So temporary timeout 30 minutes, strategic goal 5-10 minutes. Got it.

### DECISION: Strategic Solver Timeout Strategy

**DECIDED_BY:** Dan Khasis  
**DECISION:** Set temporary 30-minute timeout for strategic optimization with long-term goal of 5-10 minutes maximum execution time  
**RATIONALE:** Current 25-minute performance for 5000 locations is symptom of inefficient clustering. No cluster should exceed 2000 addresses. 30-minute timeout is interim compromise while solver and clustering algorithms are optimized. Strategic goal is aggressive reduction to 5-10 minutes to meet enterprise user experience expectations. [CEO_APPROVED - with mandated roadmap to 5-10 minute goal]  
**ALTERNATIVES_CONSIDERED:** ["No timeout", "15-minute timeout", "Dynamic timeout based on location count"]

### TECHNICAL_ISSUE: Strategic Solver Performance Bottleneck

**[00:37:26] Dan Khasis:** 25 minutes for 5000 locations is still too long. This is symptom. Root cause is inefficient clustering. No single cluster should have more than 2000 addresses.

### ACTION_ITEMS

- **OWNER:** Backend Team | **TASK:** Implement 30-minute timeout for strategic optimization solver | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Igor Skrynkovskyy | **TASK:** Optimize clustering algorithm to ensure no cluster exceeds 2000 addresses | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Igor Skrynkovskyy | **TASK:** Work toward 5-10 minute maximum execution time goal for strategic optimization | **STATUS:** in_progress | **PRIORITY:** high

---

## TOPIC: Address Book Map Performance Optimization

**TIME:** 00:48:20 - 00:50:15  
**PARTICIPANTS:** Vladimir Fedorov, Dan Khasis, Alexey Afanasiev

### DISCUSSION

**[00:39:25] Vladimir Fedorov:** [Explains optimization work on Address Book map for accounts with 10K+ addresses. Initially took up to minute to load with 30 seconds spent loading addresses alone. After backend optimization, reduced to 8 seconds for address loading.]

**[00:41:02] Dan Khasis:** Good work. But I wonder why users need to load 10,000 addresses at once. This suggests we don't have proper default views or smart filtering. Symptom of bigger UX problem. But thank you for optimization anyway.

### ACTION_ITEMS

- **OWNER:** Design Team | **TASK:** Investigate why users load 10K+ addresses at once - evaluate default views and smart filtering opportunities | **STATUS:** pending | **PRIORITY:** low

---

## TOPIC: Vehicle Tracking Visibility Crisis

**TIME:** 00:50:59 - 01:01:32  
**PARTICIPANTS:** Artur Moskalenko, Dan Khasis, Volodymyr Ishchenko, Igor Skrynkovskyy

### DISCUSSION

**[00:41:47] Artur Moskalenko:** I need to bring up issue with vehicle limits and tracking visibility. We have 100 vehicle default limit configurable in admin panel, but changes aren't applying due to caching bug. But bigger issue is vehicle tracking visibility.

**[00:42:15] Dan Khasis:** Go on, what's the tracking problem?

**[00:42:20] Artur Moskalenko:** After setting up Telematics Gateway, users can't see their vehicles because "pending" filter is disabled by default on Vehicles page. Additionally, map layers for vehicles and users aren't enabled by default on Vehicles and Users pages - only on Routes page. So vehicle tracking exists but is completely hidden. There's API for vehicle location that's been there for 15 years, but it's not exposed in UI outside route context.

**[00:45:11] Dan Khasis:** This is huge and embarrassing. This is exactly what I'm talking about. Competitors are right when they say we don't have vehicle tracking - because users can't find it! Feature exists but it's buried. Here's what needs to happen immediately. As soon as Telematics Gateway module is enabled for account, ALL tracking-related UI elements must be turned on by default everywhere. One - "pending" filter on Vehicles page ON by default. Two - Vehicle and User map layers ON by default on ALL pages with maps, not just Routes. Three - Users should see vehicle location in Vehicles Snapshot just like they see it in Route Editor. Four - Historical tracking should be visible. We have the data, we just don't show it. Volodymyr, you mentioned we don't have polylines in vehicles/users API response?

**[00:48:20] Volodymyr Ishchenko:** Correct, we have raw GPS points but not polylines like in routes. We could draw straightlines connecting points, but that looks ugly. Proper solution is to add polylines generation to backend for vehicles and users.

**[00:49:54] Dan Khasis:** Show the raw points FIRST. That's immediate solution. Straight lines connecting points every 30-60 seconds will look fine - much better than nothing. Polylines are nice-to-have optimization. But data is there, devices have local buffering and cache, even if connection drops for 5 hours all coordinates come through. Priority one is to show SOMETHING. Priority two is to make it pretty.

**[00:50:42] Igor Skrynkovskyy:** We're actually starting to collect full polylines from devices now - phones are sending complete detailed paths, not just points every 10 seconds. We're working with Andrey on compliance algorithm analysis. If it goes well we'll show this data in routes. But I don't think we can show one giant sausage of entire driving path for vehicle for all time. Better to use points for that.

**[00:51:28] Dan Khasis:** Fine. But that's future enhancement. TODAY the problem is we have vehicle location API working for 15 years and it's not visible anywhere except in route context. When you open Vehicles Snapshot there's nothing. When you open Vehicle page there's map but no vehicles shown. This must be fixed immediately. It's product death by a thousand feature flags.

**[00:52:05] Artur Moskalenko:** The feature checkboxes for Users and Vehicles map layers got tied to features during map refactoring and weren't added to default packages. That's root cause.

**[00:52:52] Dan Khasis:** This is exactly the problem. Every time we refactor something we accidentally hide existing functionality behind new feature flags that aren't enabled by default. This is systemic issue. When Telematics Gateway is enabled, it should automatically enable all dependent modules. Vehicle Tracking UI should be automatic dependency. Not separate optional feature.

### DECISION: Vehicle Tracking UI Must Be Visible By Default

**DECIDED_BY:** Dan Khasis  
**DECISION:** Immediately enable all vehicle tracking UI elements by default when Telematics Gateway module is active for an account  
**RATIONALE:** Competitors correctly claim Route4Me lacks vehicle tracking because feature is completely hidden from users despite 15-year-old working API. This is huge embarrassment and product failure. Specific requirements - (1) "pending" filter ON by default on Vehicles page so new vehicles appear immediately after Telematics setup, (2) Vehicle and User map layers ON by default on ALL pages with maps not just Routes, (3) Vehicle location visible in Vehicles Snapshot independent of routes, (4) Historical tracking data exposed in UI. Show raw GPS points immediately as straightlines - polylines are secondary optimization. Telematics Gateway should auto-enable all dependent tracking UI modules, not require separate manual feature flags. This is systemic refactoring problem - hiding working features behind new flags. [CRITICAL_DIRECTIVE - product reputation at stake]  
**ALTERNATIVES_CONSIDERED:** ["Keep current feature flag system", "Gradual rollout", "Wait for polylines before showing anything"]

### TECHNICAL_ISSUE: Vehicle Limit Caching Bug

**[00:42:20] Artur Moskalenko:** We have 100 vehicle default limit configurable in admin panel but changes aren't applying due to caching bug.

### TECHNICAL_ISSUE: Map Layer Feature Flags Hidden During Refactoring

**[00:52:05] Artur Moskalenko:** The feature checkboxes for Users and Vehicles map layers got tied to features during map refactoring and weren't added to default packages.

### ACTION_ITEMS

- **OWNER:** Backend Team | **TASK:** Fix vehicle limit caching bug preventing admin panel changes from applying | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Enable "pending" filter by default on Vehicles page for all accounts with Telematics Gateway | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Enable Vehicle and User map layers by default on ALL pages with maps (Vehicles, Users, Routes) for accounts with Telematics Gateway | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Show vehicle location in Vehicles Snapshot independent of route context using same UI as Route Editor | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Expose historical vehicle tracking data in API for UI consumption (raw GPS points as immediate solution) | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Add polylines generation for vehicles and users API (secondary enhancement after raw points deployed) | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Architecture Team | **TASK:** Create automatic dependency system where Telematics Gateway module auto-enables all related tracking UI features by default | **STATUS:** pending | **PRIORITY:** high

---

## METADATA

**TOTAL_TOPICS:** 6  
**TOTAL_DECISIONS:** 5  
**TOTAL_ACTION_ITEMS:** 23  
**KEY_FEATURES_DISCUSSED:** Service Time Analytics, Multi-Service Type Support, Strategic Optimization UI, Solver Performance, Address Book Map, Vehicle Tracking Visibility  
**TECHNICAL_ISSUES:** Dynamic Custom Service Types, Strategic Solver Clustering Performance, Vehicle Limit Caching, Map Layer Feature Flags Hidden  
**NEXT_MEETING:** Vladimir Zhakhavets presents multi-service type architecture concept (estimated 2025-11-20)
