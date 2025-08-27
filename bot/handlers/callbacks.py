"""
Callback query handlers for inline keyboard interactions
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards

logger = logging.getLogger(__name__)


# ----- Button Callback Router ----- #
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all inline keyboard button callbacks"""
    query = update.callback_query
    if not query:
        return

    await query.answer()  # Acknowledge the callback
    callback_data = query.data
    logger.info(f"Received callback: {callback_data}")

    # Route based on callback data
    if callback_data == "main_menu":
        await show_main_menu(query, context)
    elif callback_data == "help":
        await show_help_menu(query, context)
    elif callback_data.startswith("help_"):
        await handle_help_submenu(query, context, callback_data)
    elif callback_data == "settings":
        await show_settings_menu(query, context)
    elif callback_data.startswith("settings_"):
        await handle_settings_submenu(query, context, callback_data)
    elif callback_data == "about_rag":
        await show_about_rag(query, context)
    elif callback_data == "examples":
        await show_examples_menu(query, context)
    elif callback_data.startswith("example_"):
        await handle_example_submenu(query, context, callback_data)
    elif callback_data == "stats":
        await show_stats(query, context)
    elif callback_data == "restart":
        await restart_conversation(query, context)
    elif callback_data == "status":
        await show_status(query, context)
    else:
        await query.edit_message_text(
            "❌ Unknown command. Please try again.",
            reply_markup=InlineKeyboards.main_menu()
        )


# ----- Settings Submenu Handler ----- #
async def handle_settings_submenu(query, context: ContextTypes.DEFAULT_TYPE, callback_data: str):
    """Handle settings submenu button presses"""
    responses = {
        "settings_language": "🌐 <b>Language Settings</b>\n\nFeature coming soon!",
        "settings_notifications": "🔔 <b>Notification Settings</b>\n\nFeature coming soon!",
        "settings_response_style": "📝 <b>Response Style</b>\n\nFeature coming soon!",
        "settings_rag": "🎯 <b>RAG Settings</b>\n\nFeature coming soon!",
        "settings_export": "💾 <b>Export Data</b>\n\nFeature coming soon!"
    }
    text = responses.get(callback_data, "⚙️ Option under construction.")
    await query.edit_message_text(
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboards.settings_menu()
    )


# ----- Help Submenu Handler ----- #
async def handle_help_submenu(query, context: ContextTypes.DEFAULT_TYPE, callback_data: str):
    await query.edit_message_text(
        "❓ Help submenu is under construction.",
        parse_mode="HTML",
        reply_markup=InlineKeyboards.help_menu()
    )


# ----- Examples Handlers ----- #
async def handle_example_submenu(query, context: ContextTypes.DEFAULT_TYPE, callback_data: str):
    """Handle predefined example questions"""
    if callback_data == "example_phishing":
        text = (
            "🛡️ <b>What is Phishing?</b>\n\n"
            "Phishing is a type of cyber attack where attackers try to steal sensitive information "
            "like passwords or credit card numbers by pretending to be a trustworthy entity. "
            "Always verify links and emails before clicking."
        )
    elif callback_data == "example_data_protection":
        text = (
            "🔒 <b>How to protect your data?</b>\n\n"
            "Use strong passwords, enable two-factor authentication, and avoid sharing sensitive "
            "information on untrusted platforms."
        )
    elif callback_data == "example_pdpa":
        text = (
            "📧 <b>What is PDPA?</b>\n\n"
            "PDPA (Personal Data Protection Act) is a law that governs how organizations handle "
            "personal data. It ensures privacy and proper management of user information."
        )
    elif callback_data == "example_cyberlaw":
        text = (
            "🛡️ <b>What is Cyber Law?</b>\n\n"
            "Cyber Law regulates online activities and digital transactions, protecting users from "
            "illegal actions like hacking, fraud, and data breaches."
        )
    else:
        text = "❌ Unknown example. Please try again."
    
    await query.edit_message_text(
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboards.examples_menu()
    )


# ----- Main Menu Handlers ----- #
async def show_main_menu(query, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🏠 <b>Main Menu</b>\n\n"
        "Welcome to your RAG-powered Telegram bot! Choose an option below:\n\n"
        "• <b>Help</b>\n• <b>Settings</b>\n• <b>About RAG</b>\n"
        "• <b>Examples</b>\n• <b>Usage Stats</b>\n• <b>Status</b>\n• <b>Restart</b>"
    )
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.main_menu(),
        parse_mode="HTML"
    )


async def show_help_menu(query, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "❓ <b>Help Center</b>\n\n"
        "မင်္ဂလာပါ! ကျွန်ုပ် Pivot ဖြစ်ပါတယ်။ မြန်မာစီးပွားရေးလုပ်ငန်းများအတွက် သတင်းအချက်အလက်လုံခြုံရေးနှင့် ဥပဒေလိုက်နာမှုဆိုင်ရာ အကြံဉာဏ်များ ပေးနိုင်ပါတယ်။\n\n"
        "ကျွန်ုပ်သည် Cyber Law၊ PDPA (Personal Data Protection Act), ISO 27001 စသည့် လိုက်နာမှုလိုအပ်ချက်များနှင့် အွန်လိုင်းခြိမ်းခြောက်မှုများ (Phishing, Scam စသည်) အကြောင်း အလွယ်တကူ နားလည်နိုင်စွမ်းဖြင့် ဖော်ပြပေးနိုင်ပါတယ်။\n\n"
        "ယနေ့တွင် သင့်အား မည်သို့ကူညီရမည်နည်းကို မေးမြန်းနိုင်ပြီး သင်လိုချင်သည့် သတင်းအချက်အလက်လုံခြုံရေး၊ PDPA လိုက်နာမှု၊ ဝဘ်ဆိုက်လုံခြုံရေး သို့မဟုတ် အခြား မေးခွန်းများအတွက် ညွှန်ကြားချက်များ ရနိုင်ပါသည်။\n\n"
        "💡 <b>AI Guide:</b> You can ask me anything about Cyber Laws, Data Protection, Website Security, or any related topic and I will provide step-by-step guidance!"
    )
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.help_menu(),
        parse_mode="HTML"
    )
    


async def show_settings_menu(query, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "⚙️ <b>Settings</b>\n\n"
        "Customize your bot experience:\n\n"
        "• Language\n• "
    )
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.settings_menu(),
        parse_mode="HTML"
    )


async def show_about_rag(query, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📚 <b>About RAG</b>\n\n"
        "RAG (Retrieval-Augmented Generation) combines retrieval of knowledge with AI generation for accurate responses."
    )
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.back_button(),
        parse_mode="HTML"
    )


async def show_examples_menu(query, context: ContextTypes.DEFAULT_TYPE):
    text = "💡 <b>Examples</b>\n\nSee what you can ask the bot."
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.examples_menu(),
        parse_mode="HTML"
    )


async def show_stats(query, context: ContextTypes.DEFAULT_TYPE):
    user_id = query.from_user.id
    text = (
        f"📊 <b>Usage Statistics</b>\n\nUser ID: {user_id}\nMessages sent: 42\nQuestions asked: 38"
    )
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.back_button(),
        parse_mode="HTML"
    )


async def restart_conversation(query, context: ContextTypes.DEFAULT_TYPE):
    if hasattr(context, "user_data"):
        context.user_data.clear()
    text = "🔄 <b>Conversation Restarted</b>\n\nYou can start fresh now!"
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.back_button(),
        parse_mode="HTML"
    )


async def show_status(query, context: ContextTypes.DEFAULT_TYPE):
    text = "⚡ <b>Bot Status</b>\n\n✅ Online & Ready\n📱 Android App\n🌐 Web Version"
    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboards.status_menu(),
        parse_mode="HTML"
    )
