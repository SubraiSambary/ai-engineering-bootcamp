import os
import re
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
    )

def clean_json_output(output: str):
    """ Removes markdown code blocks if present. """
    output=re.sub(r"```json|```","", output)
    output=re.sub(r"```","", output)

    #Extract first JSON object from the output
    match=re.search(r"\{.*\}", output, re.DOTALL)
    if match:
        return match.group(0)

    return output.strip()

def call_llm(messages, model="openai/gpt-oss-120b", temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

def call_llm_json(messages, max_retries=3):
    """
    Forces JSON output and retries if parsing fails.
    """

    system_message = {
        "role": "system",
        "content": "You must respond ONLY in valid JSON format. No Markdown"
    }

    messages = [system_message] + messages

    for attempt in range(max_retries):
        try:
            output = call_llm(messages)

            print("\n---Raw LLM Output---",output)
            cleaned =clean_json_output(output)

            return json.loads(cleaned)
        except Exception as e:
            print(f"\nAttempt {attempt+1} failed to parse JSON. Retrying... Error: {e}")

    raise ValueError("LLM failed to return valid JSON after retries")  