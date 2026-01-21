from src.mcp_clients import support

class SupportAgent:
    async def execute(self, query: str):
        return await support.query({"text": query})
