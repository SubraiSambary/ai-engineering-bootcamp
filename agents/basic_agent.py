import json
from core.llm_client import call_llm_json
from tools.tool_registry import ToolRegistry

class BasicAgent:

    def __init__(self, goal):
        self.goal = goal
        self.memory = []
        self.finished = False
        self.plan_generated = False
        self.plan = []
        self.current_step = 0
        self .tool_registry = ToolRegistry()

    def think(self):
        if not self.plan_generated:
            prompt= f""" 
            You are an AI planning agent.

            Goal:
            {self.goal}

            Generate a step-by-step plan to achieve this goal. (3-5 steps)

            Return ONLY valid JSON:

            {{
                "type": "plan",
                "steps": ["step 1", "step 2", "step 3"]
            }}
            """
        else:
            if self.current_step < len(self.plan):
                step = self.plan[self.current_step]

                prompt = f"""
                You are executing this plan step:

                {step}

                Return ONLY valid JSON:

                {{
                    "type": "execution",
                    "result": "result of executing this step",
                    "final_answer": null
                }}
                """
            else:
                prompt= f"""
                All steps are completed.

                Here are the completed steps:
                {self.memory}
                
                Now generate a final consolidated answer for the user's goal:
                "{self.goal}"

                Return ONLY valid JSON:
                {{
                    "type": "final",
                    "final_answer": "<your detailed final answer here>"
                }}
                """
        messages = [{"role": "user", "content": prompt}]
        return call_llm_json(messages)
    
    def run(self, max_iterations=10):
        
        for i in range(max_iterations):
            print(f"\n--- Iteration {i+1} ---")

            decision = self.think()

            if not isinstance(decision, dict):
                print("⚠ Invalid decision format:", decision)
                break

            if decision["type"] == "plan":
                self.plan = decision["steps"]
                self.plan_generated = True
                print("Generated Plan:")
                for idx, step in enumerate(self.plan):
                    print(f"{idx}. {step}")

            elif decision["type"] == "execution":
                print(f"Executing Step: {self.plan[self.current_step]}")
                print(f"Result: {decision['result']}")
                self.memory.append(decision)
                self.current_step += 1

            elif decision["type"] == "final":
                print("Final Answer:")
                print(decision["final_answer"])
                break
