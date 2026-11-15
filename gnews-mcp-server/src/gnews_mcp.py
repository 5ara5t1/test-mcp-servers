from fastmcp import FastMCP


## Creating FastMCP Object
mcp = FastMCP("GNews MCP Server")

## Example tool given my main website
@mcp.tool
def get_top_10_headlines():
    """This tool gathers the top 10 english headlines in the united states. you must provide a GNews API key as an environment variable. A json array of raw data will be returned from gnews."""
    pass


if __name__ == "__main__":
    mcp.run()