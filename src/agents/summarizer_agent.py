from src.llm import run_llm

class SummarizerAgent:
    async def summarize(self, question: str, results: list):
        system = """
Combine multiple tool outputs into a single accurate response.
Clearly mention any missing or unavailable data.
"""
        return await run_llm(system, f"Question: {question}\nResults: {results}")
