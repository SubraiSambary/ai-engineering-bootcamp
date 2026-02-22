from tools.base_tool import BaseTool

class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Performs basic mathematical calculations. Input should be a valid Python arithmetic expression."

    def run(self, input_text: str) -> str:
        try:
            result = eval(input_text)
            return str(result)
        except Exception as e:
            return f"Error evaluating expression: {str(e)}"