from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "❓ <b>Help Center</b>\n\n"
        "Get help with using your RAG bot:\n\n"
        "• <b>Getting Started</b> - Basic usage guide\n"
        "• <b>Chat Commands</b> - Available commands\n"
        "• <b>Features</b> - What the bot can do\n"
        "• <b>Troubleshooting</b> - Common issues\n\n"
        "💡 <i>Choose a topic below or just start asking questions!</i>"
    )
    
    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboards.help_menu(),
        parse_mode='HTML'
    ) 