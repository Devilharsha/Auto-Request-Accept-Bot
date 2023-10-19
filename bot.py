
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatMember

pr0fess0r_99 = Client(
    "𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗣𝗹𝗲𝘢𝘀𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗢𝗽𝘂𝘀𝗧𝗲𝗰𝗵𝘇",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"]
)

CHAT_ID = int(os.environ.get("CHAT_ID", None))
TEXT = os.environ.get("BAN_WELCOME_MESSAGE", "Hello {mention}\nWelcome To {title}\n\nYour Auto Kicked")
LEFTED = os.environ.get("BAN_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    approvedbot = await client.get_me()
    button = [[
        InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴𝚉", url="https://t.me/MWUpdatez"),
        InlineKeyboardButton("𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="https://t.me/OpusTechz")
    ], [
        InlineKeyboardButton("𝚂𝚄𝙱𝚂𝚂𝚁𝙸𝙱𝙴", url=f"https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA")
    ]]
    await message.reply_text(text="**𝙷𝙴𝙻𝙻𝙾...⚡\n\n𝙸𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝴇 𝚃𝙴𝙻𝴇𝙶𝚂𝚃 𝙰𝚄𝚃𝙾 𝚁𝙴𝚆𝚄𝙴𝙴𝙿𝚂𝚃 𝙱𝙾𝚃.\n𝙵𝙾𝚁 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂 𝙲𝚁𝙴𝙰𝚃𝙴 𝙾𝙽𝙴 𝙱𝙾Τ... \n𝚅𝙸𝙳𝙴𝙾 𝙾𝙽 𝙼𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_message(filters.new_chat_members & filters.group)
async def check_member_update(client, message):
    left_member = message.left_chat_member
    if left_member:
        chat = message.chat  # Chat
        user = left_member  # User
        print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡")  # Logs
        await client.kick_chat_member(chat.id, user.id)
        if LEFTED == "on":
            await client.send_message(chat.id, TEXT.format(mention=user.mention, title=chat.title))

print("𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗣𝗹𝗲𝘀𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗢𝗽𝘂𝘀𝗧𝗲𝗰𝗵𝘇")
pr0fess0r_99.run()
