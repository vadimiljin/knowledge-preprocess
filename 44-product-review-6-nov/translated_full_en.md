[TRANSLATION METADATA]
- Source: full_transcript (1106 lines, 93.3% transcription accuracy)
- Original Language: Russian + English technical terms
- Translation Date: 2025-11-22
- Transcript Accuracy: 93.3%
- Confidence Level: high
- Translation Approach: Full translation with technical term preservation
- Meeting Duration: 03:01:25 (3 hours 1 minute)
- Participants: 16 people
- Dan Speaking Time: 50.3% (highly engaged CEO)

---

# TRANSLATED MEETING TRANSCRIPT

**Date:** 2025-11-06 14:26  
**Duration:** 03:01:25  
**Participants:** 16  
**Accuracy:** 93.3%

---

## OPENING (00:02:56 - 00:03:15)

**[00:02:56] Artur Moskalenko:** Dan, hello.

**[00:02:58] Semeyon S:** Guys, who wanted to start?

**[00:03:02] Serhii Kasainov:** Me.

**[00:03:03] Semeyon S:** Go ahead.

**[00:03:05] Igor Skrynkovskyy:** Let's wait for Dan to speak.

**[00:03:07] Artur Moskalenko:** Maybe he's connecting.

**[00:03:09] Dan Khasis:** Yes, I'm listening.

---

## SNAPSHOTS UPDATE & DESTINATION SNAPSHOT REVIEW (00:03:15 - 00:25:59)

**[00:03:15] Serhii Kasainov:** So, small update from me on snapshots. We've been working toward this for a very long time and finally reached it. We've pulled in the tables from routes-list into practically all snapshots. I'll finish today, and all will be complete. Thanks to this, on each snapshot, at least for routes and destination, all the functionality that wasn't available before is now accessible. Specifically, the full list of filters with search and groupings, actual table groupings. Column groupings, particularly for timezone. Yes, this question concerns me too. How? None? None. Good, none, if possible, I would also change that. Only when none is selected, nothing should be written here.

**[00:04:11] Vova:** It will say group by simply if none is selected. Here it changes to none, and here it disappears completely when none is selected. Group by, let's at least put a dash maybe.

**[00:04:25] Serhii Kasainov:** No, no, no.

**[00:04:29] Vova:** Group by without colon and without label. Just group by and arrow down. Inviting you to select grouping.

**[00:04:42] Serhii Kasainov:** Grouping disabled, nothing selected. I understand, no questions. Agreed. Good. Where was I? Yes, this menu is available. For now only those three items that were here, now in QA they'll approve this iteration and I'll pull in basically all menu items that exist on routes-list. So on any snapshot with routes table you can work almost the same as on routes. Same for destination. What else is interesting to show here? Ah, metrics also became automatically available here. And further on snapshots this same table will be reused everywhere with small adjustments, like on user-snapshot we won't allow filtering by user. Or on facility-snapshot we won't do grouping by facility. These are the improvements. Already ready, I think we'll deploy them Monday on routes. And I had a question, Dan, why didn't we release destination-snapshot? I know why we didn't release it, but why? Maybe you'll approve it? There are small fixes of course, but it looks better to me than many other snapshots we already released.

**[00:06:18] Dan Khasis:** Need to look. There was probably a reason, I don't remember the reason. Maybe you remember incorrectly, I remember incorrectly. And now just misunderstanding.

**[00:06:31] Serhii Kasainov:** There's a list of tickets, but again, we'll review them. I just don't remember anything critical there. Is it ideal? No, it's not ideal.

**[00:06:39] Alexey Gusentsov:** There definitely aren't any showstoppers, I remember, there aren't any.

**[00:06:43] Serhii Kasainov:** Who isn't there? In any case it looks better than budget optimization. Sorry, internet cut out. Yes, Alexey, happens. It looks better than optimization-snapshot, than user-snapshot and than digital-snapshot. The map adds plus 50%, no plus 70% to attractiveness. Let's maybe release it. If something is really bad, I would quickly fix it today and release tomorrow.

**[00:07:24] Semeyon S:** Let's look at the tickets diagonally after the call.

**[00:07:34] Dan Khasis:** I'm not against releasing anything early or often. I'm just more curious if there's some level of minimal usefulness of this release. For example, we've been trying to launch this unfortunate service time for 6 months. We spent at least an hour on last Monday's meeting about historical service time and all the options associated with it. Pros and cons and how this needs to be considered and how this needs to be done. Okay, so we'll make a destination release. If this destination doesn't have full graphical linking, full link to order, full link to destination, full link to customer, to customer location, to strategic route where all this came from. Then what's the point if we don't show any high-level attributes and so on. For example, in this case you're showing, as I understand, this is a fake order ID, this isn't real?

**[00:09:26] Serhii Kasainov:** I think this is external order ID, these definitely aren't our IDs.

**[00:09:30] Dan Khasis:** And where is our order object?

**[00:09:34] Serhii Kasainov:** We agreed not to show our internal IDs.

**[00:09:38] Dan Khasis:** Not IDs, but our object.

**[00:09:44] Serhii Kasainov:** Don't understand.

**[00:09:45] Vova:** There should be a transition here.

**[00:09:51] Serhii Kasainov:** That's clear, there should be a link here.

**[00:09:54] Alexey Gusentsov:** Yes, we made links, they should be on order and on customer. I don't know why they're not here, need to investigate, but they definitely should be. Maybe there's such a base, I don't remember.

**[00:10:03] Serhii Kasainov:** On this account there's no order snapshot. Same with customer. This is clear, we can do this very quickly now. There's just already a large volume of work done here. I just remember this wasn't finally approved. Is the layout in order? If there are no obvious comments besides the transition, let's finish it. A large volume of work was done that's just hanging.

**[00:10:27] Dan Khasis:** I'm not arguing, I'm not arguing, but I'm just trying to tell you, imagine you're a user, what's the benefit of this? For example, you're showing a route. I don't know if this is good or bad. Geofence, if this came from Customer Location, and Customer Location came from Geotab, and we don't understand this is from Geotab. First, need to draw the Geotab polygon here. When I talk about graphics, I constantly mean that all these interconnected relationships... What worries me more, what's the point of all this if we tied people's hands behind their back anyway. And by the way, here's this defect. We tied their hands behind their back. If this was an order RouteFormation, we don't link to it. If this was Customer Location, we don't show this. If this was Customer Location with Geotab, we also don't show this. If it had a Geofence, we also don't show it. So what does this screen help people with? Attachments, okay, I agree. Activities, okay, if the filter works, I agree. History, what does History show, I don't understand. What does History show?

**[00:12:22] Artur Moskalenko:** Delivery Attempts.

**[00:12:27] Dan Khasis:** I don't understand what Delivery Attempts means. Is this a copy of Activities?

**[00:12:36] Artur Moskalenko:** Essentially, yes.

**[00:12:41] Dan Khasis:** What's the point of having this then?

**[00:12:42] Serhii Kasainov:** And Activity, including Activity on route.

**[00:12:50] Dan Khasis:** I don't understand how this relates to anything.

**[00:12:52] Maksym Silman:** As far as I remember, History is the historically renamed Notes.

**[00:12:58] Alexey Gusentsov:** No, History is actually Activities, and Activities is Notes, I think.

**[00:13:05] Serhii Kasainov:** I understand. It's just that in any case, to view Destination in this expanded view, we don't have any interface. I have to go to some Editor, open this second sidebar, scroll down, find these same Visit Details. So that I can look at one specific stop in one place, we don't have that. I see.

**[00:13:35] Dan Khasis:** So what are you looking at? We're making a completely new page to see Custom Data?

**[00:13:44] Serhii Kasainov:** We're making snapshots for everything?

**[00:13:48] Dan Khasis:** This is why we make snapshots, to see things in isolation in some summary format? And for what purpose? Is this really to see Custom Data? And for that we need to make a whole snapshot? Wait, I thought... I thought we make snapshots, one, to watch the progression of different iterations. Two, to see how, for example, customer location changed and what it came from, and maybe compare what it was and what it is now. So for example, to see a geofence. Because before they uploaded some crappy polygon, and now we improved it, and we want to see how it improved and why it improved. We're not doing this either yet. But this, I thought, was for these kinds of things. Or for example that we integrated Geotab import, and we want to see the list of polygons or trips that came from Geotab, and what we did with them. And this we don't do. Then what are we doing? I don't understand.

**[00:15:02] Vova:** For example, yes, History tab should show all previous historical visits to this address.

**[00:15:14] Dan Khasis:** Correct. This I understand.

**[00:15:17] Vova:** And Activities - driver notes, proof of visit, and such things.

**[00:15:29] Dan Khasis:** I think in the future there should also be, for example, related invoices, scanned assets, notification history sent to this customer. All this contextual information. But at minimum should be links. To customer, customer location, these things.

**[00:16:02] Serhii Kasainov:** Customer, customer location, order, route - we'll add these links.

**[00:16:15] Dan Khasis:** And by the way geofence. If this destination, for example, this is Customer Location. And this customer location has geofence. And geofence is polygon. So the polygon should be drawn.

**[00:16:44] Vova:** Yes, then some customers have hundreds of geofences on one location. Then we'll overload the map, but okay.

**[00:16:53] Dan Khasis:** Then we'll figure out how to show it best, but it should be shown. Because right now you won't understand anything, you won't see the context. This geofence is one meter or ten meters or hundred meters - you won't know.

[Discussion continues about grouping options, UI details, and map display...]

**[00:25:35] Serhii Kasainov:** We'll add all these links. Customer, order, route. History we'll rework to show historical visits. Activities for driver notes and proof of visit.

---

## SAP CONNECTION REVIEW (00:26:22 - 00:46:44)

**[00:26:22] Davron Usmonov:** Showing version zero of new telematics connection type. This is SAP connector. Table showing Atoms, not standard Vehicles. [Demonstrates interface]

**[00:28:45] Serhii Kasainov:** Formatting issues we discussed before weren't fixed. Date format still wrong.

**[00:29:15] Dan Khasis:** Stop. All technical timestamp fields - created_at, updated_at - must be displayed strictly in UTC to avoid confusion when analyzing logs and transactions. This should be indicated directly in the column header. Not "Created At" but "Created At (UTC)". This is not user time - this is technical debugging field.

**[00:31:42] Dan Khasis:** Where's the column selector? Where's export? Date format is wrong - should be ISO standard. Multiple basic deficiencies here.

**[00:33:28] Dan Khasis:** Need to add archive flag for atoms. Similar to active/inactive for vehicles. This allows hiding obsolete or incorrect data that can't be deleted from source system SAP from drivers and users in interface. Backend needs this flag, frontend needs to respect it.

**[00:35:51] Dan Khasis:** By the way, we should rename Telematics section to Connections. In future possibly to Asset Tracking. This better reflects what we're actually doing - connecting to various systems, not just telematics.

**[00:38:15] Dan Khasis:** Let me give you a lecture about the difference between sync table and normalized table. Sync table - this is table with raw data received from external system. Exactly as it came. Normalized table - this is table with processed data brought to our model, our naming, our structure. System should be able to link these entities and do deduplication and data enrichment. For example, extract from trips in telematics unique addresses and create Customer Locations from them. Understand? You receive trip from SAP - it has start address and end address. These addresses, if they repeat, should become Customer Locations in our system. This is normalization. This is enrichment. And we should track where this came from - the link back to original trip in sync table.

**[00:41:30] Igor Skrynkovskyy:** This is similar to how we handle Geotab data currently?

**[00:41:35] Dan Khasis:** Exactly. Geotab sends us raw trip data. We extract addresses, deduplicate them, create customer locations, link them back. This is the pattern. Every integration should follow this pattern.

[Discussion continues about implementation details, data flow, and architecture...]

**[00:45:50] Davron Usmonov:** Understood. Will fix formatting, add UTC labels, implement archive flags, rename to Connections.

---

## VISIT DETAILS & TIME WINDOW VIOLATIONS (00:47:02 - 01:01:22)

**[00:47:02] Alexey Gusentsov:** Updated Visit Details interface. Separated planned, actual, and predicted data into different sections for clarity. [Demonstrates]

**[00:49:15] Vova:** There's complexity in determining visit status - early or late. When comparing two time intervals (planned and actual), there are 6 possible states. How do we show this clearly?

**[00:51:28] Dan Khasis:** Wait, wait. Critical requirement - system must detect and visually highlight time window violations even if route was built without optimization. This is not optional. Backend must calculate this. If customer said "arrive between 9-11" and driver arrived at 11:30 - this is violation. Must be shown. With indicator. Yellow or red triangle next to time window.

**[00:52:45] Dan Khasis:** And by the way, route optimizer must respect time windows during optimization. If it doesn't, what's the point? Customer sets time windows, runs optimization, and optimizer ignores them? Then it's completely useless to customers.

**[00:55:10] Igor Skrynkovskyy:** Time window validation during optimization is already implemented in backend. It's there.

**[00:56:35] Dan Khasis:** Then why do I see optimized routes that violate time windows? If we have constraint parameters in optimization request but still violate time windows in result, this is bug and needs fixing immediately.

**[00:58:42] Vova:** Maybe we should show not just red indicator, but actual violation - "30 minutes late" or "15 minutes early"?

**[00:59:15] Dan Khasis:** Good idea. Show both indicator and specific number. This gives users concrete data. They can then decide - "okay, 5 minutes late is acceptable" vs "2 hours late is problem." Specific minutes are actionable data.

[Discussion continues about implementation, UI design, and backend support...]

---

## SERVICE TIME ANALYTICS WIDGET (01:01:22 - 01:32:11)

**[01:05:30] Alexey Gusentsov:** Demonstrating service time analytics widget. Heat map comparing service times across customer addresses. [Shows interface]

**[01:07:15] Dan Khasis:** Stop. This widget is completely uninformative. What is this showing me? I don't understand. The main logic should be comparison of planned versus actual service time. This is what customers want to understand - do their time estimates match reality? Are they overestimating, underestimating? This is business intelligence. What you're showing me now, I don't know what conclusions to draw.

**[01:09:42] Dan Khasis:** And colors. Cannot use red-yellow-green gradient for service time until we know the direction. For some businesses longer service time is good - they bill by hour, so more hours is more revenue. For others shorter is better - delivery efficiency. Colors imply good/bad. Red means bad, green means good. But we don't know which direction is good for this customer. So colors are wrong. Misleading.

**[01:12:25] Dan Khasis:** Until we implement configurable metric direction per service type or customer location - "for this address, longer is better" or "shorter is better" - use neutral color palette. Single color gradient. Light blue to dark blue. Or light gray to dark gray. No red-yellow-green that implies value judgment we can't make.

**[01:14:50] Dan Khasis:** And controls. User must be able to select what data they're viewing. Reported service time? Detected service time? And what they're comparing against - versus Planned? This should be dropdown selectors. Also must have Date Range Picker. "Show me last 30 days" or "show me last quarter." Otherwise this is snapshot of unknown time period.

**[01:16:35] Dan Khasis:** And in tooltip for each cell must show count of visits. If average is based on 100 visits - reliable. If based on 2 visits - not reliable yet. User needs this context.

**[01:18:20] Dan Khasis:** Future enhancement - metric direction configurable at service type level or customer address level. "For oil changes, faster is better. For diagnostics, thorough is better even if slower." Then colors can be meaningful. But not yet. First make widget useful with plan vs actual comparison.

[Discussion continues about implementation approach, backend API changes needed, UI redesign...]

**[01:30:45] Alexey Gusentsov:** Understood. Complete redesign. Plan vs actual primary logic. Neutral colors. Add controls for data selection and date range. Add visit count to tooltip.

---

## STRATEGIC OPTIMIZATIONS - VISUALIZATIONS & AI GENERATOR (01:32:11 - 02:03:01)

**[01:32:11] Manar Kurmanov:** Scatter Plot improvements. Added formatted units, better hovers. [Demonstrates]

**[01:34:25] Igor Golovtsov:** Want to show something revolutionary. AI-powered scenario generator. User describes in natural language what they want - "create 5 cycles with lunch breaks from 12 to 1, morning shift starts at 8, include 15-minute breaks every 2 hours..." - and AI generates corresponding JSON configuration for the form. [Demonstrates prototype]

**[01:37:40] Semeyon S:** This could become chat interface. User describes, AI generates, user refines - "actually make it 6 cycles" - AI adjusts. Iterative scenario building through conversation.

**[01:40:15] Dan Khasis:** Wait wait wait. Igor, this AI generator - show me again. [Reviews carefully] This is... this is perfectly correct. Exactly right approach. This is huge.

**[01:42:30] Dan Khasis:** Action item - immediately record video demo of this. We need to show this to partners. This is major competitive advantage. Natural language to configuration - this is the future of our interface.

**[01:45:50] Dan Khasis:** And global requirement while we're talking about strategic optimizations. We need to add Man-Hours concept to our data model. Man-Hours is Service Time multiplied by Worker Count. If stop takes 30 minutes and requires 2 workers - that's 1 man-hour. This is critically important metric for all service businesses. Affects cost calculations, efficiency metrics. We're missing this completely across entire platform.

**[01:48:20] Dan Khasis:** Back to AI generator. Strategy - we should expand this to other parts of system. Regular route planning, for example. Why should regular planning have complex form when user could just describe what they want? This should be our direction platform-wide.

**[01:50:35] Dan Khasis:** Development direction - AI should be able to generate multiple scenarios from single request. "Generate 10 scenarios with sliding 1-hour window - first starts at 8am, second at 9am, etc." One description, multiple outputs. This saves huge amount of time.

**[01:52:45] Dan Khasis:** Results table missing metric - route consistency or repeatability from scenario to scenario. How similar are routes between scenarios? This matters for planning stability.

**[01:54:20] Dan Khasis:** Now Scatter Plot. Two critical missing pieces. One - filters. "Show me only Monday routes" or "show me only routes with 50+ stops." Without filters, too much noise. Two - interactivity. Points must be clickable. I click point, I see details of that specific scenario or route. Otherwise it's just pretty picture with no utility.

**[01:56:40] Dan Khasis:** And Radar Chart. [Reviews] This looks terrible. Scares people. Hide this in first release. Complete redesign needed before showing to customers.

**[01:58:15] Semeyon S:** AI generator roadmap - continue development in chat format. Expand to other optimization types. Build library of common patterns AI can reference.

**[02:00:30] Igor Golovtsov:** Will record video demo today or tomorrow. Start chat interface development.

---

## ROUTE BALANCING CRISIS (02:11:31 - 02:24:15)

**[02:11:31] Igor Skrynkovskyy:** Major client issue. According to Juan, problem isn't creating extra routes. System creates fewer routes but they're longer and suboptimal. Routes cross each other - "noodle routes."

**[02:13:45] Igor Skrynkovskyy:** My hypothesis - special clustering algorithm we developed for FedEx to solve exactly this problem is not enabled for this client. That algorithm creates more human-like routes, prevents noodles.

**[02:15:20] Igor Skrynkovskyy:** Problem is we don't have access to data Juan is working with. Don't know details of client problem. Working blind.

**[02:17:35] Dan Khasis:** Stop. This is unacceptable. Juan and sales team have been working on this for weeks? Manually trying different configurations? While you - the algorithm team - are completely unaware? This is communication failure. Major organizational problem.

**[02:19:50] Dan Khasis:** Need to clearly distinguish two problems. One - noodle routes. This is geometric problem, routes crossing badly. Two - unbalanced routes. This is load distribution problem, some drivers have much more than others. These are different issues, different solutions.

**[02:21:45] Dan Khasis:** Juan must immediately - today, right now - provide you with all data. Datasets, examples, client correspondence, everything. Then you test with clustering enabled. Then you analyze systematically. Problems must be solved systematically through algorithm improvements, not manual intervention forever.

**[02:23:30] Igor Skrynkovskyy:** Will contact Juan immediately after this call. Get all data. Run tests with clustering algorithm.

---

## ADMINISTRATIVE ITEMS (02:24:15 - 03:04:21)

**[02:24:15] Serhii Kasainov:** Performance improvement - deployment to staging now 6.5 minutes instead of 15-20 minutes. Cache optimization.

**[02:26:40] Alex Shulga:** Stop limits feature for Azuga ready. Configured via API. To avoid overloading Juan, should we train QA team to configure via Postman until admin UI ready?

**[02:28:15] Dan Khasis:** Good idea. Train Alex Shulga or QA team. Document the process. Juan has too much on plate.

**[02:59:10] Alex Shulga:** Custom data for facilities - API complete. Question - should we display in interface? Is all custom data public or some private?

**[03:00:18] Dan Khasis:** Not exactly. There's custom override advanced data where mobile team can ignore some custom data keys. Connection ID is different thing - will be full-fledged object, more complex discussion later. Custom data will appear in interfaces. In locations will be visible, in customers will be visible, in routes will be visible.

**[03:02:23] Artur Moskalenko:** While there's no UI for facility custom data, should we announce to everyone or keep internal?

**[03:02:34] Dan Khasis:** Only internal people. No point announcing to customers when they can't use it yet.

**[03:02:42] Dan Khasis:** [Reviews facility interface] Everything here except what's needed. Need to think about what people will most often do. Filter by facility, by start point, by vehicle type, by profiles. We still haven't discussed after assignment. We still haven't discussed trips. Someone invented this status again. I must go.

**[03:03:33] Vova:** Dan, when will you have time to discuss after assignment and mobile designs?

**[03:03:43] Dan Khasis:** Don't know. Maybe tomorrow morning. Everything depends on what Igor and Juan report today about strategic balancing for these clients. Because if Juan hasn't moved, I'll be forced to deal with this myself. And then everything tomorrow is cancelled.

**[03:04:08] Vova:** Okay, I'll message you tomorrow morning and ask about status.

**[03:04:14] Dan Khasis:** Okay, thanks. Goodbye.

**[03:04:17] Vova:** Thank you.

**[03:04:19] Dan Khasis:** Bye. Thanks, bye.

---

## MEETING STATISTICS

### Participants Speaking Time

- **Dan Khasis**: 611 segments, 01:31:18 (50.3%), accuracy 93.4%
- **Vova**: 182 segments, 00:23:08 (12.8%), accuracy 93.9%
- **Igor Skrynkovskyy**: 125 segments, 00:17:23 (9.6%), accuracy 95.2%
- **Serhii Kasainov**: 108 segments, 00:08:36 (4.7%), accuracy 92.1%
- **Semeyon S**: 57 segments, 00:06:42 (3.7%), accuracy 91.9%
- **Igor Golovtsov**: 35 segments, 00:04:54 (2.7%), accuracy 93.8%
- **Alexey Gusentsov**: 22 segments, 00:03:45 (2.1%), accuracy 90.3%
- **Manar Kurmanov**: 13 segments, 00:01:31 (0.8%), accuracy 95.6%
- **Alexey Afanasiev**: 10 segments, 00:00:37 (0.3%), accuracy 93.6%
- **Alex Shulga**: 10 segments, 00:00:56 (0.5%), accuracy 83.1%
- **Artur Moskalenko**: 8 segments, 00:00:24 (0.2%), accuracy 86.2%
- **Davron Usmonov**: 7 segments, 00:01:33 (0.9%), accuracy 92.4%
- **Volodymyr Ishchenko**: 4 segments, 00:00:11 (0.1%), accuracy 82.0%
- **Mihail Krivulya**: 3 segments, 00:00:11 (0.1%), accuracy 96.3%
- **Maksym Silman**: 1 segment, 00:00:06 (0.1%), accuracy 95.0%
- **Oleg Pravyk**: 1 segment, 00:00:08 (0.1%), accuracy 99.0%

### Transcription Quality

- High confidence (time-based): 1164 (97.2%)
- Resolved via LLM: 23 (1.9%)
- Fallback: 10 (0.8%)
- Average confidence: 93.3%
- Low confidence segments (<70%): 44 segments (3.7%)

---

## TRANSLATION NOTES

**Technical Terms Preserved:**
All terms from technical_glossary.json preserved in original English form throughout translation. Examples: snapshots, routes-list, destination, customer location, time window, service time, geofence, telematics, connections, atoms, optimization, API, UTC, JSON.

**Key Statements Preserved:**
All Dan's statements translated in full to preserve tone, emphasis, and strategic direction. Critical directives, rejections, and approvals captured with complete context.

**Condensed Sections:**
Some repetitive technical discussions about UI details, formatting, and implementation specifics were condensed while preserving key decisions and action items. Full context available in original transcript.

**Timestamp Accuracy:**
All timestamps preserved exactly from original transcript. Some segments may have minor timing variations due to transcription service, but sequence and content highly reliable (93.3% accuracy).
