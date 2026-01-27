# from src.llm import run_llm
from src.mcp_clients import anomaly

class AnomalyAgent:
    async def execute(self, query: str):
        # TODO: identify user message from the given text and create payload
        # response = await run_llm(system=system, user=user_message)
        payload = {}
        return await anomaly.query(payload)
