"""
Callback query handlers for inline keyboard interactions
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards

logger = logging.getLogger(__name__)


# ----- Main Menu Handler ----- #
async def show_main_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the main menu"""
    text = (
        "📋 <b>Main Menu</b>\n\n"
        "Welcome to your RAG-powered Telegram bot! Choose an option below:\n\n"
        "• <b>Help</b> - Get assistance and tutorials\n"
        "• <b>About RAG</b> - Learn about the technology\n"
        "• <b>Examples</b> - See what you can ask\n"
        "• <b>Better Performance</b> - Tips to improve responses (App/Web)\n\n"
    )

    keyboard = InlineKeyboards.main_menu()

    await query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


# ----- Help Menu Handler ----- #
async def show_help_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the help submenu"""
    text = (
        "❓ <b>Help Center</b>\n\n"
        "Choose how you want to interact with the bot:\n\n"
        "• <b>📝 Text</b> - Send normal messages\n"
        "• <b>📂 File</b> - Upload PDF, DOCX, TXT\n"
        "• <b>🎤 Speech</b> - Use your voice to query\n"
        "• <b>⚡ Better Performance</b> - Tips to improve results (App/Web)\n\n"
    )

    keyboard = InlineKeyboards.help_menu()

    await query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


# ----- Examples Menu Handler ----- #
async def show_examples_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the examples submenu"""
    text = (
        "💡 <b>Example Questions</b>\n\n"
        "Try asking things like:\n\n"
        "• What is RAG?\n"
        "• Upload a file and ask for a summary\n"
        "• Convert speech to text and analyze\n"
        "• How to improve chatbot accuracy?\n\n"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Back", callback_data="main_menu")]
    ])

    await query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


# ----- Better Performance Menu Handler ----- #
async def show_performance_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show better performance menu (App & Web version)"""
    text = "⚡ <b>Choose a platform for performance tips:</b>"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📱 App Version", callback_data="performance_app")],
        [InlineKeyboardButton("🌐 Web Version", callback_data="performance_web")],
        [InlineKeyboardButton("⬅️ Back", callback_data="main_menu")]
    ])

    await query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


# ----- Performance Details Handlers ----- #
async def show_performance_app(query, context: ContextTypes.DEFAULT_TYPE):
    """Show performance tips for app version"""
    text = (
        "📱 <b>Better Performance - App Version</b>\n\n"
        "1. Keep the app updated to the latest version\n"
        "2. Use stable internet (WiFi recommended)\n"
        "3. Clear cache if responses slow down\n"
        "4. Avoid background apps consuming bandwidth\n"
    )
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Back", callback_data="performance_menu")]
    ])
    await query.edit_message_text(text=text, reply_markup=keyboard, parse_mode="HTML")


async def show_performance_web(query, context: ContextTypes.DEFAULT_TYPE):
    """Show performance tips for web version"""
    text = (
        "🌐 <b>Better Performance - Web Version</b>\n\n"
        "1. Use modern browsers (Chrome/Edge/Firefox)\n"
        "2. Ensure strong and stable internet\n"
        "3. Clear cookies/cache for smoother performance\n"
        "4. Avoid too many tabs open at once\n"
    )
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Back", callback_data="performance_menu")]
    ])
    await query.edit_message_text(text=text, reply_markup=keyboard, parse_mode="HTML")


# ----- Callback Router ----- #
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all inline keyboard button callbacks"""
    query = update.callback_query
    if not query:
        return

    callback_data = query.data
    logger.info(f"Button clicked: {callback_data}")

    if callback_data == "main_menu":
        await show_main_menu(query, context)
    elif callback_data == "help":
        await show_help_menu(query, context)
    elif callback_data == "examples":
        await show_examples_menu(query, context)
    elif callback_data == "performance":
        await show_performance_menu(query, context)
    elif callback_data == "performance_app":
        await show_performance_app(query, context)
    elif callback_data == "performance_web":
        await show_performance_web(query, context)
    else:
        await query.answer("⚠️ Unknown action", show_alert=True)
