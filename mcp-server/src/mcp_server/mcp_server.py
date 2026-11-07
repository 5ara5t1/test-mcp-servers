from mcp.server.mcpserver import MCPServer

# Create a fast mcp server instance
mcp = MCPServer("mcp-documentation-server")

# Register the fool using the FastMCP decorator
@mcp.tool()
def get_documentation_from_database() -> dict:
    """
    This tool returns the documentation for the project. It is very
    Useful for figuring out what the documentation is about
    """
    ### Actual implementation using a real database here
    return {
        "title":"How to use MCP Servers",
        "body": "This is the mocked documentation from the database. MCP servers expose tooling for ai systems and allow them to execute commands remotely.",
        "source": "mocked_database"
    }

def main():
    mcp.run("stdio")

if __name__ == "__main__":
    main()