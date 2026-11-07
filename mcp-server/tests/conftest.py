import pytest
from mcp import Client

from mcp_server.mcp_server import mcp


@pytest.fixture
def anyio_backend():
    # anyio's pytest plugin (installed with mcp) runs @pytest.mark.anyio tests on this backend.
    return "asyncio"


@pytest.fixture
async def client():
    # Connects a real MCP client to the server in-process: no subprocess, no stdio.
    async with Client(mcp) as c:
        yield c
