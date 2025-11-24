[TRANSLATION METADATA]
- Source: full_transcript + summary
- Original Language: Russian + English technical terms
- Translation Date: 2025-11-22
- Transcript Accuracy: 96.7%
- Confidence Level: high

---

# Meeting Transcript (Full Translation)

**Date:** 2025-11-13 14:28
**Duration:** 01:02:10
**Participants:** 10
**Accuracy:** 96.7%

---

**Vova** [00:00:06 - 00:00:07]: Hello, Dan.

**Dan Khasis** [00:00:09 - 00:00:09]: Yes, hello.

**Vova** [00:00:16 - 00:01:54]: While you weren't here, I used the guys to help pick the palette. So, this is Customer Allocation Snapshot. Average Service Time. Here you can choose which type of Service Time you're looking at. You can look at Actual, Plant, the difference Actual vs Plant, or the percentage difference. And then you can choose the metric direction Lower is Better or Higher is Better. And from this, the palette colors from green to red or from red to green. Then, when hovering over a specific cell, you see the composition - how many total visits there were during this time, over all time, and how many on average. Yes, and we also forgot the control method here, the Average method. Which method to use for calculating - median or weighted average or with peak trimming. There will be another control here for selecting the Average method. What do you think? And I'll pass the screen to the guys.

**Alexey Afanasiev** [00:01:56 - 00:01:58]: Wait, you, Asterix.

**Dan Khasis** [00:02:08 - 00:02:44]: I don't know what I think. I think this is Customer Location, Destination. And this is on location, Customer Location from the book. But this, in principle, can be shown. The same thing in Route Destination Snapshot, right? In Destination Snapshot you can, but this would then refer not to this Destination, but to this address. No, it refers to this Destination.

**Vova** [00:02:44 - 00:03:08]: Well, to this address, because Destination is one visit. It's in one route, and Destination isn't repeated twice, but an address can occur multiple times. On an address this can be shown. That is, it can be shown in Destination Snapshot, but it will be tied not to Destination, but to the address. Because Destination is one visit.

**Dan Khasis** [00:03:14 - 00:03:23]: No, this is like in programming. You have PassByReference, PassByValue.

**Vova** [00:03:24 - 00:03:34]: But Destination is an instance of an address. One specific visit to this address in our paradigm, as far as I know.

**Dan Khasis** [00:03:35 - 00:04:02]: And in RouteData there can be Destination, and Destination has a full link to CustomerLocation. When you open Service Time, if I were a client, I would immediately understand that you highlighted with some icon that this is Service Time. Not of this Destination, but Service Time.

**Vova** [00:04:04 - 00:04:11]: Statistically. Statistically of this Location, yes. Well, we just need to write Location, Service Time and that's it, without an icon.

**Dan Khasis** [00:04:12 - 00:04:14]: Just need to make the link.

**Vova** [00:04:33 - 00:04:34]: Yes, this will be visible there.

**Alexey Afanasiev** [00:04:42 - 00:04:43]: Do you like the colors?

**Vova** [00:04:50 - 00:05:12]: There was a second idea - to highlight, give the user the ability to choose what they want to focus on, bad or good. If they say focus on bad, then red accents on bad things. If they say focus on good, then the palette flips, and here it becomes green to indifferent.

**Alexey Afanasiev** [00:05:33 - 00:05:43]: Dan, you dropped out from the second device. I didn't drop out.

**Dan Khasis** [00:05:43 - 00:11:37]: Here? I heard what Vova said when I reconnected. Vova is absolutely right. But this report doesn't show what Vova voiced. It needs to be done, advanced a bit, so I can explain what I mean. We have a problem due to legacy decisions, due to past decisions. If you look at custom location in our database, in UI or even in the database, we have two or three huge problems at the custom location level. Service time at the location level, but service time should be at the level of service type and location. The second problem is the incorrect assumption that at the level of one location there is only one service type. This is our second problem. Because here, as Vova said, there can be delivery, and service, and inspection, and so on. And here everything changes proportionally to this. Because if you made a route today, which was, which during planning, we have a fourth problem. That the destination type selection should somehow happen intelligently when you send. You have recurring schedule, but ours is wrong. Our recurring schedule is at the location level, but recurring schedule should be at location plus service time potentially. And then this service time dynamically changes by day of week and so on. That is, ordered and actual also change dynamically. But we don't have support for this. So if we're already doing this, we just need to finish it properly. Because right now I was talking with Parker about why we'll lose two deals right now. And it's because we can't plan from customer locations. We can't do planning from customer locations to what? Strategic? Strategic. Although they have a huge problem. What's their problem, this client? Their problem is they have 15 thousand destinations and they have 15 warehouses, depots. And Kh

wan has to do this manually? Or some assistant of Parker has to do this manually? Why can't, if you have one facility linked to a customer, and you selected all customers in some polygon? Or you selected, what are they called, drew something on the map, drew a polygon. And now you want to take, you want to make strategic? There may be an intermediate step that tells you, okay, we noticed that you selected there 15, 20, 100 thousand customers, and we noticed that these customers you selected, they're linked to various, what are they called, facilities. And now our task in this pop-up is to search, which facilities would you like to consider in this strategic optimization. And without limit, let's say, 500 pieces. Okay, 500 pieces. And now it says, ah, look, you have... We're talking about for-loop wrapper, that because of there five for-loop wrappers we're losing, you could say, millions of dollars. If you make abstraction to the highest level of this situation, that we're losing millions of dollars due to the absence of for-loops in async mode. Because how this would work, is that they would take, upload their 25 thousand addresses that are linked to facility, select all addresses in one go. Addresses are already tagged with something, for example, what are they called? Day of week, day of month, service type, service type by day of week and so on. And then simply a situation occurs where the system says, oh, look, they have there 15 depots. And it goes through each depot. It knows that this one has a thousand clients, this one has a thousand clients, this one has a thousand clients, this one has a thousand clients of the depot. And it simply initializes strategic on each depot. And this solves 80% of all problems for all clients. Because now they send their files that go to Bogdan or to Khemlut or to Vlad. They sit in Excel, a thousand fifty variants of these Excel files.

**Vova** [00:11:37 - 00:11:44]: Oh, show me service time like this, oh, show me service time like this.

**Dan Khasis** [00:11:44 - 00:13:30]: Because of what? Due to the absence of a new scenario where we can say, again, another for loop. Ah, change my service time plus-minus 10%, five intervals up and five intervals down. This is a new scenario. No, for this they have to upload 25 or 50 CSV files. Again because of for loop. So now it turns out that optimizers don't care, right? That's it. And the algorithm. It only matters to initialize. You don't even need to redo distance matrix, because it's already cached. Only some miserable service time changes. So what I'm trying to say is that this thing you drew, it's 90% correct, but it's 10% useful for the types of clients that David wants us to be able to sell to them. Because service time changes, as you yourself said. Service type from time of day, time of day, season and so on.

**Vova** [00:13:32 - 00:13:46]: If we tag these destinations somehow, when they do one type of service, when they do another type of service, then we can simply give them the ability to choose here and say which service type you want to consider now.

**Dan Khasis** [00:13:46 - 00:14:02]: Absolutely right. Or all at once, yes. And Artem should take, there's one thing missing in the tooltip, that as soon as we write average, people like David cling to this. This is why don't you use line energy, why don't you use this.

**Vova** [00:14:02 - 00:14:21]: They assume they know statistics. Yes, here there will be a way, averaging method, mathematical formula to choose. Which is used. And there will be several options.

**Dan Khasis** [00:14:22 - 00:14:47]: Such, such, such. Because there's moving average, exponential moving average, different options exist. Maybe we don't even publish, maybe we shouldn't even say our method.

**Vova** [00:14:47 - 00:14:55]: Why even write average at all?

**Dan Khasis** [00:14:55 - 00:16:02]: Maybe we can write service time, detected service time. Why even write the word average, if it comes to that? Well, I think smart guys will want to know what math is inside. Yes, so smart guys, you'll click on the cell, and you'll open a scatter plot, or you'll open a line graph that will be a curve both by time and by the selected range of this report. This curve will show, as in scope, green-yellow-red ranges, and it will, and the curve will show within those ranges, within that historical trend history for that cell. Because the cell is an hourly range plus a factor. Factor like day of week, factor like season, factor like quarter, and so on. We need to look, if you want, right now on custom allocations, right now to decide or figure out how to add service type and time in custom allocations editor.

**Vova** [00:16:12 - 00:16:40]: I'll think about it. If very quickly, what I think about it now, possibly it's something like some new entity, a service contract for this customer location, you can have multiple service contracts simultaneously for the same location, and each contract has its own schedule, its own conditions, its own visit frequency and visit duration.

**Dan Khasis** [00:16:41 - 00:16:58]: Yes, but even before talking about contract, we can talk about, not even talk about contract, but just add an elementary config table in custom allocations. The most elementary.

**Vova** [00:16:59 - 00:17:35]: Yes, and then... Imagine you have a location. In this location editor, there's currently nothing related to scheduling or service type. But there should be. What should be there? There could be something like a table. Just imagine, a table. Location - service type, frequency - there's already frequency. But duration. Duration. And you can add rows. Click add. Service type - delivery. Frequency - daily. Duration - 20 minutes. Add. Service type - inspection. Frequency - weekly on Mondays. Duration - 40 minutes. You add a row. And so there can be multiple rows in this table.

**Dan Khasis** [00:17:35 - 00:18:17]: When you come to strategic, you'll already have what should be planned. Instead of manually in Excel creating multiple CSVs for one and the same address. This all already exists in database and in the table. So strategic, we'll automatically understand, ah, this one - delivery, that one - delivery and service, that one - only service. Moreover, even when you start planning master routes with this logic, it becomes clear what's planned. Because now when someone plans, or when someone makes recurring schedule, the assumption is the same visit everywhere. But there can be different visits depending on the day. Different visits.

**Vova** [00:18:17 - 00:18:56]: Well, that's how custom routes generally are, we have a recurring visit. But here we can have two recurring visits. Not one. Multiple. And then, at the optimization stage, we have this whole table. At the planning stage, like at the strategic stage, I select my locations and say I want to make strategic optimization. In the background, strategic optimization goes and looks, oh, look, these locations of yours, they have not just one service type, but three different ones. Which one do you want to optimize for today?

**Dan Khasis** [00:18:56 - 00:19:01]: So we still need dynamic custom types.

**Vova** [00:19:01 - 00:19:15]: But if we have these service types, this is no longer a problem. Because we'll just pass them to strategic. And strategic optimization will have no problem with this.

**Dan Khasis** [00:19:15 - 00:19:18]: What do you mean? What's our problem with custom types?

**Vova** [00:19:18 - 00:19:36]: I don't know if this is a backend or database problem. We can't dynamically add service types. They're kind of hardcoded in our database. Right? They're stored in some kind of enum or something. And we can't dynamically add service types.

**Dan Khasis** [00:19:37 - 00:19:45]: Yes. We need to make a service types table. Where there are enums that exist by default in the system.

**Vova** [00:19:45 - 00:20:22]: And the user can add their own. User can add and create. But then the problem is, remember we discussed with Igor, we have different icons for different service types. If someone creates their own service type, we can't have an icon for it. So we'll just give them a circle or a square. They draw icon themselves. Then another problem. When you're making a destination, when you're planning a route, you say, what's your service type today? In this dropdown, you need to show all these different service types. Or you need to say, this is fixed for this location - service type.

**Dan Khasis** [00:20:22 - 00:21:47]: This is what I'm talking about. When destination is created, destination is created based on customer location. When you're making new destination, system looks, ah, customer location X, look, this customer location has these service types configured. If these service types are fixed, meaning, like, delivery always, service once a week, inspection once every two weeks - this is recurring schedule. Then route planner can automatically in UI say, I see that you added this customer location, oh, and I see that today according to its schedule, it should have service and inspection, not delivery, because delivery is on other days. And here the route planner already knows from the schedule. But if the schedule isn't fixed, route planner simply offers all available service types for this location as possible options, and user picks which they want. But the problem is that now, when route planner creates destination for this location, if there are three different service times, the system doesn't know which service time to assign.

**Vova** [00:21:47 - 00:22:21]: Well, in the dropdown you'll select service type first, and only after you select service type, the system can autocomplete service time based on that service type. Okay, let's say user manually creates destination for this customer location. First they pick service type. Then service time automatically fills in. If not, they can override. Okay. But we still have a huge problem. That service time can change by day of week.

**Dan Khasis** [00:22:21 - 00:22:34]: Even more. Time of day, day of week. Because, for example, morning rush hour. Morning delivery might take longer than afternoon delivery.

**Vova** [00:22:34 - 00:23:44]: So service time becomes not a number anymore. Service time becomes a function. A formula. Service time equals if day of week equals Monday and if time of day between 8 and 10 AM, then 30 minutes, else if... Or maybe it's a table. Like, you have a table. Column one - day of week. Column two - time of day range. Column three - service time. And you have rows. Monday, 8-10 AM, 30 minutes. Monday, 10 AM-12 PM, 25 minutes. Tuesday, 8-10 AM, 20 minutes. This is the service time table.

**Dan Khasis** [00:23:44 - 00:24:19]: This is exactly what I showed in heat map. But we're not showing this for individual location. We're showing aggregated statistics. What you're talking about, each location should have its own mini heat map potentially. In the location editor. Click on service time cell, boom, opens a modal with this table, or this heat map. User fills it in. Or system automatically learns from history. System says, based on your past visits to this location, we detected these patterns. Do you want to use detected patterns or override manually?

**Vova** [00:24:19 - 00:24:34]: Automatically learning from history is exactly what the analytical report does. The report you're seeing now. This is what it does. It aggregates historical data.

**Dan Khasis** [00:24:34 - 00:25:13]: But this is aggregated across all locations. What I'm saying is, for each individual location, system should be able to say, for customer location ABC Plumbing, we detected that on Mondays at 9 AM, service time is usually 45 minutes, but on Fridays at 3 PM it's 20 minutes. And this is specific to ABC Plumbing, not averaged across all customers. That's the difference. This report is useful for enterprise analytics. But for route planning and optimization, we need per-location intelligence.

**Vova** [00:25:13 - 00:25:47]: I understand. So in the location editor, there should be something like... A button. "Configure Service Time Intelligence" or something. Click it, opens a modal. Shows the same heat map, but filtered to this location only. Shows historical patterns. User can accept automated suggestions or manually override any cell. Save. Now this location has intelligent service time.

**Dan Khasis** [00:25:47 - 00:26:29]: Exactly. And this intelligence should be used everywhere. In recurring schedule, in strategic optimization, in route planning. Everywhere. So this is why I'm saying, this report is great for analytics team, for management to understand overall performance. But it doesn't solve the core problem, which is: how do we intelligently assign service time during planning, taking into account service type, day of week, time of day, and historical patterns for that specific location?

**Vova** [00:26:29 - 00:26:54]: Got it. So this report is a foundation. It shows the system works. But we need to extend this intelligence down to individual location level. And make it actionable in editors. I'll work on this. Show you the concept next week.

**Alexey Afanasiev** [00:26:54 - 00:27:03]: Can I show strategic optimization now? I think we should move on. We have limited time.

**Dan Khasis** [00:27:03 - 00:27:06]: Yes, go ahead.

**Manar Kurmanov** [00:27:03 - 00:30:11]: [Demonstrates new strategic optimization UI flow, showing selection from customer locations list, filtering options, and the new "Create Optimization" workflow. Explains that instead of starting with file upload, users now start with selecting customer locations, can filter them, then proceed to configure optimization settings.]

**Dan Khasis** [00:30:11 - 00:33:08]: This is much better than before. Starting from customer locations makes sense. But I have critical feedback on the depot selection step. [Shows screen] Here, you have a text input field where user types depot address and geocodes it. This is completely wrong approach for enterprise clients. They don't want to type depot address every time. They have 15 depots already configured in the system. They want to SELECT from existing facilities, not type and geocode new ones. This text field should be replaced with a searchable, filterable table showing all their existing facilities. User checks the ones they want to use for this optimization. It's like selecting customers - same UX pattern. And THEN, as a secondary option, if they really need to add a new depot for what-if scenario, there can be a button "Add New Depot" which opens geocoding. But primary flow is SELECT existing facilities. This is non-negotiable for enterprise. Without this, we can't sell to large clients.

**Manar Kurmanov** [00:33:08 - 00:33:42]: Understood. So main interface is a facilities table with checkboxes and search. Adding new depot address is secondary option, accessed via button. Will redesign this immediately.

**Semeyon S** [00:33:42 - 00:33:54]: While we're on strategic optimization topic, I have a question about solver performance. What's acceptable timeout?

**Dan Khasis** [00:33:54 - 00:34:15]: What are we seeing now? What's current performance?

**Igor Skrynkovskyy** [00:34:15 - 00:37:26]: Currently with new FastAPI solver using C++ library, we're seeing much better performance. 2500-5000 locations taking about 25 minutes. Above 1500 addresses, automatic clustering kicks in. The new solver is faster and uses less memory than old Python solver.

**Dan Khasis** [00:37:26 - 00:39:04]: 25 minutes for 5000 locations is still too long. This is a symptom. The root cause is inefficient clustering. No single cluster should have more than 2000 addresses. Long-term goal should be 5-10 minutes maximum for any optimization. But as interim solution, while we optimize the solver, let's set timeout at 30 minutes. Anything longer than that, we kill it and tell user to break it into smaller optimizations. But we need to work toward that 5-10 minute goal aggressively.

**Semeyon S** [00:39:04 - 00:39:12]: So temporary timeout 30 minutes, strategic goal 5-10 minutes. Got it.

**Alexey Afanasiev** [00:39:12 - 00:39:25]: Can I quickly show Address Book map performance improvements?

**Vladimir Fedorov** [00:39:25 - 00:41:02]: [Explains optimization work on Address Book map for accounts with 10K+ addresses. Initially took up to a minute to load, with 30 seconds spent loading addresses alone. After backend optimization, reduced to 8 seconds for address loading.]

**Dan Khasis** [00:41:02 - 00:41:38]: Good work. But I wonder why users need to load 10,000 addresses at once. This suggests we don't have proper default views or smart filtering. A symptom of bigger UX problem. But thank you for the optimization anyway.

**Artur Moskalenko** [00:41:47 - 00:42:15]: I need to bring up an issue with vehicle limits and tracking visibility. We have a 100 vehicle default limit that's configurable in admin panel, but changes aren't applying due to caching bug. But bigger issue is vehicle tracking visibility.

**Dan Khasis** [00:42:15 - 00:48:20]: Go on, what's the tracking problem?

**Artur Moskalenko** [00:42:20 - 00:45:11]: After setting up Telematics Gateway, users can't see their vehicles because "pending" filter is disabled by default on Vehicles page. Additionally, map layers for vehicles and users aren't enabled by default on Vehicles and Users pages - only on Routes page. So vehicle tracking exists but is completely hidden. There's API for vehicle location that's been there for 15 years, but it's not exposed in UI outside route context.

**Dan Khasis** [00:45:11 - 00:48:20]: This is huge and embarrassing. This is exactly what I'm talking about. Competitors are right when they say we don't have vehicle tracking - because users can't find it! The feature exists but it's buried. Here's what needs to happen immediately: As soon as Telematics Gateway module is enabled for an account, ALL tracking-related UI elements must be turned on by default everywhere: 
1. "Pending" filter on Vehicles page - ON by default
2. Vehicle and User map layers - ON by default on ALL pages with maps, not just Routes
3. Users should see vehicle location in Vehicles Snapshot - just like they see it in Route Editor
4. Historical tracking should be visible - we have the data, we just don't show it

Volodymyr, you mentioned we don't have polylines in vehicles/users API response?

**Volodymyr Ishchenko** [00:48:20 - 00:49:54]: Correct, we have raw GPS points but not polylines like in routes. We could draw straightlines connecting points, but that looks ugly. Proper solution is to add polylines generation to backend for vehicles and users.

**Dan Khasis** [00:49:54 - 00:50:42]: Show the raw points FIRST. That's the immediate solution. Straight lines connecting points every 30-60 seconds will look fine - much better than nothing. Polylines are nice-to-have optimization. But the data is there, the devices have local buffering and cache, even if connection drops for 5 hours, all coordinates come through. Priority one is to show SOMETHING. Priority two is to make it pretty.

**Igor Skrynkovskyy** [00:50:42 - 00:51:28]: We're actually starting to collect full polylines from devices now - phones are sending complete detailed paths, not just points every 10 seconds. We're working with Andrey on compliance algorithm analysis. If it goes well, we'll show this data in routes. But I don't think we can show one giant sausage of the entire driving path for a vehicle for all time. Better to use points for that.

**Dan Khasis** [00:51:28 - 00:52:05]: Fine. But that's future enhancement. TODAY the problem is we have vehicle location API working for 15 years and it's not visible anywhere except in route context. When you open Vehicles Snapshot, there's nothing. When you open Vehicle page, there's map but no vehicles shown. This must be fixed immediately. It's product death by a thousand feature flags.

**Artur Moskalenko** [00:52:05 - 00:52:52]: The feature checkboxes for Users and Vehicles map layers got tied to features during map refactoring and weren't added to default packages. That's the root cause.

**Dan Khasis** [00:52:52 - 00:53:45]: This is exactly the problem. Every time we refactor something, we accidentally hide existing functionality behind new feature flags that aren't enabled by default. This is systemic issue. When Telematics Gateway is enabled, it should automatically enable all dependent modules - Vehicle Tracking UI should be automatic dependency. Not separate optional feature.

**Volodymyr Ishchenko** [00:53:45 - 00:54:23]: I want to add - we've been recording vehicle history for a long time. Igor, correct me if wrong, but there are no polylines in the response for vehicles and users specifically. For routes we have polylines. For vehicles and users we don't. But we have raw points that we can draw with straightlines, but it won't look pretty. So first, we need to add polylines to backend for vehicles and users.

**Dan Khasis** [00:54:23 - 00:55:08]: What's your opinion on why it won't look pretty? Points are connected point-to-point. If they come every 30-60 seconds, the line will be adequate. Show the points. That's priority one. Generating polylines is priority two. Doing something else is priority three.

**Igor Skrynkovskyy** [00:55:08 - 00:56:29]: We're starting to collect full detailed polylines from devices now - the phones send us polylines, not just points once every 10 seconds or once a minute. They send us complete detailed path of how the vehicle drove. We're analyzing this data now for compliance algorithm. If everything works well, we'll display this data in routes. But I don't think we'll be able to show one long sausage of everywhere the vehicle drove for all time. Better to use points for that.

**Dan Khasis** [00:56:29 - 00:57:11]: Okay, I'm very late for this other meeting. I have to go. There's no information here. Okay, I have to go again, I'm very late.

**Igor Skrynkovskyy** [00:57:11 - 00:57:12]: Okay, bye then.

**Dan Khasis** [00:57:12 - 00:57:13]: Thanks, bye.

**Igor Golovtsov** [00:57:13 - 00:57:18]: Semeyon, Manar, while you're both here, before you run away. I have a question about...

[Meeting ends]

---

## Statistics

### Participants

- **Dan Khasis**: 182 segments, 00:32:44 (52.7%), accuracy 96.0%
- **Manar Kurmanov**: 26 segments, 00:01:59 (3.2%), accuracy 96.1%
- **Vova**: 25 segments, 00:06:35 (10.6%), accuracy 98.4%
- **Igor Skrynkovskyy**: 22 segments, 00:05:15 (8.5%), accuracy 98.5%
- **Alexey Afanasiev**: 15 segments, 00:00:49 (1.3%), accuracy 97.4%
- **Semeyon S**: 12 segments, 00:02:14 (3.6%), accuracy 98.7%
- **Artur Moskalenko**: 9 segments, 00:03:11 (5.1%), accuracy 99.0%
- **Igor Golovtsov**: 4 segments, 00:00:10 (0.3%), accuracy 96.0%
- **Vladimir Fedorov**: 3 segments, 00:00:46 (1.2%), accuracy 97.7%
- **Volodymyr Ishchenko**: 2 segments, 00:00:33 (0.9%), accuracy 99.0%

### Alignment Quality

- High confidence (time-based): 298 (99.3%)
- Resolved via LLM: 0 (0.0%)
- Fallback: 2 (0.7%)
- Average confidence: 96.7%
- [!] Low confidence (<70%): 1 segment (0.3%)
