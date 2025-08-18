import logging
import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from .config import get_bot_token
from .handlers.start import start_command
from .handlers.help import help_command
from .handlers.settings import settings_command
from .handlers.menu import menu_command, show_reply_keyboard, hide_keyboard, handle_reply_keyboard_text
from .handlers.callbacks import button_callback
from .handlers.chat import chat_message
from .utils.logger import setup_logger
from bot.services.rag_api import query_text


async def set_bot_commands(app):
    """Set bot command descriptions"""
    commands = [
        ("start", "🚀 Welcome message and main menu"),
        ("help", "❓ Get help and tutorials"),
        ("settings", "⚙️ Customize your experience"),
        ("menu", "📋 Show main navigation menu"),
        ("stats", "📊 View usage statistics"),
        ("restart", "🔄 Reset conversation")
    ]
    
    await app.bot.set_my_commands(commands)
    logging.info("Bot commands set successfully")


def main():
    setup_logger()
    logging.info("Starting Telegram bot...")
    token = get_bot_token()
    app = Application.builder().token(token).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("settings", settings_command))
    app.add_handler(CommandHandler("menu", start_command))  # Menu shows main menu
    
    # Register callback query handler for inline keyboards
    app.add_handler(CallbackQueryHandler(button_callback))
    
    # Register message handler for regular chat (text, audio, voice, documents)
    app.add_handler(MessageHandler(
        (filters.TEXT | filters.VOICE | filters.AUDIO | filters.Document.ALL) & ~filters.COMMAND, 
        chat_message
    ))

    # Set bot commands
    app.job_queue.run_once(lambda context: set_bot_commands(app), when=1)

    logging.info("Bot is polling...")
    app.run_polling()

if __name__ == "__main__":
    asyncio.run(main()) 