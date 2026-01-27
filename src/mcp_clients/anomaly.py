import os
import httpx

ANOMALY_MCP_URL = os.getenv("ANOMALY_MCP_URL")

if not ANOMALY_MCP_URL:
    raise RuntimeError("ANOMALY_MCP_URL environment variable is not set")

async def query(payload: dict):
    """
    Executes a POST request to the Anomaly MCP server.
    """

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(
            ANOMALY_MCP_URL+"/",
            # json=payload, # TODO: to pass payload and convert this into post query
        )
        response.raise_for_status()
        return response.json()

