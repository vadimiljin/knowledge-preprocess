[TRANSLATION METADATA]
- Source: full_transcript
- Original Language: Russian + English technical terms
- Translation Date: 2025-11-22
- Transcript Accuracy: 94.5%
- Confidence Level: high
- Meeting Duration: 00:25:28
- Participants: 9

---

**[00:00:00 - 00:00:23] Serhii Kasainov**: We'll show this. It looks pretty cool. I might reduce its brightness a bit more. It should really be completely in the background. But overall it's really cool. Dima, is there anything interesting with DestinationDriver?

**[00:00:23 - 00:00:40] Dmitry Smaliak**: No, I haven't looked at DestinationDriver yet. I'm currently working on the snapshots in Destinations, so that we have this whole story. It was working. I'll roll this out.

**[00:00:40 - 00:00:41] Serhii Kasainov**: In what sense?

**[00:00:41 - 00:00:47] Dmitry Smaliak**: In terms of the snapshot. Well, our tracking number wasn't working in the copy table.

**[00:00:47 - 00:00:50] Serhii Kasainov**: It wasn't working at all?

**[00:00:50 - 00:00:59] Dmitry Smaliak**: Or is this related to AZUGA? No-no-no, it wasn't working in the table. It used to work on snapshots, but when we pulled...

**[00:00:59 - 00:01:09] Serhii Kasainov**: Okay, so we need to pull... That wasn't there. We need to pull fresh core.next because I fixed the fallback value there.

**[00:01:09 - 00:01:19] Semeyon S**: And is Alexandr Kovtunov here? No.

**[00:01:19 - 00:01:29] Serhii Kasainov**: Well, I'll write to him that we need to roll out the backend fix to snapshots as well, to routes.list. I asked QA where else we might have tracking.

**[00:01:29 - 00:01:44] Alexey Afanasiev**: We need to roll out the fresh fix from core and from backend everywhere, if I understand correctly. And, please show me... Does the fix relate to redirecting white label accounts to another domain, right?

**[00:01:44 - 00:02:09] Serhii Kasainov**: Yes, there's some clunky frontend logic with fallback, and specifically on AZUGA and several other white label accounts, the backend for some reason has a condition not to send this key. Please show the columns "distance to the next destination" and "drive time to the next destination". Here they are. Added. Oh, there's proper formatting.

**[00:02:10 - 00:02:12] Dmitry Smaliak**: All correct. Added.

**[00:02:14 - 00:02:20] Serhii Kasainov**: Does anyone have any comments? Please show the filters.

**[00:02:20 - 00:02:24] Semeyon S**: Did you add filters on destinations?

**[00:02:26 - 00:02:41] Serhii Kasainov**: No, Dan really requested these two columns. And did you add them to snapshots? We're rolling them out now, if they're tested here and there are no comments, we'll immediately roll this out with a library update to snapshots.

**[00:02:41 - 00:02:47] Dmitry Smaliak**: Yes, I'll roll this out now, it will go together with the tracking number copy fix.

**[00:02:47 - 00:02:52] Igor Skrynkovskyy**: Serhii, and the link here will change too, right?

**[00:02:52 - 00:03:13] Serhii Kasainov**: It's just good that we coordinated hand and foot. And I said that we need to update core.next, definitely for Dima, together with this tracking number fix. But I'm also writing to Kovtunov to update the internal pages for these modules as well. So, I have a question then.

**[00:03:13 - 00:03:29] Dmitry Smaliak**: I'm just looking at how tracking number was built in snapshots. Now I'll see how this link works. Because it's built from the frontend.

**[00:03:29 - 00:03:45] Serhii Kasainov**: We can solve this tête-à-tête, but we need to check. We just brought in fresh logic specifically for the tracking number link. We need to coordinate it everywhere.

**[00:03:45 - 00:04:00] Dmitry Smaliak**: Yes, let's discuss it, because I copied the tracking page from snapshots as it was before. So, what else to show?

**[00:04:00 - 00:04:04] Serhii Kasainov**: I think that's all.

**[00:04:08 - 00:04:16] Dmitry Smaliak**: Semeyon, what you wrote yesterday about filters, has strategic optimization and scenario filters come in here? Is this local or is this already on staging?

**[00:04:16 - 00:04:21] Semeyon S**: No, this is already on staging.

**[00:04:21 - 00:04:25] Dmitry Smaliak**: Oh, cool.

**[00:04:25 - 00:04:33] Semeyon S**: Igor Golovtsov, please note for yourself. You can quickly add links to the numbers now.

**[00:04:37 - 00:04:53] Serhii Kasainov**: I remember correctly. This will be a link from strategic to routes.list with these filters activated, right? Yes. I didn't dream it. There wasn't such a thing in the ticket.

**[00:04:53 - 00:05:04] Dmitry Smaliak**: Look, wait, wait. This is a different ticket. Yes, this is a different ticket. We'll need to finish it so that it pulls from the URL directly here.

**[00:05:04 - 00:05:15] Serhii Kasainov**: Yes, that's all correct. Are we sure about this group, that it's assignment and attribution? I don't think so.

**[00:05:15 - 00:05:18] Dmitry Smaliak**: Or yes?

**[00:05:18 - 00:05:21] Serhii Kasainov**: We can move it out, I added it by analogy.

**[00:05:21 - 00:05:28] Igor Skrynkovskyy**: So this is a question to discuss with everyone. I think this is different.

**[00:05:28 - 00:05:42] Semeyon S**: Because this is not about assignment or attribution at all. This is about graph relationships. This isn't even quite customer linking. Close, of course, but...

**[00:05:42 - 00:05:45] Serhii Kasainov**: I think this deserves a separate group.

**[00:05:45 - 00:05:49] Igor Skrynkovskyy**: Yes, we can make a separate group.

**[00:05:49 - 00:05:52] Dmitry Smaliak**: Can you scroll down a bit, what other groups are there.

**[00:05:52 - 00:06:09] Igor Skrynkovskyy**: And matrix. Because it's similar, we have filters there with contacts, with orders. And this is very similar to this. That is, possibly, as you say, a separate group. Like address book details, probably make it a separate group too.

**[00:06:09 - 00:06:16] Dmitry Smaliak**: Yes, no problem. Just need a group name.

**[00:06:16 - 00:06:23] Serhii Kasainov**: Something like strategic planning. The section is now called scenarios.

**[00:06:23 - 00:06:26] Semeyon S**: Well, in the menu.

**[00:06:26 - 00:06:30] Serhii Kasainov**: Strategic routing.

**[00:06:30 - 00:06:33] Semeyon S**: Oh, let's call it strategic routing.

**[00:06:33 - 00:06:37] Igor Skrynkovskyy**: Maybe let's call it strategic routing.

**[00:06:37 - 00:06:40] Dmitry Smaliak**: No-no-no, guys, wait.

**[00:06:40 - 00:07:08] Semeyon S**: This is a section. And scenarios will send you to the strategic optimizations list. And there, this is, Semeyon, these are filters. That is, there are filters for optimizations and for scenarios. Change. So maybe we should first ask Dan.

**[00:07:08 - 00:07:11] Igor Skrynkovskyy**: And then do it right.

**[00:07:11 - 00:07:18] Dmitry Smaliak**: Generally worth asking. Let's try somehow.

**[00:07:18 - 00:07:21] Serhii Kasainov**: Well, let's name it.

**[00:07:21 - 00:07:25] Dmitry Smaliak**: So, we tried.

**[00:07:25 - 00:07:28] Serhii Kasainov**: If we ask, we won't learn anything.

**[00:07:28 - 00:07:31] Dmitry Smaliak**: And if we do it wrong, we'll find out very quickly.

**[00:07:31 - 00:07:38] Serhii Kasainov**: So, we already did it. This is very wrong.

**[00:07:38 - 00:07:52] Semeyon S**: Let's make it a little bit wrong. Let me call it scenarios. This is the result of synchronization. You can participate.

**[00:07:52 - 00:07:55] Serhii Kasainov**: Oh, okay, okay.

**[00:07:55 - 00:08:33] Semeyon S**: Also, recurring routes that we have are from templates that create other routes. That is, it should be in a separate group, and strategic routing fits in that sense. Filter by master route should be added there too - logical?

**[00:08:33 - 00:08:53] Serhii Kasainov**: These are just routes that have master route set. It's just a filter. If you want, you can place it there. You can place it. It's just in routes.list we have a filter "is template". Like that. But we don't have master route ID filtering yet. If we have it, we can add it. If not - later.

**[00:08:53 - 00:09:03] Dmitry Smaliak**: I can't say. This is backend. This is what routes return to us.

**[00:09:03 - 00:09:41] Serhii Kasainov**: Okay. So if there is, we'll add later. That's it. Manar, to you.

**[00:09:41 - 00:10:14] Manar Kurmanov**: The main update relates to optimization. New flow behind a feature flag allows selecting from custom relocation via list or filters, or both. For example, two filters can be applied. Or inclusion/exclusion modes for them. Both inclusion and exclusion are available. This also works on the very first step.

**[00:10:14 - 00:10:29] Serhii Kasainov**: Where are the filter groupings?

**[00:10:29 - 00:10:54] Semeyon S**: Serhii means groupings within filters. Custom relocation doesn't have them. But we're not doing that now, right? No.

**[00:10:54 - 00:11:01] Igor Golovtsov**: Let's never reference custom relocation as a model.

**[00:11:01 - 00:12:10] Manar Kurmanov**: Understood. Moving forward: inclusion/exclusion modes work. A new step is now common for the entire optimization - you can set a name, select from facilities, or manually input addresses via search. For facilities, we select and it shows in the table. Next step - here you can edit the name. All three modes work. When you select locations, you need to specify from what location you want to optimize. Locations are actually like addresses, they're not depots. At any given time, your location might not be at the depot but somewhere else. Therefore, it asks where to start optimization from. Since we have multiple selection, you can select all and then choose the starting location. Also, you can rename the optimization here.

**[00:12:10 - 00:12:28] Igor Skrynkovskyy**: If creating through location selection, must specify start location. Multiple selections possible. Optimization can be renamed.

**[00:12:28 - 00:12:39] Manar Kurmanov**: New name saves in the optimization itself.

**[00:12:39 - 00:12:53] Semeyon S**: Does this multi-select facility/manual feature exist?

**[00:12:53 - 00:13:15] Igor Skrynkovskyy**: Wait - nobody disabled depots. What feature flags control display of this radio button for facilities vs start location?

**[00:13:15 - 00:13:44] Manar Kurmanov**: For facilities radio to show table, we have feature flag "facility view". For multiple vs single depot, I removed the feature yesterday after discussion that it wouldn't be needed and would be everywhere.

**[00:13:44 - 00:14:13] Semeyon S**: Not exactly what we said. We said for first step we can assume heavy strategic clients always have multiple depots feature, but we need to support it in next steps even for single depot.

**[00:14:13 - 00:14:35] Igor Golovtsov**: This came from someone who manages features - either Artur or Oleg Shulga.

**[00:14:35 - 00:15:00] Igor Skrynkovskyy**: The question is about properly displaying this input button via feature flag. 5% have depot when they have multiple depot, others don't need it. This product might even be sold separately. And used separately. Therefore, what settings, in which case, in which package will be, we can't predict ahead of time. I wrote it down, we'll clarify. We can generally continue moving forward. It's clear that we need to figure this out.

**[00:15:00 - 00:15:25] Semeyon S**: Good. I'll separately tag Semeyon, Igor, to clarify what's there. Okay. Can I add one more thing quickly? Just you're moving fast. If back to the previous...

**[00:15:25 - 00:15:36] Igor Golovtsov**: Yes. Look, here it says database. Is this approved?

**[00:15:36 - 00:15:54] Igor Skrynkovskyy**: We're not saying this is customer location or something else. Look, at the top it says select locations. And on Thursday the guys showed a local version. I asked them to write database here. Well, Dan didn't complain about it.

**[00:15:54 - 00:16:12] Semeyon S**: Approved like that. Good. Next question. Here we're not adding a map. To conditionally draw.

**[00:16:12 - 00:16:30] Igor Skrynkovskyy**: In the next steps. Next iteration. Okay. All. Thanks.

**[00:16:30 - 00:16:56] Semeyon S**: And by the way, guys, I completely forgot. We need to check the default field set. In this view. Well, so that it makes sense. I wrote it down. Because now I look, there's a lot of white space. This is where ours goes. Very beautiful.

**[00:16:57 - 00:17:04] Manar Kurmanov**: We'll need to configure on backend, it will come automatically. Although we'll need to clarify whether this is the same as the routes view or a different custom view.

**[00:17:04 - 00:17:12] Semeyon S**: That's what I'm talking about. Are we copying one-to-one or are we making our own view after all?

**[00:17:12 - 00:19:45] Manar Kurmanov**: That's the question. So. In general, these are all the big changes. Also looked at additional work from Vova. He has big developments going on there. I won't comment on them now. They're not approved. One comment I'll say is that there might not be just two options here. Manual and selection. He talked about one business case where the user wants to test which depot they should buy to see whether it will affect their business or not and so on. Something like that. He mentioned such a case. They're drawing in design now. In general, the whole process from Create Optimization they took for refinement. They had comments about sizes, paddings, fonts. There's a lot of work going on there. We'll take this in one of the later iterations. As soon as someone approves it. And then everything is exactly the same. A new step is created. And optimization goes based on our locations. This is the biggest update. Also this is now on staging. You can plan strategic optimization in the same way from here. Everything is exactly the same. Let's say we take this facility. The next transition is like this. This is now in merge request. When the user clicks plan optimization, it immediately redirects them to the third step. No, this is a different ticket. Okay, I won't confuse things. In general, it redirects to the third step immediately to create settings. This is also on review now. These are the changes from my side. Regarding the feature flag for multi-depot. Ideally I initially added it, but then the guys said it needed to be removed. I removed it, I can bring it back.

**[00:19:45 - 00:19:49] Igor Golovtsov**: Don't get stuck on this, we'll figure it out.

**[00:19:49 - 00:19:52] Manar Kurmanov**: Yes, I wrote it down, I'll figure it out.

**[00:19:52 - 00:20:24] Semeyon S**: Something like that. Very big request. Please, ASAP, push to staging. We've been waiting for this functionality for a very long time, really. Anything else on staging, on strategic. And what about the table in this, inline mode for scenarios, Igor? Nothing.

**[00:20:24 - 00:20:32] Igor Golovtsov**: Eugene made the first step in that direction. And went...

**[00:20:32 - 00:20:35] Semeyon S**: Unfinished, in short.

**[00:20:35 - 00:20:47] Igor Golovtsov**: I can show all sorts of small things, like deletion modal, deletion and so on, but I don't think it's interesting to show here in the last 4 minutes. Well, verbally then, Igor, did the team add scenario deletion? Well, so you could clean up.

**[00:20:47 - 00:20:55] Semeyon S**: Deletion, but not scenarios. Optimization deletion.

**[00:20:55 - 00:20:59] Igor Golovtsov**: Optimization, sorry.

**[00:20:59 - 00:21:07] Semeyon S**: But there's a nuance, there's no pusher now, so it works ugly. It works but you need to manually refresh the page.

**[00:21:07 - 00:21:19] Igor Golovtsov**: It works and... No, there's a request. A deletion request is sent, and then when it successfully completes...

**[00:21:19 - 00:21:22] Semeyon S**: Well, like it does for me today...

**[00:21:22 - 00:22:19] Igor Golovtsov**: And like in your case, it simply re-requests the combine, but it's not updated yet. And therefore it doesn't go anywhere for you. Yes, pushers fix this. Well, for the end user, you understand, doesn't matter. I understand, yes, it's just an explanatory brigade. And from what else is probably useful for the user, we now have errors and statuses for creation, specifically creation status, we now have it for both scenarios and optimizations, and errors, if they're validation errors, they're drawn for the entire optimization if the entire optimization failed, and for a specific scenario if it failed partially. Well, that's it.

**[00:22:30 - 00:22:43] Alexey Afanasiev**: That's all for us, Serhii ran away, so won't look at ERP, and routes, location, snapshot aren't ready. Well, in general, that's all for today.

**[00:22:47 - 00:22:54] Semeyon S**: And if it's not difficult for you, about the documentation, what was planned? I'll check.

**[00:22:54 - 00:22:57] Alexey Afanasiev**: No.

**[00:22:57 - 00:23:01] Semeyon S**: Ah, now I turned this on.

**[00:23:01 - 00:23:09] Alexey Afanasiev**: This isn't ready, this isn't ready yet. Here Serhii ran away, so...

**[00:23:12 - 00:23:16] Semeyon S**: And what's our assignment status?

**[00:23:22 - 00:23:31] Alexey Afanasiev**: Assignment board isn't here at all. They're only switching today. In the switching process. Well, from strategic.

**[00:23:34 - 00:23:52] Eugene**: Well, we made some small changes two weeks ago, added links, updated filters. Now we're going to design, to clarify two questions, and then the status will be clear. Please tell me the answer about tomorrow's demo.

**[00:23:52 - 00:23:58] Igor Golovtsov**: It won't happen or is it still under question?

**[00:23:58 - 00:24:11] Semeyon S**: Well, it won't happen. Dan cancelled, and I don't always decide to drive such a large number of people back and forth.

**[00:24:12 - 00:24:13] Igor Golovtsov**: Okay.

**[00:24:14 - 00:24:26] Semeyon S**: Roughly speaking, this internal mini-demo of ours is a replacement for tomorrow's. So we all sit down, look at who has what results, get some minimal feedback and move forward.

**[00:24:26 - 00:24:34] Igor Golovtsov**: Okay, thanks. Alright, I'm running to the next call.

**[00:24:43 - 00:24:49] Alexey Afanasiev**: Eugene, then let's go to the current design call. It's a bit earlier.

**[00:24:49 - 00:24:52] Eugene**: Let's just wait until they finish with strategic.

**[00:24:52 - 00:24:55] Alexey Afanasiev**: I really want Igor to look at and listen to this too.

**[00:24:55 - 00:25:01] Eugene**: Maybe even Serhii. I think we're going to build a spaceship now.

**[00:25:01 - 00:25:08] Alexey Afanasiev**: So, Igor will be there. Golovtsov.

**[00:25:15 - 00:25:17] Semeyon S**: Alright, shall we close the call then?

**[00:25:17 - 00:25:19] Alexey Afanasiev**: Yes. Thanks.

**[00:25:20 - 00:25:21] Semeyon S**: Igor, do you have any questions?

**[00:25:22 - 00:25:22] Igor Skrynkovskyy**: Not anymore.

**[00:25:23 - 00:25:26] Semeyon S**: Alright, thanks everyone, bye.

**[00:25:27 - 00:25:28] Igor Skrynkovskyy**: Thanks, bye.

---

## Translation Statistics

- Total Segments Translated: 378
- Transcript Accuracy: 94.5%
- Technical Terms Preserved: 35+
- Participants: 9
- Meeting Duration: 00:25:28
