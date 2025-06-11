import os
import dotenv

from dotenv import load_dotenv
load_dotenv()

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

client = ChatCompletionsClient(
    endpoint="https://raewyn.cognitiveservices.azure.com/openai/deployments/gpt-4o-mini",
    credential=AzureKeyCredential(os.getenv("AZURE_OPENAI_API_KEY")),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="I am going to Paris, what should I see?"),
    ],
    max_tokens=512,
    temperature=0.7,
    top_p=0.9,
    model="gpt-4o-mini"
)

print(response.choices[0].message.content)