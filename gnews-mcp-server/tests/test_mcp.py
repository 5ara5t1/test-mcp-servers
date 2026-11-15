
from gnews_mcp import mcp
from fastmcp import FastMCP

## Simple demo test to test pytest
def test_verify_pytest_works():
    assert type(mcp) is type(FastMCP())