[TRANSLATION METADATA]
- Source: full_transcript (310 lines, 93.5% accuracy) + summary
- Original Language: Russian + English technical terms
- Translation Date: 2025-11-23
- Transcript Accuracy: 93.5%
- Confidence Level: HIGH
- Meeting Duration: 00:48:46
- Dan Speaking Time: 00:19:42 (40.4% - dominant speaker)

---

**[00:01:45] Kateryna Shevchenko**: Hello, everyone.

**[00:03:32] Artur Moskalenko**: Alexey.

**[00:03:34] Alexey Afanasiev**: Yes, me.

**[00:03:36] Artur Moskalenko**: Why am I asking about geographies?

**[00:03:42] Alexey Afanasiev**: Well, let me ask.

**[00:03:47] Artur Moskalenko**: No, well, we discussed it and there are mockups and tasks.

**[00:03:59] Alexey Afanasiev**: Well, probably just need to ask if we started or not. Are there any new inputs.

**[00:04:07] Artur Moskalenko**: Okay.

**[00:04:08] Alexey Afanasiev**: And what's the priority? So, we don't have Igor. Serhii either. Ah, Serhii.

**[00:04:27] Artur Moskalenko**: Well I don't know, we haven't finished assets yet, and here's geographies to start.

**[00:04:36] Semeyon S**: Dan wrote that he'll be a few minutes late, as will Igor. So, we'll have to wait a bit.

**[00:04:44] Alexey Afanasiev**: Well, let's start.

**[00:04:47] Dan Khasis**: I have 30 minutes. Let's just vote. We have a demo with Iron Mountain. Let's discuss the highest priorities so everyone understands. First point is to bring to completion all agreed things related to Strategic Road Planner. Especially maps, export, scenario duplication. This preview map, comparing things, comparing different scenarios with each other. And more flexibility related. The algorithm team has already made, I think, big changes that are already stable. Although that client said they won't sign, they're done. Route consistency and so on. And of course, move all backend API from hwang code. From UI perspective, did we roll out to production read-only mode for routes or not? Rolled out. Today there's a demo in 30 minutes with Iron Mountain. So can we show this on production?

**[00:06:29] Semeyon S**: I think yes. I'm checking right now.

**[00:06:34] Dan Khasis**: We signed a contract. I don't want you to think I'm sick or something. But I can say, you can congratulate the team that we signed the first contract with a client for Strategic Road Planner only. Small money, but nevertheless. And only for 3 months, but better than nothing. So they're buying only Strategic Road Planner, nothing else. Of course... What?

**[00:07:11] Vova**: This proves we're moving in the right direction?

**[00:07:16] Dan Khasis**: Yes, it proves. There's just one problem. About... If you can't plan from Customer Locations. This is very, very problematic for people. Who's going to constantly upload CSV file? They want to constantly have all these settings in the database. Settings about Windows. Settings about all these things. Every time must upload. Our CSV files don't even support. You know, settings about Monday. They have time windows from 4 to 6. On Tuesday from 7 to 8. On Wednesday they only have two windows. On Friday it takes 12 minutes. But on Wednesday it takes 45 minutes. Who's going to upload this into CSV file? And even CSV file itself doesn't allow this.

**[00:08:45] Vova**: I'm sharing now the UI we drew for this.

**[00:08:49] Dan Khasis**: No, you're sharing UI for editing all these things. I'm talking about functionality. I have UI for a lightbulb. I'm talking about functionality. All these things must go into this strategic plan. What they call database. We need to understand how frontend and backend will extract. If you selected a thousand, 5000 customers. Then you selected, filtered them by territory or by tags. Other methods. And now you want to take and shove these things somewhere. Into strategic plan you can't. And if you do export, you'll still lose all parameters. And then if you do import, it doesn't support importing these parameters. What's the word? Yes, straitjacket. You feel it, and the client feels they're in this straitjacket. Wherever you... Squirming in any direction, and impossible to achieve, like, the goal. Without export and without import, this is all very painful, and almost impossible to use. Another thing, we sent Hwang exemplary code for Pattern Analysis. One client group has a list of millions of orders from last year. But they don't really know how long it takes them to do something. They don't know, in principle, how often and with what frequency they visit people. We can take these orders, and we can do Pattern Analysis. Chat GPT wrote that code from my prompt to Hwang. And Hwang said he ran the code without defects. Everything worked perfectly, and quickly by the way, everything ran. That is, optimal code was written. What's Pattern Analysis? One client group says we'll be here next Thursday-Friday, and so on. Another client group doesn't know when they want to be there. The system should tell them when they should be. We already told this to Serhii. So if we're talking about Strategic Road Planner strategy, we're talking about this time, that we need this functionality. Need this functionality. They need to make API for this. Imagine this scenario. You have some system now, and you want our system to do better for you. We need to somehow load into our system some data about your customers, about your historical services. And don't forget that all these transactions happened historically in external system, and that we need to analyze all these transactions, and constantly have like an internal archive of all these historical things, so that Vova, for example, showed Heatmap Service Time. Okay, great, but where did it come from? It's useless until people started using Route4Me. But they have 5 years of data from Geotab, they have 10 years of data from another system. But we still, if we're playing on top priorities, we still don't download actual trips from Telematics, because if we downloaded, we could correlate to customer, and we could then import all historical things. But we don't do this, since we don't do this, we can't optimize anything historically. So integrating Pattern Analysis into Strategic Planner will also open big opportunities for us. Then we have these filters, Serhii, did we add these missing filters in strategic, or not yet?

**[00:15:12] Serhii Kasainov**: Semeyon, did we add any filters after what I added?

**[00:15:19] Semeyon S**: We added, but not all, haven't added yet on backend what concerns filtering days and weeks. Haven't added that yet. Dan, important nuance, can you look at the screen from phone now?

**[00:15:49] Dan Khasis**: In principle, I can.

**[00:15:52] Semeyon S**: I opened Strategic on your account, you can see the map, it works. But important nuance, this works on the last optimization, name starting with test-2. Because someone from QA uploaded it today, probably Artur, and it works. In other optimizations it doesn't work, because data's old, backend's old. Need to show either last optimization or create new one. Just saying just in case, so it doesn't come up in demo. Thank you. This is of course wrong, but good. Yes, should have deleted.

**[00:17:03] Dan Khasis**: Okay, so next point about this.

**[00:17:11] Igor Golovtsov**: Without filters and without export this is all, of course, very unpleasant to use, as you understand.

**[00:17:19] Dan Khasis**: Exports are in process, will come in beginning of next week. Look at the interface someone just showed, Semeyon or someone. In that interface you'll notice you're not respecting agreed standards. UI that we agreed has information that we won't meaninglessly show points after decimal point that are useless. Although we show 3 or 4 points for average. This should have filtering and protection. You understand what I mean?

**[00:18:36] Semeyon S**: Protection not very clear. Dan, you're on mute, just so you know.

**[00:19:24] Dan Khasis**: I have 5 seconds. You said you understood, Semeyon?

**[00:19:28] Semeyon S**: No, I didn't understand what you meant by filter protection.

**[00:19:33] Dan Khasis**: Not filter, not filter, at the bottom. There's average value there, right? Yes. Look, there are 3 or 4 digits after the point.

**[00:19:51] Semeyon S**: So, well here in average in one of them was this. You mean this? This average destination per route 4,7.

**[00:20:01] Vova**: I think, Dan, hard to see, this is comma thousands.

**[00:20:08] Alexey Afanasiev**: No, Semeyon, here were thousandths, when you select something else now, there were thousandths here.

**[00:20:15] Semeyon S**: Well let's see. Ah, here. This is wrong rounding, yes, this is a bug.

**[00:20:21] Alexey Afanasiev**: Need to remove these extras.

**[00:20:33] Dan Khasis**: Okay, then next priority is related to... I need 15 seconds, guys, 1 second.

**[00:22:53] Semeyon S**: Eugene, are you here? While we wait. Yes, here. Here, short key, really missing it strongly, want to switch keyboard, ones.

**[00:23:10] Vova**: We drew a switcher there that lets you jump forward a week. And label that shows which day you'll jump to.

**[00:23:29] Semeyon S**: This is also good. Serhii, probably we also need to think how to build hotkey into architecture, missing in places.

**[00:24:22] Dan Khasis**: Yes, I apologize. Yes, so here the situation is that after this Strategic Planner we need to just bring to minimal functionality. With all the things we discussed. Assume that default planning behavior 99% of time will always go from Customer Locations Database, not from file upload. From Customer Locations Database. This will be the default path for all this.

**[00:25:17] Semeyon S**: Yes, we have a task in the list, so from Locations you can create bulk, and from strategic. Same table was built in, so you can filter, select and run scenario on it. As soon as new engine is ready, we'll take this on.

**[00:25:54] Dan Khasis**: Yes, then another thing. You know, for example, someone did Strategic Route Planning, someone had some scenario number 3. Scenario number 3 then turned into something else, into Import, into Master Route, then Master Route became regular route. Right? This is our order. Now, what happened, you opened route, and you have no fucking clue which scenario it came from, which simulation, which Master Route. In all places in Routes.list and in Destinations we must tag where all these things came from, where they were all created. People don't understand where this came from. You want to review, for example, a week later, what was the plan for something that happened, and you have no fucking clue what the plan was. You understand what I mean?

**[00:27:10] Semeyon S**: You're not accidentally talking about settings now?

**[00:27:15] Igor Skrynkovskyy**: This is about Relation between created and imported. Dan, we have the information, we just don't output it. Somewhere it's not in API, somewhere it is in API, but it's probably not displayed. But everything's ready there, we'll somehow pay attention to this and add it.

**[00:27:35] Vova**: And filtering by scenario from which all this came would also make sense?

**[00:27:39] Igor Skrynkovskyy**: Of course.

**[00:27:41] Dan Khasis**: So I just said that I don't understand.

**[00:28:09] Semeyon S**: Okay, we'll extract priorities from the call and refine them. We have this all more or less.

**[00:28:21] Dan Khasis**: Need to hurry up, of course. Yes, so with this Strategic Comparison, I think the following. Then another thing that annoys people is that after Strategic Route modification, they want to take and somehow edit one of these scenarios. But our, we're like, so if we let them have the right to modify scenario, we'll lose our original idea, right? They, no one will know till the end how we originally intended, if we let them modify something. So we need to figure out this funnel that will allow. We came up with 50 routes, you modified right.

**[00:29:38] Semeyon S**: Dan, repeat, you're breaking up.

**[00:29:44] Dan Khasis**: Now we generated 50 routes, for Monday route 1, Monday 1. And now it's not clear to the person how they can edit the 3rd, 4th route they don't like. They're obliged to import everything into Master Route, then in Master Route manually update everything, then from Master Route that they manually updated, they lose our original idea. And since there's nowhere no filter, no source, no origin, nothing, people don't know where all this came from.

**[00:30:38] Semeyon S**: But linking and sources we'll definitely add this.

**[00:30:43] Dan Khasis**: If they start editing, how will we know something useful. I understand we don't allow this now, but in principle we can make miniature route editor, if we want, on JSON files. And save these JSON files, we're saving all scenarios now, where and how.

**[00:31:12] Semeyon S**: And they're saved in database as draft models? You think?

**[00:31:19] Dan Khasis**: I think they're in JSON lying on flatfile somewhere.

**[00:31:23] Semeyon S**: Ah, scenarios themselves, yes, I mixed up. They're lying now exactly as JSON files, haven't transferred to API yet, haven't gotten to this. So in principle we can pull them.

**[00:31:40] Igor Skrynkovskyy**: This is a bit not like that. We have scenarios as duplicates, as results, data artifacts, they lie as copy. But additionally everything's stored in database in DynamoDB.

**[00:31:54] Dan Khasis**: Well how would you do editing? How would you do editing, Igor?

**[00:32:03] Igor Skrynkovskyy**: We have scenario, scenario has parameters. If we're talking about needing versioning, we add versioning and depending on versions will work with this.

**[00:32:17] Dan Khasis**: I don't think we're talking versioning. Google Cloud does.

**[00:32:24] Igor Skrynkovskyy**: No-no-no, I'm telling you, if you're saying we need to change but keep some previous state because it's important to us, then that's versioning as an option.

**[00:32:36] Dan Khasis**: But we can easily change any parameters, do reoptimization or replanning of all these optimizations and get some other result.

**[00:32:51] Vova**: I would imagine this such that when person makes edits inside scenario, then this whole scenario duplicates and writes there scenario 2, and further scenario 2 manual modification. And you thus see two rows, original and what you fixed yourself. And can compare them between each other.

**[00:33:21] Dan Khasis**: Almost same thing, like doing import into AdHocRoute.

**[00:33:44] Vova**: You're completely inaudible, you disappeared.

**[00:33:47] Dan Khasis**: I need to go to this call with Iron Mountain. I'm just trying to say that what you said and what I said is almost the same thing. It's just a duplicate of something. Either you make duplicate in AdHocRoute, or you make duplicate in ScenarioRoute. It's duplicate with duplicate.

**[00:34:14] Vova**: Important that they can then be compared, original with duplicate.

**[00:34:18] Dan Khasis**: To understand if I made good edit or bad. Serhii, will we ever be able to make difference between your approach and my approach? The thing is that with my approach they did import of everything into override. That is into AdHocRoute or into MasterRoute. They easily edited everything with existing tools. For Gantt chart that exist, tools that exist for Multiple Routes Map, tools that exist for Comparison, Manifest, Export and so on. Otherwise they have to rewrite everything from scratch in Scenario Builder. Yes, this is of course an argument. Okay, in short, I'm super late. Last point I want to say. That if you look at this situation, like this word, we still haven't solved in Strategic Route Planner unique route checks, right? That is, no one knows till the end that route number one is really constant route number one in second week, third week, fourth week. You agree with this that we haven't solved this? Judging by silence no.

**[00:35:56] Igor Skrynkovskyy**: No, why not. We have exactly this constant produced by Solver. That is, our routes, they're constant. That is at Solver level they're directly copied. That is if there are same rules, same addresses, they're copied as whole routes to same day, well like plus seven days is done.

**[00:36:26] Dan Khasis**: And where's our, where's this ID of this route? I never saw it in UI. Filter by route number.

**[00:36:41] Igor Skrynkovskyy**: We haven't added yet, right? Well that is, it exists, but we haven't added yet. This is in process.

**[00:36:47] Dan Khasis**: Okay, then you must add and include filter.

**[00:36:53] Semeyon S**: Look, route name column in strategic already exists. You're talking about this, Igor? No.

**[00:37:00] Igor Skrynkovskyy**: Look, this route and this route, they're identical. Why? Because same set of addresses. As here in filter said, like give me all identical routes for entire period.

**[00:37:15] Dan Khasis**: This route number 1, it must be route number 1 always. Okay, guys, I need to go sell Iron Mountain. I'm late. There are 10 people gathering. If Strategic Route Planner consists of these, maps, constant route IDs plus all things we discussed. And assignment board just looks shameful now. Everything's not highlighted there. These numbers, these counters, these absences. Show me all drivers, all vehicles, all routes with some attributes simultaneously. Impossible to do anything. This tool is beautiful to sell, but as soon as they log in, they'll understand this is all nonsense. I'll write you more. Okay, I'm gone. Thank you.

**[00:38:19] Semeyon S**: Serhii, Alexey, maybe we ourselves quickly look at this route comparison?

**[00:38:27] Alexey Gusentsov**: Yes, give me a minute, now. A bit our snapshot switched. Starting up. So, I was doing this here. Can you hear me? Yes.

**[00:39:15] Semeyon S**: Can hear you?

**[00:39:18] Alexey Gusentsov**: Yes. Internet's shit.

**[00:39:26] Vova**: Shadow disappeared. There was here...

**[00:39:29] Alexey Gusentsov**: Here, all, now should be audible.

**[00:39:31] Vova**: Each row here we lost shadow.

**[00:39:34] Alexey Gusentsov**: Yes, all. Actually, this is first prototype, let's say. Shadow I saw later, but they're not everywhere. And it's unclear, they exist, for example, on this column, on this column, but on this column it's not there.

**[00:39:47] Vova**: Yes. Except first row on all.

**[00:39:54] Alexey Gusentsov**: They're needed to separate maps between each other. Many moments that will need to be done on next iteration. Many moments, but for now it looks like this, meaning. Scrolling. I have four originals. Changing. Already have such colored labels. And can add... Well, that is, I didn't do yet this dropdown with selection of specific route. Understandably, because these are all mocks. That is columns are added there, all okay. And there you'll be able to remove from here. For now it looks like this.

**[00:40:46] Alexey Afanasiev**: We don't want to scroll these routes horizontally discretely. Discretely?

**[00:40:53] Vova**: What does discretely mean?

**[00:40:57] Alexey Afanasiev**: By whole route.

**[00:41:01] Vova**: By column width, yes. Don't think so. Don't you think? Let it be uniform. What would be very good is to give ability to resize this first column. As they want. Because they'll have manager, they want to see rows. Accordingly this column can be shorter or wider. And secondly, for this to give ability, so it's to grab any strip here. And resize proportionally all columns simultaneously. Because if I want, for example, to reduce maps, so more fits on screen, so I could grab this row, pull it left, and automatically all like accordion folded, rows became narrower.

**[00:41:48] Maksym Silman**: This will be non-obvious. Need separate control for that you want to drag one or all. Because we have everywhere...

**[00:41:54] Vova**: I don't want them to drag one by one. They'll always drag all, because here maps must be consistent height, consistent proportions.

**[00:42:08] Alexey Afanasiev**: This is really such technical void for us? Yes. And what's on right?

**[00:42:21] Vova**: It disappears when you hide maps.

**[00:42:27] Artur Moskalenko**: Guys, can I interrupt. Let me interrupt. Dan writes, why no duplicate, scenarios. This feature closed? Scenario.

**[00:42:47] Semeyon S**: Yes wait, there is. Though, maybe we're talking about different things with Dan. Yes, Dan means on create, most likely. Here it is. He has this on his account now. Artur, take screenshot or Igor.

**[00:43:14] Artur Moskalenko**: Yes I'll do straight from screen now.

**[00:43:17] Vova**: And I think Dan talks about duplication when ready scenario already ran. And need to duplicate already ready scenario. And run one more scenario in optimization.

**[00:43:30] Semeyon S**: But we haven't done this yet, yes. Though also a thing. Although, wait. No, not yet.

**[00:43:46] Vova**: It should be on upper level, when you're here on scenarios. Then click on separate scenario, it should have action button. Triangles and duplicates.

**[00:43:57] Semeyon S**: Here should also be.

**[00:44:00] Vova**: Here should be save as preset. Should be thing.

**[00:44:07] Semeyon S**: Yes, well both should be. Both save as template, and just as scenario. Maybe I want to right here now run from location. I'm not against forbidding both actions.

**[00:44:29] Vova**: And miracle duplicate can also. I'd only put miracle duplication. Not necessarily in settings, but just right here.

**[00:44:39] Semeyon S**: Well, although this all relates to scenario, can be here too. Only thing, historically we have icons here, mainly, that turn on different tiles.

**[00:44:56] Vova**: No, we have here, right here in this point we have first primary action on right, then further left go secondary action. And enabling panels, they go further, in next. And just turns out that often primary button there's none, and secondary button none, and therefore immediately everything starts with panels.

**[00:45:35] Semeyon S**: Last question about comparison. You're doing now immediately so scenarios can be slipped in, compare on strategic, as Dan just said and so on.

**[00:45:48] Vova**: I shared you at beginning of call.

**[00:45:52] Semeyon S**: Technical question, Vova. This is technical question to guys.

**[00:45:58] Serhii Kasainov**: I haven't reviewed yet, but idea yes. This is essentially table. We pass columns, we pass rows, all.

**[00:46:07] Semeyon S**: Serhii, maybe to be sure, as soon as first zero version is ready, immediately attach it to strategic and staging, to immediately collect all rakes.

**[00:46:23] Vova**: And then we'll want to compare facilities, and then we'll also want to compare drivers.

**[00:46:30] Semeyon S**: Vova, this is obvious. I'm now talking about nearest steps.

**[00:46:35] Serhii Kasainov**: I think next week we'll pull this to both route list and strategic.

**[00:46:42] Semeyon S**: Agreed. In two places at once.

**[00:46:47] Alexey Gusentsov**: Yes, Maksym, about absence of space on right. I just physically cropped width to show when it's cropped, and scrolling. Because this is local development, I'm generally developing on route, what we have on strategic there doesn't work a bit accordingly. This is just visually looks like this for now. Thank you.

**[00:47:09] Vova**: If you have lots of space left, there starts such grid of strips. Like markup exists, that here you can insert more columns. That is when you have space left, there's mockup where it's drawn what will be when lots of space remains.

**[00:47:27] Maksym Silman**: This is all by mockups, yes? By mockups, yes.

**[00:47:33] Alexey Gusentsov**: Once more, I didn't quite understand about fade, this side one. That is side fade, it exists only...

**[00:47:39] Vova**: It separates between each other these variants and lays them as layers and makes left one top layer, because you intuitively pulled what you like to left, and what you don't like forward.

**[00:47:54] Alexey Gusentsov**: I understood this. I didn't understand one thing, why it doesn't have on first column and why it's only on map.

**[00:48:00] Vova**: It's needed to raise higher in hierarchy first route, and this thing - this is first layer, topmost level, second, third, fourth.

**[00:48:15] Alexey Gusentsov**: All, I understood, okay. In short, that is in working column it's only on map conditionally, in others... Well not in others, but in these already...

**[00:48:24] Vova**: It's not there. If map, then it's only on map, this gradient.

**[00:48:33] Igor Golovtsov**: Can I say more? In Vova's mockup it's drawn that this is in drawer. No.

**[00:48:39] Vova**: No, this is fullscreen, this is not drawer. Dan asked us to make this fullscreen. Doesn't matter, this is fullscreen. Wait, this is fullscreen, good.

**[00:48:54] Igor Golovtsov**: What's done now, this is just on page in our layout, and looks like it's fucked up face and it just went away. No, Dan specifically said, I want fullscreen comparison.

**[00:49:03] Vova**: This is not fullscreen.

**[00:49:08] Alexey Gusentsov**: So I just said I'm just developing in routes. This is just, well that is, looking only at internal part.

**[00:49:15] Alexey Afanasiev**: Igor, nothing will be on top.

**[00:49:19] Alexey Gusentsov**: Yes, it embeds wherever you want. This is just consider I'm developing in storybook, but storybook has big problems now, so I had to just hack this in routes.

**[00:49:33] Serhii Kasainov**: Piled on Alexey, damn. Yeah I was trying here generally.

**[00:49:37] Vova**: Alexey, you're great. Did cool, and very quickly most importantly.

**[00:49:43] Serhii Kasainov**: Oh, agree. Pity Dan didn't see, but okay, will see straight in action.

**[00:49:52] Semeyon S**: Well polish a bit, when it's closer to final look. Take screenshot, yes, send to Slack. From preview.

**[00:50:04] Serhii Kasainov**: We'll also get feedback, because we were basically eating feedback and doing.

**[00:50:08] Semeyon S**: Actually yes, actually yes. Didn't work out now, but in asynchronous mode. Okay, any more questions or dispersing?

**[00:50:26] Igor Golovtsov**: No, now have questions for Alexey.

**[00:50:29] Igor Skrynkovskyy**: Guys, I apologize please.

---

## STATISTICS

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
- **Kateryna Shevchenko**: 1 segment, 00:00:01 (0.0%), accuracy 99.0%

### Alignment Quality

- High confidence (time-based): 328 (96.5%)
- Resolved through LLM: 7 (2.1%)
- Fallback: 5 (1.5%)
- Average confidence: 93.5%
- [!] Low confidence (<70%): 14 segments (4.1%)
