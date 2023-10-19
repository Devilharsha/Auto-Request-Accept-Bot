import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name)

pr0fess0r_99 = Client(
    "Bot Started Please Subscribe OpusTechz",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"]
)

CHAT_ID = -1001792377084  # Replace with the actual chat ID
TEXT = os.environ.get("BAN_WELCOME_MESSAGE", "Hello {mention}\nWelcome To {title}\n\nYou've been banned.")
LEFTED = os.environ.get("BAN_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    approvedbot = await client.get_me()
    button = [
        [
            InlineKeyboardButton("Subscribe to OpusTechz", url="https://t.me/OpusTechz")
        ]
    ]
    await message.reply_text(text="**Hello! I am a simple bot. For your chat's protection, I'll ban anyone who leaves.**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_chat_member_updated()
async def check_member_update(client, message):
    try:
        member = message.new_chat_member
        if member and member.status == "left":
            chat = message.chat
            user = member.user
            logger.info(f"{user.first_name} left the chat ⚡")
            await client.kick_chat_member(chat.id, user.id)
            if LEFTED == "on":
                await client.send_message(chat.id, TEXT.format(mention=user.mention, title=chat.title))
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

# Auto-accept join requests
@pr0fess0r_99.on_chat_member_updated()
async def auto_accept_join_request(client, message):
    try:
        member = message.new_chat_member
        if member and member.status == "member":
            await client.promote_chat_member(CHAT_ID, member.user.id, can_send_messages=True)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    logger.info("Bot Started, Monitoring for Members Leaving and Auto-Accepting Join Requests")
    pr0fess0r_99.run()
