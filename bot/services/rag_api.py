import logging
import httpx
import os

# Base URL for your RAG API
RAG_API_BASE = os.getenv("RAG_API_URL", "http://127.0.0.1:8000/api/v2/telegram")

# Friendly messages to show to end users
USER_FRIENDLY_ERRORS = {
    404: "Sorry, the service is temporarily unavailable. Please try again later.",
    500: "Our system had an internal issue. We’re fixing it, please try again soon.",
    "http": "There was a network issue. Please check your connection and try again.",
    "unknown": "Something went wrong. Please try again later."
}

def format_status_error(resp: httpx.Response) -> str:
    """Return a friendly error for the user based on status code."""
    return USER_FRIENDLY_ERRORS.get(resp.status_code, USER_FRIENDLY_ERRORS["unknown"])


# Text Query Handler
async def query_text(query: str) -> str:
    url = f"{RAG_API_BASE}/text"
    data = {"query": query}
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url, data=data, timeout=30)
            if resp.status_code == 200:
                return resp.json().get("response", "[No response from RAG API]")
            else:
                logging.error(f"RAG API error {resp.status_code}: {resp.text}")
                return resp.json().get("detail", format_status_error(resp))
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return USER_FRIENDLY_ERRORS["unknown"]


# File + Text Query Handler
async def query_text_with_file(query: str, file_bytes: bytes, filename: str) -> dict:
    url = f"{RAG_API_BASE}/file"
    files = {"file": (filename, file_bytes)}
    data = {"query": query}
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url, data=data, files=files, timeout=60)
            if resp.status_code == 200:
                return resp.json()
            else:
                logging.error(f"RAG API error {resp.status_code}: {resp.text}")
                return {"detail": resp.json().get("detail", format_status_error(resp))}
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return {"detail": USER_FRIENDLY_ERRORS["unknown"]}


# Speech Query Handler
async def speech_to_text(audio_bytes: bytes, filename: str) -> dict:
    url = f"{RAG_API_BASE}/speech"
    files = {"audio_file": (filename, audio_bytes)}
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url, files=files, timeout=60)
            if resp.status_code == 200:
                return resp.json()
            else:
                logging.error(f"RAG API error {resp.status_code}: {resp.text}")
                return {"detail": resp.json().get("detail", format_status_error(resp))}
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return {"detail": USER_FRIENDLY_ERRORS["unknown"]}


