"""Protocol tests: talk to the server through a real MCP client (see conftest.py)."""

import json

import pytest

TOOL = "get_documentation_from_database"

pytestmark = pytest.mark.anyio


async def get_tool(client, name):
    tools = await client.list_tools()
    return next((t for t in tools.tools if t.name == name), None)


async def test_tool_is_listed(client):
    assert await get_tool(client, TOOL) is not None


async def test_tool_has_a_description_for_the_model(client):
    tool = await get_tool(client, TOOL)
    assert tool.description and tool.description.strip()


async def test_tool_takes_no_required_arguments(client):
    tool = await get_tool(client, TOOL)
    assert tool.input_schema.get("required", []) == []


async def test_calling_tool_returns_the_doc(client):
    result = await client.call_tool(TOOL)

    assert not result.is_error
    # A plain `-> dict` return comes back as JSON text, not structured_content.
    doc = json.loads(result.content[0].text)
    assert doc["source"] == "mocked_database"


async def test_unknown_tool_returns_an_error_result(client):
    result = await client.call_tool("does_not_exist")

    assert result.is_error
    assert "Unknown tool" in result.content[0].text
