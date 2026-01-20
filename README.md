  
  
To install the following 'add_tool' MCP server, run the following command:

'''json
  {
  "mcpServers": {
    "ServerTest": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/jimevansv/mcpservertest.git",
        "mcp-server"
      ]
    }
  }
}'''