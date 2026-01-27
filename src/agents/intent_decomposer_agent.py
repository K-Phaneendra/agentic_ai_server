import json
from src.llm import run_llm

class IntentDecomposerAgent:
    async def decompose(self, text: str, memory: list[str]):
        system = """
You are an intent decomposition agent.

Your job is to break a user request into independent tasks.
Each task must target exactly ONE system.

Allowed targets:
- sales
- news
- support
- anomaly

Details of targets:
- sales: related to sales information
- anomaly: identify anomaly of a specific metric

Rules:
- Return ONLY valid JSON
- Do NOT add explanations
- If no tasks apply, return an empty array []

Output format:
[
  {"target": "sales|news|support|anomaly", "query": "specific task"}
]
"""

# TODO: can add conversation history
#         user_prompt = f"""
# Conversation history:
# {memory}

# User request:
# {text}
# """
        user_prompt = f"""
User request:
{text}
"""

        response = await run_llm(system=system, user=user_prompt)

        if not response.strip():
            raise RuntimeError("LLM returned empty response for intent decomposition")

        return json.loads(response)
