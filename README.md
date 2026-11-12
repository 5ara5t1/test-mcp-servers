# test-mcp-servers

Small Model Context Protocol (MCP) servers in Python, written while working through a [Udemy course on building MCP servers](https://www.udemy.com/course/complete-mcp-developer-guide-ai-agents-servers-tools).

Status: early. Course work in progress, cleanup to follow.

## What's here

`mcp-server/` is a minimal MCP server that exposes one tool, `get_documentation_from_database`, over stdio. The tool returns mocked data for now. It is a uv package with pytest tests.

## Run it

```
cd mcp-server
uv sync
uv run pytest
uv run python -m mcp_server.mcp_server
```
