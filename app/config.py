import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_OWNER_ID: int = int(os.getenv("OWNER_CHAT_ID", 0))

settings = Settings()
