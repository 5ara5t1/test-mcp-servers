
from gnews_mcp import mcp, get_top_10_headlines
from fastmcp import FastMCP
import asyncio

EXPECTED_TOOL_DOCSTRING_DESCRIPTION = "This tool gathers the top 10 english headlines in the united states. you must provide a GNews API key as an environment variable. A json array of raw data will be returned from gnews."

## HELPER FUNCTION: get tool names
def get_tool_names_from_MCP_Server(mcp_server) -> list[str]:
    tools = asyncio.run(mcp_server.list_tools())
    return [t.name for t in tools]

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
    toolNames = get_tool_names_from_MCP_Server(mcp)
    assert "get_top_10_headlines" in toolNames

def test_tool_has_docstring_instructions():
    # List and grab tool by name
    tools = asyncio.run(mcp.list_tools())
    top_10_headlines = next((t for t in tools if t.name == "get_top_10_headlines"), None)

    # Confirm tool exist
    assert top_10_headlines is not None

    assert top_10_headlines.description == EXPECTED_TOOL_DOCSTRING_DESCRIPTION
