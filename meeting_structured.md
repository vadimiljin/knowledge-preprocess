# MEETING: Team Sync - Route4Me Development
**DATE:** 2025-11-19  
**DURATION:** 00:25:28  
**ATTENDEES:** Serhii Kasainov, Dmitry Smaliak, Semeyon S, Alexey Afanasiev, Igor Skrynkovskyy, Manar Kurmanov, Igor Golovtsov, Eugene, Alexey Gusentsov

---

## TOPIC: DestinationDriver & Tracking Number Fix
**TIME:** 00:00:00 - 00:04:00  
**PARTICIPANTS:** Serhii Kasainov, Dmitry Smaliak, Alexey Afanasiev

### DISCUSSION
**[00:00:23] Dmitry Smaliak:** No progress on DestinationDriver yet. Currently working on fixing tracking number in Destinations snapshots - copy table tracking number was not working.

**[00:00:47] Serhii Kasainov:** Was it completely broken?

**[00:00:50] Dmitry Smaliak:** Not working in the table. Previously worked on snapshots, but broke after update.

**[00:00:59] Serhii Kasainov:** Need to pull fresh core.next - fixed fallback value there.

### DECISION: Backend Fix Deployment
**DECIDED_BY:** Serhii Kasainov  
**DECISION:** Deploy backend fix to snapshots and routes.list for tracking number issue  
**RATIONALE:** Tracking number fallback logic was broken on AZUGA and other white label accounts

### ACTION_ITEMS
- **OWNER:** Serhii Kasainov | **TASK:** Contact Kovtunov Aleksandr to deploy backend fix to snapshots | **STATUS:** pending
- **OWNER:** Dmitry Smaliak | **TASK:** Deploy core.next update with tracking number fix | **STATUS:** in_progress

---

## TOPIC: Distance & Drive Time Columns Addition
**TIME:** 00:02:00 - 00:04:00  
**PARTICIPANTS:** Serhii Kasainov, Dmitry Smaliak, Alexey Afanasiev

### DISCUSSION
**[00:02:09] Serhii Kasainov:** Requesting to show new columns - "distance to the next destination" and "drive time to the next destination"

**[00:02:10] Dmitry Smaliak:** Added them. Proper formatting is in place.

**[00:02:26] Serhii Kasainov:** Dan specifically requested these two columns. Need to add them to snapshots as well.

**[00:02:41] Dmitry Smaliak:** Will deploy this together with the tracking number fix via library update to snapshots.

### DECISION: Column Deployment Strategy
**DECIDED_BY:** Serhii Kasainov, Dmitry Smaliak  
**DECISION:** Deploy new columns to snapshots immediately after testing, bundled with tracking number fix  
**RATIONALE:** Dan requested these columns, no issues found in testing

### ACTION_ITEMS
- **OWNER:** Dmitry Smaliak | **TASK:** Bundle new columns with tracking number fix for snapshot deployment | **STATUS:** in_progress
- **OWNER:** Serhii Kasainov | **TASK:** Update core.next and coordinate with internal pages for modules | **STATUS:** pending

---

## TOPIC: Strategic Optimization Filter Grouping
**TIME:** 00:04:00 - 00:09:00  
**PARTICIPANTS:** Serhii Kasainov, Dmitry Smaliak, Semeyon S, Igor Skrynkovskyy, Igor Golovtsov

### DISCUSSION
**[00:04:16] Semeyon S:** Strategic optimization and scenario filters are now deployed to staging.

**[00:04:25] Semeyon S:** Igor Golovtsov, please add links to the numbers quickly.

**[00:04:37] Serhii Kasainov:** This will be a link from strategic to routes.list with these filters activated, correct?

**[00:05:04] Serhii Kasainov:** Are we sure this filter group should be "assignment and attribution"? I think not.

**[00:05:28] Semeyon S:** This is not about assignment or attribution at all - it's about graph relationships. Not quite customer linking, but close.

**[00:05:42] Serhii Kasainov:** I think this deserves a separate group.

**[00:06:16] Dmitry Smaliak:** Need a group name.

**[00:06:26] Serhii Kasainov:** Something like "strategic planning" - the section is now called "scenarios"

**[00:06:30] Semeyon S:** Let's call it "strategic routing"

### DECISION: Filter Group Naming
**DECIDED_BY:** Semeyon S, Serhii Kasainov, Igor Skrynkovskyy  
**DECISION:** Create separate filter group named "Strategic Routing" instead of placing under "Assignment and Attribution"  
**RATIONALE:** The filters relate to graph relationships and strategic planning, not assignment/attribution. Section is called "scenarios" in menu.  
**ALTERNATIVES_CONSIDERED:** ["Strategic Planning", "Assignment and Attribution"]

**[00:07:08] Igor Skrynkovskyy:** Maybe we should ask Dan first, then do it properly?

**[00:07:18] Serhii Kasainov:** Let's name it and see. If we ask, we'll get no answer.

**[00:07:28] Dmitry Smaliak:** If we do it wrong, we'll find out very quickly.

**[00:07:38] Semeyon S:** Let's do it slightly wrong. I'll call it "scenarios" - synchronization result.

**[00:08:33] Serhii Kasainov:** We also have recurring routes consisting of templates generating other routes. Strategic routing fits in that sense. Filter by master route should be added there too - logical?

### ACTION_ITEMS
- **OWNER:** Igor Golovtsov | **TASK:** Add links to numbers from strategic optimization | **STATUS:** assigned
- **OWNER:** Dmitry Smaliak | **TASK:** Create "Strategic Routing" filter group | **STATUS:** in_progress
- **OWNER:** Semeyon S | **TASK:** Confirm filter naming with Dan | **STATUS:** pending
- **OWNER:** Team | **TASK:** Add master route filtering to Strategic Routing group (if available) | **STATUS:** pending

---

## TOPIC: Strategic Optimization UI Development
**TIME:** 00:09:00 - 00:20:00  
**PARTICIPANTS:** Manar Kurmanov, Serhii Kasainov, Semeyon S, Igor Golovtsov, Igor Skrynkovskyy

### DISCUSSION
**[00:09:41] Manar Kurmanov:** Main update relates to optimization. New flow behind feature flag allows selecting from custom relocation via list or filters, or both.

**[00:10:14] Serhii Kasainov:** Where are filter groupings?

**[00:10:29] Semeyon S:** Serhii means groupings within filters. Custom relocation doesn't have them.

**[00:10:54] Igor Golovtsov:** Let's never reference custom relocation as a model.

**[00:11:01] Manar Kurmanov:** Understood. Moving forward: inclusion/exclusion modes work. New step is now common for entire optimization - can set name, select from facilities, or manually input addresses via search.

**[00:12:10] Igor Skrynkovskyy:** If creating through location selection, must specify start location. Multiple selections possible. Optimization can be renamed.

**[00:12:28] Manar Kurmanov:** New name saves in the optimization itself.

### TECHNICAL_ISSUE: Multiple Depot Feature Flag
**[00:12:39] Semeyon S:** Does this multi-select facility/manual feature exist?

**[00:12:53] Igor Skrynkovskyy:** Wait - nobody disabled depots. What feature flags control display of this radio button for facilities vs start location?

**[00:13:15] Manar Kurmanov:** For facilities radio to show table, we have feature flag "facility view". For multiple vs single depot, I removed the feature yesterday after discussion that it wouldn't be needed and would be everywhere.

**[00:13:44] Semeyon S:** Not exactly what we said. We said for first step we can assume heavy strategic clients always have multiple depots feature, but we need to support it in next steps even for single depot.

**[00:14:13] Igor Golovtsov:** This came from someone who manages features - either Artur or Oleg Shulga.

**[00:14:35] Igor Skrynkovskyy:** The question is about properly displaying this input button via feature flag. 5% have depot when they have multiply depot, others don't need it. This product might even be sold separately, so we can't predict which settings in which package ahead of time.

### DECISION: Feature Flag Strategy
**DECIDED_BY:** Semeyon S, Igor Skrynkovskyy  
**DECISION:** Keep multiple depot feature flag support - don't remove it. Will clarify with Artur/Oleg Shulga on exact requirements.  
**RATIONALE:** Product may be sold separately with different configurations. 5% have multiple depot capability. Early assumptions need validation.

**[00:15:25] Igor Golovtsov:** Is "database" as label approved?

**[00:15:36] Igor Skrynkovskyy:** Header says "select locations", and in Thursday demo I asked to write "database" here. Dan didn't complain - approved.

**[00:15:54] Semeyon S:** Are we adding a map here to draw conditionally?

**[00:16:12] Igor Skrynkovskyy:** Next iteration.

**[00:16:30] Semeyon S:** Need to check default field set in this view to make sense. Very white space heavy now.

**[00:16:57] Manar Kurmanov:** Need to configure on backend, it will come automatically. Need to verify if this is same as routes view or different custom view.

**[00:17:12] Manar Kurmanov:** These are the major changes. Also looked at additional work from Vova - big developments there. Won't comment as not approved yet. One comment: might not be just two options (manual and selection). He mentioned business case where user wants to test which depot to buy to see business impact - something like that. They're designing now.

**[00:19:45] Igor Golovtsov:** Don't get stuck on this, we'll figure it out.

### ACTION_ITEMS
- **OWNER:** Manar Kurmanov | **TASK:** Clarify multiple depot feature flag requirements with Artur/Oleg Shulga | **STATUS:** assigned | **PRIORITY:** high
- **OWNER:** Manar Kurmanov | **TASK:** Push strategic optimization to staging ASAP | **STATUS:** in_progress | **PRIORITY:** high
- **OWNER:** Team | **TASK:** Review and configure default field set for optimization view | **STATUS:** pending
- **OWNER:** Design Team (Vova) | **TASK:** Complete design review for Create Optimization process | **STATUS:** in_progress

---

## TOPIC: Scenarios Table & Inline Edit Mode
**TIME:** 00:20:00 - 00:22:30  
**PARTICIPANTS:** Semeyon S, Igor Golovtsov, Eugene

### DISCUSSION
**[00:20:24] Semeyon S:** What's the status on table inline mode for scenarios, Igor?

**[00:20:32] Igor Golovtsov:** Eugene made first step toward it, but incomplete.

**[00:20:35] Semeyon S:** Unfinished, in short.

**[00:20:47] Semeyon S:** Verbally then, Igor - did team add scenario deletion?

**[00:20:55] Igor Golovtsov:** Optimization deletion was added, not scenarios.

**[00:20:59] Semeyon S:** But there's a nuance - no pusher now, so works ugly. It works but need to manually refresh page.

**[00:21:07] Igor Golovtsov:** Request is sent for deletion, and when successfully completed it re-requests the combine, but it's not updated yet, so doesn't disappear. Pushers will fix this.

**[00:22:19] Igor Golovtsov:** Also useful: we now have creation status and errors for both scenarios and optimizations. Validation errors display for entire optimization if completely failed, or for specific scenario if partially failed.

### ACTION_ITEMS
- **OWNER:** Eugene | **TASK:** Complete inline edit mode implementation for scenarios | **STATUS:** in_progress
- **OWNER:** Backend Team | **TASK:** Implement pusher support for optimization deletion | **STATUS:** pending

---

## TOPIC: ERP & Assignment Board Status
**TIME:** 00:22:30 - 00:23:40  
**PARTICIPANTS:** Alexey Afanasiev, Semeyon S, Eugene

### DISCUSSION
**[00:22:30] Alexey Afanasiev:** Serhii left, so won't review ERP. Routes, location, snapshot not ready either. That's all for today.

**[00:22:54] Alexey Afanasiev:** Documentation not ready either. 

**[00:23:22] Alexey Afanasiev:** Assignment board status - not here at all, they're just switching today. In process.

**[00:23:34] Eugene:** For strategic, made small changes two weeks ago - added links, updated filters. Now going to design team to clarify two questions, then status will be clear.

---

## TOPIC: Meeting Wrap-up & Demo Cancellation
**TIME:** 00:23:40 - 00:25:28  
**PARTICIPANTS:** Igor Golovtsov, Semeyon S, Alexey Afanasiev, Eugene

### DISCUSSION
**[00:23:52] Igor Golovtsov:** What's the answer about tomorrow's demo?

**[00:23:58] Semeyon S:** Won't happen. Dan cancelled, and I don't want to move so many people around for it.

**[00:24:14] Semeyon S:** Basically, this internal mini-demo serves as replacement for tomorrow's demo. So we all sit together, look at results, get minimal feedback and move forward.

**[00:24:43] Alexey Afanasiev:** Eugene, let's join the current design call. Happens a bit earlier.

**[00:24:52] Eugene:** Let's wait until they finish with strategic.

**[00:24:55] Alexey Afanasiev:** I really want Igor to look at and listen to this too. Maybe even Serhii. I think we're about to build a spaceship.

**[00:25:01] Alexey Afanasiev:** Igor will be there - Golovtsov.

### DECISION: Demo Cancellation
**DECIDED_BY:** Dan, Semeyon S  
**DECISION:** Cancel tomorrow's demo. This internal sync serves as replacement.  
**RATIONALE:** Dan cancelled; not worth coordinating large group. Internal mini-demo provides necessary feedback to continue.

### ACTION_ITEMS
- **OWNER:** Alexey Afanasiev, Eugene, Igor Golovtsov | **TASK:** Attend design call about strategic optimization | **STATUS:** scheduled

---

## METADATA
**TOTAL_TOPICS:** 7  
**TOTAL_DECISIONS:** 6  
**TOTAL_ACTION_ITEMS:** 15  
**KEY_FEATURES_DISCUSSED:** DestinationDriver, Tracking Number, Distance/Drive Time Columns, Strategic Optimization, Filter Grouping, Inline Edit Mode, Assignment Board  
**TECHNICAL_ISSUES:** Tracking number fallback, Feature flag configuration, Pusher support  
**NEXT_MEETING:** Design call (same day, after this meeting)
