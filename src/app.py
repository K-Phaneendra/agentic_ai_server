import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
env_file = os.path.join(BASE_DIR, ".env")
load_dotenv(env_file)

from fastapi import FastAPI
from src.orchestrator import Orchestrator

app = FastAPI(title="AgenticAI with MCP Servers")

orchestrator = Orchestrator()

@app.post("/chat")
async def chat(session_id: str, message: str):
    return await orchestrator.handle(session_id, message)
