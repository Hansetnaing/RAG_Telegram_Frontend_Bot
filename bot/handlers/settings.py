"""
Settings command handler with interactive menu
"""

from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards


async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /settings command"""
    text = (
        "⚙️ <b>Settings</b>\n\n"
        "Customize your bot experience:\n\n"
        "• <b>Notifications</b> - Alert preferences\n"
        "• <b>Language</b> - Interface language\n"
        "• <b>Response Style</b> - How the bot responds\n"
        "• <b>RAG Settings</b> - Search and retrieval options\n"
        "• <b>Export Data</b> - Download your data\n"
        "• <b>Clear History</b> - Reset conversation history"
    )
    
    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboards.settings_menu(),
        parse_mode='HTML'
    )
