[TRANSLATION METADATA]
- Source: full_transcript
- Original Language: Russian + English technical terms
- Translation Date: 2024-11-24
- Transcript Accuracy: 92.7%
- Confidence Level: high
- Meeting Duration: 02:29:34
- Participants: 17

---

# Meeting Transcript (Summary)

**Date:** 2025-09-04 13:27
**Duration:** 02:29:34
**Participants:** 17
**Accuracy:** 92.7%

---

**[00:01:40] Dmitry Smaliak**: Hello everyone.

**[00:01:58] Maksym Silman**: Hello.

**[00:02:09] Serhii Kasainov**: Maksym, sorry, but I'll ask one last final time, honestly. Regarding Setin's account, there are three lines there, so that the page updates, can we finish this?

**[00:02:24] Maksym Silman**: Yes, please send an email.

**[00:02:26] Serhii Kasainov**: You already have an email, or should have, let me double-check again. User Setin SDP, yes.

**[00:02:35] Maksym Silman**: Yeah, yes, found it. Yes, I replied, please send.

**[00:02:57] Serhii Kasainov**: Thank you.

**[00:03:14] Davron Usmonov**: Alexey, quick moment, in our product document. Please look, the percentages are wrong. There's 80, 25.

**[00:03:25] Alexey Afanasiev**: We have some ending, looking. Really the product one? Yes, which. Ah, August 7th, I messed that up. Well.

**[00:03:33] Davron Usmonov**: Sorry, sorry, sorry. Yeah.

**[00:05:40] Igor Skrynkovskyy**: Hello everyone.

**[00:05:43] Kateryna Shevchenko**: Hello.

**[00:05:44] Oleksandr Ishchenko**: Hello.

**[00:05:47] Igor Skrynkovskyy**: Something with Zoom I constantly can't hear, turn on microphone. Hello everyone, if you didn't hear.

**[00:05:53] Vova**: Hearing perfectly, hello.

**[00:05:57] Igor Skrynkovskyy**: Until you fix it, it won't work. Now good, thanks.

**[00:06:03] Vova**: I have Slack working very similarly. Actually, the opposite, Zoom always works, but Slack always needs adjusting.

**[00:06:10] Igor Skrynkovskyy**: For me it's opposite, I constantly have problems with Zoom.

**[00:06:17] Oleksandr Ishchenko**: You say needs adjusting, how do you see the fixing action?

**[00:06:22] Vova**: Doesn't select the program, selects wrong audio device.

**[00:06:27] Oleksandr Ishchenko**: Ah, haven't had that in a long time, neither in Slack nor Zoom, everything works perfectly.

**[00:06:32] Igor Skrynkovskyy**: For me it selects the right device, but constantly resets the input volume slider to 30%. Constantly, with every call. Mac probably working. OS maybe.

**[00:06:53] Volodymyr Ishchenko**: Windows quirks.

**[00:06:56] Igor Skrynkovskyy**: This isn't Windows.

**[00:06:59] Volodymyr Ishchenko**: Windows-Slack, Windows-Zoom quirks, I think, because on Mac this really doesn't happen.

**[00:07:03] Igor Skrynkovskyy**: But I'm on Mac. Ah, damn. Misha, Sasha, did you look at the problems I wrote about regarding this user? For some reason BlueNet says that these settings that are being set, they don't transfer to users, to newly created users. I understand.

**[00:07:47] Alexandr Kovtunov**: Where are these default settings located that should be applied?

**[00:07:53] Volodymyr Ishchenko**: Configuration Case.

**[00:07:59] Igor Skrynkovskyy**: We made a key that describes default fields in JSON format. These things, they say that from some recent time it doesn't work for them. And this is reproducible on all accounts. Possibly we, I don't know, made some changes or something, basically broke something. Still unclear.

**[00:08:55] Dan Khasis**: Hello.

**[00:08:57] Vova**: Hello-hello.

**[00:09:07] Dan Khasis**: Let's start with the email that was written about Iron Mountain. Did you have a chance to read it?

**[00:09:23] Vova**: I haven't read it yet, if you copied me.

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

**[00:12:58] Igor Skrynkovskyy**: Ah, yes, yes, you're right.

**[00:13:05] Dan Khasis**: The reincarnation process. Anyway, we're competing with people who will never work infinitely. So in our situation, our thing is that you already implemented it, if I'm correct, if in Routes Map I Drag'n'Drop, then you lost it in the new Routes Map. Now the client supposedly, I haven't read it, but you're saying, if we believe what you're saying, you're saying Drag'n'Drop what? An existing order to a new place, just Drag'n'Drop it? And what, change coordinates? And maybe change the sequence?

[Content continues with technical discussion about drag-and-drop functionality, Iron Mountain issues, and various product features...]

**[02:26:03] Dan Khasis**: Grouping and everything is perfect. I already said everything is perfect except this. Vova will have to explain this to me separately. Just when you now find some asset, and we sync it from Samsara or from Geotab, it would be good, I'm saying again, to change the color depending on status. Or from ping, or from health, or from something, or maybe they even have health of this sensor in their API. And of course, click on any of them so that any driver could pick up this thing into a route or service this thing. I need to move on. This can be launched. Only there's no import assets here, I assume, should come only from Telematics systems. I wouldn't spend time making manual import at this moment. Only do it when a client asks. Or we'll load through API to some big client if it comes to that. For now we can easily do this through Telematics import of all these assets. When you click on any asset, an Asset Snapshot will open. And in that snapshot will be the same. Map, some data and then some data, for example, Location History, for example, Event History, for example, something else. Everything will be visible here.

**[02:27:54] Maksym Silman**: Asset Snapshot is drawn a bit lower here.

**[02:28:15] Dan Khasis**: Yes, there should be statistics and Location History and so on. Okay, I understood. Go back up for a second please. Hold on. We'll need to think about how to map their asset type to ours, because we have like 20 or 30 types. Thank you. Don't forget to turn Map Layers back on.

**[02:29:52] Artur Moskalenko**: Weather, maybe, layers.

**[02:29:55] Oleksandr Ishchenko**: I think that's what he meant. This was mentioned 3 times in the last 2.5 weeks. Weather Layer.

**[02:30:05] Dan Khasis**: We had it, for years.

**[02:30:07] Artur Moskalenko**: Yes, this is already in progress.

**[02:30:11] Oleksandr Ishchenko**: Prioritized yesterday. Or the day before. Artur, I don't remember when you did this.

**[02:30:18] Artur Moskalenko**: Eugene Bondarenko is doing this.

**[02:30:32] Serhii Kasainov**: Just, if this needs to be on production faster, then let's push either Eugene or me.

**[02:30:40] Alexey Afanasiev**: Okay. Eugene is working on it. We just need to talk with Igor tomorrow morning. That's all. Let's wrap up.

**[02:31:00] Dan Khasis**: Goodbye, thank you. Turn on layers everywhere they're needed. Goodbye.

**[02:31:07] Alexey Afanasiev**: Bye-bye.

**[02:31:10] Artur Moskalenko**: Yes, bye.

**[02:31:12] Dmitry Smaliak**: Goodbye everyone.

---

## Statistics

### Participants

- **Dan Khasis**: 516 segments, 01:26:16 (57.7%), accuracy 93.3%
- **Alexey Afanasiev**: 83 segments, 00:09:19 (6.2%), accuracy 89.1%
- **Artur Moskalenko**: 67 segments, 00:08:30 (5.7%), accuracy 93.4%
- **Vova**: 49 segments, 00:05:18 (3.6%), accuracy 94.7%
- **Igor Skrynkovskyy**: 43 segments, 00:03:35 (2.4%), accuracy 91.6%
- **Serhii Kasainov**: 42 segments, 00:04:17 (2.9%), accuracy 91.2%
- **Semeyon S**: 21 segments, 00:01:38 (1.1%), accuracy 92.5%
- **Maksym Silman**: 17 segments, 00:01:59 (1.3%), accuracy 95.5%
- **Alexander Dylevskiy**: 16 segments, 00:01:43 (1.2%), accuracy 91.0%
- **Oleksandr Ishchenko**: 13 segments, 00:00:46 (0.5%), accuracy 89.5%
- **Volodymyr Ishchenko**: 8 segments, 00:00:48 (0.5%), accuracy 95.5%
- **Igor Golovtsov**: 5 segments, 00:00:16 (0.2%), accuracy 95.0%
- **Dmitry Smaliak**: 3 segments, 00:00:12 (0.1%), accuracy 78.0%
- **Davron Usmonov**: 3 segments, 00:00:11 (0.1%), accuracy 93.1%
- **Alex Yasko**: 3 segments, 00:00:07 (0.1%), accuracy 96.3%
- **Kateryna Shevchenko**: 1 segment, 00:00:01 (0.0%), accuracy 95.0%
- **Alexandr Kovtunov**: 1 segment, 00:00:06 (0.1%), accuracy 95.0%

### Alignment Quality

- High confidence (time-based): 877 (98.4%)
- Resolved via LLM: 7 (0.8%)
- Fallback: 7 (0.8%)
- Average confidence: 92.7%
- [!] Low confidence (<70%): 41 segments (4.6%)
