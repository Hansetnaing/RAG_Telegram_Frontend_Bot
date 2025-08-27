"""
Enhanced start command handler for Legal Compliance & Cybersecurity RAG Bot
Specialized for SMEs and Startups
"""

from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome message for legal compliance & cybersecurity RAG bot"""
    text = (
        "⚖️ <b>Welcome to your Legal & Cyber Security Assistant!</b>\n\n"
        "🚀 <b>Built for SMEs & Startups</b>\n"
        "I'm your AI companion for navigating the complex world of legal compliance, "
        "cybersecurity, and data privacy. Whether you're just starting out or scaling up, "
        "I'll help you stay compliant and secure.\n\n"
        "🔍 <b>What I can help with:</b>\n"
        "• <b>Legal Compliance</b> - Business setup, contracts, regulations\n"
        "• <b>Cybersecurity</b> - Threat protection, policies, incident response\n"
        "• <b>Privacy & Data</b> - GDPR, PDPA, privacy policies\n"
        "• <b>Quick Actions</b> - Templates, checklists, emergency guides\n\n"
        "✨ <b>How to get started:</b>\n"
        "• Ask me any question directly (e.g., 'Do I need a privacy policy?')\n"
        "• Use the menu below for structured guidance\n"
        "• Try emergency help for urgent situations\n\n"
        "📱 <b>Pro tip:</b> For better experience with saved conversations and file management, "
        "check out our mobile and web apps!\n\n"
        "💡 <i>Ready to help you build a compliant and secure business!</i>"
    )

    await update.message.reply_text(
        text=text,
        reply_markup=InlineKeyboards.main_menu(),
        parse_mode='HTML'
    )
