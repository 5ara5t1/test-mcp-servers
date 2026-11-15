from fastmcp import FastMCP


## Creating FastMCP Object
mcp = FastMCP("GNews MCP Server")

## Example tool given my main website
@mcp.tool
def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    mcp.run()