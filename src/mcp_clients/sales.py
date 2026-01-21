import os
import httpx
import msgspec
from datetime import date
from typing import Literal, TypedDict, Optional

SALES_MCP_URL = os.getenv("SALES_MCP_URL")

if not SALES_MCP_URL:
    raise RuntimeError("SALES_MCP_URL environment variable is not set")

class TimeRange(TypedDict):
    # Using 'date' type ensures YYYY-MM-DD validation
    start: date
    end: date

class Payload(msgspec.Struct):
    metrics: list[str]
    dimensions: list[str]
    filters: dict[Literal["sales_person", "country", "product", "date"], str]
    time_range: TimeRange
    limit: Optional[int] = None

async def query(payload: Payload):
    """
    Executes a POST request to the Sales MCP server.
    """

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(
            SALES_MCP_URL,
            json=payload,
        )
        response.raise_for_status()
        return response.json()
