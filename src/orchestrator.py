import asyncio
from src.agents.intent_decomposer_agent import IntentDecomposerAgent
from src.agents.summarizer_agent import SummarizerAgent
from src.agents.sales_agent import SalesAgent
from src.agents.news_agent import NewsAgent
from src.agents.support_agent import SupportAgent
from src.memory import ConversationMemory

class Orchestrator:
    def __init__(self):
        self.memory = ConversationMemory()
        self.decomposer = IntentDecomposerAgent()
        self.summarizer = SummarizerAgent()

        self.agents = {
            "sales": SalesAgent(),
            "news": NewsAgent(),
            "support": SupportAgent(),
        }

    async def handle(self, session_id: str, text: str):
        self.memory.append(session_id, text)
        history = self.memory.get(session_id)

        tasks = await self.decomposer.decompose(text, history)

        async def run_task(task):
            agent = self.agents.get(task["target"])
            if not agent:
                return {"error": f"No agent for {task['target']}"}
            try:
                return await agent.execute(task["query"])
            except Exception as e:
                return {"fallback": str(e)}

        results = await asyncio.gather(
            *[run_task(t) for t in tasks],
            return_exceptions=False
        )

        answer = await self.summarizer.summarize(text, results)

        return {
            "answer": answer,
            "used_agents": [t["target"] for t in tasks],
            "results": results
        }
