# model_bridge.py

import os
import requests
import subprocess

USE_LOCAL_MODEL = True  # Set to False to use OpenAI API

# If using OpenAI:
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4"

# If using local Mistral via Ollama:
OLLAMA_MODEL = "mistral"

print("[DEBUG] model_bridge.py loaded")

def get_model_response(prompt):
    if USE_LOCAL_MODEL:
        return query_ollama_model(prompt)
    else:
        return query_openai_model(prompt)

def query_ollama_model(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL, prompt],
            capture_output=True, text=True, timeout=60
        )
        return result.stdout.strip()
    except Exception as e:
        return f"[ERROR] Local model failed: {str(e)}"

def query_openai_model(prompt):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": OPENAI_MODEL,
        "messages": [
            {"role": "system", "content": "You are an AI ethics advisor engaging in decision justification simulations."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[ERROR] OpenAI API failed: {str(e)}"
