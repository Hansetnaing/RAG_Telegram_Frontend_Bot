import logging
import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from .config import get_bot_token
from .handlers.start import start_command
from .handlers.menu import menu_command
from .handlers.callbacks import button_callback, show_main_menu
from .handlers.chat import chat_message
from .utils.logger import setup_logger
from bot.services.rag_api import query_text


# --- /help command handler --- #
async def help_command(update, context):
    """Show help message"""
    text = (
        "❓ <b>Help Center</b>\n\n"
        "မင်္ဂလာပါ! ကျွန်ုပ် Pivot ဖြစ်ပါတယ်။\n\n"
        "➡️ သင့်ဆီမှာ လုပ်ဆောင်နိုင်တဲ့ feature တွေ:\n"
        " - 📝 အကျဉ်းချုပ်စာသား (Text Input)\n"
        " - 📂 ဖိုင်များ (PDF, DOCX, TXT)\n"
        " - 🎤 အသံထည့်သွင်းမှု (Speech Input)\n"
        " - ⚡ AI RAG Q&A Service\n\n"
        "👉 အခြားအကြောင်းအရာများကို /menu မှတဆင့် ကြည့်နိုင်ပါတယ်။"
    )
    await update.message.reply_html(text)


async def set_bot_commands(app):
    """Set bot command descriptions"""
    commands = [
        ("start", "🚀 Start the bot and open the main menu"),
        ("help", "❓ Get help, tips, and guides"),
        ("menu", "📋 Show navigation options"),
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
    app.add_handler(CommandHandler("menu", start_command))  # /menu shows main menu

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
