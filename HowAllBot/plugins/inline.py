import random

from HowAllBot import pbot
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
)

text = """
<b>đĄ Either press the button attached to this message and select the chat you would like to post in or simply enter "@How_All_Bot" into your text box.</b>

<b>đŦ Please Don't Come Asking Help on Your Fork:</b>
<b>ÂŠī¸ @Aasf_Cyberking</b>
"""

aasf = (
"Small",
"Medium",
"Large"
)


@pbot.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.lower()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>đĨI am</b> {random.randint(1, 100)}<b>% Horny!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/fab6e21499ac634c02e00.jpg",
                    title=f"đĨ How honry are U?",
                    description=f"Send Your Current hornyess To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your horyness! đĨ", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>đŗī¸âđI am</b> {random.randint(1, 100)}<b>% Gay!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/de5777c0bc54e6c5b6d89.jpg",
                    title=f"đŗī¸âđ How Gay are U?",
                    description=f"Send Your Current Gayness To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your Gayness! đŗī¸âđ", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>đI am</b> {random.randint(1, 100)}<b>% lezbian!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/5d0f9f2b1140054297986.jpg",
                    title=f"đ How Lezbian are U?",
                    description=f"Send Your Current Lezbianess To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your Lezbianess! đ", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>đ§ I am</b> {random.randint(1, 100)}<b>% iq!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/03f0e2ccfa9728c1eafde.jpg",
                    title=f"đ§  How iq are U?",
                    description=f"Send Your Current iq To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your iq! đ§ ", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>đĢI am</b> {random.randint(1, 100)}<b>% Tired!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/70bfd9c3e310a3475ebb8.jpg",
                    title=f"đĢ How tired are U?",
                    description=f"Send Your Current tiredness To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your tiredness! đĢ", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>đĨēI am</b> {random.randint(1, 100)}<b>% Cute!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/0f1e2402ae4a689c342ed.jpg",
                    title=f"đĨē How cute are U?",
                    description=f"Send Your Current cuteness To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your cuteness! đĨē", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>đĻļ My foot size is</b> {random.randint(1, 100)}<b>!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/1d153acd01d24c49fef0f.jpg",
                    title=f"đĻļ What's your foot size?",
                    description=f"Send Your Current Foot Size To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your foot size! đĻļ", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>đ My boobs size is</b> {random.randint(1, 100)}<b>!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/4ff0bdbff806bd026dc13.jpg",
                    title=f"đ Whats your boobs size?",
                    description=f"Send Your Current Boobs Size To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your boobs size! đ", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>đ My cock size is</b> {random.randint(1, 100)}<b>inch!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/3397fc1c23cc5dbeb5981.jpg",
                    title=f"đ Whats your cock size?",
                    description=f"Send Your Current Cock Size To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your cock size! đ", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"<b>đ My ass is</b> {random.choice(aasf)} <b>!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/7a110bc87f55234239fbf.jpg",
                    title=f"đ What's your ass size?",
                    description=f"Send Your Current Ass Size To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your ass size! đ", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        text, disable_web_page_preview=True
                    ),
                    thumb_url="https://telegra.ph/file/32075ee5edfd88e99f6c3.jpg",
                    title=f"đ¤ Help",
                    description=f"Send The Usage Guidelines To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Repo! đģ",
                                    url="https://github.com/Team-Aasf/HowAllBot",
                                ),
                                InlineKeyboardButton(
                                    "Share any thing! đ¤", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
            ],
        )
