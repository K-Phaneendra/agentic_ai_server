from dotenv import load_dotenv
from fastapi import FastAPI
from src.orchestrator import Orchestrator

load_dotenv()

app = FastAPI(title="AgenticAI with MCP Servers")

orchestrator = Orchestrator()

@app.post("/chat")
async def chat(session_id: str, message: str):
    return await orchestrator.handle(session_id, message)
