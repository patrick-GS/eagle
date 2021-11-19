""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.khelp$")
async def usit(e):
    await e.edit(
        f"      ╔════════════╗\n     **__✟BANTUAN✟__**     \n╚════════════╝ \n"
        f"**Hai Jamet {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "═⎆ developer  : [Mustache](t.me/Manusiabajingann) \n"
        "═⎆ Repository : [Ganesha-Userbot](https://github.com/eagleprojects) \n"
        "═⎆ Instragam  : [Instagram Mustache](Instagram.com/edxwans) \n"
        "═⎆ Grup Support : [Ganesha Userbot Support](https://t.me/EagleSupport)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"      ╔════════════╗\n  **__✟DAFTAR VARS✟__**     \n╚════════════╝ \n"
        f"**Disini Daftar Vars Dari Ganesha** {DEFAULTUSER} :\n"
        "═⎆ Daftar Vars : [DAFTAR VARS](https://raw.githubusercontent.com/eagleprojects/Ganesha/Ganesha/varshelper.txt)")


CMD_HELP.update(
    {
        "helper": "**✘ Plugin :** `Helper`\
        \n\n  •  **Perintah :** `.khelp`\
        \n  •  **Function : **Bantuan Untuk ✟ Ganesha-Userbot ✟\
        \n\n  •  **Perintah :** `.vars`\
        \n  •  **Function : **Melihat Daftar Vars\
    "
    }
)
