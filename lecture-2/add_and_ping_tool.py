# Simple tool: ping
@mcp.tool()
def ping(ctx: Context) -> str:
    """Check if server is alive"""
    return "pong"

# Math tool
@mcp.tool()
def add(ctx: Context, a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b
