import logging
import httpx
import os
from typing import Optional

RAG_API_BASE = os.getenv("RAG_API_URL", "http://127.0.0.1:8000/api/v2")

async def query_text(query: str) -> str:
    url = f"{RAG_API_BASE}/text"
    logging.debug(f"Querying RAG API with URL: {url}")
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url, json={"query": query}, timeout=30)
            print("Status code:", resp.status_code)
            print("Response text:", resp.text)
            resp.raise_for_status()
            data = resp.json()
            return data.get("response", "[No response from RAG API]")
        except Exception as e:
            import traceback
            traceback.print_exc()
            return f"[RAG API error: {e}]"


# async def query_text(query: str) -> str:
#     url = f"{RAG_API_BASE}/text"
#     logging.debug(f"Querying RAG API with URL: {url}")
#     async with httpx.AsyncClient() as client:
#         try:
#             resp = await client.post(url, json={"query": query}, timeout=30)
#             resp.raise_for_status()
#             data = resp.json()
#             return data.get("response", "[No response from RAG API]")
#         except Exception as e:
#             return f"[RAG API error: {e}]"

async def query_text_with_file(query: str, file_bytes: bytes, filename: str) -> str:
    url = f"{RAG_API_BASE}/text-with-file"
    files = {"file": (filename, file_bytes)}
    data = {"query": query}
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url, data=data, files=files, timeout=60)
            resp.raise_for_status()
            data = resp.json()
            return data.get("response", "[No response from RAG API]")
        except Exception as e:
            return f"[RAG API error: {e}]"

async def upload_file(file_bytes: bytes, filename: str) -> dict:
    url = f"{RAG_API_BASE}/file"
    files = {"file": (filename, file_bytes)}
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url, files=files, timeout=60)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

async def speech_to_text(audio_bytes: bytes, filename: str) -> dict:
    url = f"{RAG_API_BASE}/speech"
    files = {"audio_file": (filename, audio_bytes)}
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url, files=files, timeout=60)
            logging.critical(f"Speech to text response: {resp.json()}")
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            return {"error": str(e)} 