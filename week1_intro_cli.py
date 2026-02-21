from core.llm_client import call_llm_json

def explain_topic(topic):
    messages = [
        {"role": "user", 
         "content": f"""
         Explain the {topic} in structured format.
         Return JSON with:
            {{
                "definition": "...",
                "key_concepts": ["...", "..."],
                "real_world_example": "..."
            }}
            """
        }
    ]
    return call_llm_json(messages)

if __name__ == "__main__":
    topic = input("Enter a topic: ")
    result = explain_topic(topic)

    print("\n---Structured AI Output---")
    print(result)