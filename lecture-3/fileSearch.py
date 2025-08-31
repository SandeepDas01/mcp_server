import os
from pathlib import Path
from mcp.server.fastmcp import FastMCP, Context

# MCP server banaya
server = FastMCP("fs-server")

# Tool define kiya
@server.tool()
def search_file(ctx: Context, filename: str, path: str = "/content") -> str:
  
    start_dir = Path(path)
    if not start_dir.exists() or not start_dir.is_dir():
        return f"⚠️ Invalid directory: {path}"

    matches = []
    for root, dirs, files in os.walk(start_dir):
        if filename in files:
            full_path = os.path.join(root, filename)
            matches.append(full_path)

    if matches:
        return "✅ Found:\n" + "\n".join(matches)
    else:
        return f"❌ File '{filename}' not found under {path}"


#test
print(search_file(None, "README.md"))  
