import os
import logging
from pyrogram import Client, filters

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name)

# Initialize the Pyrogram Client
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define the chat or channel ID to monitor
chat_id = os.getenv("CHAT_ID")

# Start command handler
@app.on_message(filters.command("start") & filters.chat(chat_id))
async def start_command(client, message):
    await message.reply_text("Welcome to the Channel Monitor Bot! I will automatically ban members who leave the channel.")

# Member left handler
@app.on_message(filters.chat(chat_id) & filters.left_chat_member)
async def on_member_left(client, message):
    member = message.left_chat_member
    try:
        if member:
            user = member.user
            logger.info(f"Banning user: {user.first_name} (ID: {user.id})")
            await client.kick_chat_member(chat_id, user.id)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    logger.info("Bot Started, Monitoring for Members Leaving and Banning Them")
    app.run()
