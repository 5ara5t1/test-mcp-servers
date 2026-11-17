from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
import os
import asyncio



## Creating FastMCP Object
mcp = FastMCP("GNews MCP Server")

## Example tool given my main website
@mcp.tool
async def get_top_10_headlines(category: str, language: str):
    """This tool gathers the top 10 english headlines in the united states. you must provide a GNews API key as an environment variable. A json array of raw data will be returned from gnews."""
    if "GNEWS_API_KEY" not in os.environ:
        raise ToolError("ERROR: EMPTY GNEWS_API_KEY ENVIRONMENT_VARIABLE")
    return None


if __name__ == "__main__":
    mcp.run()