from src.mcp_clients import news

class NewsAgent:
    async def execute(self, query: str):
        return await news.query({"text": query})
