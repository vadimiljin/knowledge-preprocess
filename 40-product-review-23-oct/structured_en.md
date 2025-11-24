# MEETING: Product Review - Critical Facilities Issue & Strategic Planner Evolution

**DATE:** 2025-10-23  
**DURATION:** 03:45:56  
**ATTENDEES:** Dan Khasis (CEO), Semeyon S. (VP Platform), Artur Moskalenko (QA Director), Alex Shulga (QA), Vova (UI/UX), Serhii Kasainov (Frontend Lead), Igor Golovtsov (Senior Frontend Engineer), Dmitry Smaliak (Frontend Engineer), Davron Usmonov (Frontend Engineer), Alexey Afanasiev (Frontend Lead), Alexey Gusentsov (Frontend Engineer), Artem Klopov (Backend Engineer), Alexander Dylevskiy, Oleg Pravyk (QA), Vladyslav Feshchenko (QA)  
**DAN_PRESENT:** yes  
**MEETING_TYPE:** Product Review  
**DATA_SOURCE:** full_transcript + summary  
**CONFIDENCE_LEVEL:** high

---

## TOPIC: Critical Facilities Attribution Issue for Matthews Client

**TIME:** 00:00:45 - 00:15:10, 00:44:11 - 01:01:45  
**PARTICIPANTS:** Dan Khasis, Artur Moskalenko, Alex Shulga, Semeyon S., Artem Klopov

### DISCUSSION

**[00:00:45] Artur Moskalenko:** We have a critical issue with facilities for one of our top-3 clients, Matthews. Routes lost their facility attribution after we removed the automatic assignment mechanism.

**[00:05:20] Alex Shulga:** Previously, routes were automatically linked to the facility of whoever created them. We removed this because one user could be associated with multiple facilities, causing incorrect attribution of multiple facilities to a single route.

**[00:10:30] Dan Khasis:** Let me explain the business context. This is critical. Each facility for this client is a separate legal entity. Wrong facility attribution makes correct billing impossible, which "blows up their entire accounting."

**[00:12:45] Dan Khasis:** The old automatic binding mechanism was initially incorrect, but the problem only became obvious when the client had more than one facility. The main current problem is the impossibility of automatic facility attribution when uploading routes via file import.

**[00:15:10] Artur Moskalenko:** I'm concerned that we erased all historical attributes, which is a serious problem for the client.

**[00:44:11] Dan Khasis:** We need to implement fallback logic. Here's the hierarchy for automatic facility determination when not explicitly specified: First priority - facility of assigned user or driver. Second - facility of assigned vehicle if driver has no facility. Third - facility of planner, lowest priority, only useful if planner is planning for themselves.

**[00:48:30] Alex Shulga:** What happens if we try to assign a user to a route with a facility they don't have access to?

**[00:49:15] Dan Khasis:** The system must issue a warning and offer solutions - either unlink the user or change the route's facility. We need validation on both frontend and backend.

**[00:55:20] Artem Klopov:** There's also a UI bug - facility grouping disappeared from the interface. I'll fix it.

### DECISION: Implement Facilities Fallback Logic

**DECIDED_BY:** Dan Khasis  
**DECISION:** Implement hierarchical fallback logic for automatic facility attribution with three-tier priority system  
**RATIONALE:** Matthews client (top-3 customer) cannot perform billing due to missing facility attribution. Each facility represents a separate legal entity requiring correct financial reporting. System must handle both file import and UI assignment scenarios. [CEO_APPROVED] This is a critical revenue blocker affecting client accounting operations.  
**ALTERNATIVES_CONSIDERED:** ["Keep manual-only assignment", "Single-tier fallback (driver only)", "Remove facility requirement"]

### DECISION: Add Facility Support to File Import

**DECIDED_BY:** Dan Khasis  
**DECISION:** Add functionality to specify facility for each route during file import  
**RATIONALE:** Currently impossible to set facility during bulk route import, forcing manual assignment for large datasets. This is the primary blocker for Matthews client workflow. [CEO_APPROVED] Urgent implementation required.  
**ALTERNATIVES_CONSIDERED:** []

### TECHNICAL_ISSUE: Historical Facility Data Loss

**[00:15:10] Artur Moskalenko:** All historical facility attributions were erased during the system change, creating data integrity issues for the client's historical reporting.

### TECHNICAL_ISSUE: Missing Facility Grouping in UI

**[00:55:20] Artem Klopov:** The facility grouping display disappeared from routes.list interface due to a recent bug. This makes it impossible for users to see routes organized by facility.

### ACTION_ITEMS

- **OWNER:** Artem Klopov | **TASK:** Fix UI bug causing facility grouping to disappear from interface | **STATUS:** assigned | **PRIORITY:** high | **DEADLINE:** 2025-10-25
- **OWNER:** Backend Team | **TASK:** Implement three-tier fallback logic for facility attribution (driver → vehicle → planner) | **STATUS:** assigned | **PRIORITY:** high | **DEADLINE:** 2025-10-30
- **OWNER:** Backend Team | **TASK:** Add facility field to file import functionality for routes | **STATUS:** assigned | **PRIORITY:** high | **DEADLINE:** 2025-10-30
- **OWNER:** Frontend Team | **TASK:** Add validation warning when assigning user to route with inaccessible facility | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Backend Team | **TASK:** Add backend validation for facility-user access conflicts | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Strategic Planner Architecture - Data Sets Concept

**TIME:** 01:32:56 - 02:03:41  
**PARTICIPANTS:** Dan Khasis, Semeyon S., Vova, Serhii Kasainov

### DISCUSSION

**[01:32:56] Vova:** How should users modify input data like service time for a location and rerun calculations?

**[01:35:20] Vova:** Changes should be made in the main location list, then optimization can be restarted.

**[01:38:45] Semeyon S.:** When changing data for a new scenario, the system should completely copy the previous state, creating a new independent version.

**[01:42:10] Dan Khasis:** We absolutely cannot force clients to upload millions of historical orders into the operational database. This would destroy performance. The Strategic Planner must work with "Data Sets" - temporary, isolated data collections.

**[01:48:30] Dan Khasis:** The system must allow uploading historical orders, not just locations, into cheap storage like Google BigQuery or Spanner. From this data, location attributes should be statistically calculated - visit frequency, average service time, days of week.

**[01:52:15] Dan Khasis:** I'm proposing a new entity - "Data Set" or "Snapshot". This will allow users to create datasets from different sources: filtered list from customer_locations, upload new file with potential customers, historical orders. Edit these datasets in a sandbox without affecting master data. Use these Data Sets as input for creating multiple planning scenarios.

**[01:56:40] Dan Khasis:** Versioning is critical. If scenario "B" is created based on scenario "A" with changed parameters, the user must see this dependency and understand exactly what was changed.

**[02:00:20] Dan Khasis:** We need to fix the metrics. There must be clear distinction between average per route and average per stop to correctly assess capacity utilization.

### DECISION: Implement Data Sets Architecture

**DECIDED_BY:** Dan Khasis  
**DECISION:** Architect system to work with Data Sets based on cheap data storage, separating strategic planning from operational database  
**RATIONALE:** Cannot force clients to load historical orders into operational database - will destroy performance and increase costs. Strategic planning requires analyzing large volumes of historical data to model scenarios. Data Sets provide isolated sandbox for what-if analysis without risking operational data. [CEO_APPROVED] This is strategic architectural direction for the product.  
**ALTERNATIVES_CONSIDERED:** ["Continue using operational database", "Use only location data without orders", "Build separate strategic planning product"]

### DECISION: Scenario Versioning and Dependency Tracking

**DECIDED_BY:** Dan Khasis  
**DECISION:** Implement versioning system showing parent-child relationships between scenarios with change tracking  
**RATIONALE:** Users need to understand how scenarios relate to each other and what specific parameters changed between versions for meaningful comparison. [CEO_APPROVED] Critical for what-if analysis value proposition.  
**ALTERNATIVES_CONSIDERED:** ["Independent scenarios only", "Simple copy without tracking"]

### DECISION: Improve Metrics Display for Clarity

**DECIDED_BY:** Dan Khasis  
**DECISION:** Rework metrics UI to clearly distinguish between total, average per route, and average per stop  
**RATIONALE:** Current metrics like "Average Route Cube" are ambiguous - unclear if referring to route average or stop average. Correct capacity assessment requires clear metric definitions. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS

- **OWNER:** Semeyon S. | **TASK:** Design Data Sets architecture using cheap storage (BigQuery/Spanner) separate from operational database | **STATUS:** assigned | **PRIORITY:** high | **DEADLINE:** 2025-11-15
- **OWNER:** Backend Team | **TASK:** Implement Data Sets entity for creating isolated datasets from multiple sources | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Create UI for Data Sets management - creation, editing, source selection | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Implement scenario versioning UI showing parent-child relationships and change tracking | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Redesign metrics display to clearly show total vs. per-route vs. per-stop values | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Build statistical calculation engine to derive location attributes from historical orders | **STATUS:** pending | **PRIORITY:** high

---

## TOPIC: Scatterplot Visualization for Strategic Optimization

**TIME:** 00:03:48 - 00:04:19  
**PARTICIPANTS:** Dan Khasis, Artur Moskalenko, Vova

### DISCUSSION

**[00:03:48] Dan Khasis:** We saw it beautiful, Vova drew it beautifully.

**[00:03:53] Artur Moskalenko:** And it will be approximately the same beautiful when there are 20-30-50 scenarios.

**[00:03:58] Dan Khasis:** When a person has 2-3 scenarios, it's ugly there. We need to show this too. Admit honestly, this time did you see that what Vova drew turned into 100% what Vova drew?

### DECISION: Show Scatterplot with Limited Data

**DECIDED_BY:** Dan Khasis  
**DECISION:** Display scatterplot visualization even when user has only 2-3 scenarios to demonstrate how it appears with limited data  
**RATIONALE:** Important to show realistic visualization behavior, not just ideal state with 30+ scenarios. Users need to understand how tool performs with their actual data volume. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** ["Only show when sufficient data", "Use radar chart instead"]

### ACTION_ITEMS

- **OWNER:** Frontend Team | **TASK:** Implement scatterplot that displays gracefully with 2-3 scenarios minimum | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: UI/UX Improvements - Maps, Timeline, and Export

**TIME:** 02:23:42 - 03:05:35  
**PARTICIPANTS:** Dan Khasis, Serhii Kasainov, Igor Golovtsov, Vova

### DISCUSSION

**[02:23:42] Serhii Kasainov:** Fixed map shifting issues, improved layout, implemented drag-and-drop for locations to map and timeline.

**[02:26:15] Vova:** Concerned that drag-and-drop without preview and validation could cause serious route errors - for example, adding an address from another continent.

**[02:28:30] Dan Khasis:** I agree with Vova. This functionality requires a sandbox or at minimum a modal window with change preview and explicit user confirmation. Must show how the action will affect the route.

**[02:31:45] Dan Khasis:** We should think about multi-window mode - dispatcher could see map and route list simultaneously on multiple monitors and drag tasks between them.

**[02:35:20] Igor Golovtsov:** Presenting updated export UI. Two options for preset control button placement: icons at top or text buttons at bottom.

**[02:37:40] Dan Khasis:** Insist on variant with buttons and text. Target audience is age 40-60, may not understand icon meanings. Make the export modal narrower and place buttons on right to save space.

**[02:42:15] Dan Khasis:** Critical deficiency - export must be hierarchical. When exporting scenario list, user must be able to export all nested routes and their stops so data is suitable for Excel analysis.

**[02:48:30] Serhii Kasainov:** Added columns with time in user timezone and route timezone. Technical issue with sorting and grouping if making route time the primary column.

**[02:50:45] Dan Khasis:** I approve the approach with multiple columns, but rename for clarity - for example, "Your Time" and "Route Time". Move timezone abbreviation into "Your Time" column header.

### DECISION: Require Preview Modal for Drag-and-Drop Operations

**DECIDED_BY:** Dan Khasis  
**DECISION:** Add modal window with preview and confirmation for drag-and-drop operations before executing changes  
**RATIONALE:** Drag-and-drop without validation could cause catastrophic routing errors such as adding addresses from wrong continent. Users need to see impact before confirming. [CEO_APPROVED] Safety-critical UI requirement.  
**ALTERNATIVES_CONSIDERED:** ["Immediate drag-and-drop", "Undo functionality only"]

### DECISION: Implement Hierarchical Export with Checkboxes

**DECIDED_BY:** Dan Khasis  
**DECISION:** Build hierarchical export allowing users to select data depth via checkboxes - scenarios, routes, stops  
**RATIONALE:** Current export only captures top-level data. Users need complete nested data for Excel analysis - exporting scenarios without their routes and stops makes data unusable for business intelligence. [CEO_APPROVED] Core data export requirement.  
**ALTERNATIVES_CONSIDERED:** ["Flat export only", "Separate exports per level"]

### DECISION: Use Text Buttons for Export UI

**DECIDED_BY:** Dan Khasis  
**DECISION:** Implement export UI with text buttons instead of icon-only interface  
**RATIONALE:** Target audience (age 40-60) may not understand icon meanings without text labels. Text improves accessibility and reduces learning curve. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** ["Icon-only interface", "Icons with tooltips"]

### DECISION: Rename Timezone Columns for Clarity

**DECIDED_BY:** Dan Khasis  
**DECISION:** Rename timezone columns to "Your Time" and "Route Time" with timezone abbreviation in "Your Time" header  
**RATIONALE:** Current naming is ambiguous. Clear naming improves user understanding and reduces support burden. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** []

### ACTION_ITEMS

- **OWNER:** Serhii Kasainov | **TASK:** Add modal window with preview and confirmation for drag-and-drop operations | **STATUS:** assigned | **PRIORITY:** high | **DEADLINE:** 2025-11-05
- **OWNER:** Igor Golovtsov | **TASK:** Implement export UI with text buttons instead of icons | **STATUS:** assigned | **PRIORITY:** normal | **DEADLINE:** 2025-11-01
- **OWNER:** Igor Golovtsov | **TASK:** Add hierarchical export with checkboxes for selecting data depth (scenarios/routes/stops) | **STATUS:** assigned | **PRIORITY:** high | **DEADLINE:** 2025-11-10
- **OWNER:** Serhii Kasainov | **TASK:** Rename timezone columns to "Your Time" and "Route Time" with abbreviation in header | **STATUS:** assigned | **PRIORITY:** low | **DEADLINE:** 2025-10-31
- **OWNER:** Serhii Kasainov | **TASK:** Research multi-window interface feasibility for dispatcher workflow | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Native Push Notifications for Mobile App

**TIME:** 03:11:15 - 03:19:48  
**PARTICIPANTS:** Dan Khasis, Serhii Kasainov, Backend Team, Mobile Team

### DISCUSSION

**[03:11:15] Serhii Kasainov:** Current notifications only work inside the open app, not in background mode.

**[03:12:30] Dan Khasis:** The lack of native push notifications makes the app "useless." A driver who closes the app won't learn about critical route changes, new messages, or cancellations.

**[03:14:45] Dan Khasis:** Use Uber as the benchmark - all key events are accompanied by instant notifications to the home screen. We need configurable notifications in Organization Settings - administrators must control which events trigger which channels: push, email, SMS.

**[03:17:20] Dan Khasis:** Critical notification scenarios: route change, new message from dispatcher, missed delivery of expensive equipment.

**[03:18:50] Dan Khasis:** Also need automatic message translation between driver, dispatcher, and customer if they speak different languages.

### DECISION: Implement Native Push Notifications

**DECIDED_BY:** Dan Khasis  
**DECISION:** Prioritize native push notification implementation for mobile app displaying in OS notification center  
**RATIONALE:** Current state is unacceptable - app provides no value if driver closes it and misses critical updates. Push notifications are table stakes for modern mobile logistics apps (see Uber). [CEO_APPROVED] High priority for mobile app value proposition.  
**ALTERNATIVES_CONSIDERED:** ["In-app notifications only", "Email notifications only"]

### DECISION: Create Notification Settings in Organization Settings

**DECIDED_BY:** Dan Khasis  
**DECISION:** Build UI in Organization Settings for managing notification types and delivery channels per event  
**RATIONALE:** Different organizations have different notification needs. Administrators must control which events trigger notifications and through which channels (push/email/SMS) to avoid notification fatigue while ensuring critical alerts reach users. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** ["Fixed notification rules", "Per-user settings only"]

### ACTION_ITEMS

- **OWNER:** Mobile Team | **TASK:** Implement native push notifications for iOS and Android displaying in notification center | **STATUS:** assigned | **PRIORITY:** high | **DEADLINE:** 2025-11-30
- **OWNER:** Backend Team | **TASK:** Integrate notification service (e.g., OneSignal) for push delivery management | **STATUS:** pending | **PRIORITY:** high
- **OWNER:** Frontend Team | **TASK:** Create notification settings UI in Organization Settings | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Build notification rule engine for event-to-channel mapping | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Custom Data and Color Coding System

**TIME:** 01:08:15 - 01:20:08  
**PARTICIPANTS:** Dan Khasis, Vova, Serhii Kasainov

### DISCUSSION

**[01:08:15] Dan Khasis:** There's no way to search locations by custom data. Show me all routes with more than 20 working hours and less than 4 - they should all be colored accordingly.

**[01:11:26] Vova:** There's a problem with color assignment - when one user assigns a color, another user looking at that color doesn't understand what it means. We should assign labels along with colors to communicate information between users.

**[01:12:09] Dan Khasis:** You're right, but this doesn't solve the problem that they've been happily using colors for years - their company has this established concept. We need to add another thing here - color coding rules or label sets. Administrators can manage this. But until we do this - unclear when it will all work out - we need to enable the hex color backend already has so they can select colors here. We can show on the map with a border to display their chosen color next to our entity color.

**[01:14:30] Dan Khasis:** We'll assign each entity its own shape and make color coding dynamic so for each entity the user can choose which parameter drives colorization. They can choose no colorization - entities will have their base color. Or they can say colorize by custom color, or by revenue, or by territory, or by facility - any object by any property can be colorized on the map.

**[01:18:50] Dan Khasis:** We need smart layering - if at a location's level there's both an order and a generator, 100% there will be. You have a customer, they have this building, and you service the generator here, the gas tank for generator fuel, do inspection of electrical panels servicing the generator, etc. Then an order comes for servicing electricity, gas, and generator. Now you have service time and service type: generator inspection, this inspection, that inspection - 5 minutes, 10 minutes, 20 minutes, all together 25 minutes service time.

### DECISION: Implement Dynamic Color Coding by Any Property

**DECIDED_BY:** Dan Khasis  
**DECISION:** Build dynamic colorization system where users can choose which property drives color coding per entity type  
**RATIONALE:** Users need to color code map entities by different business attributes - revenue, territory, facility, custom fields. System must support user-defined color rules while maintaining entity shape distinction. [CEO_APPROVED] Core map visualization requirement.  
**ALTERNATIVES_CONSIDERED:** ["Fixed color schemes only", "Color by entity type only"]

### DECISION: Add Label System with Colors

**DECIDED_BY:** Dan Khasis  
**DECISION:** Implement label sets in Organization Settings allowing administrators to define color-label combinations for company-wide use  
**RATIONALE:** Colors alone don't communicate meaning between users. Labels provide shared understanding of what colors represent. Solves collaboration problem while maintaining visual coding benefits. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** ["Colors only without labels", "Labels only without colors"]

### DECISION: Enable Interim Hex Color Selection

**DECIDED_BY:** Dan Khasis  
**DECISION:** Temporarily enable basic hex color selection before full color coding rules system is complete  
**RATIONALE:** Backend already supports hex colors. Users need basic color functionality immediately even if it's not the final ideal solution. Don't let perfect be enemy of good. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** ["Wait for complete system", "Remove color coding entirely"]

### ACTION_ITEMS

- **OWNER:** Frontend Team | **TASK:** Enable basic hex color selection for locations | **STATUS:** pending | **PRIORITY:** normal | **DEADLINE:** 2025-11-01
- **OWNER:** Frontend Team | **TASK:** Design and implement color coding rules system in Organization Settings | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Implement dynamic colorization allowing users to select property for color coding per entity | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Frontend Team | **TASK:** Build smart layering system for overlapping map entities | **STATUS:** pending | **PRIORITY:** low

---

## TOPIC: Organization Settings Refactoring

**TIME:** 01:02:10 - 01:04:30  
**PARTICIPANTS:** Dan Khasis, Vova

### DISCUSSION

**[01:02:10] Dan Khasis:** We need an elementary panel for classifying service types as a new thing in Organization Settings. We insert Service Types here. We can insert different types here.

**[01:03:24] Vova:** Then let them manually insert if they want - for a given service type I have a list of 10 arbitrary service types. If there are 10 here, there won't be a dropdown of 10, they're massively increasing. They'll have the ability to either hardcode or increase. They're now putting a new table, backend, backend, a separate table describing that for this location from such-and-such time to such-and-such time there were these service types with these many seconds.

**[01:04:30] Artur Moskalenko:** This is wrong, this is override. You need to make baseline, then you can override some fragments.

### DECISION: Add Service Types to Organization Settings

**DECIDED_BY:** Dan Khasis  
**DECISION:** Create Service Types management panel in Organization Settings for company-wide service type definitions  
**RATIONALE:** Service types need centralized definition at organization level. Allows standardization across planning processes while supporting custom per-location overrides. [CEO_APPROVED]  
**ALTERNATIVES_CONSIDERED:** ["Per-location service types only", "Hardcoded service types"]

### ACTION_ITEMS

- **OWNER:** Frontend Team | **TASK:** Design and implement Service Types panel in Organization Settings | **STATUS:** pending | **PRIORITY:** normal
- **OWNER:** Backend Team | **TASK:** Create service types database table with baseline and override support | **STATUS:** pending | **PRIORITY:** normal

---

## TOPIC: Comparison Routes Feature

**TIME:** Various segments  
**PARTICIPANTS:** Alexey Gusentsov, Dmitry Smaliak

### DISCUSSION

**[Various timestamps]:** Discussion of comparison routes functionality being developed by Alexey Gusentsov and Dmitry Smaliak. Feature allows side-by-side route comparison for analysis.

### ACTION_ITEMS

- **OWNER:** Alexey Gusentsov | **TASK:** Continue comparison routes feature development | **STATUS:** in_progress | **PRIORITY:** normal
- **OWNER:** Dmitry Smaliak | **TASK:** Support comparison routes feature implementation | **STATUS:** in_progress | **PRIORITY:** normal

---

## TOPIC: Activity Feed Updates

**TIME:** Brief mentions  
**PARTICIPANTS:** Alexey Afanasiev

### DISCUSSION

**[Brief mentions]:** Alexey Afanasiev working on Activity Feed improvements referenced in ticket R4MWEB-26294.

### ACTION_ITEMS

- **OWNER:** Alexey Afanasiev | **TASK:** Complete Activity Feed updates per R4MWEB-26294 | **STATUS:** in_progress | **PRIORITY:** normal

---

## METADATA

**TOTAL_TOPICS:** 11  
**TOTAL_DECISIONS:** 17  
**TOTAL_ACTION_ITEMS:** 32  
**KEY_FEATURES_DISCUSSED:** Facilities attribution, Strategic Planner, Data Sets architecture, Scatterplot visualization, Hierarchical export, Push notifications, Color coding system, Service types, Multi-window interface, Drag-and-drop with preview, Timezone handling  
**TECHNICAL_ISSUES:** Facilities data loss, Missing facility grouping, Background notifications, Color coding communication, Smart layering for overlapping entities  
**NEXT_MEETING:** Not specified
