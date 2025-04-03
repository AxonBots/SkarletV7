from pyrogram import Client, filters
from database.users_chats_db import db
from info import ADMINS

@Client.on_message(filters.command("exempt_token") & filters.user(ADMINS))
async def exempt_token_command(bot, message):
    if len(message.command) < 2:
        await message.reply("Usage: /exempt_token <group_id>")
        return
    try:
        group_id = int(message.command[1])
        settings = await db.get_settings(group_id)
        settings['token_exempt'] = True
        await db.update_settings(group_id, settings)
        await message.reply(f"Group {group_id} is now exempt from token system.")
    except Exception as e:
        await message.reply(f"Error: {str(e)}")

@Client.on_message(filters.command("unexempt_token") & filters.user(ADMINS))
async def unexempt_token_command(bot, message):
    if len(message.command) < 2:
        await message.reply("Usage: /unexempt_token <group_id>")
        return
    try:
        group_id = int(message.command[1])
        settings = await db.get_settings(group_id)
        settings['token_exempt'] = False
        await db.update_settings(group_id, settings)
        await message.reply(f"Group {group_id} is no longer exempt from token system.")
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
