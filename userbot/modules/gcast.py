#----------------------------------------------------------------------------------------------------------------------------#
#                                                                                                                            #
#     ______________              ________                ________________        ____                    ______________     #
#    |              |           /          \             |                |      |    |                  |              |    #
#    |     _________|          /   _____    \            |     ___________|      |    |                  |     _________|    #
#    |    |                   /   /     \    \           |    |                  |    |                  |    |              #
#    |    |_________         /   /_______\    \          |    |   ________       |    |                  |    |_________     #
#    |              |       /    _________     \         |    |  |____    |      |    |                  |              |    #
#    |     _________|      /    /          \    \        |    |       |   |      |    |                  |     _________|    #
#    |    |               /    /            \    \       |    |_______|   |      |    |                  |    |              #
#    |    |_________     /    /              \    \      |                |      |    |___________       |    |_________     #
#    |              |   /    /                \    \     |                |      |                |      |              |    #
#    |______________|  /____/                  \____\    |________________|      |________________|      |______________|    #
#                                                                                                                            #
#----------------------------------------------------------------------------------------------------------------------------#
from userbot.events import register
from userbot import CMD_HELP, bot

GCAST_BLACKLIST = [
    -1001558180556,  # EagleSupport
]


@register(outgoing=True, pattern="^.gcast (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Mohon Berikan Sebuah Pesan`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`Mengirim Pesan Global... 📣`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**")


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Berikan beberapa teks untuk Siaran Global`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`Sedang Mengirim pesan secara global...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Berhasil Mengirim Pesan Ke `{done}` obrolan, kesalahan dalam `{er}` obrolan(s)")


CMD_HELP.update(
    {
        "gcast": "**✘ Plugin :** `Global Broadcast`\
        \n\n  •  **Perintah :** `.gcast` <Text>\
        \n  •  **Function :** Mengirim Pesan Group Secara Global.\
        \n\n  •  **Perintah :** `.gucast` <Text>\
        \n  •  **Function :** Mengirim Pesan Pribadi Secara Global\
    "
    }
)
