from agents.basic_agent import BasicAgent

if __name__ == "__main__":
    goal = input("Enter the agent's goal: ")
    agent = BasicAgent(goal)
    agent.run()
    