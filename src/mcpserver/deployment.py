from mcp.server.fastmcp import FastMCP

# create an MCP server instance
mcp = FastMCP("Demo")

#Add an additional tool
@mcp.tool()
def add(int_a: int, int_b: int) -> int:
    """Add two integers together."""
    return int_a + int_b

