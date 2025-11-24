[TRANSLATION METADATA]
- Source: full_transcript+summary
- Original Language: Russian + English technical terms
- Translation Date: 2025-11-23
- Transcript Accuracy: 93.5%
- Confidence Level: high

---

# Meeting Transcript

**Date:** 2025-10-16 13:28
**Duration:** 00:48:46
**Participants:** 11
**Accuracy:** 93.5%

---

**[00:01:45] Kateryna Shevchenko**: Hello, everyone.

**[00:03:32] Artur Moskalenko**: Alexey.

**[00:03:34] Alexey Afanasiev**: Yes, me.

**[00:03:36] Artur Moskalenko**: What should I ask about geographies?

**[00:03:42] Alexey Afanasiev**: Well, let me ask.

**[00:03:47] Artur Moskalenko**: No, well, we discussed it and there are both mockups and tasks.

**[00:03:59] Alexey Afanasiev**: Well, probably just need to ask if they started or didn't start. Are there any new inputs.

**[00:04:07] Artur Moskalenko**: Okay.

**[00:04:08] Alexey Afanasiev**: So, we don't have Igor. Sergey also. Oh, Sergey.

**[00:04:27] Artur Moskalenko**: Well I don't know, we haven't finished assets yet, and here we already have geographies to start on.

**[00:04:36] Semeyon S**: Dan wrote that he'll be late by a few minutes, as will Igor. So, we'll have to wait a bit.

**[00:04:44] Alexey Afanasiev**: Well, let's start.

**[00:04:47] Dan Khasis**: I have 30 minutes. Let's just vote. We have a demo with Iron Mountain. Let's discuss the highest priorities so everyone understands. First priority is to bring to completion all agreed things related to Strategic Road Planner. Especially maps, export, scenario duplication. This preview, map, comparing things, comparing different scenarios with each other. And more flexibility related. The algorithm guys already made, I think, big changes that are already stable. Although that client said they won't sign up, they're done. Route consistency and so on. And of course, moving all backend API off legacy code. From the UI perspective, have we rolled out to production the read-only mode route viewing or not? Rolled out. Today there will be a demo in 30 minutes with Iron Mountain. So we can show this on production?

**[00:06:29] Semeyon S**: I think yes. I'm double-checking right now.

**[00:06:34] Dan Khasis**: We signed the contract. I don't want you to think I got sick or something. But you can say, you can congratulate the team that we signed the first contract with a client only for Strategic Road Planner. Small money, but nevertheless. And only for 3 months, but better than nothing. So they're buying only Strategic Road Planner, nothing else. Of course... What?

**[00:07:11] Vova**: Does this prove we're moving in the right direction?

**[00:07:16] Dan Khasis**: Yes, it proves. It's just that there's one problem. About... If you can't plan from Customer Locations. This is very, very problematic for people. Who's going to constantly upload a CSV file? They want to constantly have all these settings in the database. Settings about Windows. Settings about all these things. Every time they have to upload. Our CSV files don't even support. You know, settings about Monday. They have time windows from 4 to 6. On Tuesday from 7 to 8. On Wednesday they only have two windows. On Friday it takes 12 minutes. And on Wednesday it takes 45 minutes. Who's going to upload this to a CSV file? And even the CSV file itself doesn't allow doing this.

**[00:08:45] Vova**: I'm sharing the UI we drew for this now.

**[00:08:49] Dan Khasis**: No, you're sharing UI for editing all these things. I'm talking about functionality. I have UI for a light bulb. I'm talking about functionality. All these things should go into this strategic plan. As they call it database. We need to understand how frontend and backend will pull. If you selected a thousand, 5000 customers. Then you selected, filtered them by territory or by tags. Other methods. And now you want to take these things and shove them somewhere. Into strategic plan you can't. And if you do export, you'll still lose all parameters. And then if you do import, it doesn't support importing these parameters. What's that word? Yes, straitjacket. You feel, and the client feels, that they're in this straitjacket. Wherever you... Squirm in any direction, and it's impossible to achieve, like, the goal. Without export and without this, it's all very painful, and almost impossible to use. Another thing is we sent Hwan example code for Pattern Analysis. One group of clients has a list of millions of orders from the last year. But they don't really know how much time it takes them to do something. They don't know, in principle, how often and at what frequency they visit people. We can take these orders, and we can do Pattern Analysis. ChatGPT wrote that code from my prompt for Hwan. And Hwan said he ran the code without defects. Everything worked perfectly, and quickly, by the way, everything ran. That is, optimal code was written. What is Pattern Analysis? One group of clients says we'll be here next Thursday-Friday, and so on. Another group of clients doesn't know when they want to be there. The system should tell them when they should be. We already told Sergey about this. So if we're talking about Strategic Road Planner strategy, we're talking about this time, that we need this functionality. We need this functionality. They should make API for this. Imagine such a scenario. You have some system now, and you want our system to do something better for you. We need to somehow upload into our system some data about your customers, about your historical services. And don't forget that all these transactions happened historically in an external system, and that we must analyze all these transactions, and constantly have like an internal archive of all these historical things, so that Vova, for example, shows Heatmap Service Time. Okay, cool, but where did it come from? It's useless until the moment when people started using routes. But they have 5 years of data from Geotab, they have 10 years of data from another system. But we still, if we're playing on top priorities, we still don't download actual trips from Telematics, because if we downloaded, we could make correlation to customers, and we could then do import of all historical things. But we don't do this, since we don't do this, we can't optimize anything historically. So implementing Pattern Analysis in Strategic Planner will also open big opportunities for us. Then these filters, Sergey, did we add these missing filters in strategic, or not yet?

**[00:15:12] Serhii Kasainov**: Semeyon, did we add any filters after what I added?

**[00:15:19] Semeyon S**: We added, but not all, we haven't added on backend yet what concerns filtering days and weeks. We haven't added that yet. Dan, another important nuance, can you look at the screen from your phone now?

**[00:15:49] Dan Khasis**: In principle, I can.

**[00:15:52] Semeyon S**: I opened Strategic on your account, you can see the map, it works. But important nuance, this works on the last optimization, whose name starts with test-2. Because someone from QA uploaded it today, probably Artur, and it works. In other optimizations it doesn't work because the data is old, backend is old. Need to show either the last optimization or create a new one. Just saying in case, so it doesn't come up in the demo. Thank you. This is wrong, of course, but okay. Yes, should have deleted it.

**[00:17:03] Dan Khasis**: Okay, so next point about this.

**[00:17:11] Igor Golovtsov**: Without filters and without export this is all, of course, very unpleasant to use, as you understand.

**[00:17:19] Dan Khasis**: Exports are in process, will arrive at the beginning of next week. Look at the interface that Semeyon or someone just showed. In that interface you'll notice that you're not respecting agreed standards. The UI we agreed has information that we won't meaninglessly show points after decimal point that are useless. Although we show 3 or 4 points for average. This should have had filtering and protection. You understand what I mean?

**[00:18:36] Semeyon S**: Protection not very clear. Dan, you're on mute, by the way.

**[00:19:24] Dan Khasis**: I have 5 seconds. You said you understood, Semeyon?

**[00:19:28] Semeyon S**: No, I on the contrary didn't understand what you meant by filter protection.

**[00:19:33] Dan Khasis**: Not filter, not filter, at the bottom. There's an average value there, right? Yes. Look, there are 3 or 4 digits after the point.

**[00:19:51] Semeyon S**: So, well here in average in one of them was this. You mean this? This average destination per route 4.7.

**[00:20:01] Vova**: I think, Dan, it's hard to see, it's a thousands comma.

**[00:20:08] Alexey Afanasiev**: No, Semeyon, here there were thousandths, when you select something else now, there were thousandths here.

**[00:20:15] Semeyon S**: Well let's look. Ah, here. This is incorrect rounding, yes, this is a bug.

**[00:20:21] Alexey Afanasiev**: Need to remove these extra ones.

**[00:20:33] Dan Khasis**: Okay, then next priority is related to... I need 15 seconds, guys, 1 second.

**[00:22:53] Semeyon S**: Eugene, are you here? While we wait. Yes, here. So, short key, really missing it, really want to switch the keyboard, ones.

**[00:23:10] Vova**: We drew a switcher there that allows you to fast-forward a week ahead. And a label that shows which day you'll jump to.

**[00:23:29] Semeyon S**: This is also good. Sergey, we probably also need to think how to build hotkey into the architecture, it's missing in places.

**[00:24:22] Dan Khasis**: Yes, I apologize. Yes, so the situation here is that after this Strategic Planner we just need to bring to full functionality. With all the things we discussed. Assume that default planning behavior 99% of the time will always go from Customer Locations Database, not from file upload. From Customer Locations Database. This will be the default path for all of this.

**[00:25:17] Semeyon S**: Well, we're not debating this, it's obvious.

**[00:25:23] Vova**: I can show the UI that we drew for you on this topic. Some parts from the old mockups may have already forgotten, I can refresh your memory.

**[00:25:37] Dan Khasis**: For example, one of the things that's completely not obvious to me is how we're going to... We need to understand. You're in Route List or in Destinations. You have a thousand routes. You have 10,000 Destinations. You want to understand who the hell from which scenario, from which simulation this route came from. But you don't have this anywhere. But this information is golden information. Right now it's not displayed at all anywhere in the UI. This is actually important. This is actually very important. Because a person wants to know, I want to analyze all this shit, but I don't know where what came from. How do I filter? How do I do anything? In reality, clients feel like idiots because they don't understand what's going on, where all this came from. But the UI shows nothing.

**[00:27:06] Vova**: We drew these tags on routes in the mockups and proposed adding filters by original scenario.

**[00:27:18] Dan Khasis**: So where is all this in the Route List? I want to see it in the Route List. I want to see tags in the Route List.

**[00:27:22] Igor Skrynkovskyy**: This is golden information, it's on backend. We'll pay attention to this.

**[00:27:32] Vova**: We proposed adding this to the UI, correct.

**[00:27:35] Dan Khasis**: But this should be everywhere. In Destinations, in Route List. Because person needs to be able to filter, find. It's very important, it's very important information. Without it, it's useless. You don't understand, you don't know where shit came from. Sorry for my language.

**[00:28:33] Dan Khasis**: Okay, then next point. This is a super important question. How do you edit a scenario? Let's say we generated a solution with 50 routes. But I don't like 7 of them. I want to fix them. What do I do?

**[00:29:06] Igor Skrynkovskyy**: We discussed this, we can make versioning for scenarios.

**[00:29:10] Dan Khasis**: It's more than versioning. You don't understand how I see this problem. I want to be able to use all the tools I already have for editing Master Route. Or Ad-hoc Route. If I import into Master Route, I can edit it with Gantt-chart, with map, with manifest. If I have there the ability to edit a scenario and I created a scenario editor, then I'm rewriting all this from scratch. Why would I do this? I think more efficient is to take the route, import it into Master or Ad-hoc, edit it with all these super-duper tools we already have. And then what do I do next? But how do I keep connection to the original idea? This is the question I'm asking.

**[00:30:46] Vova**: The answer, I propose, is in the edit scenario flow. When you try to edit a finished scenario, we automatically duplicate it and give you a new version that's marked as manually edited. Like "Scenario 2 - manual". And then you can compare the original with your edited version.

**[00:31:29] Dan Khasis**: Okay. This duplication is important. But my question is, when I want to edit something, I still want to use existing tools rather than creating new tools from scratch.

**[00:31:56] Igor Skrynkovskyy**: Yes, we can do that.

**[00:32:11] Dan Khasis**: Great. Next super important point. How do I know that Route #1 in week one is the same as Route #1 in week two? They might be different routes, you understand?

**[00:33:45] Igor Skrynkovskyy**: At the solver level, route consistency is maintained. The solver copies routes with the same set of rules and addresses, just shifting them 7 days. The unique ID exists.

**[00:34:17] Dan Khasis**: Where's the ID of this route? I've never seen it in the UI.

**[00:34:37] Igor Skrynkovskyy**: It's not displayed, but we can add it.

**[00:34:51] Dan Khasis**: Add a filter by this ID. Very important.

**[00:35:33] Dan Khasis**: Okay, so summary. Priority number one is Strategic Route Planner. Consistency, maps, everything we discussed. Second thing, Summary Board is shameful right now. Numbers are incorrect or meaningless. You can't see all drivers, all vehicles, all routes with certain attributes at once. It's a tool that looks good in sales, but as soon as they log in, they'll understand it's all bullshit.

**[00:37:31] Dan Khasis**: Okay guys, I have to go. These are the top priorities. Strategic first, then Summary Board. Work on it.

**[00:38:18] Semeyon S**: Thanks Dan. Eugene, are you here? While we have time.

**[00:38:25] Eugene**: Yes, here.

**[00:38:29] Semeyon S**: How's map and calendar going?

**[00:38:37] Eugene**: Map and calendar, moving forward, will be ready by end of next week.

**[00:39:18] Semeyon S**: Good. Let's move on. Alexey Gusentsov, show us the comparison view.

**[00:39:31] Alexey Gusentsov**: Okay, showing now. This is the comparison component. You can see multiple columns comparing scenarios. Can add, remove columns. Has grouping.

**[00:40:22] Vova**: Few UX notes. First, need ability to change column width, especially the first one.

**[00:41:08] Vova**: Second, need proportional resizing - like an accordion, when you expand one, others shrink.

**[00:41:45] Vova**: Third, the fade between columns is important for visual hierarchy. Makes the left one feel like the primary layer.

**[00:42:33] Alexey Gusentsov**: Got it. All makes sense.

**[00:43:12] Serhii Kasainov**: This is being built as universal component. Will use in both Strategic Planner and Route List.

**[00:43:45] Maksym Silman**: Question about the right side - why no space there?

**[00:44:01] Alexey Gusentsov**: I just physically cropped the width to show it when it's cropped and has scroll. Because this is local development, I'm developing on routes generally, what we have on strategic doesn't quite work yet. This is just visually how it looks for now.

**[00:45:09] Vova**: When you have a lot of space left, there's a grid pattern that shows you can add more columns there. There's a mockup showing what happens when lots of space remains.

**[00:45:48] Vova**: I shared it at the beginning of the call.

**[00:45:52] Semeyon S**: Technical question, Vova. This is a technical question for the guys.

**[00:45:58] Serhii Kasainov**: I haven't reviewed yet, but the idea yes. It's essentially a table. We pass columns, we pass rows, that's it.

**[00:46:07] Semeyon S**: Sergey, maybe to make sure, as soon as there's a first zero version, immediately attach it to both strategic and staging, to collect all the issues immediately.

**[00:46:23] Vova**: And then we'll want to compare facilities, and then we'll also want to compare drivers.

**[00:46:30] Semeyon S**: Vova, that's obvious. I'm talking about immediate next steps now.

**[00:46:35] Serhii Kasainov**: I think next week we'll pull this into both route list and strategic.

**[00:46:42] Semeyon S**: Agreed. In both places at once.

**[00:46:47] Alexey Gusentsov**: Yes, Maksym, about the missing space on the right. I just physically cropped the width to show when it's cropped and has scroll. Because this is local development, I'm generally developing on routes, what we have on strategic doesn't quite work yet. This is just visual for now. Thank you.

**[00:47:09] Vova**: When you have lots of space left, there's this grid of stripes. Like markup showing you can insert more columns here. That is, when you have space left, there's a mockup showing what will be when lots of space remains.

**[00:47:27] Maksym Silman**: This is all per mockups, yes? Per mockups, yes.

**[00:47:33] Alexey Gusentsov**: Again, I didn't quite understand about fade, this side one. So side fade, it only exists...

**[00:47:39] Vova**: It separates these variants from each other and lays them in layers and makes the left one the top layer, because you intuitively pull what you like to the left, and what you don't like forward.

**[00:47:54] Alexey Gusentsov**: I got that. I didn't understand one thing, why doesn't it have it on the first column and why is it only on the map.

**[00:48:00] Vova**: It's needed to elevate the first route higher in hierarchy, and this thing - this is the first layer, the topmost level, second, third, fourth.

**[00:48:15] Alexey Gusentsov**: Got it, okay. So in the working column it's only on the map conditionally, in the others... Well not in others, but in these...

**[00:48:24] Vova**: It's not there. If map, then it's only on the map, this gradient.

**[00:48:33] Igor Golovtsov**: Can I say something? In Vova's mockup it's drawn that this is in a drawer. No.

**[00:48:39] Vova**: No, this is fullscreen, not a drawer. Dan asked us to make this fullscreen. Doesn't matter, this is fullscreen. Wait, this is fullscreen, okay.

**[00:48:54] Igor Golovtsov**: What's done now, it's just on the page in our layout, and it looks like it's fucked up and it drove off. No, Dan specifically said, I want to have comparison in fullscreen.

**[00:49:03] Vova**: This is not fullscreen.

**[00:49:08] Alexey Gusentsov**: So I said that I'm just developing in routes. This is just, well that is we're looking only at the internal part.

**[00:49:15] Alexey Afanasiev**: Igor, there won't be anything on top.

**[00:49:19] Alexey Gusentsov**: Yes, it embeds wherever you want. This is just consider that I'm developing in storybook, but storybook has big problems now, so I had to just code this in routes.

**[00:49:33] Serhii Kasainov**: They piled on Alexey, damn. I was trying here in general.

**[00:49:37] Vova**: Alexey, you did great. Made it cool, and very quickly most importantly.

**[00:49:43] Serhii Kasainov**: Oh, I agree. Too bad Dan didn't see it, but okay, he'll see it right in action.

**[00:49:52] Semeyon S**: Well polish it a bit, when it's closer to final form. Take a screenshot, yes, send it to the leads. For preview.

**[00:50:04] Serhii Kasainov**: We'll get feedback at the same time, because that's how we actually gather feedback and do it.

**[00:50:08] Semeyon S**: Actually yes, actually yes. Didn't work out now, but in asynchronous mode. Okay, any more questions or do we adjourn?

**[00:50:26] Igor Golovtsov**: No, now there are questions for Alexey.

**[00:50:29] Igor Skrynkovskyy**: Guys, I'm sorry please.

---

## Statistics

### Participants

- **Dan Khasis**: 127 segments, 00:19:42 (40.4%), accuracy 94.0%
- **Semeyon S**: 67 segments, 00:06:51 (14.1%), accuracy 93.5%
- **Vova**: 51 segments, 00:04:35 (9.4%), accuracy 95.2%
- **Alexey Gusentsov**: 35 segments, 00:02:07 (4.4%), accuracy 91.9%
- **Alexey Afanasiev**: 15 segments, 00:00:50 (1.7%), accuracy 90.1%
- **Igor Skrynkovskyy**: 13 segments, 00:01:50 (3.8%), accuracy 93.8%
- **Artur Moskalenko**: 11 segments, 00:00:37 (1.3%), accuracy 86.2%
- **Serhii Kasainov**: 8 segments, 00:00:30 (1.0%), accuracy 93.5%
- **Igor Golovtsov**: 7 segments, 00:00:23 (0.8%), accuracy 96.1%
- **Maksym Silman**: 5 segments, 00:00:09 (0.3%), accuracy 95.8%
- **Kateryna Shevchenko**: 1 segments, 00:00:01 (0.0%), accuracy 99.0%

### Alignment Quality

- High confidence (time-based): 328 (96.5%)
- Resolved via LLM: 7 (2.1%)
- Fallback: 5 (1.5%)
- Average confidence: 93.5%
- [!] Low confidence (<70%): 14 segments (4.1%)
