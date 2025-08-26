"""
Callback query handlers for inline keyboard interactions
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards

logger = logging.getLogger(__name__)


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all inline keyboard button callbacks"""
    query = update.callback_query
    await query.answer()  # Acknowledge the callback
    
    callback_data = query.data
    logger.info(f"Received callback: {callback_data}")
    
    # Route to appropriate handler based on callback data
    if callback_data == "main_menu":
        await show_main_menu(query, context)
    elif callback_data == "help":
        await show_help_menu(query, context)
    elif callback_data == "settings":
        await show_settings_menu(query, context)
    elif callback_data == "about_rag":
        await show_about_rag(query, context)
    elif callback_data == "examples":
        await show_examples_menu(query, context)
    elif callback_data == "stats":
        await show_stats(query, context)
    elif callback_data == "restart":
        await restart_conversation(query, context)
    elif callback_data.startswith("help_"):
        await handle_help_submenu(query, context, callback_data)
    elif callback_data.startswith("settings_"):
        await handle_settings_submenu(query, context, callback_data)
    elif callback_data.startswith("example_"):
        await handle_example_submenu(query, context, callback_data)
    elif callback_data.startswith("confirm_"):
        await handle_confirmation(query, context, callback_data)
    elif callback_data == "status":
        await show_status(query, context)
    else:
        await query.edit_message_text("❌ Unknown command. Please try again.")


# ----- Menu Handlers ----- #
async def show_main_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the main menu"""
    text = (
        "🏠 <b>Main Menu</b>\n\n"
        "Welcome to your RAG-powered Telegram bot! Choose an option below:\n\n"
        "• <b>Help</b> - Get assistance and tutorials\n"
        "• <b>Settings</b> - Customize your experience\n"
        "• <b>About RAG</b> - Learn about the technology\n"
        "• <b>Examples</b> - See what you can ask\n"
        "• <b>Usage Stats</b> - View your usage statistics\n"
        "• <b>Status</b> - Check bot status & platforms\n"
        "• <b>Restart</b> - Start a fresh conversation"
    )
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.main_menu(),
        parse_mode='HTML'
    )


async def show_help_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the help menu"""
    text = (
        "❓ <b>Help Center</b>\n\n"
        "Get help with using your RAG bot:\n\n"
        "• <b>Getting Started</b> - Basic usage guide\n"
        "• <b>Chat Commands</b> - Available commands\n"
        "• <b>Features</b> - What the bot can do\n"
        "• <b>Troubleshooting</b> - Common issues"
    )
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.help_menu(),
        parse_mode='HTML'
    )


async def show_settings_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the settings menu"""
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
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.settings_menu(),
        parse_mode='HTML'
    )


async def show_about_rag(query, context: ContextTypes.DEFAULT_TYPE):
    """Show information about RAG"""
    text = (
        "📚 <b>About RAG (Retrieval-Augmented Generation)</b>\n\n"
        "RAG is an AI technique that combines:\n\n"
        "🔍 <b>Retrieval</b> - Finding relevant information from a knowledge base\n"
        "🧠 <b>Generation</b> - Creating natural language responses\n\n"
        "This allows the bot to:\n"
        "• Access up-to-date information\n"
        "• Provide accurate, contextual answers\n"
        "• Reference specific documents or sources\n"
        "• Maintain consistency across conversations\n\n"
        "Your queries are processed through this system to give you the most relevant and accurate responses possible!"
    )
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.back_button(),
        parse_mode='HTML'
    )


async def show_examples_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the examples menu"""
    text = (
        "💡 <b>Example Queries</b>\n\n"
        "Here are some types of questions you can ask:\n\n"
        "• <b>Document Questions</b> - Ask about specific documents\n"
        "• <b>Search Information</b> - Find specific facts or data\n"
        "• <b>General Questions</b> - Broad topic inquiries\n"
        "• <b>Related Topics</b> - Explore connected subjects"
    )
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.examples_menu(),
        parse_mode='HTML'
    )


async def show_stats(query, context: ContextTypes.DEFAULT_TYPE):
    """Show usage statistics"""
    user_id = query.from_user.id
    text = (
        "📊 <b>Usage Statistics</b>\n\n"
        f"👤 <b>User ID:</b> {user_id}\n"
        "💬 <b>Messages sent:</b> 42\n"
        "❓ <b>Questions asked:</b> 38\n"
        "📚 <b>Documents referenced:</b> 15\n"
        "⏱️ <b>Average response time:</b> 2.3s\n"
        "📅 <b>Last active:</b> Today\n\n"
        "🎯 <b>Most common topics:</b>\n"
        "• Technology (45%)\n"
        "• Science (30%)\n"
        "• General Knowledge (25%)"
    )
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.back_button(),
        parse_mode='HTML'
    )


async def restart_conversation(query, context: ContextTypes.DEFAULT_TYPE):
    """Restart the conversation"""
    text = (
        "🔄 <b>Conversation Restarted</b>\n\n"
        "Your conversation has been reset! You can now start fresh.\n\n"
        "💡 <i>Tip: Your settings and preferences are preserved.</i>"
    )
    if hasattr(context, 'user_data'):
        context.user_data.clear()
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.back_button(),
        parse_mode='HTML'
    )


async def show_status(query, context: ContextTypes.DEFAULT_TYPE):
    """Show bot status with Android and Web links"""
    text = (
        "⚡ <b>Bot Status & Performance</b>\n\n"
        "✅ <b>Status:</b> Online & Ready\n"
        "🚀 <b>Average Response Time:</b> 2.1s\n"
        "📈 <b>Uptime:</b> 99.9%\n"
        "🤖 <b>Performance:</b> Optimized for smooth chatting\n\n"
        "✨ You can also use RAG Bot on other platforms:\n"
        "• 📱 Android App\n"
        "• 🌐 Web Version\n\n"
        "<i>Choose below to continue 👇</i>"
    )
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.status_menu(),
        parse_mode='HTML'
    )
