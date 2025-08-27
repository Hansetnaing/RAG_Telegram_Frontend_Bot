from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
    "👋 <b>Hi there, welcome to RAG Bot!</b>\n\n"
    "I'm here to help answer your questions quickly and clearly. "
    "Think of me as your smart assistant who can look things up and explain them in simple terms.\n\n"
    "✨ <b>How to start:</b>\n"
    "• Just send me any question you have\n"
    "• Use the menu for extra options\n"
    "• Type /help if you’d like more details\n\n"
    "💡 <i>Go ahead, ask me anything — I’ll do my best to help!</i>"
)

    
    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboards.main_menu(),
        parse_mode='HTML'
    ) 