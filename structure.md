telegram_bot/
│
├── bot/
│   ├── __init__.py
│   ├── main.py             # Entry point for the bot
│   ├── config.py           # Configuration (API keys, settings)
│   ├── handlers/           # Telegram command/message handlers
│   │   ├── __init__.py
│   │   ├── start.py
│   │   ├── help.py
│   │   └── chat.py         # Handles chat, calls RAG API
│   ├── services/           # Integrations (RAG API, DB, etc.)
│   │   ├── __init__.py
│   │   └── rag_api.py      # Logic for calling your RAG API
│   ├── utils/              # Utility functions (logging, helpers)
│   │   ├── __init__.py
│   │   └── logger.py
│
├── tests/
│   ├── __init__.py
│   └── test_chat.py
│
├── requirements.txt
├── README.md
└── .env