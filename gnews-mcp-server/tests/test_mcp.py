
from gnews_mcp import mcp, get_top_10_headlines
from fastmcp import FastMCP, Client
import asyncio
from fastmcp.exceptions import ToolError
import pytest
import inspect
from pathlib import Path
import httpx
import json

EXPECTED_TOOL_DOCSTRING_DESCRIPTION = "This tool gathers the top 10 english headlines in the united states. you must provide a GNews API key as an environment variable. A json array of raw data will be returned from gnews."
EXPECTED_TOOL_TOP_10_HEADLINES_FUNCTION_PARAMETERS = {'category', 'language', 'country'}
TEST_PARAMATER_CATEGORY = "Technology"
TEST_PARAMATER_LANGUAGE = "en"
TEST_PARAMATER_COUNTRY = "us"



### FIXTURES
FIXTURES = Path(__file__).parent / "fixtures"
GNEWS_ROUTE = dict(host="gnews.io", path="/api/v4/top-headlines")

@pytest.fixture
def headlines_payload():
    return json.loads((FIXTURES / "top_headlines.json").read_text())

@pytest.fixture
def api_key(monkeypatch):
    monkeypatch.setenv("GNEWS_API_KEY", "test-key-123")
    return "test_key_123"



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

def test_get_top_10_headlines_tool_has_parameters():

    function_signature = inspect.signature(get_top_10_headlines)
    param_names = list(function_signature.parameters.keys())
    assert EXPECTED_TOOL_TOP_10_HEADLINES_FUNCTION_PARAMETERS.issubset(param_names)
    

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

# Using monkeypatch to set empty environment variable
@pytest.mark.asyncio
async def test_fetch_top_10_headlines_missing_environment_error(monkeypatch):
    # Delete enviroment varailbe if it exists already
    monkeypatch.delenv("GNEWS_API_KEY", raising=False)
    
    with pytest.raises(ToolError, match="ERROR: EMPTY GNEWS_API_KEY ENVIRONMENT_VARIABLE"):
        await get_top_10_headlines(category=TEST_PARAMATER_CATEGORY, language=TEST_PARAMATER_LANGUAGE, country=TEST_PARAMATER_COUNTRY)

@pytest.mark.asyncio
async def test_returns_articles_from_gnews(respx_mock, api_key, headlines_payload):
    respx_mock.get(**GNEWS_ROUTE).mock(
        return_value=httpx.Response(200, json=headlines_payload)
    )

    result = await get_top_10_headlines(category=TEST_PARAMATER_CATEGORY, language=TEST_PARAMATER_LANGUAGE, country=TEST_PARAMATER_COUNTRY)

    assert result == headlines_payload["articles"]



# FUNCTIONAL_TESTS
@pytest.mark.asyncio
async def test_missing_key_via_client(monkeypatch):
    monkeypatch.delenv("GNEWS_API_KEY", raising=False)

    async with Client(mcp) as client:
        with pytest.raises(ToolError):
            await client.call_tool("get_top_10_headlines", {"category": TEST_PARAMATER_CATEGORY, "language": TEST_PARAMATER_LANGUAGE, "country": TEST_PARAMATER_COUNTRY})