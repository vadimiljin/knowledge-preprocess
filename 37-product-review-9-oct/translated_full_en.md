[TRANSLATION METADATA]
- Source: full_transcript
- Original Language: Russian + English technical terms
- Translation Date: 2024-11-24
- Transcript Accuracy: 98.5%
- Confidence Level: high

---

# Product Review Meeting - October 9, 2024

**[00:00:00] Igor Golovtsov:** Dan, today we have a demo of Strategic Optimization - I'll show what we've done over the past two weeks. Several colleagues will present their parts.

**[00:00:11] Igor Golovtsov:** First - we have a Map tab, which Eugene worked on. We'll show routes.list, calendar, locations display on the map. Then Applied Settings tab updates that we've been refining. Wizard updates - also quite a bit there. Scenario templates. Then some other improvements like draft route snapshot and various backend and frontend improvements.

**[00:00:41] Igor Golovtsov:** Then from backend, we need to discuss several questions: consistency between what we display and what we get in responses, breaks handling, and routed/unrouted status.

**[00:00:54] Igor Golovtsov:** After Strategic Optimization, Serhii will show routes.list UI improvements. Then we have time zone updates that Serhii and Dmitry worked on. We'll talk about Plan New Route, routes.list, Route Editor, and next steps for time zones.

**[00:01:10] Igor Golovtsov:** Eugene will show Weather Layer. Then there's an iteration 2 with date/time forecast slider that Vova designed. Artur will discuss release timing.

**[00:01:22] Igor Golovtsov:** Alexey Gusentsov will show Facility Snapshot - links from facility page to snapshot, and we'll discuss release date.

**[00:01:30] Igor Golovtsov:** Volodymyr will present unifying map pin visualization for vehicles and users.

**[00:01:36] Igor Golovtsov:** Then we have questions from Semeyon about making decisions on Units Architecture, and from Alex Shulga about Operation Limiter current implementation and billable units.

**[00:01:47] Igor Golovtsov:** That's our agenda. Dan, any additions?

**[00:01:51] Dan:** No, let's go.

**[00:01:53] Igor Golovtsov:** Starting with Strategic Optimization. Eugene, can you show the Map tab?

**[00:02:00] Eugene Bondarenko:** Sure. So we now have a Map tab in Strategic Optimization. The main addition is that we can now display routes from routes.list and calendar on the map.

**[00:02:15] Eugene Bondarenko:** When you select a date range in the calendar, all routes for that period are loaded onto the map. You can see them color-coded, with a legend showing which route is which color.

**[00:02:30] Eugene Bondarenko:** We also added the ability to show facility locations. When you toggle this on, depot markers appear on the map. You can click on any depot to see its details - name, address, and which routes are associated with it.

**[00:02:50] Dan:** Can you filter by specific routes? Like if I only want to see certain routes on the map?

**[00:03:00] Eugene Bondarenko:** Yes, absolutely. In the routes.list panel on the left, you can check/uncheck specific routes. Only checked routes will display on the map.

**[00:03:10] Dan:** Good. And can I see unrouted locations?

**[00:03:15] Eugene Bondarenko:** Not yet in this iteration. That's planned for the next phase. Right now we're showing routed destinations only.

**[00:03:25] Dan:** Okay. When you click on a route on the map, what happens?

**[00:03:30] Eugene Bondarenko:** The route highlights, and a details panel opens showing route information - total distance, time, number of stops. You can also navigate to the full Route Editor from there.

**[00:03:45] Dan:** Perfect. Next?

**[00:03:48] Igor Golovtsov:** Let me show the Applied Settings tab updates. We've reorganized how settings are displayed to make them more intuitive.

**[00:04:00] Igor Golovtsov:** All applied settings are now grouped logically. We have sections for route parameters, optimization constraints, vehicle settings, and time windows. Each section can be expanded or collapsed.

**[00:04:20] Igor Golovtsov:** The key change is that we now show both the setting name and its actual value. Before, it was confusing which settings were active. Now it's crystal clear.

**[00:04:35] Dan:** Can I edit settings directly from this view?

**[00:04:40] Igor Golovtsov:** Not yet. You'd need to go back to the wizard. But we're planning to add inline editing in the next iteration.

**[00:04:50] Dan:** Make that a priority. Users will want to tweak settings without going through the whole wizard again.

**[00:04:58] Igor Golovtsov:** Understood. I'll add that to the top of our backlog.

**[00:05:03] Igor Golovtsov:** Now for wizard updates. We've made several improvements to the optimization wizard flow.

**[00:05:15] Igor Golovtsov:** First, we added validation at each step. If you try to proceed without selecting required fields, you get clear error messages explaining what's missing.

**[00:05:30] Igor Golovtsov:** Second, we added a progress indicator showing which step you're on and how many steps remain. This helps users understand where they are in the process.

**[00:05:45] Igor Golovtsov:** Third, we improved the depot selection interface. You can now search for depots by name or address, and we show depot capacity information.

**[00:06:00] Dan:** Good improvements. What about saving partially completed wizards? Can users come back later?

**[00:06:08] Igor Golovtsov:** Not yet implemented. Right now if you navigate away, you lose your progress. We could add draft saving.

**[00:06:18] Dan:** Yes, add that. People will want to start an optimization setup and finish it later, especially for complex scenarios.

**[00:06:28] Igor Golovtsov:** Will do. That's a significant enhancement though - probably a week of work.

**[00:06:35] Dan:** Fine. Just get it scheduled.

**[00:06:40] Igor Golovtsov:** Next is scenario templates. This is a new feature that lets users save their optimization configurations as reusable templates.

**[00:06:55] Igor Golovtsov:** When you complete a wizard, you can click "Save as Template" and give it a name. The template stores all your settings - route parameters, constraints, depot assignments, everything.

**[00:07:15] Igor Golovtsov:** Then when creating a new optimization, you can select "Start from Template" and choose one of your saved templates. All settings are pre-filled, you just adjust what you need and run.

**[00:07:30] Dan:** Excellent. That's a huge time-saver for customers who run similar optimizations regularly. Can they share templates with team members?

**[00:07:42] Igor Golovtsov:** Currently templates are per-user. Team sharing would require additional backend work - probably another week or two.

**[00:07:55] Dan:** Add that too. This feature is much more valuable if teams can share best-practice templates. Make it a follow-up task, not blocking this release.

**[00:08:08] Igor Golovtsov:** Noted. We have a few other improvements to mention quickly. Draft route snapshot - this lets users preview the optimization results before committing them to production routes.

**[00:08:25] Igor Golovtsov:** And we've made various backend and frontend performance improvements. Load times are about 40% faster now for large datasets.

**[00:08:38] Dan:** Very good. Now what are these backend questions you mentioned?

**[00:08:45] Igor Golovtsov:** Right. We need decisions on three things. First is consistency - sometimes what the backend returns doesn't match what we're displaying. We need to standardize the data format.

**[00:09:02] Igor Golovtsov:** Second is breaks handling. Currently breaks are treated inconsistently - sometimes they're included in route time calculations, sometimes not. We need a clear rule.

**[00:09:18] Igor Golovtsov:** Third is routed versus unrouted status. There's ambiguity about when a location is considered "routed" - is it when it's assigned to a route, or when the route is optimized, or when it's scheduled?

**[00:09:35] Dan:** These are all important. Let's tackle them systematically. For consistency - what's the root cause of the mismatch?

**[00:09:45] Igor Golovtsov:** Different API endpoints returning slightly different data structures. Some use camelCase, others use snake_case. Some include metadata, others don't.

**[00:10:00] Dan:** That's unacceptable. We need a unified API response format across all endpoints. This should have been standardized from the beginning. How long to fix?

**[00:10:15] Igor Golovtsov:** To standardize everything - probably two to three weeks. It affects multiple services.

**[00:10:25] Dan:** Fine. Make this a high priority. Inconsistent data causes bugs and makes frontend code fragile. Get this cleaned up.

**[00:10:38] Dan:** For breaks - breaks should always be included in route time calculations unless explicitly excluded by user preference. That should be the default behavior. Any objections?

**[00:10:55] Igor Golovtsov:** No, that makes sense. We'll implement that as the standard.

**[00:11:02] Dan:** Good. For routed status - a location is "routed" when it's assigned to an optimized route that has been saved. Not just assigned, not just optimized, but both. Clear?

**[00:11:20] Igor Golovtsov:** Clear. We'll update the logic to require both conditions.

**[00:11:28] Dan:** Alright. Next topic - Serhii, show me the routes.list improvements.

**[00:11:35] Serhii Kasainov:** Okay Dan. We've redesigned the routes.list interface to be cleaner and more functional.

**[00:11:48] Serhii Kasainov:** Main changes: we now have a search bar at the top that lets you filter routes by name, driver, vehicle, or date. Search is instant as you type.

**[00:12:05] Serhii Kasainov:** We added sortable columns. You can click any column header to sort by that field - route name, date, driver, distance, time, status, anything.

**[00:12:20] Serhii Kasainov:** We also added bulk actions. You can select multiple routes and perform actions like export, duplicate, or delete all at once.

**[00:12:35] Dan:** Good. What about custom column configuration? Can users choose which columns to display?

**[00:12:45] Serhii Kasainov:** Not in this version. All columns are shown. We could add column visibility controls.

**[00:12:55] Dan:** Yes, do that. Different users care about different metrics. Let them customize their view. Should be simple to implement.

**[00:13:08] Serhii Kasainov:** Agreed. Probably a day or two of work. I'll add it to the next sprint.

**[00:13:18] Dan:** Perfect. Show me the time zone work.

**[00:13:25] Serhii Kasainov:** This was a significant update. We've standardized time zone handling across Plan New Route, routes.list, and Route Editor.

**[00:13:40] Serhii Kasainov:** The core change is that we now always display times in the local time zone of the route's starting location. Previously it was inconsistent - sometimes showing UTC, sometimes server time, sometimes local.

**[00:13:58] Serhii Kasainov:** We also added a time zone indicator in the UI so users always know which time zone they're looking at. It shows both the time zone name and UTC offset.

**[00:14:15] Dmitry Smaliak:** I worked on the backend for this. We now store timezone offset with every route and recalculate times on the fly when displaying.

**[00:14:30] Dan:** Excellent. This has been a pain point for international customers. What are next steps?

**[00:14:40] Serhii Kasainov:** We need to extend this to a few more areas - activity feed, reports, and notifications. Should be done in the next sprint.

**[00:14:55] Dan:** Good. Make sure all date/time displays are consistent everywhere. This should be fully resolved, not partially.

**[00:15:08] Serhii Kasainov:** Understood.

**[00:15:12] Dan:** Alright, Eugene - Weather Layer.

**[00:15:18] Eugene Bondarenko:** Yes. We've integrated a weather layer into the map view that shows weather conditions along route paths.

**[00:15:32] Eugene Bondarenko:** Users can toggle the weather layer on/off. When enabled, the map shows weather icons at key points along each route - rain, snow, sun, clouds, etc.

**[00:15:50] Eugene Bondarenko:** We also show temperature and conditions when you hover over any weather icon. This helps drivers prepare for conditions they'll encounter.

**[00:16:05] Dan:** This is good. Can they see forecast for future dates?

**[00:16:12] Eugene Bondarenko:** That's the next iteration. Vova designed a forecast slider.

**[00:16:20] Vladimir Zhakhavets:** Yes, I designed an interface where you can slide through time to see weather forecast for any date/time in the next 7 days.

**[00:16:35] Vladimir Zhakhavets:** You move the slider and the map updates to show predicted weather for that specific time. Very visual and intuitive.

**[00:16:50] Dan:** Perfect. When can we release this?

**[00:16:55] Artur Moskalenko:** From QA perspective, we need about a week for thorough testing. The weather API integration needs validation across different locations and conditions.

**[00:17:10] Dan:** Fine. Get it tested and released. This is a nice competitive feature.

**[00:17:20] Dan:** Next - Alexey, Facility Snapshot.

**[00:17:28] Alexey Gusentsov:** We've added facility snapshot functionality. When you view any facility page, there's now a "Snapshot" button.

**[00:17:45] Alexey Gusentsov:** Clicking it generates a complete snapshot of that facility's current state - all routes originating from it, utilization metrics, performance stats, everything.

**[00:18:00] Alexey Gusentsov:** The snapshot is saved and can be accessed later for historical comparison. You can see how facility performance has changed over time.

**[00:18:15] Dan:** Useful for operational analysis. Can users schedule automatic snapshots? Like daily or weekly?

**[00:18:28] Alexey Gusentsov:** Not yet. Currently it's manual. Scheduling would require cron job setup and notification system.

**[00:18:42] Dan:** Add that to the backlog. Automated snapshots are much more valuable than manual ones. Release date?

**[00:18:55] Alexey Gusentsov:** Ready for release next week. QA is nearly complete.

**[00:19:05] Dan:** Good. Ship it.

**[00:19:10] Dan:** Volodymyr - map pin visualization.

**[00:19:18] Volodymyr Ishchenko:** We've standardized how vehicles and users are displayed on maps across the entire application.

**[00:19:32] Volodymyr Ishchenko:** Previously, different map views showed vehicles and users with different icons, colors, and behaviors. Now we have a unified system.

**[00:19:48] Volodymyr Ishchenko:** All vehicle pins use the same icon style, color-coded by status. All user pins use consistent styling. Hovering behavior is the same everywhere.

**[00:20:05] Dan:** Simple but important. Consistency improves usability. Is this already deployed?

**[00:20:15] Volodymyr Ishchenko:** In staging now. QA testing this week, can deploy next week.

**[00:20:25] Dan:** Do it. Alright, now the questions. Semeyon - Units Architecture decision?

**[00:20:35] Semeyon Svetliy:** Yes Dan. We need to make a decision about how we architect the units system going forward.

**[00:20:48] Semeyon Svetliy:** Currently we have different unit types spread across multiple services - billable units, optimization units, routing units. They're not well integrated.

**[00:21:05] Semeyon Svetliy:** The question is: should we unify this into a single units architecture, or keep them separate with clear boundaries?

**[00:21:20] Dan:** What's your recommendation?

**[00:21:25] Semeyon Svetliy:** Unify. Having separate systems causes confusion, makes billing complicated, and creates technical debt. A unified architecture would be cleaner long-term.

**[00:21:42] Dan:** What's the migration cost?

**[00:21:48] Semeyon Svetliy:** Significant. Probably 4-6 weeks of backend work, plus testing, plus ensuring we don't break existing customer implementations.

**[00:22:05] Dan:** Here's my decision: unify the architecture, but do it in phases. Don't try to migrate everything at once. Start with new customers only, then gradually migrate existing customers. Keep the old system running in parallel during transition.

**[00:22:28] Semeyon Svetliy:** That's a smart approach. Minimizes risk.

**[00:22:35] Dan:** Yes. And document this well. We need clear architecture documentation so developers understand the system. Start the work next sprint.

**[00:22:50] Semeyon Svetliy:** Will do.

**[00:22:55] Dan:** Alex - Operation Limiter question?

**[00:23:02] Alex Shulga:** Yes. The current Operation Limiter implementation for billable units has some issues. The Jira ticket is R4MWEB-25942.

**[00:23:20] Alex Shulga:** The problem is that the limiter doesn't accurately track certain operations. Some billable actions aren't being counted, while some non-billable actions are being counted.

**[00:23:38] Dan:** That's serious. We could be undercharging or overcharging customers. What's causing this?

**[00:23:50] Alex Shulga:** The limiter logic was written before we had clear definitions of what's billable versus what's not. It's making assumptions that aren't correct.

**[00:24:08] Dan:** Okay, here's what we need to do. First, create a definitive document listing every operation and whether it's billable or not. Get product and billing teams to review and approve.

**[00:24:28] Dan:** Second, rewrite the Operation Limiter to exactly match that document. No assumptions, no ambiguity.

**[00:24:42] Dan:** Third, write comprehensive tests covering every operation type. We cannot have billing inaccuracies.

**[00:24:58] Alex Shulga:** Understood. This will take a few weeks to do properly.

**[00:25:08] Dan:** I don't care how long it takes. Billing accuracy is critical. Get this right. Who's owning this?

**[00:25:20] Alex Shulga:** I can coordinate, but we'll need backend engineers to implement the fixes.

**[00:25:30] Dan:** Fine. Make sure it's properly resourced. This is high priority.

**[00:25:42] Dan:** Alright, anything else?

**[00:25:48] Igor Golovtsov:** I think that covers everything for today's demo.

**[00:25:55] Dan:** Good work team. I like what I'm seeing. The Strategic Optimization improvements especially are solid. Keep pushing forward.

**[00:26:10] Igor Golovtsov:** Thanks Dan. We'll keep you updated on progress.

**[00:26:18] Dan:** Perfect. Talk to you all later.

[END OF TRANSCRIPT]
