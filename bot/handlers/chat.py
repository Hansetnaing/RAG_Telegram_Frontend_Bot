from datetime import datetime
import random
from telegram import Update
from telegram.ext import ContextTypes
from bot.services.rag_api import query_text, query_text_with_file, upload_file, speech_to_text
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
            
            # ##################

            # Save audio file in OGG format
            
            # try:
            #     # Create audio directory if it doesn't exist
            #     audio_dir = Path("audio_files")
            #     audio_dir.mkdir(exist_ok=True)
                
            #     # Generate unique filename with timestamp
            #     user_id = update.effective_user.id
            #     ogg_filename = f"audio_{user_id}_{random.randint(100000,999999)}.ogg"
            #     ogg_path = audio_dir / ogg_filename
                
            #     # Save the audio file
            #     with open(ogg_path, 'wb') as f:
            #         f.write(file_bytes)
                
            #     logging.info(f"Audio file saved: {ogg_path}")
            #     print(f"Audio file saved: {ogg_path}")
                
            # except Exception as e:
            #     logging.error(f"Error saving audio file: {e}")
            #     print(f"Error saving audio file: {e}")
            # ##################

            result = await speech_to_text(bytes(file_bytes), filename)
            print("Voice to text result: ", result)
            if "error" in result:
                await message.reply_text(f"❌ Speech error: {result['error']}")
            else:
                await message.reply_text(f"🗣️ {result.get('transcription', '')}\n\n{result.get('response', '')}")
            return

        # 2. File (document)
        if message.document:
            logging.info("Processing document message")
            file_obj = await message.document.get_file()
            file_bytes = await file_obj.download_as_bytearray()
            filename = message.document.file_name
            # File with caption (text + file)
            if message.caption:
                print("Caption ", message.caption)
                response = await query_text_with_file(message.caption, bytes(file_bytes), filename)
                await message.reply_text(response)
            else:
                result = await upload_file(bytes(file_bytes), filename)
                print("Uploaded ", filename)
                if "error" in result:
                    await message.reply_text(f"❌ File upload error: {result['error']}")
                else:
                    await message.reply_text(f"✅ {result.get('message', 'File uploaded.')}")
            return

        # 3. Text only
        if message.text:
            logging.info("Processing text message")
            response = await query_text(message.text)
            logging.info(f"Response: {response}")
            await message.reply_text(response)
            return

        # 4. Unsupported
        await message.reply_text("❌ Unsupported message type. Please send text, a document, or an audio message.")
    except Exception as e:
        logging.error(f"Error in chat_message: {e}")
        await message.reply_text("❌ Sorry, something went wrong. Please try again later.") 