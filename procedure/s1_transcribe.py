# %%
import os
from openai import AzureOpenAI

# %%
# ------------------------------------------------------------
# 指定パスの音声ファイルを文字起こし出力を返す関数
# ------------------------------------------------------------
def transcribe_audio(file_path):
    """
    指定された音声ファイルを文字起こしし、結果を返す関数。
    
    Args:
        file_path (str): 音声ファイルのパス。
    
    Returns:
        str: 文字起こし結果。
    """
    # Azure OpenAIのクライアントを初期化
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_WHISPER_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_WHISPER_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_WHISPER_ENDPOINT"),
    )

    # 音声ファイルを開いて文字起こしを実行
    with open(file_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model="whisper",
            file=audio_file,
            response_format="text",
            language="ja"
        )
    return response
