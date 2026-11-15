
from gnews_mcp import mcp, get_top_10_headlines
from fastmcp import FastMCP
import asyncio

## Simple demo test to test pytest
def test_MCP_object_created():
    assert mcp is not None
    assert mcp.name == "GNews MCP Server"


# test mcp tool functionality, 
def test_get_top_10_headlines_tool_exists_and_is_mcp_tool():
    # Verify tool exists and is callable
    assert get_top_10_headlines is not None
    assert callable(get_top_10_headlines)

def test_get_top_10_headlines_tool_is_registerd_as_mcp_tool():
    tools = asyncio.run(mcp.list_tools())
    tool_names = [t.name for t in tools]
    assert "get_top_10_headlines" in tool_names
