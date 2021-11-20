# Copyright (C) 2021 King - Userbot
# Created by Apis
# Jangan hapus credit asu!!!

from random import choice

from userbot import CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
XBOT_STRINGS = [
    "Aku userbot",
    "Jangan main main ya!",
    "Gw gban mampus lu",
    "Gw pake Eagle-Userbot",
    "Tidak",
    "Awas aja sampe ngelawan ama gw",
    "Bacot kau",
    "Hilih",
    "Bicit banget lu",
    "Hahahaha",
    "Stres",
    "lmao",
    "Goblok!",
    "Apa anjeng!",
    "Idih sokap",
    "Babi",
    "Dasar lu",
    "Grup sepi jan sok keras",
    "Uang hasil link jan sok keras",
    "Hadeh",
    "Orang gilak",
    "Pasar baru",
    "Koran kabar lama",
    "Batri lama",
    "Tolol sekali",
    "Najis alay",
    "Okey",
    "Asoo",
    "Bangsat",
    "Anjg",
    "Bego amat",
    "Sawadikap tod",
    "Kenapa?",
    "Poci...",
    "mtk",
    "Asu capek:)",
    "Ke kamar yuk",
    "Gosok gigi",
    "Gak bisa ngomong r",
    "Upin dan ipin",
    "Python",
    "Ceunah",
]


@register(outgoing=True, pattern="^.xbot$")
async def xbot(xbotpis):
    await xbotpis.edit(choice(XBOT_STRINGS))

CMD_HELP.update(
    {
        "xbot": "**✘ Plugin :** `xbot`\
        \n\n  •  **Perintah :** `.xbot`\
        \n  •  **Function : **Xbot random untuk bersenang senang saja\
    "
    }
)
