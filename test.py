from tools.tool_registry import ToolRegistry

registry = ToolRegistry()

print("Available tools:", registry.list_tools())

tool = registry.get_tool("calculator")
print(tool.run("5 * 10"))