import os
from openai import AsyncOpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY environment variable is not set")

client = AsyncOpenAI(api_key=OPENAI_API_KEY)


async def run_llm(system: str, user: str) -> str:
    """
    Executes a chat completion call and returns the assistant text.
    This function is intentionally simple and deterministic.
    """

    response = await client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        max_completion_tokens=500,
    )

    return response.choices[0].message.content.strip()
