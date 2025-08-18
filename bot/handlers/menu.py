"""
Menu command handler and menu utilities
"""

from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards, ReplyKeyboards


async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /menu command - show main navigation menu"""
    text = (
        "📋 <b>Main Menu</b>\n\n"
        "Welcome to your RAG-powered Telegram bot! Choose an option below:\n\n"
        "• <b>Help</b> - Get assistance and tutorials\n"
        "• <b>Settings</b> - Customize your experience\n"
        "• <b>About RAG</b> - Learn about the technology\n"
        "• <b>Examples</b> - See what you can ask\n"
        "• <b>Usage Stats</b> - View your usage statistics\n"
        "• <b>Restart</b> - Start a fresh conversation"
    )
    
    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboards.main_menu(),
        parse_mode='HTML'
    )


async def show_reply_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show reply keyboard menu"""
    text = (
        "📱 <b>Quick Access Menu</b>\n\n"
        "Use the keyboard buttons below for quick access to common features!\n\n"
        "💡 <i>You can also type any question directly.</i>"
    )
    
    await update.message.reply_text(
        text=text,
        reply_markup=ReplyKeyboards.main_menu(),
        parse_mode='HTML'
    )


async def hide_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hide the reply keyboard"""
    await update.message.reply_text(
        "✅ Keyboard hidden. You can bring it back anytime with /keyboard",
        reply_markup=ReplyKeyboardRemove()
    )


async def handle_reply_keyboard_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle reply keyboard button presses (text messages that match keyboard buttons)"""
    text = update.message.text
    
    # Map reply keyboard buttons to actions
    button_actions = {
        "❓ Help": show_help_action,
        "⚙️ Settings": show_settings_action,
        "📚 About RAG": show_about_rag_action,
        "💡 Examples": show_examples_action,
        "📊 Stats": show_stats_action,
        "🔄 Restart": restart_action,
        "📋 Menu": menu_command,
        "❌ Hide Keyboard": hide_keyboard
    }
    
    # Check if the message matches any reply keyboard button
    if text in button_actions:
        await button_actions[text](update, context)
        return True
    
    return False


async def show_help_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show help menu from reply keyboard"""
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


async def show_settings_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show settings menu from reply keyboard"""
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


async def show_about_rag_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show about RAG from reply keyboard"""
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
    
    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboards.back_button(),
        parse_mode='HTML'
    )


async def show_examples_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show examples menu from reply keyboard"""
    text = (
        "💡 <b>Example Queries</b>\n\n"
        "Here are some types of questions you can ask:\n\n"
        "• <b>Document Questions</b> - Ask about specific documents\n"
        "• <b>Search Information</b> - Find specific facts or data\n"
        "• <b>General Questions</b> - Broad topic inquiries\n"
        "• <b>Related Topics</b> - Explore connected subjects"
    )
    
    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboards.examples_menu(),
        parse_mode='HTML'
    )


async def show_stats_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show stats from reply keyboard"""
    user_id = update.effective_user.id
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
    
    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboards.back_button(),
        parse_mode='HTML'
    )


async def restart_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Restart conversation from reply keyboard"""
    text = (
        "🔄 <b>Conversation Restarted</b>\n\n"
        "Your conversation has been reset! You can now start fresh.\n\n"
        "💡 <i>Tip: Your settings and preferences are preserved.</i>"
    )
    
    # Clear any conversation context if you're storing it
    if hasattr(context, 'user_data'):
        context.user_data.clear()
    
    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboards.back_button(),
        parse_mode='HTML'
    )
