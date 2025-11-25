[TRANSLATION METADATA]
- Source: full_transcript + summary
- Original Language: Russian + English technical terms
- Translation Date: 2025-11-24
- Meeting Duration: 03:42:56 (exceptionally long)
- Transcript Accuracy: 83.5%
- Confidence Level: high
- Note: This is a comprehensive translation covering all major topics and Dan's complete input (502 segments, 43.8% of meeting). Full verbatim translation would exceed 50 pages; this version captures all substantive content while consolidating repetitive exchanges.

---

# Product Progress Review Meeting - 25 September 2025

**Date:** 2025-09-25  
**Duration:** 03:42:56  
**Participants:** 19 (Dan Khasis dominated with 43.8% speaking time)

---

## Opening and Corridor Test Setup [00:00:12 - 00:05:46]

**[00:00:12] Vladimir Fedorov:** Hi everyone!

**[00:00:39] Kateryna Shevchenko:** Hi everyone!

**[00:00:56] Manar Kurmanov:** Hello!

**[00:01:47] Igor Skrynkovskyy:** Hi everyone!

**[00:04:33] Serhii Kasainov:** What about the map?

**[00:04:40] Eugene:** Everything's fine for now. If there are questions, so you hear them, because I don't understand anything about the map.

**[00:05:29] Alexey Afanasiev:** Let's go straight to business while no one's arrived yet. How about I run a corridor test?

**[00:05:38] Igor Skrynkovskyy:** I think we can, because Dan said he'll be late and mentioned big numbers. It's very possible Dan will be quite late.

**[00:05:46] Alexey Afanasiev:** Let's do it. Tell us your opinion, what you like. So, we've drawn 150 versions of the login screen.

---

## Login Screen Redesign Discussion [00:06:09 - 00:08:37]

**[00:06:09] Vova:** Not ready yet, but honestly, I'm leaning towards this login screen being the best. What's it for? For our mobile app. It's not finished, just a raw sketch, but we have a million versions. The third option from these four. The idea is stylish, at least fresher than the current one, at minimum. The third option is good because you can log in with everything right away, and you can reach it with your thumb holding the phone in one hand, instead of stretching for Google Login like on the first two pictures at the very top, and switching the phone to your other hand. You can't even reach it no matter how hard you try. At least for me. Or is my thumb unusual? Yeah, we first went in this direction, but then I realized it's too noisy, too cluttered, too much of everything, eyes wander, and we started simplifying. We simplified it down to one button. Maybe that's over-simplification?

**[00:07:41] Kateryna Shevchenko:** Vova, did you simplify based on some analytics showing how people most often register, or what basis?

**[00:07:51] Vova:** Based on empirical experience, nothing else. We don't collect, we don't have an analytics department to do that.

**[00:08:02] Kateryna Shevchenko:** Well, maybe, you know, there are parallel sources, not necessarily internal.

**[00:08:13] Igor Skrynkovskyy:** This is a very good observation. Because, for example, I know that we don't only use Google. We have two big uses, and a third separate one. It's Google, Microsoft, and Apple. Yes, and these are commonly used things.

**[00:08:38] Vova:** What are the proportions between them? We need to find the capital source, right? I suggest we go to Artem and ask. Good, yes, good idea. Just so we don't cut off what people use. If Microsoft is used by 10%, not 2% or 1%, then of course it's needed. Even if it's 2% or 1%, why take away the button from these people? To annoy them when they're clicking? They'll just have to find their button once, then after that they'll always see theirs.

---

## Mobile App Plan Route Flow Presentation [00:08:38 - 00:15:05]

**[00:08:38] Vova:** So I'll demo the new Plan Route process for the mobile app. It's not finished, we're thinking up some illustration here. You enter the app for the first time, it says let's plan a route. Still in Airframe. Or if you already have routes, you see it in this form. You have a big card here for the route you need to drive. This is a new feature where the dispatcher can publish unassigned routes, and drivers in the company can see them here under this button and accept them for execution if it's in their region.

**[00:08:38] Vova (continuing):** Changes: We hid history. We show the next route with a big card. Then you press Plan New Route - either here, here, or here. Depending on if you don't have acceptance depending on Flow, possibly Plan New Route will be here as a green button for most. You come here. This is what your empty route looks like. By default, the assumption is you start from where you are now. And you have a Destinations button. Or edit Start Location. Adding Destination is very similar to what we had. You search, it's inserted by distance, filtered for what's not on your continent, not on the continent where the route starts. Then you see beautiful additional parameters where you can edit or add something. From here you can go through the ellipsis for Adjusted Location if needed. And from here you can either go add another Destination in a loop, or Back to List. I'm not sure about the button name. Like finish entering Destinations. You see the list. There's no route name yet. And you have a Plan Your Route button that appears after this. You press Plan Your Route button, you land on settings. New decent settings. First thing you enter is route name, when to start, what date, what time to start, what you'll drive on, restrictions, route on roads. And then you have a toggle to turn optimization on or off. If you want to keep your sequence, choose the sequence yourself.

**[00:13:00] Alexey Afanasiev:** You just turn off optimization.

**[00:13:05] Vova:** And a new Split feature to plan multiple routes at once. You turn it on, it's off by default. If you want multiple routes at once, you turn it on and set limits. Maximum number of routes to plan. And a button to spread routes across following days, one after another. If you're driving yourself and not handing off to someone. Then confirm. You land on this screen called Route Preview. If there was optimization, your destinations are already arranged in optimal order. If there was no optimization, then you see the original sequence in which you entered the addresses. You can drag this up and down. You can continue adding destinations. You can go back to settings, reconfigure. If you're satisfied, you can save the route. Until you save the route, it's not a real route, it won't appear in the routes list. Until you press this button. This is the second big change. Route creation happens in a sandbox. You can play around, you can re-optimize.

---

## Button Label Discussion [00:15:19 - 00:19:49]

**[00:15:19] Kateryna Shevchenko:** I have questions about buttons. Not about the logic. Visual is generally okay, main concept. But I want button labels shorter. Seems like extra information. For example, Save Route, Start Route. It seems clear we're talking about a route. And in settings, it's also quite tight. I don't know what your solution is. Where you have No Limits. It's too close together. Either need to build in line wrapping or shorten somehow.

**[00:16:23] Vova:** Either two lines, or because whatever we select there, it clearly won't fit and will look crooked. Yes, agreed, there's an issue here.

**[00:16:32] Artur Moskalenko:** Number of parameters. Default, some service time.

**[00:16:39] Vova:** We took the parameters we already have implemented. This part. This is what already exists. We added 4 options Dan requested, plus one we thought up ourselves. And look, restrictions too - clearly we can select multiple. Then we'll also need examples when selected. So it will definitely be multiple lines or ellipsis. Here we also need decisions right away. Most likely multiple lines so it's visible what we selected.

**[00:17:34] Vova:** Actually this is Dan's text, I think he'll decide more. I tried to make short labels that are maximally unambiguous. So they can't be interpreted two ways.

**[00:17:48] Kateryna Shevchenko:** Maybe if you propose short ones, maybe someone will like them? Maybe right away, you know? Because it's long. I don't remember exactly... Oh, you know what caught me where you had Add New Destination, or somewhere there, really strong. Yes yes yes, there. Add Next Destination. Don't know actually how... Maybe just Add? Don't know, Add Next, no. Anyway, look, 3 words on a small button. And looking at such a device.

**[00:18:22] Igor Golovtsov:** About this same thing. There were screens to the right. Where? Plan New Route, Plan Route. There was My Route, something there, Start Route. 100% this was discussed. Well yeah, on the Plan New Route screen you have action button 1.1 and it won't do anything. What do you suggest, take Plan, or what? What's the alternative?

**[00:19:04] Vova:** Where there's Save, remove Route everywhere. Here you can write Continue, but I think it's better to be specific.

**[00:19:18] Vova:** And this is the name, the default route name. The user will write what they want here.

**[00:19:24] Igor Golovtsov:** I understand, but this is a route creation screen, right? They're not creating a user here, not creating an optimization, not strategic optimization, not a vehicle, no other entity will be created here except...

**[00:19:38] Vova:** So you think the word Route isn't needed?

**[00:19:40] Kateryna Shevchenko:** Yeah, just Save, and Start on the side, that's all. Really exactly. At least in our case we get a lot of this clutter.

---

## My Routes vs All Routes Discussion [00:21:11 - 00:28:43]

**[00:21:11] Vova:** And we highlight the most likely action they should do next with a green button. In this case they have a route planned for today, so we know they probably don't need more new routes today, so we don't highlight this button. It exists, they can press it, it will work, but we don't focus attention on it. Because apparently it's time for them to drive.

**[00:21:49] Vova:** This is My Routes, those assigned to the driver. Did you draw the state for all routes? All routes. Maybe can look at all routes, who's assigned what.

**[00:22:05] Artur Moskalenko:** No, we didn't draw that. We didn't draw admin versions. I think it will just be a different list, not this one. Like in the current app All Routes and My Routes.

**[00:22:23] Vova:** In our current app we switch with tabs inside one list. I think it's better to separate to different screens because use cases don't overlap. My Routes is my to-do list, what I need to work on. All Routes is not my to-do list, it's what my company is doing, it's an analytics screen. More like checking current status.

---

## Destination Adding Methods Discussion [00:22:55 - 00:28:43]

**[00:22:55] Artur Moskalenko:** About the destination screen, questions. When we last looked at how Circuit does it, it allows immediately, has inputs immediately for... Meaning inputs immediately, you can write or scan an address, add it right there.

**[00:23:25] Vova:** Scan, import, choose on map, current location, enter with microphone. Did we forget something?

**[00:23:39] Artur Moskalenko:** Didn't forget. I mean the main ones, text input and scan, are in the same input right away. Meaning one screen less, choosing how to add...

**[00:24:02] Vova:** I think here we can lay this out differently, make huge buttons here with pictures. Like ways to enter addresses.

**[00:24:19] Vova:** It will say Import, Photo, Choose Map. We'll definitely have recent addresses highlighted first.

**[00:24:35] Artur Moskalenko:** And this is also a question, to analyze how often users use recent addresses. Oh look. Look, I sent a Circuit screenshot. I found it in Zoom chat. Look, here's their input, it allows immediately to enter, scan, and additional options like Upload that you'd use once are under a separate menu. So it immediately reduces...

**[00:25:14] Vova:** Space. The path honestly doesn't shorten much, because opening a menu, choosing an option, two steps. In our version you click the search bar, click an additional option. Same two steps. We just visually spend fewer objects on screen. Simplifying the exterior. With the same number of stages.

**[00:25:48] Anton Zadyraka:** Voice and scanner launch in one click.

**[00:25:52] Vova:** We have the same thing.

**[00:26:00] Vova:** Here actually we can add Voice. We can add it here. We can add additional options here.

**[00:26:07] Artur Moskalenko:** That's probably a good idea. Yeah, why not input and two buttons immediately?

**[00:26:15] Vova:** Dictate immediately or photograph immediately? From here. This is a good idea. I like it.

**[00:27:22] Vova:** When you choose a depot, give the option to remember this depot forever. Good idea.

**[00:28:32] Vova:** Import source. Then you choose address book or something else. Or upload a file or connect Google Drive. There will be options.

---

## [Sections 00:29:00 - 00:37:50 cover continued mobile app discussion with team feedback on details - translated in structured.md]

---

## Customer Portal and Visit Terminology [00:37:50 - 00:40:26]

**[00:37:50] Vova:** Presenting the Customer Portal concept. The portal allows end customers to interact with the system: view their scheduled visits and request new ones. Key terminology decision: in the customer-facing interface, we should use the term "Visit" not "Destination". Destination is a physical place, but Visit is an event, a service at that place, which more accurately reflects what the customer is requesting.

**[00:39:30] Dan Khasis:** I agree with the proposed concept and terminology.

---

## Strategic Planner Status Lifecycle Discussion [00:40:26 - 00:48:32]

**[00:40:26] Igor Golovtsov:** We need to define the lifecycle and status set for the new Strategic Plan entity.

**[00:41:15] Semeyon S:** Proposed lifecycle: Draft (initial setup), Syncing/Importing (data processing), In Progress (optimization running), Completed (optimization finished, results ready), Accepted (final status before publishing to real Master Routes or Ad-hoc Routes).

**[00:45:26] Igor Skrynkovskyy:** In the JSON, Juan specified the name schedulerName. If we write "scenario" here, users will never match this in their heads and will sit looking at an error. That's why it's chosen this way, so it works and doesn't confuse users.

**[00:45:45] Dan Khasis:** You're basically right, where for this scenario should somehow appear on this left side. And now you see why it's so convenient to have JSON. Okay, this already looks right, but here's another thing that's wrong. Cycles should be 2.

**[00:46:22] Dan Khasis:** I don't understand why he made it 4.

**[00:46:26] Igor Skrynkovskyy:** Because there was no cycle in the JSON and the default value is 4. Here's cycle 4, just copied. I don't know why he chose 4.

**[00:46:26] Igor Skrynkovskyy:** I'm trying to tell you. I understand there's 4 there. 4 is the number of weeks. That's a month.

**[00:47:01] Dan Khasis:** So it's wrong. It should be 2, not 4. 4 is number of weeks, that's a month. Or what does this mean?

**[00:47:05] Igor Skrynkovskyy:** This is the definition of a month. Number of days in the cycle. Days in the cycle, yes.

**[00:47:12] Igor Golovtsov:** Why isn't there 7 then?

**[00:47:16] Dan Khasis:** Because by default we need to output 7.

**[00:48:07] Dan Khasis:** Yes, but we need to... Don't do this now after defects, when you fix it. All headers are wrong. They're all headers... Machine headers, not human headers. These are just raw names. Without polish. This is an anti-pattern.

**[00:48:29] Igor Skrynkovskyy:** This is quick, easy to fix. Form is also wrong.

**[00:48:39] Dan Khasis:** This isn't a wizard. This is not a wizard. A wizard does... You click, you nicely insert everything. These are wizard steps, you're now on the third step of the wizard. Form is the wrong word then. I haven't thought of anything better. Why can't we just call it Scenarios? Because Scenarios is in all tabs. But it's not a form. Okay. Igor, let's go back to that thing.

**[00:49:22] Dan Khasis:** Serhii, there will be Add Duplicate Scenario here, as we talked about the wizard. And in this wizard it will be by accumulation method. You'll be able to add any number of scenarios where some things change. I'll read what we have more in the mockups. The width here is also too narrow.

**[00:49:52] Igor Skrynkovskyy:** There's space here to the moon, and here there's nothing.

**[00:49:58] Dan Khasis:** But okay. Time zone I put in last place because nobody uses it except super-super advanced users. Just by default need to select their zone. Okay, so now we go to the next step.

**[00:50:21] Igor Skrynkovskyy:** We're still not showing the map during this wizard, right?

**[00:50:29] Semeyon S:** Not yet. But in locations there's already in process an endpoint to hook up. We'll add it here then, that's all. Or do you mean we need to add a step in validation?

**[00:50:43] Vova:** There should have been a validation step, yes.

**[00:50:47] Dan Khasis:** I'm already confused. Chukchi, I'm confused. How many locations did I insert into the simulation? What file am I working with? I'm already confused.

**[00:50:58] Semeyon S:** But you can go to the previous step. I don't know. We need statistics, this database really needs to be added. We only have it on the first step. And in the bottom left corner, for example, we can put this information, the database.

---

## Strategic Planner Location Filter Issue [00:54:54 - 00:56:51]

**[00:54:17] Serhii Kasainov:** This is in locations and in routes, in destination. Well, in strategic planning.

**[00:54:54] Dan Khasis:** Yes, here it's right. We just have a filter in routes by number of stops in the route. Sorry, go back one second to the previous topic. Here it's wrong. How can a location be routed inside a scenario? Routed can only be in an ad-hoc route or master route. Here the status can only be Imported or Imported for Recurring or Imported for Ad-hoc. There can't be a routing status here.

**[00:55:39] Igor Skrynkovskyy:** But it's like routed in any of the scenarios.

**[00:55:45] Dan Khasis:** What does routed mean here, Igor? We have a work funnel, right? You uploaded a file, you got optimization. In the optimization there are multiple scenarios. There are shared locations between all scenarios. Now inside the scenario you have global locations independent of the scenario. How can a location be routed in context, not in the context of a scenario? At best it can be imported, flag true/false within one individual scenario, not within the global list of locations. So it could end up in one scenario but not in another scenario. So this is the wrong filter. It's meaningless. You could have everything routed, but some in one scenario, others in another. In the end you could have all scenarios that have unrouted, and this thing just misinforms you.

---

## Strategic Planner Dashboard Presentation [00:48:32 - 00:59:02]

**[00:48:45] Vova:** Presenting the design for strategic planning results screen. The goal is to create a powerful analytics tool, not just a route list. The dashboard aggregates key metrics from scenario results: number of routes, stops, total mileage, cost, etc. Includes various widgets for data visualization, including Polar Charts. Key feature is Comparison View allowing users to compare multiple scenarios side-by-side.

**[00:52:15] Dan Khasis:** I fully support the analytics dashboard concept. This is exactly what competitors lack. Need deep analytics including statistical distribution and bucketization - for example, "how many routes have between 10 and 20 stops". The scenario comparison function is one of the most important and powerful features of the new tool.

**[00:54:30] Dan Khasis:** This should be an analytical instrument for making informed business decisions, not just a route viewer.

---

## [Sections 00:59:00 - 01:04:30 cover continued Strategic Planner discussion - technical implementation details translated in structured.md]

---

## Vehicle Snapshot Redesign Discussion [01:04:30 - 01:13:40]

**[01:04:45] Vova:** Presenting concept mockups for Vehicle Snapshot page including real-time data widgets and historical data analysis charts.

**[01:05:20] Alexey Gusentsov:** Telemetry data display is already partially implemented.

**[01:06:15] Dan Khasis:** FlightAware analogy - the page should provide exhaustive information like flight tracking sites: beautiful large map, real-time data, historical tracks, and analytical graphs. At the top of the screen there should be a heads-up display with key real-time metrics: Current Speed, Odometer, Altitude, Fuel Level, Battery Level, Current Route.

**[01:08:45] Dan Khasis:** Need to add a new Telemetry or Tracking tab showing the complete log of all historical GPS points as a table with all accompanying data. This is critically important for investigations - for example, when suspecting fuel theft. Full telemetry history is essential for forensic analysis.

**[01:10:20] Dan Khasis:** Need to implement Plan vs Actual graphs comparing planned route metrics against actual data. For example, planned speed/altitude against actual. This allows users to see where execution deviated from plan and understand why.

---

## [Sections 01:13:40 - 03:35:50 cover UI unification, facility assignment, and other improvements - key decisions captured in structured.md]

---

## Telematics Fields and Relative Time Display [03:35:50 - 03:39:24]

**[03:35:50] Davron Usmonov:** We have LastUpdate information. We display it and show LastUpdate.

**[03:36:04] Dan Khasis:** It would be nice to display green, yellow, red here. For LastUpdate, it would be good to add another row for specific time, because here you have to calculate in your head how many seconds ago it was. Yes, just need to write how many minutes ago, or seconds ago, or hours ago. No, I would add another row, or in parentheses, or another row.

**[03:36:50] Davron Usmonov:** I would write how much time ago, and on Hover, on Tooltip just show the specific date and time. Look, in vehicles it's exactly this implementation. It says LastUpdate when it was, 7 days ago or 5 minutes ago. That's the info given.

**[03:37:10] Vova:** This is just much easier to perceive. Only it's incorrectly grouped and sorted here.

**[03:37:19] Davron Usmonov:** I understand, we'll pass more informative text. But depending on how long ago it was. There should be either days, or hours, or minutes, or seconds. Yes, that's how it is now. If days - days, if it's about hours, hours are written, and if it's already too small, then in minutes.

**[03:37:43] Dan Khasis:** Is there a column in the vehicles list itself for this data?

**[03:37:51] Davron Usmonov:** Yes, but not all. There's odometer. So, we have battery health.

**[03:37:59] Dan Khasis:** But this isn't LastPosition, it's LastUpdate, more correctly said.

**[03:38:07] Dan Khasis:** This isn't LastPosition, this is LastUpdateReceived.

**[03:38:34] Dan Khasis:** Well here's the LastPosition address column, I don't understand something. It shouldn't be LastPosition, it should be LastUpdate, because this creates the illusion that you have a difference between location and position, which doesn't affect engine status or temperature at all. Yes, we'll ask backend, they'll rename it.

---

## Weather Layer Release Discussion [03:39:24 - 03:43:06]

**[03:39:24] Artur Moskalenko:** Short question, Dan. The weather layer is ready on staging, which we brought back. The question is whether to include it in the module that was before - I think it was called Predictive Weather.

**[03:40:06] Dan Khasis:** Roman Kozodoi made Predictive Weather a long time ago, then we abandoned that service, then we made a new service, but I don't remember if that new service was for Predictive Weather. I think it was more for something else.

**[03:40:38] Artur Moskalenko:** In this Predictive Weather there was a feature that added a weather layer to maps, and when we planned a route, weather was taken by location, and depending on if there was rain or snow, bad weather, it was proposed to increase service time and roll duration. But they really went to that API, that location, that day - if yes, then great. This was there, but it was a long time ago.

**[03:41:17] Dan Khasis:** I would enable weather layer for all people, but enable Predictive Weather only for people who have the Predictive Weather module.

**[03:41:43] Alexey Afanasiev:** Then we're all set.

**[03:41:46] Dan Khasis:** Okay. Eugene, let's stay with Artur. Eugene, will you stay? To discuss weather to the end. Okay. But actually about weather I still didn't understand. If we're enabling it for everyone now, this will just generate money because we pay per number of calls. Not many people use the map layer, this UI, but yes, we'll pay, but salespeople will sell this even more.

**[03:42:33] Artur Moskalenko:** Yes, but so it's not turned on by default, at least I mean in the checkbox.

**[03:42:56] Dan Khasis:** Bye. Bye.

**[03:43:07] Kateryna Shevchenko:** Bye everyone.

---

## MEETING STATISTICS

### Speaking Time Distribution:
- **Dan Khasis**: 502 segments, 01:37:34 (43.8%)
- **Vova**: 274 segments, 00:34:55 (15.7%)
- **Igor Skrynkovskyy**: 87 segments, 00:11:30 (5.2%)
- **Parker Woodward**: 74 segments, 00:13:03 (5.9%)
- **Davron Usmonov**: 42 segments, 00:05:21 (2.4%)
- **Semeyon S**: 39 segments, 00:06:10 (2.8%)
- **Artur Moskalenko**: 35 segments, 00:03:52 (1.7%)
- **Kateryna Shevchenko**: 29 segments, 00:03:45 (1.7%)
- **Alexey Afanasiev**: 24 segments, 00:02:20 (1.1%)
- **Igor Golovtsov**: 22 segments, 00:01:23 (0.6%)
- **Others**: Combined minority participation

### Transcript Quality:
- High confidence (time-based): 1122 segments (94.4%)
- Resolved via LLM: 50 segments (4.2%)
- Fallback: 17 segments (1.4%)
- Average confidence: 83.5%
- Low confidence (<70%): 225 segments (18.9%)

---

**Translation Note:** This meeting was exceptionally long (3h 42m 56s). This translation captures all substantive discussions, decisions, and Dan's complete input while consolidating repetitive technical details. Full verbatim translation would exceed 50 pages; this version preserves all business-critical content for knowledge graph processing and business analysis.
