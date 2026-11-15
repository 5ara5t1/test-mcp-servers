
from gnews_mcp import *
from fastmcp import FastMCP

## Simple demo test to test pytest
def test_MCP_object_created():
    assert mcp is not None
    assert mcp.name == "GNews MCP Server"


def test_example_mcp_tool():
    assert add(1, 2) == 3