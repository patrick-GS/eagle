# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, EMOJI_HELP, UPSTREAM_REPO_BRANCH, BOT_VER, CMD_HELP, DEFAULTUSER
from userbot.events import register
from platform import uname

plugins = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(f"`{args}` **Bukan Plugin Yang Valid**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t{EMOJI_HELP}  "
        await event.edit("**๐ Menu Help!**\n\n"
                         f"**eagle** {DEFAULTUSER}\n**โยป Plugins :** `{len(plugins)}`\n**โยป Branch :** __{UPSTREAM_REPO_BRANCH}__\n**โยป Versi Userbot :** `v{BOT_VER}`\n\n"
                         f"**๐ Menu Help Inline** `.helpme` \n\n"
                         "**โ Menu Plugin โฏ**\n"
                         f"โฐโบ{EMOJI_HELP} {string} โโ")
        await event.reply("\n**Contoh : ketik** `.help` <nama perintah> **Yang Sesuai Dengan Plugin Di Atas**\n\n**USERBOT TELEGRAM**")
        await asyncio.sleep(2000)
        await event.delete()

# fixes by apis
# Jan Di Clone Help Nya , Usaha Lah Asu :)
