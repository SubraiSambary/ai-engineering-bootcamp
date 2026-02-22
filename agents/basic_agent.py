import json
from core.llm_client import call_llm_json

class BasicAgent:

    def __init__(self, goal):
        self.goal = goal
        self.memory = []
        self.finished = False

    def think(self):
        messages = [
            {"role": "user", 
             "content": f"""
            You are an autonomous AI agent.

            Goal:
            {self.goal}

            Current memory:
            {json.dumps(self.memory)}

            You must return ONLY valid JSON.
            No markdown.
            No explanation outside JSON.

            Return EXACTLY this format:

            {{
                "thought": "...",
                "action": "...",
                "final_answer": null
            }}

            If the task is complete, replace null with the final answer string.
            """
            }
        ]
        return call_llm_json(messages)
    
    def run(self, max_iterations=5):
        for step in range(max_iterations):
           
           print(f"\n--- Iterations {step+1} ---")

           decisions = self.think()

           print("Thought:", decisions["thought"])
           print("Action:", decisions["action"])
            
           self.memory.append(decisions)

           final = decisions.get("final_answer")

           if final and final != "null":
                print("\nFinal Answer: ")
                print(decisions["final_answer"])
                self.finished = True
                break
           
        if not self.finished:
            print("\n⚠ Agent stopped due to iteration limit.")