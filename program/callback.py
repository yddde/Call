# Copyright (C) 2021 By A3kon

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""◌ **مرحباً بك عزيزي [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
◌ [{BOT_NAME}](https://t.me/{BOT_USERNAME})

**◌ قم بالضغط على الزر الذي تريده لمعرفه الأوامر لكل فئه منهم**

◌ [{قناة السورس}](https://t.me/{UPDATES_CHANNEL})
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◌ اضفني الى مجموعتك ◌",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("◌ دليل الإستخدام ◌", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("◌ الأوامر ◌", callback_data="cbcmds"),
                    InlineKeyboardButton("◌ المطور ◌", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "◌ كروب الدعم ◌", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "◌ قناة البوت ◌", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "◌ قناة السورس ◌", url="https://t.me/SoalfLove"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" **دليل الإستخدام**

1.) **قم بإضافة البوت في مجموعتك اولآ**
2.) **قم برفعي مشرف واعطائي جميع الصلاحيات ما عدا ميزة الاختفاء**
3.) **بعد اضافتي ورفعي مشرف استخدم أمر /reload**
3.) **قم بإضافة مساعدي @{ASSISTANT_NAME} او استخدم الامر /userbotjoin للدعوة التلقائيه**
4.) **قم بعمل مكالمه صوتيه قبل تشغيل فيديو او أغنيه**
5.) **أحيانآ امر /reload يساعدك في حل معظم المشاكل**

📌 **اذا لم ينضم مساعدي للمجموعه استخدم امر /userbotleave بعدها استخدم الامر /userbotjoin للدعوة مرة أخرى او قم باضافته يدوياً**

💡 **اذا كان لديك اي استفسار قم بزيارة كروب الدعم: @{GROUP_SUPPORT}**

◌ [{قناة السورس}](https://t.me/{UPDATES_CHANNEL})""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◌ رجوع↻", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""◌ **مرحباً بك عزيزي [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

◌ **◌ قم بالضغط على الزر الذي تريده لمعرفه الأوامر لكل فئه منهم**

◌ [{قناة السورس}](https://t.me/{UPDATES_CHANNEL})""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("◌ اوامر الادمنيه ◌", callback_data="cbadmin"),
                    InlineKeyboardButton("◌ اوامر المطور ◌", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("◌ الاوامر الاساسيه ◌", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("◌ رجوع↻", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""الاوامر الاساسيه

◌ /mplay (لتشغيل اغنيه في المحادثه الصوتيه (اسم الاغنيه / الرابط
◌ /vplay (لتشغيل فيديو في المحادثه الصوتيه (اسم الفيديو / الرابط 
◌ /vstream - رابط البث الحي + الجوده 720 360 480
◌ /playlist - لعرض قائمة التشغيل
◌ /video (اسم الفديو) + تحميل فيديو من اليوتيوب
◌ /song (اسم الاغنيه) + تحميل اغنيه من اليوتيوب
◌ /lyric (اغنيه) + جلب كلمات الاغنيه
◌ /search (الفيديو/ الاغنيه) + لجلب رابط من على اليوتيوب

◌ /ping - لمعرفة سرعة البوت
◌ /uptime - لعرض مدة التشغيل للبوت
◌ /alive - لمعرفه اذا كان البوت يعمل

◌ [{قناة السورس}](https://t.me/{UPDATES_CHANNEL})""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◌ رجوع↻", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""اوامر الادمنيه

◌ /pause - إيقاف مؤقت للاغنيه
◌ /resume - استئناف للاغنيه
◌ /skip - عمل تخطي للاغنيه
◌ /stop - ايقاف للاغنيه
◌ /vmute - كتم مساعد البوت
◌ /vunmute - الغاء كتم مساعد البوت
◌ /volume `1-200` - التحكم في الصوت للادمنيه فقط
◌ /reload - اعادة البوت وتحديث قائمه الادمنيه
◌ /userbotjoin - دعوة الحساب المساعد للكروب
◌ /userbotleave - مغادرة الحساب المساعد

◌ [{قناة السورس}](https://t.me/{UPDATES_CHANNEL})""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◌ رجوع↻", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""◌ اوامر المطور

◌ /rmw - تنظيف جميع الملفات
◌ /rmd - تنظيف جميع ملفات التحميل
◌ /sysinfo - إظهار معلومات النظام
◌ /update - تحديث البوت لآخر إصدار
◌ /restart - اعادة تشغيل للبوت
◌ /leaveall - امر المغادره من جميع الكروبات

◌ [{قناة السورس}](https://t.me/{UPDATES_CHANNEL})""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◌ رجوع↻", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n◌ revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("◌ هذا الامر بأستخدام الصلاحيه للادمنيه والمدراء فقط", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("◌ لاتوجد اغنيه تشتغل حالياً ✗ ", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("◌ هذا الامر بأستخدام الصلاحيه للادمنيه والمدراء فقط", show_alert=True)
    await query.message.delete()
