import os
from dotenv import load_dotenv

load_dotenv()

def get_bot_token() -> str:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN not set in environment variables.")
    return token 