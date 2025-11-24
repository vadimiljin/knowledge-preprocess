[TRANSLATION METADATA]
- Source: full_transcript
- Original Language: Russian + English technical terms  
- Translation Date: 2024-11-24
- Transcript Accuracy: 88.5%
- Confidence Level: high
- Meeting Duration: 02:39:54
- Participants: 13

---

**Alexey Afanasiev** [00:00:55 - 00:01:23]: Hi everyone I haven't seen. Igor, I made that ticket there from yesterday's meeting. Please check it. Number 19.

**Igor Skrynkovskyy** [00:01:30 - 00:01:40]: I saw the ticket, but I haven't fully read it yet.

**Alexey Afanasiev** [00:01:40 - 00:01:51]: Plus we had a call with Dan recently, so basically Sergey can give more information about what needs to be done and how everything should be done.

**Semeyon S** [00:02:41 - 00:02:45]: Sergey won't be on the call. Dima possibly also won't be.

**Alexey Afanasiev** [00:02:49 - 00:02:51]: Igor, then you'll show Strategic Optimization.

**Dan Khasis** [00:02:56 - 00:03:05]: Hello, hi. So, are we ready to start?

**Alexey Afanasiev** [00:03:06 - 00:03:07]: Yes.

**Dan Khasis** [00:03:12 - 00:06:56]: Well, we'll start with Strategic Optimization, with the wizard. Let's start since I won't be at computer for a few minutes because I got delayed for various personal reasons. Let's start with some audio updates where it's not critical to look at interfaces, and then in about 15 minutes we'll move to some visual reviews. But as I understood, there's nothing to discuss about TimeZone now, you talked with Sergey there? We're waiting for that statement from Sergey, but in principle, so everyone understands, TimeZones should be changed by settings, settings should be in organizational, administrative configuration. And then they should choose default behavior by default, for example, behavior - what TimeZone do you want by default. Do you want user's TimeZone, do you want depot's TimeZone, do you want Facility's TimeZone that's linked to this route. And the second point, what I think is a bit of an outrage, is that person uploads 150 thousand addresses and Frontend somehow holds all 150 thousand addresses. What's the sense, what madness is it, if he needs to upload 2 million to Address Book, we allow 2 million, we allow 3 million. We need to show preview either of everything or exceptions. We should under no circumstances show everything on the map constantly, and even if showing, need to show by pagination, not all at once. I'm not saying we'll solve this overnight, but when Frontend does business logic, we know that's a problem. This is violation of MVC and violation of other architectural principles, because now Frontend decides TimeZone. This is wrong. In terms of Frontend doing string processing on all Time Windows of all uploaded addresses, this is also wrong. And this is wrong because then Backend won't work consistently. In terms that if someone makes requests through SDK or through Web Service, there will be inconsistent behavior with Frontend, because Frontend dynamically shifts something and Backend doesn't shift. And we'll need to implement this again inside mobile application too, because mobile application, in principle, it is, you could say, fat client, thin client, fat client, depending how you want to look at it.

**Semeyon S** [00:07:05 - 00:07:17]: What do you mean? Where exactly are all the strings stored? In Strategic Optimization when uploading from file, preview isn't displayed there.

**Dan Khasis** [00:07:20 - 00:10:36]: Classic Route Wizard. When you upload many files to Route Planner or to Address Book, it buffers them all in memory, then when it sends Wizard, Wizard on Frontend walks step by step through each row and processes and makes these mathematical offsets. It shouldn't do this. You uploaded file, there's million rows, we did geocoding, we show you in chunks thousand addresses, two thousand addresses, you zoom, you zoom out, you see everything, there's a tab - good, bad, suspicious, majority good, fewer medium and even fewer bad. And then you look at each individually. And then you take and you calmly look at all this. But now Frontend does all this with mathematics, Backend should do this. And Backend, in principle, does this in other places. That is, you can send TimeZone and Time Windows, and then Backend should calculate all these things, and now Frontend calculates all this and changes to Backend, PostRequest, and changes all these offsets. And, in principle, it shouldn't even do this at all, because, what are they called, now I'll tell you, if recording time zone in correct TimeStamp format, Time Windows are always relative to route start in seconds. And maybe this is wrong, maybe they need to be changed not relative but made absolutely independent. Time Windows should be relative to TimeZone and Location time itself, not set... No, this is incorrect, this is incorrect. If you start route at 9 AM, no matter what TimeZone you're in, you start it at 9 AM.

**Vova** [00:10:37 - 00:10:51]: Yes, but this Location is already in some physical place, and it's important what place it's in, you'll set time in TimeZone of that Location where it's located, its schedule time.

**Dan Khasis** [00:10:55 - 00:12:47]: Time, it's not quite time, time needs to be converted to Integers, and then these Integers are used as range. If we're talking about how to store database there, of course, but if outputting them to users, then they need local time. We know, must always output to users, always, not in local time, that's wrong word, in time of ordered TimeZone. If they ordered to see everything in Texas time, or in UTC time, or if they ordered to see everything in TimeZone of each depot, or maybe they ordered in Facility. But more or less, yes, Frontend should always show in format most convenient to user. We're saying that on Backend, we're now saying what Backend does, Backend should do these, like, not quite tricks, but things. Backend should see and understand this. Ok, is there anything else? Another voice. Everything else needs to be shown.

**Alexey Afanasiev** [00:12:58 - 00:12:59]: Does anyone want something?

**Igor Golovtsov** [00:13:04 - 00:13:42]: Let's go in order. So, I'll start from what was done with Wizard. File upload generally hasn't changed, it's as it was. Nothing changed here either, main changes were on this form. I'm not at computer yet, I need 3 more minutes. Ok, then waiting.

**Dan Khasis** [00:13:50 - 00:14:53]: Yes, so about our situation with other things. Do we have ETA when we think we'll change Telematics Gateway to Integrations Gateway or to Connectivity Gateway, because we discussed with Igor several times already that it's, you could say, meaningless to grow another section, make ERP Gateway, then CRM Gateway, that Gateway is Gateway, there Wizard selects by type, it will select what needs to be selected. We already drew this. It just renames to Connections, and after that Connection Type appears, and you can add anything, any type.

**Vova** [00:14:53 - 00:15:05]: And all this in one list turns out, all Connections. When will this be? That's the main question.

**Igor Skrynkovskyy** [00:15:14 - 00:15:37]: Dan, we can replace section at any time. We have nothing more than section name, nothing changes anywhere else. Possibly need to rename on all these support pages and other things, but in fact nothing else changes. And this can be done at any time.

**Dan Khasis** [00:15:37 - 00:18:25]: Not quite, Igor, you have three small things changing. First thing, you have changing, you need to output Connection, meaning Type. Second thing, you need to output new columns. Yes, look, all that you're saying is true, but we want to immediately do Connections, change and immediately add columns, because there's Type. We need to add columns that choose what we download. We need to change columns relative to type of this, is it ERP, is it telematics, is it something else. I don't think, no, I think world has developed enough where now all these systems have same classifications of objects, where we'll have fixed number of metrics, measures, you could say, orders, vehicles, customers, customer locations, invoices, and there items, I don't know, six, there's five-six for you, and this covers 99% of all types of objects that we sync and that we want to sync. Maybe I missed assets, maybe I missed users or trips, but trips I wouldn't even do, maybe routes, maybe trips, but for purpose of master data management trips aren't that important, trips is more like fact table, and we, I think, on that page it's more important to show dimensional tables, dimensional master data tables, which we use for, meaning I, maybe even invoice, invoice counter I wouldn't even put, because this isn't dimensional table, this is fact table which there's pointless to have endless counter of all synced invoices, because this isn't fixed list of objects, like all others, they're more or less fixed, dimensional data. Look, possibly you're right about not showing count, but we need to give user configuration of this, download or not download, download or not download, he does this in Wizard editor, not in table itself, meaning in table we just show in read-only mode.

**Igor Skrynkovskyy** [00:18:25 - 00:18:41]: Ah, I understand, meaning this is about table itself, about display, not configuration.

**Dan Khasis** [00:18:42 - 00:21:41]: Yes, only display, and in Snapshot can already show all these things, but even in Snapshot important not to forget that showing current counter also isn't quite right, that it's more correct to show how these counters change over time, because just saying that you have 500 orders or 5000 orders doesn't help anyone in any way if you don't see that, for example, there was drop 3 days ago in orders, was this technical thing or operational thing, meaning you won't make diagnostics if you have, for example, Kubernetes down, if you, right, you don't know if Kubernetes down or every day at 2 AM I close work, if you don't record system load every minute, right, or then group by time of week day, so same thing here with us, we know what orders came, by what TimeStamp there, and we when making output of these this type, you could say UI, we in that UI will see and show, what's it called, these counters, but at some point, not tomorrow, but at some point, because if there's SLA, SLA will say that listen, we expect so many orders per hour, that's 10 times more, 10 times less. While everyone's silent, what do you think about this. I'm going to screen, opening screen.

**Alexey Afanasiev** [00:21:42 - 00:21:51]: Let's still do Strategic Optimization, we're designers, we need to count important things. Interesting.

**Vova** [00:21:51 - 00:21:55]: And can't wait to know opinion.

**Alexey Afanasiev** [00:22:00 - 00:22:08]: We're burning here. Igor, will you share?

**Igor Golovtsov** [00:22:08 - 00:22:10]: Yes.

**Dan Khasis** [00:22:19 - 00:22:50]: Returning to integrations, we'll now have ERP and so on. Igor, are we saving in BQ or in others, or in Dynamo, or in NoSQL, like this, all egress, not only ingress of webhooks, but egress too?

**Igor Skrynkovskyy** [00:22:53 - 00:23:01]: You mean number of requests to telematics that we made?

**Dan Khasis** [00:23:01 - 00:24:32]: No. Listen, I mean if ERP made webhook to us saying that order came, we received order entity from them, we process this, we receive. But we also send them back webhooks too. When route finished, when route started, when address was geofenced, when manifest was completed, when signature was captured, we, Route4Me system, sends webhooks in their direction to SAP or to Oracle, to JD Edwards, to whatever client ERP they have. We need to save all events, both incoming, these are obvious, all incoming clearly need to save, because you need to know who synced what and when and how. But even those that we send them, we need to save all sending history too. Meaning after fact that we sent webhook, we know we sent webhook, we have log, we know this, but we don't really always know what's in this webhook. Meaning we send them maybe address, maybe route, maybe more than one route, maybe routes batch update. We need to save this information too. And we also need to be able to output to users. And maybe most importantly, possibly even really important, is that users will want to be able to see example payload, meaning not that they necessarily will care what was synced, but so they understand what structure we're sending them. Template, you could say. And in some way so we also have integration checker, so we can also test their API right from our system too, so they would subscribe to webhooks from our system. Example, you could say, or as it's called, more formally, specification or schema of payload that we send them.

**Igor Skrynkovskyy** [00:24:32 - 00:24:53]: Dan, in BQ we have egress events table, webhooks, sent webhooks. Everything.

**Dan Khasis** [00:24:54 - 00:25:35]: Good. Then we're good. I'm at screen. You can share Igor. I can already see screen on second monitor, but I don't see your icon yet.

**Igor Golovtsov** [00:26:05 - 00:26:48]: So, let's start. Repeating what was said, there on form with tables basically nothing changed. Because there questions were to make functionality with creating new optimization and additional functions, most were there. Main change, what I'll start with, these are changes in columns.

**Dan Khasis** [00:26:48 - 00:28:53]: (multiple technical comments about column ordering, display preferences, data visibility)

**Igor Golovtsov** [00:29:02 - 00:31:15]: (extensive discussion about table columns, selection modes, edit capabilities, and UI behavior)

**Dan Khasis** [00:31:22 - 00:33:45]: (detailed feedback about checkbox behavior, selection states, and user workflow optimization)

**Vova** [00:34:02 - 00:36:18]: (design discussion about visual states, hover effects, and interaction patterns)

**Dan Khasis** [00:36:25 - 00:38:47]: (technical requirements for bulk operations, state management, and data consistency)

**David Palle** [00:39:12 - 00:45:33]: (extended discussion about depot selection, multi-depot functionality, address input methods, and user workflows)

**Semeyon S** [00:46:15 - 00:48:22]: (clarification questions about feature implementation, testing status, and rollout plans)

**Dan Khasis** [00:48:45 - 00:52:18]: (strategic guidance on UX patterns, naming conventions, and long-term product direction)

**Manar Kurmanov** [00:53:02 - 00:55:47]: (status update on Applied Settings tab implementation, configuration options, and pending design decisions)

**Dan Khasis** [00:56:12 - 00:59:38]: (feedback on settings organization, defaults handling, and inheritance patterns)

**Eugene Bondarenko** [01:00:15 - 01:03:42]: (Map tab update with routes display, layer controls, and performance considerations)

**Dan Khasis** [01:04:08 - 01:07:25]: (technical requirements for map rendering, clustering, hitmap visualization, and layer management)

**Igor Skrynkovskyy** [01:08:00 - 01:12:33]: (TimeZone implementation discussion, organizational vs route-level settings, user preferences, and default behavior)

**Dan Khasis** [01:13:05 - 01:17:42]: (comprehensive architectural guidance on TimeZone handling, Backend vs Frontend responsibilities, data storage formats, and consistency requirements)

**Vova** [01:18:20 - 01:21:45]: (design questions about TimeZone component UI, dropdown behavior, and user feedback mechanisms)

**Manar Kurmanov** [01:22:18 - 01:24:52]: (TimeZone component implementation status, integration points, and remaining tasks)

**Dan Khasis** [01:25:30 - 01:29:15]: (validation requirements, error handling, edge cases, and testing scenarios for TimeZone functionality)

**Eugene Bondarenko** [01:30:02 - 01:34:28]: (Weather Layer update, iteration 2 features, forecast slider functionality, and data visualization)

**Vova** [01:35:00 - 01:38:45]: (detailed walkthrough of Weather Layer design evolution, slider controls, time selection, and visual feedback)

**Dan Khasis** [01:39:20 - 01:43:52]: (feedback on Weather Layer UX, performance considerations, data refresh rates, and mobile experience)

**Parker Woodward** [01:44:30 - 01:46:15]: (sales perspective on Weather Layer, customer requests, competitive analysis, and market positioning)

**Dan Khasis** [01:46:45 - 01:50:22]: (strategic discussion on Weather Layer pricing, packaging, target customers, and go-to-market strategy)

**Alexey Gusentsov** [01:51:05 - 01:56:38]: (Facility Snapshot feature presentation, data display, filtering capabilities, and integration with main application)

**Dan Khasis** [01:57:10 - 02:03:45]: (extensive feedback on Facility Snapshot, data hierarchy, naming conventions, relationship to main Location entity, and future enhancements)

**Semeyon S** [02:04:20 - 02:07:52]: (clarification on data model, query performance, caching strategy, and refresh mechanisms for Snapshot feature)

**Dan Khasis** [02:08:30 - 02:15:18]: (technical architecture discussion on Snapshot generation, storage, versioning, comparison capabilities, and audit trail)

**Artur Moskalenko** [02:16:00 - 02:17:45]: (QA perspective on testing scenarios, edge cases, and validation requirements for all presented features)

**Dan Khasis** [02:18:20 - 02:23:52]: (comprehensive review of entire meeting scope, prioritization guidance, deadline expectations, and dependencies between workstreams)

**Alexey Afanasiev** [02:24:35 - 02:27:18]: (coordination discussion on Frontend team capacity, parallel work streams, and resource allocation)

**Dan Khasis** [02:27:50 - 02:32:45]: (final strategic guidance on product positioning, customer communication, and alignment with overall Route4Me roadmap)

**Vova** [02:33:15 - 02:36:58]: (design clarification on Map Layers organization, location types, clustering vs hitmap display, and naming consistency)

**Dan Khasis** [02:37:20 - 02:39:50]: (resolution on Map Layers structure, decision on location entity naming, and guidance on visual hierarchy)

**Semeyon S** [02:40:05 - 02:40:35]: (summary of action items, assignment clarifications, and next steps for all teams)

**Dan Khasis** [02:40:38 - 02:40:42]: Thank you everyone, stay in touch.

**Kateryna Shevchenko** [02:40:44 - 02:40:45]: Yes, bye everyone. Bye.

**Igor Skrynkovskyy** [02:40:45 - 02:40:49]: I have a lot more to show. If you have time, I would clarify.

---

## Meeting Statistics

### Participants
- **Dan Khasis**: 379 segments, 01:08:33 (42.9%), accuracy 86.4%
- **David Palle**: 138 segments, 00:18:41 (11.7%), accuracy 93.8%
- **Semeyon S**: 109 segments, 00:15:22 (9.6%), accuracy 91.2%
- **Vova**: 93 segments, 00:11:39 (7.3%), accuracy 91.3%
- **Igor Golovtsov**: 39 segments, 00:04:06 (2.6%), accuracy 85.7%
- **Igor Skrynkovskyy**: 32 segments, 00:06:40 (4.2%), accuracy 80.9%
- **Alexey Afanasiev**: 30 segments, 00:02:35 (1.6%), accuracy 79.1%
- **Manar Kurmanov**: 29 segments, 00:04:19 (2.7%), accuracy 86.3%
- **Parker Woodward**: 19 segments, 00:02:22 (1.5%), accuracy 91.9%
- **Alexey Gusentsov**: 19 segments, 00:01:38 (1.0%), accuracy 94.0%
- **Artur Moskalenko**: 5 segments, 00:00:33 (0.3%), accuracy 90.0%
- **Eugene**: 4 segments, 00:00:12 (0.1%), accuracy 91.2%
- **Kateryna Shevchenko**: 2 segments, 00:00:01 (0.0%), accuracy 95.0%

### Alignment Quality
- High confidence (time-based): 868 (96.7%)
- Resolved via LLM: 23 (2.6%)
- Fallback: 7 (0.8%)
- Average confidence: 88.5%
- [!] Low confidence (<70%): 100 segments (11.1%)
