import json
from core.llm_client import call_llm_json
from tools.tool_registry import ToolRegistry
from core.retrieval_service import RetrievalService

class BasicAgent:

    def __init__(self,goal, llm_client, retrieval_service: RetrievalService):
        self.goal = goal
        self.memory = []
        self.finished = False
        #self.plan_generated = False
        #self.plan = []
        #self.current_step = 0
        self.tool_registry = ToolRegistry()
        self.llm_client = llm_client
        self.retrieval_service = retrieval_service


    def think(self):
        # Retrieve relevant context
        retrieved_docs = self.retrieval_service.retrieve(self.goal, top_k=3)
        context = "\n\n".join([doc["text"] for doc in retrieved_docs])

        prompt = f""" 
        You are a ReAct agent.
        You can think step-by-step.
        You can use tools when needed.

        Relevant Knowledge:
        {context}

        Available tools:
        - calculator: use for ANY math calculation

        Your goal: {self.goal}
        Your previous steps: {self.memory}

        Return only VALID JSON in one of these formats:
        If Reasoning:
        {{
            "type": "thought",
            "content": "your reasoning here"
        }}

        If using a tool:
        {{
            "type": "tool",
            "tool_name": "calculator",
            "input": "<math expression>"
        }}  
        if you have a final answer:
        {{
            "type": "final",
            "final_answer": "your final answer here"
        }}
        """
        messages = [{"role": "user", "content": prompt}]
        return call_llm_json(messages)
    
    def run(self, max_iterations=10):
        
        for i in range(max_iterations):
            print(f"\nInteration {i+1}")

            decision = self.think()

            if not isinstance(decision, dict):
                print("Invalid Response: ",decision)
                break

            if decision["type"] == "thought":
                print("Thought: ", decision["content"])
                self.memory.append({"type": "thought", "content": decision["content"]})
            
            elif decision["type"] == "action":
                tool_name = decision["tool_name"]
                tool_input = decision["input"]
                print(f"Action: {tool_name}({tool_input})")
                tool = self.tool_registry.get_tool(tool_name)

                if tool:
                    result = tool.run(tool_input)
                    print(f"Observations: {result}")
                    self.memory.append({
                        "type": "action", 
                        "tool": tool_name, 
                        "input": tool_input
                        })
                    
                    self.memory.append({
                        "type": "observation",
                        "result": result
                    })
                else:
                    print(f"Tool {tool_name} not found.")
                    break

            elif decision["type"] == "final":
                print("Final Answer")
                print(decision["final_answer"])
                break