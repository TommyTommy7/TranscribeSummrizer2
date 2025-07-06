# %%
import os
from openai import AzureOpenAI

# %%
api_key = os.getenv("AZURE_OPENAI_41_API_KEY")
api_endpoint = os.getenv("AZURE_OPENAI_41_ENDPOINT")
api_version = os.getenv("AZURE_OPENAI_41_API_VERSION")

# %%
client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=api_endpoint
)

# %%
# ---------------------------------
# Chat ompletions APIの呼び出しテスト
# ---------------------------------
response = client.chat.completions.create(
    model="gpt-4.1-nano",
    # model="gpt4omni-rate16k",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "こんにちは!私はジョンと言います!"}
    ],
)

print(response.to_json(indent=2))

# %%