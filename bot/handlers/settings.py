# bot/handlers/settings.py
from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards

async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /settings command"""
    text = (
        "⚙️ <b>Settings</b>\n\n"
        "Customize your bot experience:\n\n"
        "• <b>Language</b> - Interface language\n"
    )

    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboards.settings_menu(),
        parse_mode="HTML"
    )

async def clear_history_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Clears user chat history"""
    query = update.callback_query
    if not query:
        return
    await query.answer()

    chat_id = query.message.chat.id

    # Remove stored message IDs
    message_ids = context.user_data.pop("history_message_ids", [])
    for mid in message_ids:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=mid)
        except Exception:
            pass

    # Clear known conversation keys
    for k in ["history", "conversation", "messages", "dialog", "history_message_ids"]:
        context.user_data.pop(k, None)
        context.chat_data.pop(k, None)

    # Confirm to user
    confirm_text = "🧹 <b>History Cleared!</b>\n\nYour conversation history has been reset."
    try:
        await query.message.edit_text(confirm_text, parse_mode="HTML", reply_markup=InlineKeyboards.settings_menu())
    except Exception:
        await query.message.reply_text(confirm_text, parse_mode="HTML", reply_markup=InlineKeyboards.settings_menu())
