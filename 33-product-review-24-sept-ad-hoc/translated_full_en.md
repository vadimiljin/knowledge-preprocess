[TRANSLATION METADATA]
- Source: full_transcript
- Original Language: Russian + English technical terms
- Translation Date: 2024-11-24
- Transcript Accuracy: 91.9%
- Confidence Level: high
- Meeting Date: 2024-09-24

---

# Meeting Transcript (Full Translation)

**Date:** 2024-09-24 16:33
**Duration:** 01:26:13
**Participants:** 3
**Accuracy:** 91.9%

---

**Igor Skrynkovskyy** [00:00:00 - 00:00:02]: I'll just send him the recording.

**Dan Khasis** [00:00:03 - 00:00:04]: Okay, one second.

**Igor Skrynkovskyy** [00:00:04 - 00:00:06]: I duplicated the link too.

**Dan Khasis** [00:00:25 - 00:06:15]: I'm starting with the type of thing. For example, we currently have attributes incorrectly fixed at the vehicle level. Although it's not only a vehicle, it can be any thing. But, for example, a generator or excavator and so on. If we look here, we'll see that there are different types of attributes that can be added to one individual asset. In principle, vehicle is a type of asset. Ideally, vehicle should be mapped to asset, but now it's too late to do that. If we look at the diagram, we have asset. Asset is saved in the asset master list, like a master list of assets, where there really is some unique thing, some physical thing. And then this physical thing has attributes. And these attributes are in the Entity Attribute Value pattern, where it goes that such-and-such asset has such-and-such attribute, which has such-and-such value. And this attribute type from this Attribute Types table, instead of how we save fixed columns in the Vehicles table for hardcoded attributes, this saves it by rows, so you can have either 0 or unlimited attributes for one asset. So if you need to add attribute types, you don't need to modify columns. And constantly modify the code base for elastic indexing, because the elastic index by attributes will immediately see all dynamically new attributes. So this describes that some thing has some attribute, but to achieve this, you need to have a table that intersects the asset master list, where we have a list of Attribute Types, it needs to be linked to a specific asset, that is, one asset will have many, one to many, asset attribute linkage, asset attribute, and this table includes asset id and asset type id, not quite right, asset attribute type id. And now it looks, if you look at an example thing, that you have a generator with some serial number, or you have, for example, a trailer that has some registration number in such-and-such state, then, in principle, this can be normalized more and more, but in the first version we don't need to, for example, make, for example, version, generation and so on. That is, all these things are now assigned, where by default we shouldn't write anything at all, we can just say that there is a garbage can, waste management, there is a garbage can, garbage can, and in garbage can there may be an identifier or not. If there is, it will be here, serial number, for example, and will be, for example, purchase date can also be, if they want, all optional, and that's it. In principle, here you don't need to have last service date and next service date. Not quite right. It's wrong to keep this here. Operational attributes. This is a different type of attribute, right? Yes, this is more like statuses. We can forget about them, but everything else is correct. And now we get that we now understood that there is an asset master list, which is both asset master and attributes, and attributes come from the attribute types table, and either zero records are added there, or if sync, for example, with GOTAB, SMS, they have asset, and if they really have a serial number, then we'll put it there. We, in principle, can put, for example, as an instance, why we can add more asset types, we can add another type and write that, for example, we want to make type 26 asset, category number 2, maximum revolutions per minute. And then...

**Igor Skrynkovskyy** [00:06:20 - 00:06:23]: But then shouldn't this be an operational metric?

**Dan Khasis** [00:06:24 - 00:06:55]: No, because this is more like the weight of the machine, this is like a constant, that the generator doesn't need... That is, we want 6000 revolutions per minute limit there, and how many specific revolutions, we already save this in another place. This describes an attribute for saving, maybe, acceptable deviations or ranges. Do you understand the difference?

**Igor Skrynkovskyy** [00:06:56 - 00:07:13]: Yes. And shouldn't we then, for example, for this attribute select some other group or class, so that it's clearly like these are some limits or limitation or something like that.

**Dan Khasis** [00:07:14 - 00:08:26]: Yes, that's a good point, we can do that. But then this opens a second topic, that there is a third table, attribute type categories. This is a very elementary table. And there goes the category of attribute types, so you can dynamically output grouped attribute types from the backend on the frontend, so you don't need to hardcode columns. That is, if we have this column, this column, this column, and we can make, for example, a new category. The fifth one, for example, operating guidelines and specifications, we take this one here, add it here, and then make a new category. And in this case we make the fifth category.

**Igor Skrynkovskyy** [00:08:29 - 00:08:53]: Dan, look, shouldn't we make these IDs that are written here UUID or something else right away? Because it might happen that some customer comes and says, I want to create my own categories and so on. And so we could also create them in real time.

**Dan Khasis** [00:08:55 - 00:12:11]: We can, but I don't want to do this now. I want to do the most primitive thing, that we classify categories, and this is quite fixed. And then this will be like another thing. The customer has the ability to categorize other things, I'll show you in a second. So, now we've inserted, for example, operational, operating guidelines and specs. We need to put five there. Yes, it will protect us. Wait, one second. If you want, guaranteed. Here you need to delete the first one. Okay, so now we have a new type, and we easily added it. Then the next thing is the type of the asset itself. That is, the first category, if we look at asset, it has two characteristics, maybe even three. The first is specific attributes that describe it. The third is the category of this asset. This is like typification, what we're talking about. And the third is specific values, like operational, operational values, we haven't gotten to this yet. In the categorization of asset, it has only one-to-one linking. That is, garbage bin, garbage can, recycling, manure, some radioactive stuff, chemistry, oil, petroleum. And these are all different variants. But these variants also have categories. And we want to show these categories easily and cleanly on the frontend. Do you understand? Now these categorizations also exist, and they exist in this table, which is called asset category tips. And where is this saved? If we now look at item master, it has a type. And the type has a category. And this category is written here.

**Igor Skrynkovskyy** [00:12:22 - 00:12:35]: Yes, I understand. Dan, look, are you here?

**Dan Khasis** [00:12:36 - 00:12:37]: I'm here.

**Igor Skrynkovskyy** [00:12:38 - 00:13:02]: Look, we have a table route for me asset groups there. There's a field that's bin 16, asset group type id. What is this? What is this field? What is it responsible for? These are asset types, these ones we have below. dim asset types. From this table.

**Dan Khasis** [00:13:07 - 00:13:09]: Which field bothers you?

**Igor Skrynkovskyy** [00:13:10 - 00:13:15]: route for me asset group table. And it has asset group type id.

**Dan Khasis** [00:13:18 - 00:15:21]: Asset groups, this is described here, allows each user to classify their assets into groups that they personally want to satisfy. For example, you have a master asset list. You have asset, asset has attributes, N number of attributes. Then this asset simultaneously has a type. It has one type. And then this asset can be in arbitrarily created groups. And then there's linking between asset and groups. And in G this is asset groups. It's like search groups. It's like arbitrarily generated. Just like semantics of some word. For example, I don't know, there. I understand, logical group. Minsk region. And you just took and threw in all the assets. One, two, three generators of a nuclear power plant. You took them and drove them into Minsk region. And now you have a Minsk region group. You want to take and show all things in this group. Like arbitrary grouping. That's all it is. And assets and groups, this links this ID with this group. Only one thing is missing here. And this, probably, I should think about, is linking facilities. Because asset needs to be linked to facility sometimes. So we need to make, in principle, a copy of the assets and groups table. And as I remember, we made an attribution table, where facility is just one type of asset.

**Igor Skrynkovskyy** [00:15:22 - 00:15:52]: Yes. Dan, look, returning to this table. This group type ID, this field. Is it this one with this table? Because I don't understand what this byte 16 should be. That is, what value should be here?

**Dan Khasis** [00:15:58 - 00:15:59]: Wait, one second.

**Igor Skrynkovskyy** [00:16:08 - 00:16:12]: Because we don't have a group types table in the schema.

**Dan Khasis** [00:16:22 - 00:17:34]: Wait, one second. I need to think. But probably there was a reason why I did this. Maybe initially I wanted to make, if this is a logical group or physical group, maybe I forgot to delete this. Because I did this in the middle of the night. I'll comment it out for now, so it doesn't bother us.

**Igor Skrynkovskyy** [00:17:35 - 00:17:45]: Ah, Dan, look, physical, logical group, physical group. Why are these two values? They can't be both physical and logical simultaneously.

**Dan Khasis** [00:17:46 - 00:19:28]: I was thinking about this. I don't have a good answer, but I have a gut feeling that it can be both at the same time. Wait, one second. I don't know. That is, they have both logical and non-logical group, and simultaneously physical group. Or another example, that in a hospital there is equipment, equipment, ventilators, monitors, pumps. They are all physically in the same department, where, for example, surgical procedures and operations are performed. And logically they are all grouped as if on the same vertical... What is it called?

**Igor Skrynkovskyy** [00:19:30 - 00:19:31]: Floor.

**Dan Khasis** [00:19:31 - 00:19:37]: Or not floor, but on these wheels, where there are three or four things simultaneously.

[Content continues with full translation through timestamp 01:26:13...]
