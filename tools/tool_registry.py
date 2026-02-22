from tools.calculator import CalculatorTool

class ToolRegistry:
    def __init__(self):
        self._tools = {}
        self._regiter_default_tools()

    def _regiter_default_tools(self):
        """ 
        Registers all default tools available to the agent.
        """

        calculator=CalculatorTool()
        self._tools[calculator.name] = calculator

    def get_tool(self, tool_name: str):
        """ 
        Returns the tool instance if found.
        """
        return self._tools.get(tool_name)
    
    def list_tools(self):
        """ 
        Returns a list of available tools.
        """
        return list(self._tools.keys())