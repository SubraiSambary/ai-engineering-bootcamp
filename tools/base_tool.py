class BaseTool:
    name = "base_tool"
    description = "Base tool interface"

    def run(self, input_text: str) -> str:
        """
        Executes the tool logic.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Tool must implement run() menthod")