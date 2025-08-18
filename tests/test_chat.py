import pytest
import asyncio
from unittest.mock import AsyncMock, patch
from bot.services.rag_api import query_rag

@pytest.mark.asyncio
async def test_query_rag_success():
    mock_response = {"response": "Hello!"}
    with patch("httpx.AsyncClient.post") as mock_post:
        mock_post.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)
        mock_post.return_value.__aenter__.return_value.raise_for_status = AsyncMock()
        result = await query_rag("Hi")
        assert result == "Hello!"

@pytest.mark.asyncio
async def test_query_rag_error():
    with patch("httpx.AsyncClient.post", side_effect=Exception("API down")):
        result = await query_rag("Hi")
        assert "RAG API error" in result

# Test the chat_message handler (integration style)
import types
from bot.handlers import chat as chat_handler

class DummyMessage:
    def __init__(self, text):
        self.text = text
        self.replied = None
    async def reply_text(self, text):
        self.replied = text

class DummyBot:
    async def send_chat_action(self, chat_id, action):
        pass

class DummyUpdate:
    def __init__(self, text):
        self.message = DummyMessage(text)
        self.effective_chat = types.SimpleNamespace(id=123)

class DummyContext:
    def __init__(self):
        self.bot = DummyBot()

@pytest.mark.asyncio
async def test_chat_message_success(monkeypatch):
    async def mock_query_rag(query):
        return "Test response"
    monkeypatch.setattr(chat_handler, "query_rag", mock_query_rag)
    update = DummyUpdate("Hello")
    context = DummyContext()
    await chat_handler.chat_message(update, context)
    assert update.message.replied == "Test response"

@pytest.mark.asyncio
async def test_chat_message_error(monkeypatch):
    async def mock_query_rag(query):
        raise Exception("fail")
    monkeypatch.setattr(chat_handler, "query_rag", mock_query_rag)
    update = DummyUpdate("Hello")
    context = DummyContext()
    await chat_handler.chat_message(update, context)
    assert "Sorry, something went wrong" in update.message.replied 