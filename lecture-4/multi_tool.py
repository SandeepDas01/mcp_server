#multi tool
#ping
#add


from mcp.server.fastmcp import FastMCP, Context

# MCP server banaya
server = FastMCP("demo-server")


# Tool define kiya
@server.tool()
def ping(ctx: Context) -> str:
    """Check if server is alive"""
    return "ping"

@server.tool()
def add(ctx: Context, a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


dummy_ctx = Context()

# ping test
print(ping(dummy_ctx))

# add test
print(add(dummy_ctx, 20, 25))
