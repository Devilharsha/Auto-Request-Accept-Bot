import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

pr0fess0r_99 = Client(
    "Bot Started Please Subscribe OpusTechz",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"]
)

# Define the chat or channel ID to monitor
CHAT_ID = os.environ.get("CHAT_ID")
TEXT = os.environ.get("BAN_WELCOME_MESSAGE", "Hello {mention}\nYou've been banned from {title}.")
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

@pr0fess0r_99.on_chat_member_left()
async def ban_left_member(client, message):
    try:
        user = message.left_chat_member
        chat = message.chat
        if user:
            logger.info(f"{user.first_name} left the chat ⚡")
            await client.kick_chat_member(chat.id, user.id)
            logger.info(f"{user.first_name} has been banned ⚡")
            if LEFTED == "on":
                await client.send_message(chat.id, TEXT.format(mention=user.mention, title=chat.title))
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    logger.info("Bot Started, Monitoring for Members Leaving and Sending Ban Messages")
    pr0fess0r_99.run()
