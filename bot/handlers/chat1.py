import re

def escape_markdown_v2(text: str) -> str:
    """
    Escape Telegram MarkdownV2 special characters except those used for valid formatting.
    - Preserves **bold**, *italic*, and bullet points.
    - Escapes other unsafe characters.
    """
    if not isinstance(text, str):
        text = str(text)
    # Escape all MarkdownV2 special chars except asterisks used for bold/italic and bullets
    # Do not escape asterisks that are part of **bold** or *italic* or at start of line (bullets)
    # Escape: _ [ ] ( ) ~ ` > # + - = | { } . !
    # First, escape all except *, then handle *
    escape_chars = r'_ [ ] ( ) ~ ` > # + - = | { } . !'
    for char in escape_chars.split():
        text = text.replace(char, f'\\{char}')
    # Now escape asterisks not part of bold/italic or bullet
    # Replace single * not surrounded by word chars or at start of line
    def asterisk_replacer(match):
        s = match.group(0)
        # If it's ** or * at start of line, don't escape
        if s == '**' or s == '*' or s.startswith('* '):
            return s
        return '\*'
    # Escape single * not part of **bold** or *italic* or bullet
    text = re.sub(r'(?<!\*)\*(?!\*)', asterisk_replacer, text)
    return text
from datetime import datetime
import random
from telegram import Update
from telegram.ext import ContextTypes
from bot.services.rag_api import query_text, query_text_with_file, speech_to_text  # remove upload_file

import logging

from pathlib import Path

from bot.utils import logger

async def chat_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    message = update.message
    logging.info(f"Message type: {type(message)}")
    logging.info(f"Voice: {message.voice}")
    logging.info(f"Audio: {message.audio}")
    logging.info(f"Document: {message.document}")
    logging.info(f"Text: {message.text}")
    logging.info(f"Caption: {message.caption}")
    

    try:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

        # 1. Speech (voice or audio)
        if message.voice or message.audio:
            logging.info("Processing voice/audio message")
            file = message.voice or message.audio
            file_obj = await file.get_file()
            file_bytes = await file_obj.download_as_bytearray()
            filename = file.file_name if hasattr(file, 'file_name') and file.file_name else f"audio.{file.mime_type.split('/')[-1]}"
            result = await speech_to_text(bytes(file_bytes), filename)
            print("Voice to text result: ", result)
            if "error" in result:
                await message.reply_text(escape_markdown_v2(f"❌ Speech error: {result['error']}"), parse_mode="MarkdownV2")
            else:
                transcription = escape_markdown_v2(result.get('transcription', ''))
                response_text = escape_markdown_v2(result.get('response', ''))
                await message.reply_text(f"🗣️ {transcription}\n\n{response_text}", parse_mode="MarkdownV2")
            return

        # 2. File (document)
        if message.document:
            logging.info("Processing document message")
            file_obj = await message.document.get_file()
            file_bytes = await file_obj.download_as_bytearray()
            filename = message.document.file_name
            # File with caption (text + file)
            query = message.caption if message.caption else "What is this document about?"
            response = await query_text_with_file(query, bytes(file_bytes), filename)
            if isinstance(response, dict):
                reply = response.get("response", str(response))
            else:
                reply = str(response)
            await message.reply_text(escape_markdown_v2(reply), parse_mode="MarkdownV2")
            return

        # 4. Text only
        if message.text:
            logging.info("Processing text message")
            response = await query_text(message.text)
            logging.info(f"Response: {response}")
            await message.reply_text(escape_markdown_v2(response), parse_mode="MarkdownV2")
            return

        # 4. Unsupported
        await message.reply_text(escape_markdown_v2("❌ Unsupported message type. Please send text, a document, or an audio message."), parse_mode="MarkdownV2")
    except Exception as e:
        logging.error(f"Error in chat_message: {e}")
        await message.reply_text(escape_markdown_v2("❌ Sorry, something went wrong. Please try again later."), parse_mode="MarkdownV2")