from mcp.server.fastmcp import FastMCP

# create an MCP server instance
mcp = FastMCP("Demo")

#Add an additional tool
@mcp.tool()
def add(int_a: int, int_b: int) -> str:
    """Add two integers together and display a message and the result."""
    c = int_a + int_b
    return f"Say hi to Andy!!! - from John Mama.\nThe answer for the addition is: {c}"

