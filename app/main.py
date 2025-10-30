from fastapi import FastAPI, HTTPException
from aiogram.exceptions import TelegramBadRequest
from app.schemas import FormData
from app.bot import bot, dp
from app.handlers import start_handler
from fastapi.middleware.cors import CORSMiddleware

CHAT_IDS = ['388115743', '7550484867', '5774623098']

# Register handlers
dp.include_router(start_handler.router)

app = FastAPI(title="Form to Telegram API (aiogram)")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit")
async def submit_form(form: FormData):
    """Receive form data and send it to Telegram"""
    try:
        message = (
            f"📩 <b>New Form Submission</b>\n\n"
            f"<b>Name:</b> {form.full_name}\n"
            f"<b>Phone:</b> {form.phone_number}\n"
            f"<b>Message:</b>\n{form.comment}"
        )
        for chat_id in CHAT_IDS:
            try:
                await bot.send_message(
                    chat_id=chat_id,
                    text=message,
                    parse_mode="HTML"
                )
            except Exception as e:
                print("Exception occured:", e)
        return {"success": True, "message": "Form sent successfully"}

    except TelegramBadRequest as e:
        raise HTTPException(status_code=400, detail=f"Telegram error: {e.message}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
