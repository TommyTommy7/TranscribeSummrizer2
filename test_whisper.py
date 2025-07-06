# %%
import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_WHISPER_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_WHISPER_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_WHISPER_ENDPOINT"),
)
# %%
# Whisperモデルで音声認識
with open("speech_source/20250523_音声データ1件目.MP3", "rb") as audio_file:
    response = client.audio.transcriptions.create(
        model="whisper",
        file=audio_file,
        response_format="text",
        language="ja"
    )

print(response)