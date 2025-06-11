import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Use this code to test your Azure OpenAI API key.

# Configuration
API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

# Payload for the request
payload = {
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": os.environ.get("PROMPT")
        }
      ]
    }
  ],
  "temperature": os.environ.get("TEMPERATURE"),
  "top_p": os.environ.get("TOP_P"),
  "max_tokens": os.environ.get("MAX_TOKENS")
}

# Use your Azure OpenAI endpoint
ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")

# Send request
try:
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

# Handle the response as needed (e.g., print or process)
print(response.json())