import openai
import os

openai.api_key = os.getenv("AIPROXY_TOKEN")

def call_llm(prompt: str) -> str:
    response = openai.Completion.create(
        engine="gpt-4-mini",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
    )
    return response.choices[0].text.strip()