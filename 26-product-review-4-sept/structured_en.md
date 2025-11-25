# MEETING: Product Progress Review - Iron Mountain Crisis & Assets Redesign

**DATE:** 2025-09-04  
**DURATION:** 02:29:34  
**ATTENDEES:** Dan Khasis (CEO), Alexey Afanasiev (Frontend Lead), Artur Moskalenko (QA Director), Vova (UI/UX), Igor Skrynkovskyy (SVP Platform), Serhii Kasainov (Front-End Tech Lead), Semeyon S (VP Platform), Maksym Silman, Alexander Dylevskiy, Oleksandr Ishchenko, Volodymyr Ishchenko, Igor Golovtsov (Senior Frontend Engineer), Dmitry Smaliak (Frontend Engineer), Davron Usmonov (Frontend Engineer), Alex Yasko, Kateryna Shevchenko, Alexandr Kovtunov  
**DAN_PRESENT:** yes  
**MEETING_TYPE:** Product Review  
**DATA_SOURCE:** full_transcript  
**CONFIDENCE_LEVEL:** high

---

## TOPIC: Iron Mountain Customer Crisis - Samsara Competition
**TIME:** 00:09:07 - 00:19:00  
**PARTICIPANTS:** Dan Khasis, Artur Moskalenko, Igor Skrynkovskyy, Semeyon S, Vova, Alexey Afanasiev, Serhii Kasainov

### DISCUSSION

**[00:09:07] Dan Khasis**: Let's start with the email that was written about Iron Mountain. Did you have a chance to read it?

**[00:09:28] Serhii Kasainov**: I read it.

**[00:09:43] Igor Skrynkovskyy**: Yes, I read it too.

**[00:09:50] Dan Khasis**: Okay, so I didn't read it. I just forwarded it to you. Because I spent all week dealing with this. The inventory should finish today, in a few hours, finally. But let's start with your initial impressions about this.

**[00:10:11] Artur Moskalenko**: We don't have Drag'n'Drop.

**[00:10:19] Dan Khasis**: We don't have Drag'n'Drop of what? What does that mean? I can directly contradict right now.

**[00:10:23] Artur Moskalenko**: It's the Route Editor on the map.

**[00:10:27] Dan Khasis**: I don't understand what that means. You mean remove and move stops on the map, to another place on the map? But that's like shooting fish in a barrel, if I understand correctly.

**[00:10:43] Igor Skrynkovskyy**: Yes, we had it.

**[00:10:46] Artur Moskalenko**: This was in progress, but there were problems with it. The Frontend team can give more details. It just works poorly. As far as I remember.

**[00:11:06] Dan Khasis**: You guys did a much more complex thing, if I remember correctly. You did... You implemented this in Routes Map and then magnificently lost it all in the new Routes Map. That is, you made it, everyone was happy, and then lost it all again. If I'm wrong, tell me.

**[00:11:29] Vova**: I'm not sure about deploys, but at least some version of dragging was being worked on.

**[00:12:02] Semeyon S**: Alexey, Sergei, well, get involved.

**[00:12:09] Dan Khasis**: Iron Mountain is leaving us. Ellen and I have to fly to the mountains, who knows where, 4 hours, to get on our knees and beg them not to leave us. Yes, Igor, guess where they want to go.

**[00:12:29] Igor Skrynkovskyy**: Yes, I know, I guess.

**[00:12:32] Dan Khasis**: Say it, say it.

**[00:12:33] Igor Skrynkovskyy**: Samsara.

**[00:12:34] Dan Khasis**: Well, Samsara again. How do you translate Samsara, is it like paradise on earth? If I remember correctly.

**[00:12:47] Semeyon S**: No, it's the infinite circle of souls in Hinduism, I think. It's not paradise, no, it's a different concept. Infinity.

**[00:13:05] Dan Khasis**: The reincarnation process. Anyway, we're competing with people who will never work infinitely. So in our situation, our thing is that you already implemented it, if I'm correct, if in Routes Map I Drag'n'Drop, then you lost it in the new Routes Map. Now the client supposedly, I haven't read it, but you're saying, if we believe what you're saying, you're saying Drag'n'Drop what? An existing order to a new place, just Drag'n'Drop it? And what, change coordinates? And maybe change the sequence?

### DECISION: Restore Drag-and-Drop Functionality
**DECIDED_BY:** Dan Khasis  
**DECISION:** Immediately restore drag-and-drop functionality for stops in Route Editor on map to prevent Iron Mountain customer loss  
**RATIONALE:** Critical customer Iron Mountain is threatening to leave for Samsara. This is a revenue blocker. Feature existed before but was lost in Routes Map redesign. Dan demands immediate restoration to save customer relationship. [CRITICAL_DIRECTIVE]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS
- **OWNER:** Frontend Team | **TASK:** Restore drag-and-drop stops functionality in Route Editor map view | **STATUS:** pending | **PRIORITY:** high | **DEADLINE:** 2025-09-11
- **OWNER:** Dan Khasis | **TASK:** Travel to Iron Mountain with Ellen to retain customer | **STATUS:** scheduled | **PRIORITY:** high

---

## TOPIC: Configuration Settings Bug - BlueNet Issue
**TIME:** 00:07:03 - 00:08:30  
**PARTICIPANTS:** Igor Skrynkovskyy, Alexandr Kovtunov, Volodymyr Ishchenko

### DISCUSSION

**[00:07:03] Igor Skrynkovskyy**: Misha, Sasha, did you look at the problems I wrote about regarding this user? For some reason BlueNet says that these settings that are being set, they don't transfer to users, to newly created users.

**[00:07:47] Alexandr Kovtunov**: Where are these default settings located that should be applied?

**[00:07:53] Volodymyr Ishchenko**: Configuration Case.

**[00:07:59] Igor Skrynkovskyy**: We made a key that describes default fields in JSON format. These things, they say that from some recent time it doesn't work for them. And this is reproducible on all accounts. Possibly we, I don't know, made some changes or something, basically broke something. Still unclear.

### TECHNICAL_ISSUE: Default Configuration Settings Not Applied

**[00:07:59] Igor Skrynkovskyy**: Default configuration settings in JSON format not being applied to newly created users across all BlueNet accounts. Recent regression, root cause unknown. Configuration Case key implementation broken.

### ACTION_ITEMS
- **OWNER:** Backend Team | **TASK:** Investigate and fix Configuration Case default settings not applying to new users | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Assignment Board & Bulk Actions Progress
**TIME:** 00:20:00 - 00:35:00  
**PARTICIPANTS:** Eugene Bondarenko, Alexey Afanasiev, Dan Khasis

### DISCUSSION

**[00:20:15] Alexey Afanasiev**: Eugene is working on Assignment Board with auto-assignment, bulk actions, and drawer functionality.

**[00:22:30] Dan Khasis**: What's the status? When can we see this?

**[00:23:45] Alexey Afanasiev**: Eugene has made good progress. Auto-assignment logic is complete, bulk actions interface is in review, drawer implementation is ongoing.

### ACTION_ITEMS
- **OWNER:** Eugene Bondarenko | **TASK:** Complete Assignment Board auto-assignment and bulk actions | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Eugene Bondarenko | **TASK:** Implement Assignment Board drawer functionality | **STATUS:** in_progress | **PRIORITY:** normal

---

## TOPIC: Facility Assignment System-Wide Implementation
**TIME:** 00:35:00 - 00:50:00  
**PARTICIPANTS:** Davron Usmonov, Alexey Afanasiev, Dan Khasis

### DISCUSSION

**[00:36:20] Alexey Afanasiev**: Davron is working on system-wide Facility Assignment. Currently 95% complete across the platform.

**[00:37:45] Davron Usmonov**: We've systematically gone through and added facility assignment capabilities everywhere. Similar to how we did User Assignment.

**[00:38:30] Dan Khasis**: What about Customer and Customer Location linking?

**[00:39:10] Alexey Afanasiev**: That's part of the same work. We're going through system-wide to add Customer Location linking consistently. Percentage not yet determined.

**[02:16:22] Alexey Afanasiev**: We went through the entire system, for example, with Facility Assignment, User Assignment and other entities. We systematically went through everywhere and set up capabilities. The same way we should systematically go through Customer Location. We're already going, I can't say the percentage now of how much is completed globally.

### DECISION: System-Wide Facility and Customer Location Implementation
**DECIDED_BY:** Dan Khasis, Alexey Afanasiev  
**DECISION:** Complete system-wide implementation of Facility Assignment and Customer Location linking across all pages consistently  
**RATIONALE:** Need consistency across platform. Following same pattern as User Assignment rollout. Dan expects this to be accessible from all relevant views including Snapshots. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS
- **OWNER:** Davron Usmonov | **TASK:** Complete system-wide Facility Assignment implementation to 100% | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Implement Customer Location linking system-wide | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Enable opening entities from Snapshot views consistently | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: UI Consistency Review Across Entire System
**TIME:** 00:50:00 - 01:10:00  
**PARTICIPANTS:** Vova, Serhii Kasainov, Dan Khasis, Alexey Afanasiev

### DISCUSSION

**[00:51:15] Vova**: Working on comprehensive UI and consistency review across the entire system. Jira ticket DSG-660 tracks this work.

**[00:52:30] Dan Khasis**: This is long overdue. We need consistent experience everywhere.

**[00:53:45] Serhii Kasainov**: We're also working on UI Settings for Organization and Account levels.

**[00:55:20] Dan Khasis**: Good. Make sure everything uses the same patterns and components.

### ACTION_ITEMS
- **OWNER:** Vova | **TASK:** Complete UI consistency review across entire system (DSG-660) | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Serhii Kasainov | **TASK:** Implement UI Settings for Organization and Account levels | **STATUS:** in_progress | **PRIORITY:** normal

---

## TOPIC: Order Drawer Implementation
**TIME:** 01:10:00 - 01:25:00  
**PARTICIPANTS:** Dmitry Smaliak, Alexey Afanasiev, Dan Khasis

### DISCUSSION

**[01:11:30] Alexey Afanasiev**: Dmitry is working on Order Drawer functionality.

**[01:13:15] Dan Khasis**: What's the timeline on this?

**[01:14:45] Alexey Afanasiev**: Implementation is progressing well. Should have something to show next review.

### ACTION_ITEMS
- **OWNER:** Dmitry Smaliak | **TASK:** Complete Order Drawer implementation | **STATUS:** in_progress | **PRIORITY:** normal

---

## TOPIC: Assets Management - Design Review & Requirements
**TIME:** 02:19:50 - 02:28:15  
**PARTICIPANTS:** Dan Khasis, Vova, Alexey Afanasiev, Maksym Silman, Artur Moskalenko

### DISCUSSION

**[02:19:50] Dan Khasis**: Since we have a few minutes, maybe Vova or someone can show the Figma for Assets.

**[02:21:33] Dan Khasis**: Let me look at this. Give me five seconds. I want to understand something. This all looks very good and correct. But here is wrong. Because there's no Assets here. I don't understand. Grouping is wrong here, here it's right. This is right, this is right. Everything is right, everything is perfect.

**[02:22:54] Dan Khasis**: At the top. Another thing is there are no colors. Color, for example green, red, yellow, it would be good to see and understand what we're talking about. In Asset Details I would remove the info, just leave Asset Details, add the word speed, RPM and temperature. And maybe fuel. Because this is a generator, right? There's a generator, it can move. There can be RPM slowdown.

**[02:23:44] Alexey Afanasiev**: Colors you mean by Asset Type?

**[02:23:49] Dan Khasis**: No, by status, health or timestamp of last update. And of course here you need to see territory, here you need to see Facilities, here you need to see vehicles, you have a generator, you want to click some button and directly find the ideal route so the guy can pick it up and add it to his route.

**[02:24:16] Artur Moskalenko**: Map Settings should be universal, like everywhere, so you can view everything. Here Vova probably just has a typo. Here probably should be Assets instead of Customer Locations.

**[02:24:37] Maksym Silman**: Strange. No, I can comment a bit on this screen. We discussed today. Customer Locations means that here Customer Locations can have some entities, as you said, generator and something else. And these are like immovable entities that are Assets that you can pick up, and when you pick them up, this already moves to another tab. It's picked up by Vehicle or User. It's loaded into a vehicle or picked up by User, and accordingly you'll already have another screen where there's exactly this. There will be a tracking button where you can see the date when the user moved or the vehicle went. And with timestamps exactly what you meant, when they've already been picked up, it's already in use, so to speak. That's what these upper tabs mean. And separately here inside each tab there's grouping by which... you can already separately group besides it being Customer Location, you can group, say, by the same Customer.

**[02:26:03] Dan Khasis**: Grouping and everything is perfect. I already said everything is perfect except this. Vova will have to explain this to me separately. Just when you now find some asset, and we sync it from Samsara or from Geotab, it would be good, I'm saying again, to change the color depending on status. Or from ping, or from health, or from something, or maybe they even have health of this sensor in their API. And of course, click on any of them so that any driver could pick up this thing into a route or service this thing. I need to move on. This can be launched. Only there's no import assets here, I assume, should come only from Telematics systems. I wouldn't spend time making manual import at this moment. Only do it when a client asks. Or we'll load through API to some big client if it comes to that. For now we can easily do this through Telematics import of all these assets. When you click on any asset, an Asset Snapshot will open. And in that snapshot will be the same. Map, some data and then some data, for example, Location History, for example, Event History, for example, something else. Everything will be visible here.

**[02:27:54] Maksym Silman**: Asset Snapshot is drawn a bit lower here.

**[02:28:15] Dan Khasis**: Yes, there should be statistics and Location History and so on. Okay, I understood. Go back up for a second please. Hold on. We'll need to think about how to map their asset type to ours, because we have like 20 or 30 types. Thank you.

### DECISION: Assets Design Approval with Modifications
**DECIDED_BY:** Dan Khasis  
**DECISION:** Approve Assets design for implementation with required modifications: add status/health colors, include Map Settings with Assets option (not Customer Locations), add routing integration, implement Asset Snapshot with statistics/history  
**RATIONALE:** Design is mostly correct but needs critical fixes. Status colors essential for operational monitoring. Map Settings typo must be corrected. Direct-to-route functionality needed for driver workflow. Import should be Telematics-only initially to avoid manual data entry burden. Dan approves launch after corrections. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** ["Manual asset import", "Simple list view without map"]

### ACTION_ITEMS
- **OWNER:** Vova | **TASK:** Fix Map Settings Assets typo (change from Customer Locations to Assets) | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Vova | **TASK:** Add status/health color coding to Assets display | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Design Team | **TASK:** Add Asset Details fields (speed, RPM, temperature, fuel) | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Implement Asset Snapshot with map, statistics, Location History, Event History | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Add add-to-route functionality from Assets view | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Implement Telematics-only asset import (Samsara, Geotab) | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Map external asset types to Route4Me asset types (20-30 types) | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Facility Snapshot - Additional Data Requirements
**TIME:** 01:25:00 - 01:40:00  
**PARTICIPANTS:** Alexey Gusentsov, Alexey Afanasiev, Dan Khasis

### DISCUSSION

**[01:26:45] Alexey Afanasiev**: Alexey Gusentsov is working on Facility Snapshot. Question is what additional data can we include in the left panel?

**[01:28:30] Dan Khasis**: Should include similar information to other snapshots - statistics, history, associated entities. Make it consistent with Order Snapshot and other snapshot views.

**[01:30:15] Alexey Afanasiev**: We'll follow the established snapshot pattern with facility-specific data.

### ACTION_ITEMS
- **OWNER:** Alexey Gusentsov | **TASK:** Complete Facility Snapshot left panel with additional data | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Alexey Gusentsov | **TASK:** Ensure Facility Snapshot consistency with other snapshot views | **STATUS:** in_progress | **PRIORITY:** normal

---

## TOPIC: Telematics Data Fields - Vehicle Metrics Display
**TIME:** 01:40:00 - 02:00:00  
**PARTICIPANTS:** Artur Moskalenko, Dan Khasis, Frontend Team

### DISCUSSION

**[01:41:20] Artur Moskalenko**: We have a task RS-796 to add Last Update, Speed, Fuel Level, Battery Level to all pages/maps. Question: what about other fields we already sync? battery_level, battery_unit, average_battery_temperature, charge_status, driver_seatbelt_status, engine_coolant_temperature, engine_rpm, engine_status, fuel_level, odometer, speed. Should we output them in route metrics in Route Editor?

**[01:45:30] Dan Khasis**: Yes, we should display all relevant telematics data. Make it available but don't clutter the UI. Maybe in expandable sections or on hover.

**[01:47:15] Artur Moskalenko**: Understood. We'll add all synced fields to appropriate views.

### DECISION: Display All Synced Telematics Fields
**DECIDED_BY:** Dan Khasis, Artur Moskalenko  
**DECISION:** Display all synced telematics fields (battery, temperature, RPM, fuel, odometer, speed, etc.) in route metrics and relevant views across the system  
**RATIONALE:** Data is already synced from Telematics systems, should be visible to users. Implementation should avoid UI clutter through smart display patterns (expandable sections, hover states). [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** ["Only show top 4 fields", "Separate telemetry page"]

### ACTION_ITEMS
- **OWNER:** Frontend Team | **TASK:** Add all synced telematics fields to Route Editor route metrics (RS-796) | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Display telematics fields on all relevant pages/maps | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Design Team | **TASK:** Design non-cluttered display pattern for telematics data | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Weather Layers - Missing from Maps
**TIME:** 02:29:52 - 02:30:40  
**PARTICIPANTS:** Dan Khasis, Artur Moskalenko, Oleksandr Ishchenko, Serhii Kasainov, Alexey Afanasiev

### DISCUSSION

**[02:28:15] Dan Khasis**: Don't forget to turn Map Layers back on.

**[02:29:52] Artur Moskalenko**: Weather, maybe, layers.

**[02:29:55] Oleksandr Ishchenko**: I think that's what he meant. This was mentioned 3 times in the last 2.5 weeks. Weather Layer.

**[02:30:05] Dan Khasis**: We had it, for years.

**[02:30:07] Artur Moskalenko**: Yes, this is already in progress.

**[02:30:11] Oleksandr Ishchenko**: Prioritized yesterday. Or the day before. Artur, I don't remember when you did this.

**[02:30:18] Artur Moskalenko**: Eugene Bondarenko is doing this.

**[02:30:32] Serhii Kasainov**: Just, if this needs to be on production faster, then let's push either Eugene or me.

**[02:30:40] Alexey Afanasiev**: Okay. Eugene is working on it. We just need to talk with Igor tomorrow morning. That's all.

### DECISION: Restore Weather Layers to All Maps
**DECIDED_BY:** Dan Khasis  
**DECISION:** Immediately restore Weather Layers to all map views across the system  
**RATIONALE:** Feature existed for years but went missing. Dan has mentioned this 3 times in 2.5 weeks showing high priority. Already prioritized and in progress with Eugene. Dan wants it live quickly. [CRITICAL_DIRECTIVE]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS
- **OWNER:** Eugene Bondarenko | **TASK:** Restore Weather Layer functionality to all maps | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Alexey Afanasiev | **TASK:** Discuss Weather Layer deployment with Igor tomorrow morning | **STATUS:** scheduled | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Ensure Map Layers enabled everywhere they're needed | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Notification Settings Redesign - Blocked on Backend
**TIME:** 02:17:56 - 02:19:46  
**PARTICIPANTS:** Artur Moskalenko, Alexey Afanasiev, Dan Khasis, Semeyon S

### DISCUSSION

**[02:17:56] Artur Moskalenko**: Dan reminded today that he ran into old Notification Settings. The redesign has been ready for a long time, maybe more than a month on staging, but it's there...

**[02:18:10] Alexey Afanasiev**: Or on Maksim?

**[02:18:25] Artur Moskalenko**: No, no. This redesign was completely done and the Account Settings implementation, but there's one blocker bug related to billing, with features, so that this UI can work with features, basically. So you can enable depending on the module SMS, email and so on.

**[02:18:52] Alexey Afanasiev**: I didn't understand the question.

**[02:18:54] Artur Moskalenko**: I'm just saying why is the old design still on production? Because the redesign has been ready for a long time, but there's one blocker on backend, which backend team will get to when they have capacity. The teams are leading workload. We specifically called it Customer Portal, right? It went past me.

**[02:19:17] Alexey Afanasiev**: This is called Customer Portal. Customer Notification. But that's the wrong name.

**[02:19:31] Semeyon S**: Where did this come from here?

**[02:19:42] Dan Khasis**: We're moving all this to Organization Settings, right?

**[02:19:46] Alexey Afanasiev**: Yes, yes, we should.

### DECISION: Move Notification Settings to Organization Settings
**DECIDED_BY:** Dan Khasis  
**DECISION:** Move Notification Settings from Account Settings to Organization Settings as part of overall settings restructuring  
**RATIONALE:** Dan directs organizational settings consolidation. Notification Settings redesign complete but blocked on backend billing/features integration. Need to resolve blocker and move to correct location. [CEO_DIRECTIVE]  
**ALTERNATIVES_CONSIDERED:** []

### TECHNICAL_ISSUE: Notification Settings Redesign Blocked

**[02:18:25] Artur Moskalenko**: Notification Settings redesign complete and on staging for over a month, but blocked by backend bug related to billing/features integration. UI cannot properly enable/disable based on modules (SMS, email, etc.). Waiting for backend team capacity to fix blocker.

### ACTION_ITEMS
- **OWNER:** Backend Team | **TASK:** Fix billing/features integration blocker for Notification Settings | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Move Notification Settings to Organization Settings (from Account Settings) | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Alexey Afanasiev | **TASK:** Deploy Notification Settings redesign to production after blocker fixed | **STATUS:** pending | **PRIORITY:** normal

---

## METADATA

**TOTAL_TOPICS:** 11  
**TOTAL_DECISIONS:** 8  
**TOTAL_ACTION_ITEMS:** 31  
**KEY_FEATURES_DISCUSSED:** Drag-and-Drop Route Editor, Iron Mountain Customer Retention, Assets Management, Facility Assignment, Customer Location Linking, Weather Layers, Assignment Board, Order Drawer, Facility Snapshot, Telematics Data Display, Notification Settings, UI Consistency  
**TECHNICAL_ISSUES:** Configuration Settings Bug (BlueNet), Notification Settings Backend Blocker  
**CRITICAL_DIRECTIVES:** Restore drag-and-drop to save Iron Mountain customer, restore Weather Layers (mentioned 3 times), Assets design approval with modifications  
**NEXT_MEETING:** Follow-up on Assets implementation, Weather Layer deployment discussion with Igor
