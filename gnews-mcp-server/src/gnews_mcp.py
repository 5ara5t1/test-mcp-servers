from fastmcp import FastMCP


## Creating FastMCP Object
mcp = FastMCP("GNews MCP Server")

## Example tool given my main website
@mcp.tool
def get_top_10_headlines():
    pass


if __name__ == "__main__":
    mcp.run()