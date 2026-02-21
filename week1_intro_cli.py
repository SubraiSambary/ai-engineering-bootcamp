import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
    )

def generate_response(topic):
    prompt = f"""
    Explain {topic} in a simple but technically accurate way.
    Keep it structured.
    """
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", 
             "content": prompt}
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    topic = input("Enter a topic: ")
    response = generate_response(topic)
    print("\n--- AI Response ---\n")
    print(response)