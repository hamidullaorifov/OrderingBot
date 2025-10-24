from aiogram import Router, types
from aiogram.filters import CommandStart
router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message):
    chat_id = message.chat.id
    username = message.from_user.username or "Unknown"

    print(f"✅ New user started the bot! Chat ID: {chat_id}, Username: @{username}")

    await message.answer(
        f"👋 Hello, {message.from_user.first_name}!\n"
        f"Your chat ID is <code>{chat_id}</code>.",
        parse_mode="HTML"
    )
