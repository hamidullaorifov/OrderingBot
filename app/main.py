import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from aiogram.exceptions import TelegramBadRequest
from app.config import settings
from app.schemas import FormData
from app.bot import bot, dp
from app.handlers import start_handler

# Register handlers
dp.include_router(start_handler.router)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     print("🚀 Bot is starting...")
#     polling_task = asyncio.create_task(dp.start_polling(bot))
#     yield  # <-- App runs while this block is open
#     print("🛑 Shutting down bot...")
#     polling_task.cancel()
#     await bot.session.close()

app = FastAPI(title="Form to Telegram API (aiogram)")

@app.post("/submit")
async def submit_form(form: FormData):
    """Receive form data and send it to Telegram"""
    try:
        message = (
            f"📩 <b>New Form Submission</b>\n\n"
            f"<b>Name:</b> {form.first_name} {form.last_name}\n"
            f"<b>Phone:</b> {form.phone_number}\n"
            f"<b>Message:</b>\n{form.comment}"
        )
        print('---> chat_id: ', settings.TELEGRAM_OWNER_ID)
        await bot.send_message(
            chat_id=settings.TELEGRAM_OWNER_ID,
            text=message,
            parse_mode="HTML"
        )

        return {"success": True, "message": "Form sent successfully"}

    except TelegramBadRequest as e:
        raise HTTPException(status_code=400, detail=f"Telegram error: {e.message}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
