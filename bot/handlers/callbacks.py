"""
Enhanced callback query handlers for Legal Compliance & Cybersecurity RAG Bot
Specialized for SMEs and Startups
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.utils.keyboards import InlineKeyboards

logger = logging.getLogger(__name__)


# ----- Main Menu Handler ----- #
async def show_main_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the main menu for legal & cybersecurity"""
    text = (
        "⚖️ <b>Legal & Cyber Security Assistant</b>\n\n"
        "Your AI companion for SME & Startup compliance needs:\n\n"
        "🔒 <b>Cybersecurity</b> - Threat protection & best practices\n"
        "⚖️ <b>Legal Compliance</b> - Regulations & requirements\n"
        "🛡️ <b>Privacy</b> - Data protection & GDPR/PDPA\n"
        "🚀 <b>Quick Actions</b> - Common compliance tasks\n"
        "📱 <b>Better Experience</b> - Use our mobile/web apps\n\n"
        "<i>💡 Tip: Type any question directly or use the menu below</i>"
    )

    keyboard = InlineKeyboards.main_menu()

    await query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


# ----- Cybersecurity Menu Handlers ----- #
async def show_cybersecurity_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the cybersecurity submenu"""
    text = (
        "🔒 <b>Cybersecurity for SMEs & Startups</b>\n\n"
        "Protect your business from digital threats:\n\n"
        "🎯 <b>Threat Assessment</b> - Identify risks to your business\n"
        "🛡️ <b>Security Policies</b> - Create protection protocols\n"
        "👥 <b>Employee Training</b> - Build security awareness\n"
        "🚨 <b>Incident Response</b> - Handle security breaches\n"
        "📋 <b>Compliance Frameworks</b> - ISO 27001, SOC 2, etc.\n\n"
        "💡 <i>Ask: 'How do I protect my startup from cyber attacks?'</i>"
    )

    keyboard = InlineKeyboards.cybersecurity_menu()

    await query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


async def show_cyber_threats(query, context: ContextTypes.DEFAULT_TYPE):
    """Show cybersecurity threat information"""
    text = (
        "🎯 <b>Cybersecurity Threat Assessment</b>\n\n"
        "Common threats facing SMEs & Startups:\n\n"
        "• <b>Phishing Attacks</b> - Fraudulent emails targeting credentials\n"
        "• <b>Ransomware</b> - Malware that encrypts your data\n"
        "• <b>Data Breaches</b> - Unauthorized access to sensitive info\n"
        "• <b>Social Engineering</b> - Manipulation tactics\n"
        "• <b>Insider Threats</b> - Risks from employees/contractors\n"
        "• <b>Supply Chain Attacks</b> - Compromised vendors/partners\n\n"
        "💡 <i>Try asking: 'What's my biggest cybersecurity risk?'</i>"
    )
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Back to Cybersecurity", callback_data="cybersecurity")]
    ])
    
    await query.edit_message_text(text=text, reply_markup=keyboard, parse_mode="HTML")


# ----- Legal Menu Handlers ----- #
async def show_legal_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the legal compliance submenu"""
    text = (
        "⚖️ <b>Legal Compliance for SMEs & Startups</b>\n\n"
        "Navigate legal requirements with confidence:\n\n"
        "🏢 <b>Business Setup</b> - Company formation & registration\n"
        "📄 <b>Contracts</b> - Terms, NDAs, employment agreements\n"
        "💡 <b>Intellectual Property</b> - Trademarks, copyrights, patents\n"
        "📊 <b>Regulations</b> - Industry-specific compliance\n"
        "👨‍💼 <b>Employment Law</b> - Hiring, contracts, policies\n\n"
        "💡 <i>Ask: 'What legal documents does my startup need?'</i>"
    )

    keyboard = InlineKeyboards.legal_menu()

    await query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


# ----- Privacy Menu Handlers ----- #
async def show_privacy_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the privacy & data protection submenu"""
    text = (
        "🛡️ <b>Privacy & Data Protection</b>\n\n"
        "Ensure compliance with data protection laws:\n\n"
        "🇪🇺 <b>GDPR</b> - European General Data Protection Regulation\n"
        "🇸🇬 <b>PDPA</b> - Personal Data Protection Act (Singapore)\n"
        "📋 <b>Privacy Policies</b> - Create compliant policies\n"
        "🗺️ <b>Data Mapping</b> - Understand your data flows\n"
        "✅ <b>Consent Management</b> - Proper consent collection\n"
        "🚨 <b>Breach Response</b> - 72-hour notification requirements\n\n"
        "💡 <i>Ask: 'Do I need a privacy policy for my app?'</i>"
    )

    keyboard = InlineKeyboards.privacy_menu()

    await query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


async def show_privacy_gdpr(query, context: ContextTypes.DEFAULT_TYPE):
    """Show GDPR compliance information"""
    text = (
        "🇪🇺 <b>GDPR Compliance Guide</b>\n\n"
        "Key GDPR requirements for businesses:\n\n"
        "• <b>Lawful Basis</b> - Legal grounds for processing data\n"
        "• <b>Consent</b> - Clear, specific, informed agreement\n"
        "• <b>Data Subject Rights</b> - Access, rectification, erasure\n"
        "• <b>Privacy by Design</b> - Built-in data protection\n"
        "• <b>DPO Requirements</b> - When you need a Data Protection Officer\n"
        "• <b>Breach Notification</b> - 72-hour reporting rule\n\n"
        "⚠️ <b>Fines:</b> Up to €20M or 4% of annual turnover\n\n"
        "💡 <i>Ask: 'Is my startup GDPR compliant?'</i>"
    )
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Back to Privacy", callback_data="privacy")]
    ])
    
    await query.edit_message_text(text=text, reply_markup=keyboard, parse_mode="HTML")


# ----- Quick Actions Menu Handlers ----- #
async def show_quick_actions_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the quick actions submenu"""
    text = (
        "🚀 <b>Quick Actions & Templates</b>\n\n"
        "Ready-to-use compliance resources:\n\n"
        "📋 <b>Checklists:</b>\n"
        "• GDPR compliance checklist\n"
        "• Cybersecurity audit checklist\n"
        "• Startup legal requirements\n\n"
        "📄 <b>Templates:</b>\n"
        "• Privacy policy template\n"
        "• Data processing agreement (DPA)\n"
        "• Security incident report form\n\n"
        "💡 <i>Say: 'Show me the GDPR checklist'</i>"
    )

    keyboard = InlineKeyboards.quick_actions_menu()

    await query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


async def show_gdpr_checklist(query, context: ContextTypes.DEFAULT_TYPE):
    """Show GDPR compliance checklist"""
    text = (
        "📋 <b>GDPR Compliance Checklist</b>\n\n"
        "✅ <b>Essential Steps:</b>\n\n"
        "□ Conduct data audit & mapping\n"
        "□ Update privacy policy\n"
        "□ Implement consent mechanisms\n"
        "□ Establish data subject request procedures\n"
        "□ Review data processing agreements\n"
        "□ Implement data breach procedures\n"
        "□ Conduct privacy impact assessments\n"
        "□ Train staff on GDPR requirements\n"
        "□ Appoint DPO (if required)\n"
        "□ Review international data transfers\n\n"
        "💡 <i>Ask: 'Help me complete the GDPR checklist'</i>"
    )
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Back to Quick Actions", callback_data="quick_actions")]
    ])
    
    await query.edit_message_text(text=text, reply_markup=keyboard, parse_mode="HTML")


# ----- Emergency Menu Handlers ----- #
async def show_emergency_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show the emergency response submenu"""
    text = (
        "🆘 <b>Emergency Response Center</b>\n\n"
        "Immediate help for urgent situations:\n\n"
        "🚨 <b>Data Breach</b> - Step-by-step response guide\n"
        "⚠️ <b>Cyber Attack</b> - Immediate containment steps\n"
        "📞 <b>Legal Emergency</b> - When to call a lawyer\n"
        "🔍 <b>Compliance Violation</b> - Damage control measures\n\n"
        "⏰ <b>Critical:</b> GDPR breach notification within 72 hours\n"
        "🚨 <b>Remember:</b> Document everything for legal protection\n\n"
        "💡 <i>Type: 'We've been hacked, what do I do?'</i>"
    )

    keyboard = InlineKeyboards.emergency_menu()

    await query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


async def show_data_breach_guide(query, context: ContextTypes.DEFAULT_TYPE):
    """Show data breach response guide"""
    text = (
        "🚨 <b>Data Breach Response Guide</b>\n\n"
        "⏰ <b>Immediate Actions (First 24 hours):</b>\n\n"
        "1️⃣ <b>Contain the breach</b> - Stop further data loss\n"
        "2️⃣ <b>Assess the damage</b> - What data was compromised?\n"
        "3️⃣ <b>Document everything</b> - Timeline, impact, actions\n"
        "4️⃣ <b>Notify authorities</b> - Within 72 hours (GDPR)\n"
        "5️⃣ <b>Inform affected individuals</b> - If high risk\n"
        "6️⃣ <b>Contact legal counsel</b> - Get professional advice\n"
        "7️⃣ <b>Review insurance</b> - Check cyber liability coverage\n\n"
        "⚠️ <b>Don't:</b> Panic, hide the breach, or delay reporting\n\n"
        "💡 <i>Ask: 'Help me respond to a data breach'</i>"
    )
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Back to Emergency", callback_data="emergency")]
    ])
    
    await query.edit_message_text(text=text, reply_markup=keyboard, parse_mode="HTML")


# ----- Better Apps Menu Handler ----- #
async def show_better_apps_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show better apps menu"""
    text = (
        "📱 <b>Better Experience with Our Apps</b>\n\n"
        "Why use our mobile & web apps instead of Telegram?\n\n"
        "✅ <b>Session Persistence</b> - Your conversations are saved\n"
        "✅ <b>Message History</b> - Access previous discussions\n"
        "✅ <b>User Profiles</b> - Personalized experience\n"
        "✅ <b>File Management</b> - Upload & organize documents\n"
        "✅ <b>Advanced Features</b> - Better search & filtering\n"
        "✅ <b>Offline Access</b> - View saved content offline\n\n"
        "🚀 <b>Perfect for:</b> Legal research, compliance tracking, document management"
    )

    keyboard = InlineKeyboards.better_apps_menu()

    await query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


# ----- Callback Router ----- #
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all inline keyboard button callbacks"""
    query = update.callback_query
    if not query:
        return

    callback_data = query.data
    logger.info(f"Button clicked: {callback_data}")

    # Import handlers from menu
    from bot.handlers.menu import show_text_usage, show_file_usage, show_voice_usage, show_purpose, show_better_experience

    # Main menu callbacks
    if callback_data == "main_menu":
        await show_main_menu(query, context)
    
    # New Burmese menu callbacks
    elif callback_data == "text_usage":
        # Convert query to update format for menu handlers
        fake_update = type('obj', (object,), {'message': type('obj', (object,), {'reply_photo': query.message.reply_photo})()})()
        await show_text_usage(fake_update, context)
    elif callback_data == "file_usage":
        fake_update = type('obj', (object,), {'message': type('obj', (object,), {'reply_photo': query.message.reply_photo})()})()
        await show_file_usage(fake_update, context)
    elif callback_data == "voice_usage":
        fake_update = type('obj', (object,), {'message': type('obj', (object,), {'reply_photo': query.message.reply_photo})()})()
        await show_voice_usage(fake_update, context)
    elif callback_data == "purpose":
        fake_update = type('obj', (object,), {'message': type('obj', (object,), {'reply_photo': query.message.reply_photo})()})()
        await show_purpose(fake_update, context)
    elif callback_data == "better_experience":
        fake_update = type('obj', (object,), {'message': type('obj', (object,), {'reply_text': query.message.reply_text})()})()
        await show_better_experience(fake_update, context)
    
    # Fallback for unhandled callbacks
    else:
        await query.answer("🔧 This feature is coming soon! Ask me directly instead.", show_alert=True)
