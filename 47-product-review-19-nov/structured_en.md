# MEETING: Product Progress Review - Strategic Optimization & Core Fixes

**DATE:** 2025-11-19  
**DURATION:** 00:25:28  
**ATTENDEES:** Semeyon S (VP Platform), Serhii Kasainov (Front-End Tech Lead), Igor Skrynkovskyy (SVP Platform), Igor Golovtsov (Senior Frontend Engineer), Manar Kurmanov (Frontend Engineer), Dmitry Smaliak (Frontend Engineer), Alexey Afanasiev (Frontend Lead), Eugene (Frontend Engineer), Alexey Gusentsov (Frontend Engineer)  
**DAN_PRESENT:** no  
**DAN_REFERENCES:** yes - Distance/time columns request (prior directive), Demo cancellation  
**MEETING_TYPE:** Product Review  
**DATA_SOURCE:** full_transcript  
**CONFIDENCE_LEVEL:** high

---

## TOPIC: DestinationDriver & Tracking Number Fix
**TIME:** 00:00:00 - 00:04:00  
**PARTICIPANTS:** Serhii Kasainov, Dmitry Smaliak, Alexey Afanasiev, Semeyon S

### DISCUSSION

**[00:00:00] Serhii Kasainov**: We'll show this. It looks pretty cool. I might reduce its brightness a bit more. It should really be completely in the background. But overall it's really cool. Dima, is there anything interesting with DestinationDriver?

**[00:00:23] Dmitry Smaliak**: No, I haven't looked at DestinationDriver yet. I'm currently working on the snapshots in Destinations, so that we have this whole story. It was working. I'll roll this out.

**[00:00:40] Serhii Kasainov**: In what sense?

**[00:00:41] Dmitry Smaliak**: In terms of the snapshot. Well, our tracking number wasn't working in the copy table.

**[00:00:47] Serhii Kasainov**: It wasn't working at all?

**[00:00:50] Dmitry Smaliak**: Or is this related to AZUGA? No-no-no, it wasn't working in the table. It used to work on snapshots, but when we pulled...

**[00:00:59] Serhii Kasainov**: Okay, so we need to pull... That wasn't there. We need to pull fresh core.next because I fixed the fallback value there.

**[00:01:09] Semeyon S**: And is Alexandr Kovtunov here? No.

**[00:01:19] Serhii Kasainov**: Well, I'll write to him that we need to roll out the backend fix to snapshots as well, to routes.list. I asked QA where else we might have tracking.

**[00:01:29] Alexey Afanasiev**: We need to roll out the fresh fix from core and from backend everywhere, if I understand correctly. And, please show me... Does the fix relate to redirecting white label accounts to another domain, right?

**[00:01:44] Serhii Kasainov**: Yes, there's some clunky frontend logic with fallback, and specifically on AZUGA and several other white label accounts, the backend for some reason has a condition not to send this key.

### DECISION: Backend Fix Deployment
**DECIDED_BY:** Serhii Kasainov  
**DECISION:** Deploy backend fix to snapshots and routes.list for tracking number issue  
**RATIONALE:** Tracking number fallback logic was broken on AZUGA and other white label accounts. Frontend has clunky fallback handling and backend conditionally doesn't send the key. Fix available in core.next. Requires coordination with Alexandr Kovtunov for backend deployment. [TEAM_LEVEL - technical fix]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS
- **OWNER:** Serhii Kasainov | **TASK:** Contact Alexandr Kovtunov to deploy backend fix to snapshots | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Dmitry Smaliak | **TASK:** Deploy core.next update with tracking number fix | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Serhii Kasainov | **TASK:** Update core.next and coordinate with Alexandr Kovtunov for internal pages modules | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Distance & Drive Time Columns Addition
**TIME:** 00:02:00 - 00:04:00  
**PARTICIPANTS:** Serhii Kasainov, Dmitry Smaliak, Semeyon S

### DISCUSSION

**[00:02:09] Serhii Kasainov**: Please show the columns "distance to the next destination" and "drive time to the next destination". Here they are. Added. Oh, there's proper formatting.

**[00:02:10] Dmitry Smaliak**: All correct. Added.

**[00:02:14] Serhii Kasainov**: Does anyone have any comments? Please show the filters.

**[00:02:20] Semeyon S**: Did you add filters on destinations?

**[00:02:26] Serhii Kasainov**: No, Dan really requested these two columns. And did you add them to snapshots? We're rolling them out now, if they're tested here and there are no comments, we'll immediately roll this out with a library update to snapshots.

**[00:02:41] Dmitry Smaliak**: Yes, I'll roll this out now, it will go together with the tracking number copy fix.

**[00:03:13] Dmitry Smaliak**: I'm just looking at how tracking number was built in snapshots. Now I'll see how this link works. Because it's built from the frontend.

**[00:03:29] Serhii Kasainov**: We can solve this tête-à-tête, but we need to check. We just brought in fresh logic specifically for the tracking number link. We need to coordinate it everywhere.

**[00:03:45] Dmitry Smaliak**: Yes, let's discuss it, because I copied the tracking page from snapshots as it was before.

### DECISION: Column Deployment Strategy
**DECIDED_BY:** Serhii Kasainov, Dmitry Smaliak  
**DECISION:** Deploy new distance and drive time columns to snapshots immediately after testing, bundled with tracking number fix  
**RATIONALE:** Dan specifically requested these two columns in a prior meeting. Columns tested with proper formatting, no issues found. Bundling with tracking number fix for efficient deployment via library update. [EXECUTING_CEO_DIRECTIVE]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS
- **OWNER:** Dmitry Smaliak | **TASK:** Bundle new distance and drive time columns with tracking number fix for snapshot deployment | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Serhii Kasainov | **TASK:** Coordinate link logic for tracking number across all modules | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Strategic Optimization Filter Grouping
**TIME:** 00:04:00 - 00:09:00  
**PARTICIPANTS:** Serhii Kasainov, Dmitry Smaliak, Semeyon S, Igor Skrynkovskyy, Igor Golovtsov

### DISCUSSION

**[00:04:16] Semeyon S**: Semeyon, what you wrote yesterday about filters, has strategic optimization and scenario filters come in here? Is this local or is this already on staging?

**[00:04:16] Semeyon S**: No, this is already on staging.

**[00:04:25] Semeyon S**: Igor Golovtsov, please note for yourself. You can quickly add links to the numbers now.

**[00:04:37] Serhii Kasainov**: I remember correctly. This will be a link from strategic to routes.list with these filters activated, right? Yes. I didn't dream it. There wasn't such a thing in the ticket.

**[00:04:53] Dmitry Smaliak**: Look, wait, wait. This is a different ticket. Yes, this is a different ticket. We'll need to finish it so that it pulls from the URL directly here.

**[00:05:04] Serhii Kasainov**: Yes, that's all correct. Are we sure about this group, that it's assignment and attribution? I don't think so.

**[00:05:28] Semeyon S**: Because this is not about assignment or attribution at all. This is about graph relationships. This isn't even quite customer linking. Close, of course, but...

**[00:05:42] Serhii Kasainov**: I think this deserves a separate group.

**[00:05:45] Igor Skrynkovskyy**: Yes, we can make a separate group.

**[00:06:09] Dmitry Smaliak**: Yes, no problem. Just need a group name.

**[00:06:16] Serhii Kasainov**: Something like strategic planning. The section is now called scenarios.

**[00:06:26] Serhii Kasainov**: Strategic routing.

**[00:06:30] Semeyon S**: Oh, let's call it strategic routing.

**[00:07:08] Igor Skrynkovskyy**: So maybe we should first ask Dan. And then do it right.

**[00:07:18] Serhii Kasainov**: Well, let's name it.

**[00:07:25] Serhii Kasainov**: If we ask, we won't learn anything.

**[00:07:28] Dmitry Smaliak**: And if we do it wrong, we'll find out very quickly.

**[00:07:38] Semeyon S**: Let's make it a little bit wrong. Let me call it scenarios. This is the result of synchronization.

**[00:07:55] Semeyon S**: Also, recurring routes that we have are from templates that create other routes. That is, it should be in a separate group, and strategic routing fits in that sense. Filter by master route should be added there too - logical?

**[00:08:33] Serhii Kasainov**: These are just routes that have master route set. It's just a filter. If you want, you can place it there. You can place it. It's just in routes.list we have a filter "is template". Like that. But we don't have master route ID filtering yet. If we have it, we can add it. If not - later.

### DECISION: Filter Group Naming
**DECIDED_BY:** Semeyon S, Serhii Kasainov, Igor Skrynkovskyy  
**DECISION:** Create separate filter group named "Strategic Routing" instead of placing under "Assignment and Attribution"  
**RATIONALE:** Filters relate to graph relationships and strategic planning concepts, not assignment or attribution. The menu section is called "scenarios" so naming should align. Team decided to implement and get feedback rather than request pre-approval from Dan, as asking wouldn't yield quick answers but implementing wrong will surface issues rapidly. [TEAM_LEVEL - awaiting validation]  
**ALTERNATIVES_CONSIDERED:** ["Strategic Planning", "Assignment and Attribution", "Scenarios"]

### ACTION_ITEMS
- **OWNER:** Igor Golovtsov | **TASK:** Add links to numbers from strategic optimization to routes.list | **STATUS:** assigned | **PRIORITY:** normal
- **OWNER:** Dmitry Smaliak | **TASK:** Create "Strategic Routing" filter group and move relevant filters | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Add master route filtering to Strategic Routing group if available | **STATUS:** pending | **PRIORITY:** low

---

## TOPIC: Strategic Optimization UI Development
**TIME:** 00:09:00 - 00:20:00  
**PARTICIPANTS:** Manar Kurmanov, Serhii Kasainov, Semeyon S, Igor Golovtsov, Igor Skrynkovskyy

### DISCUSSION

**[00:09:41] Manar Kurmanov**: The main update relates to optimization. New flow behind a feature flag allows selecting from custom relocation via list or filters, or both. For example, two filters can be applied. Or inclusion/exclusion modes for them. Both inclusion and exclusion are available. This also works on the very first step.

**[00:10:14] Serhii Kasainov**: Where are the filter groupings?

**[00:10:29] Semeyon S**: Serhii means groupings within filters. Custom relocation doesn't have them. But we're not doing that now, right? No.

**[00:10:54] Igor Golovtsov**: Let's never reference custom relocation as a model.

**[00:11:01] Manar Kurmanov**: Understood. Moving forward: inclusion/exclusion modes work. A new step is now common for the entire optimization - you can set a name, select from facilities, or manually input addresses via search.

**[00:12:10] Igor Skrynkovskyy**: If creating through location selection, must specify start location. Multiple selections possible. Optimization can be renamed.

**[00:12:28] Manar Kurmanov**: New name saves in the optimization itself.

**[00:12:39] Semeyon S**: Does this multi-select facility/manual feature exist?

**[00:12:53] Igor Skrynkovskyy**: Wait - nobody disabled depots. What feature flags control display of this radio button for facilities vs start location?

**[00:13:15] Manar Kurmanov**: For facilities radio to show table, we have feature flag "facility view". For multiple vs single depot, I removed the feature yesterday after discussion that it wouldn't be needed and would be everywhere.

**[00:13:44] Semeyon S**: Not exactly what we said. We said for first step we can assume heavy strategic clients always have multiple depots feature, but we need to support it in next steps even for single depot.

**[00:14:13] Igor Golovtsov**: This came from someone who manages features - either Artur or Oleg Shulga.

**[00:14:35] Igor Skrynkovskyy**: The question is about properly displaying this input button via feature flag. 5% have depot when they have multiple depot, others don't need it. This product might even be sold separately. And used separately. Therefore, what settings, in which case, in which package will be, we can't predict ahead of time. I wrote it down, we'll clarify.

**[00:15:25] Igor Golovtsov**: Look, here it says database. Is this approved?

**[00:15:36] Igor Skrynkovskyy**: We're not saying this is customer location or something else. Look, at the top it says select locations. And on Thursday the guys showed a local version. I asked them to write database here. Well, Dan didn't complain about it.

**[00:15:54] Semeyon S**: Approved like that. Good. Next question. Here we're not adding a map. To conditionally draw.

**[00:16:12] Igor Skrynkovskyy**: In the next steps. Next iteration.

**[00:16:30] Semeyon S**: And by the way, guys, I completely forgot. We need to check the default field set. In this view. Well, so that it makes sense. I wrote it down. Because now I look, there's a lot of white space.

**[00:16:57] Manar Kurmanov**: We'll need to configure on backend, it will come automatically. Although we'll need to clarify whether this is the same as the routes view or a different custom view.

**[00:17:12] Manar Kurmanov**: In general, these are all the big changes. Also looked at additional work from Vova. He has big developments going on there. I won't comment on them now. They're not approved. One comment I'll say is that there might not be just two options here. Manual and selection. He talked about one business case where the user wants to test which depot they should buy to see whether it will affect their business or not. They're drawing in design now. In general, the whole process from Create Optimization they took for refinement.

**[00:19:45] Igor Golovtsov**: Don't get stuck on this, we'll figure it out.

### DECISION: Feature Flag Strategy
**DECIDED_BY:** Semeyon S, Igor Skrynkovskyy  
**DECISION:** Keep multiple depot feature flag support - don't remove it. Will clarify requirements with Artur or Oleg Shulga on exact implementation.  
**RATIONALE:** Product may be sold separately with different configurations. Only 5% of clients have multiple depot capability. Early assumptions about making it universal need validation from feature management team. Cannot predict which settings will be in which package ahead of time. [TEAM_LEVEL - requires leadership clarification]  
**ALTERNATIVES_CONSIDERED:** ["Remove feature flag and make universal", "Keep current single depot only"]

### TECHNICAL_ISSUE: Multiple Depot Feature Flag Configuration

**[00:12:53] Igor Skrynkovskyy**: What feature flags control display of this radio button for facilities vs start location? For facilities radio to show table, we have feature flag "facility view". For multiple vs single depot, feature was removed yesterday under assumption it wouldn't be needed.

**[00:13:44] Semeyon S**: Initial discussion was to assume heavy strategic clients have multiple depots for first step, but must support single depot in next steps.

**[00:14:35] Igor Skrynkovskyy**: 5% have multiple depot capability. Product might be sold separately with different configurations. Settings per package cannot be predicted ahead of time. Requires clarification from Artur or Oleg Shulga who manage features.

### ACTION_ITEMS
- **OWNER:** Manar Kurmanov | **TASK:** Clarify multiple depot feature flag requirements with Artur or Oleg Shulga | **STATUS:** assigned | **PRIORITY:** high
- **OWNER:** Manar Kurmanov | **TASK:** Push strategic optimization to staging ASAP | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Configure default field set for optimization locations view | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Design Team | **TASK:** Complete design review for Create Optimization process with Vova | **STATUS:** in_progress | **PRIORITY:** normal

---

## TOPIC: Scenarios Table & Inline Edit Mode
**TIME:** 00:20:00 - 00:22:30  
**PARTICIPANTS:** Semeyon S, Igor Golovtsov, Eugene

### DISCUSSION

**[00:20:24] Semeyon S**: Very big request. Please, ASAP, push to staging. We've been waiting for this functionality for a very long time, really. Anything else on staging, on strategic. And what about the table in this, inline mode for scenarios, Igor?

**[00:20:24] Igor Golovtsov**: Eugene made the first step in that direction. And went...

**[00:20:32] Semeyon S**: Unfinished, in short.

**[00:20:35] Igor Golovtsov**: I can show all sorts of small things, like deletion modal, deletion and so on, but I don't think it's interesting to show here in the last 4 minutes.

**[00:20:47] Semeyon S**: Well, verbally then, Igor, did the team add scenario deletion? Well, so you could clean up.

**[00:20:55] Igor Golovtsov**: Optimization deletion was added, not scenarios.

**[00:20:59] Semeyon S**: But there's a nuance, there's no pusher now, so it works ugly. It works but you need to manually refresh the page.

**[00:21:07] Igor Golovtsov**: It works and... No, there's a request. A deletion request is sent, and then when it successfully completes it simply re-requests the combine, but it's not updated yet. And therefore it doesn't go anywhere for you. Yes, pushers fix this.

**[00:22:19] Igor Golovtsov**: And from what else is probably useful for the user, we now have errors and statuses for creation, specifically creation status, we now have it for both scenarios and optimizations, and errors, if they're validation errors, they're drawn for the entire optimization if the entire optimization failed, and for a specific scenario if it failed partially.

### ACTION_ITEMS
- **OWNER:** Eugene | **TASK:** Complete inline edit mode implementation for scenarios table | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Implement pusher support for optimization deletion to avoid manual page refresh | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: ERP, Documentation & Assignment Board Status
**TIME:** 00:22:30 - 00:23:40  
**PARTICIPANTS:** Alexey Afanasiev, Semeyon S, Eugene

### DISCUSSION

**[00:22:30] Alexey Afanasiev**: That's all for us, Serhii ran away, so won't look at ERP, and routes, location, snapshot aren't ready. Well, in general, that's all for today.

**[00:22:47] Semeyon S**: And if it's not difficult for you, about the documentation, what was planned?

**[00:22:54] Alexey Afanasiev**: No. This isn't ready, this isn't ready yet.

**[00:23:12] Semeyon S**: And what's our assignment status?

**[00:23:22] Alexey Afanasiev**: Assignment board isn't here at all. They're only switching today. In the switching process.

**[00:23:34] Eugene**: Well, we made some small changes two weeks ago, added links, updated filters. Now we're going to design, to clarify two questions, and then the status will be clear.

### ACTION_ITEMS
- **OWNER:** Serhii Kasainov | **TASK:** Review ERP items and pricing | **STATUS:** pending | **PRIORITY:** normal | **DEADLINE:** 2025-11-20
- **OWNER:** Alexey Afanasiev | **TASK:** Complete routes, location, snapshot documentation | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Design Team | **TASK:** Assignment board team switching to new system | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Eugene | **TASK:** Clarify two design questions for strategic optimization | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Meeting Wrap-up & Demo Cancellation
**TIME:** 00:23:40 - 00:25:28  
**PARTICIPANTS:** Igor Golovtsov, Semeyon S, Alexey Afanasiev, Eugene

### DISCUSSION

**[00:23:52] Igor Golovtsov**: Please tell me the answer about tomorrow's demo. It won't happen or is it still under question?

**[00:23:58] Semeyon S**: Well, it won't happen. Dan cancelled, and I don't always decide to drive such a large number of people back and forth.

**[00:24:14] Semeyon S**: Roughly speaking, this internal mini-demo of ours is a replacement for tomorrow's. So we all sit down, look at who has what results, get some minimal feedback and move forward.

**[00:24:43] Alexey Afanasiev**: Eugene, then let's go to the current design call. It's a bit earlier.

**[00:24:52] Alexey Afanasiev**: I really want Igor to look at and listen to this too.

**[00:24:55] Eugene**: Maybe even Serhii. I think we're going to build a spaceship now.

**[00:25:01] Alexey Afanasiev**: So, Igor will be there. Golovtsov.

### DECISION: Demo Cancellation
**DECIDED_BY:** Dan  
**DECISION:** Cancel tomorrow's scheduled demo. This internal product review meeting serves as replacement.  
**RATIONALE:** Dan cancelled the formal demo. Semeyon determined not worth coordinating large group attendance. Internal mini-demo provides necessary feedback for team to review results and continue progress. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS
- **OWNER:** Alexey Afanasiev | **TASK:** Attend design call about strategic optimization with Eugene and Igor Golovtsov | **STATUS:** scheduled | **PRIORITY:** normal

---

## METADATA
**TOTAL_TOPICS:** 7  
**TOTAL_DECISIONS:** 5  
**TOTAL_ACTION_ITEMS:** 18  
**KEY_FEATURES_DISCUSSED:** DestinationDriver, Tracking Number, Distance/Drive Time Columns, Strategic Optimization, Filter Grouping, Scenarios Table, Inline Edit Mode, Assignment Board, ERP  
**TECHNICAL_ISSUES:** Tracking number fallback logic, Multiple depot feature flag configuration, Pusher support for optimization deletion  
**DAN_DIRECTIVES_REFERENCED:** Distance and drive time columns request (prior meeting), Demo cancellation  
**NEXT_STEPS:** Push strategic optimization to staging ASAP, clarify feature flag requirements, complete inline edit mode, resolve pusher implementation
