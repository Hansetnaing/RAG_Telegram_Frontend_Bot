"""
Chat message handler for Legal Compliance & Cybersecurity RAG Bot
Handles text, voice, audio, and document messages
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from bot.services.rag_api import query_text
from bot.handlers.menu import handle_reply_keyboard_text

logger = logging.getLogger(__name__)


async def chat_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming chat messages (text, voice, audio, documents)"""
    
    # First check if it's a reply keyboard button press
    if update.message.text:
        keyboard_handled = await handle_reply_keyboard_text(update, context)
        if keyboard_handled:
            return
    
    # Handle different message types
    if update.message.text:
        await handle_text_message(update, context)
    elif update.message.voice:
        await handle_voice_message(update, context)
    elif update.message.audio:
        await handle_audio_message(update, context)
    elif update.message.document:
        await handle_document_message(update, context)
    else:
        await update.message.reply_text(
            "🤔 I can help with text questions, voice messages, audio files, and documents. "
            "What would you like to know about legal compliance or cybersecurity?"
        )


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages using RAG API"""
    user_message = update.message.text
    user_id = update.effective_user.id
    
    logger.info(f"Processing text message from user {user_id}: {user_message[:50]}...")
    
    try:
        # Show typing indicator
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
        
        # Query the RAG API
        response = await query_text(user_message, user_id)
        
        # Send response
        await update.message.reply_text(
            response,
            parse_mode='HTML'
        )
        
    except Exception as e:
        logger.error(f"Error processing text message: {e}")
        await update.message.reply_text(
            "⚠️ Sorry, I encountered an error processing your question. "
            "Please try again or use /help for assistance."
        )


async def handle_voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle voice messages"""
    await update.message.reply_text(
        "🎤 <b>Voice Message Received</b>\n\n"
        "Voice message processing is coming soon! For now, please:\n\n"
        "• Type your question as text\n"
        "• Use our mobile/web apps for voice features\n"
        "• Check /menu for quick actions\n\n"
        "💡 <i>Ask me anything about legal compliance or cybersecurity!</i>",
        parse_mode='HTML'
    )


async def handle_audio_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle audio files"""
    await update.message.reply_text(
        "🎵 <b>Audio File Received</b>\n\n"
        "Audio file processing is coming soon! For now, please:\n\n"
        "• Type your question as text\n"
        "• Use our mobile/web apps for audio features\n"
        "• Check /menu for quick actions\n\n"
        "💡 <i>Ask me anything about legal compliance or cybersecurity!</i>",
        parse_mode='HTML'
    )


async def handle_document_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle document uploads"""
    document = update.message.document
    file_name = document.file_name
    file_size = document.file_size
    
    await update.message.reply_text(
        f"📄 <b>Document Received: {file_name}</b>\n\n"
        f"Size: {file_size:,} bytes\n\n"
        "Document analysis is coming soon! For now, please:\n\n"
        "• Ask questions about the document content as text\n"
        "• Use our mobile/web apps for full document processing\n"
        "• Check /menu for document templates\n\n"
        "💡 <i>Try asking: 'I need a privacy policy template'</i>",
        parse_mode='HTML'
    )
