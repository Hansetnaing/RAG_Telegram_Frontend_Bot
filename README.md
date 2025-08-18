# Telegram RAG Chatbot

A production-ready Telegram chatbot that uses a Retrieval-Augmented Generation (RAG) API for answering user queries.

## Features
- Handles /start, /help, and chat messages
- Integrates with a RAG API for intelligent responses
- Supports file uploads and advanced features (see API docs)
- Production-ready: error handling, logging, config via .env

## Setup

1. **Clone the repo and enter the directory:**
   ```bash
   git clone <repo-url>
   cd telegram_bot
   ```

2. **Create and edit your `.env` file:**
   ```env
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token-here
   RAG_API_URL=http://localhost:8000/text
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the bot:**
   ```bash
   source env/Scripts/activate
   python -m bot.main
   ```

## Project Structure
See `structure.md` for a detailed breakdown.

## API Reference
See `api_doc.md` for backend API endpoints.

## Notes
- Make sure your RAG API is running and accessible at the URL specified in `.env`.
- For production, use a process manager (e.g., systemd, pm2, Docker) and secure your environment variables. 