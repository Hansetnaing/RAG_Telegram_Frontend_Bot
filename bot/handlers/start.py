from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 <b>Welcome to RAG Bot!</b>\n\n"
        "I'm your AI-powered assistant using Retrieval-Augmented Generation to provide accurate, contextual answers.\n\n"
        "🚀 <b>Quick Start:</b>\n"
        "• Just type any question to get started\n"
        "• Use the menu below for more options\n"
        "• Try /help for detailed assistance\n\n"
        "💡 <i>Ask me anything and I'll search for the best answer!</i>"
    )
    
    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboards.main_menu(),
        parse_mode='HTML'
    ) 