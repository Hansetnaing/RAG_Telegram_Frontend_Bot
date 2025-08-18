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
    else:
        await query.edit_message_text("❌ Unknown command. Please try again.")


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
    # In a real implementation, you'd fetch actual stats from a database
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
    
    # Clear any conversation context if you're storing it
    if hasattr(context, 'user_data'):
        context.user_data.clear()
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.back_button(),
        parse_mode='HTML'
    )


async def handle_help_submenu(query, context: ContextTypes.DEFAULT_TYPE, callback_data: str):
    """Handle help submenu selections"""
    help_type = callback_data.replace("help_", "")
    
    help_content = {
        "getting_started": (
            "🚀 <b>Getting Started</b>\n\n"
            "1. Simply type your question or message\n"
            "2. The bot will search relevant information\n"
            "3. You'll receive a comprehensive answer\n\n"
            "<b>Tips:</b>\n"
            "• Be specific in your questions\n"
            "• You can ask follow-up questions\n"
            "• Use /help for this menu anytime\n"
            "• Try /settings to customize your experience"
        ),
        "commands": (
            "💬 <b>Available Commands</b>\n\n"
            "/start - Welcome message and main menu\n"
            "/help - Show this help system\n"
            "/settings - Open settings menu\n"
            "/menu - Show main navigation menu\n"
            "/stats - View your usage statistics\n"
            "/restart - Reset conversation context\n\n"
            "<b>Quick Actions:</b>\n"
            "• Just type any question to get started\n"
            "• Use the menu buttons for navigation"
        ),
        "features": (
            "📋 <b>Bot Features</b>\n\n"
            "🔍 <b>Smart Search:</b> Advanced information retrieval\n"
            "💬 <b>Natural Chat:</b> Conversational interface\n"
            "📚 <b>Document Analysis:</b> Reference specific sources\n"
            "🎯 <b>Context Aware:</b> Maintains conversation context\n"
            "⚙️ <b>Customizable:</b> Adjust settings to your needs\n"
            "📊 <b>Analytics:</b> Track your usage patterns\n"
            "🔔 <b>Notifications:</b> Optional alerts and updates"
        ),
        "troubleshooting": (
            "🔧 <b>Troubleshooting</b>\n\n"
            "<b>Bot not responding?</b>\n"
            "• Check your internet connection\n"
            "• Try /restart to reset\n\n"
            "<b>Wrong answers?</b>\n"
            "• Be more specific in your questions\n"
            "• Check RAG settings in /settings\n\n"
            "<b>Technical issues?</b>\n"
            "• Use /restart to clear any errors\n"
            "• Contact support if problems persist\n\n"
            "<b>Need more help?</b>\n"
            "• Try the examples in the main menu\n"
            "• Experiment with different question styles"
        )
    }
    
    text = help_content.get(help_type, "❌ Help topic not found.")
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.back_button("help"),
        parse_mode='HTML'
    )


async def handle_settings_submenu(query, context: ContextTypes.DEFAULT_TYPE, callback_data: str):
    """Handle settings submenu selections"""
    setting_type = callback_data.replace("settings_", "")
    
    if setting_type == "clear":
        text = (
            "🗑️ <b>Clear History</b>\n\n"
            "⚠️ This will permanently delete:\n"
            "• Your conversation history\n"
            "• Stored context\n"
            "• Cached responses\n\n"
            "Your settings will be preserved.\n\n"
            "Are you sure you want to continue?"
        )
        reply_markup = InlineKeyboards.confirmation_menu("clear")
        
    elif setting_type == "export":
        text = (
            "💾 <b>Export Data</b>\n\n"
            "⚠️ This will export:\n"
            "• Your conversation history\n"
            "• Settings and preferences\n"
            "• Usage statistics\n\n"
            "The data will be sent as a file.\n\n"
            "Continue with export?"
        )
        reply_markup = InlineKeyboards.confirmation_menu("export")
        
    else:
        # For other settings, show a placeholder
        settings_info = {
            "notifications": "🔔 <b>Notification Settings</b>\n\nFeature coming soon! You'll be able to customize when and how you receive notifications.",
            "language": "🌐 <b>Language Settings</b>\n\nCurrently supporting English. More languages coming soon!",
            "response_style": "📝 <b>Response Style</b>\n\nChoose how detailed you want the bot's responses to be. Feature coming soon!",
            "rag": "🎯 <b>RAG Settings</b>\n\nCustomize search parameters and retrieval settings. Advanced feature coming soon!"
        }
        
        text = settings_info.get(setting_type, "⚙️ Settings panel under development.")
        reply_markup = InlineKeyboards.back_button("settings")
    
    await query.edit_message_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )


async def handle_example_submenu(query, context: ContextTypes.DEFAULT_TYPE, callback_data: str):
    """Handle example submenu selections"""
    example_type = callback_data.replace("example_", "")
    
    examples = {
        "documents": (
            "📖 <b>Document Questions</b>\n\n"
            "Try asking questions like:\n\n"
            "• \"What does the user manual say about installation?\"\n"
            "• \"Find information about pricing in the documentation\"\n"
            "• \"Summarize the key points from the latest report\"\n"
            "• \"What are the requirements mentioned in the specs?\""
        ),
        "search": (
            "🔍 <b>Search Information</b>\n\n"
            "Try these search queries:\n\n"
            "• \"What is machine learning?\"\n"
            "• \"Find data about climate change trends\"\n"
            "• \"Search for information about Python programming\"\n"
            "• \"Look up facts about renewable energy\""
        ),
        "general": (
            "💡 <b>General Questions</b>\n\n"
            "Ask about any topic:\n\n"
            "• \"Explain how blockchain works\"\n"
            "• \"What are the benefits of meditation?\"\n"
            "• \"How does photosynthesis work?\"\n"
            "• \"Tell me about artificial intelligence\""
        ),
        "related": (
            "🔗 <b>Related Topics</b>\n\n"
            "Explore connections:\n\n"
            "• \"What topics are related to data science?\"\n"
            "• \"Show me connected concepts to quantum physics\"\n"
            "• \"Find similar topics to sustainable development\"\n"
            "• \"What else should I know about cybersecurity?\""
        )
    }
    
    text = examples.get(example_type, "💡 Example not found.")
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.back_button("examples"),
        parse_mode='HTML'
    )


async def handle_confirmation(query, context: ContextTypes.DEFAULT_TYPE, callback_data: str):
    """Handle confirmation dialogs"""
    action = callback_data.replace("confirm_", "")
    
    if action == "clear":
        # Clear user data
        if hasattr(context, 'user_data'):
            context.user_data.clear()
        
        text = (
            "✅ <b>History Cleared</b>\n\n"
            "Your conversation history has been successfully cleared.\n"
            "You can start fresh now!"
        )
        
    elif action == "export":
        # In a real implementation, you'd generate and send a file
        text = (
            "💾 <b>Data Export</b>\n\n"
            "Your data export is being prepared...\n"
            "You'll receive a file shortly with your information.\n\n"
            "<i>Note: This is a demo implementation.</i>"
        )
    
    else:
        text = "❌ Unknown confirmation action."
    
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.back_button("settings"),
        parse_mode='HTML'
    )
