# %%
import os
from openai import AzureOpenAI

from config import base_dir, prompts_dir

# %%
# ------------------------------------------------------------
# 指定パスの文字起こしファイルの要約した結果を返す関数
# ------------------------------------------------------------
def summarize_transcription(file_path):
    """
    指定された文字起こしファイルを要約し、結果を返す関数。
    
    Args:
        file_path (str): 文字起こしファイルのパス。
    
    Returns:
        str: 要約結果。
    """
    # Azure OpenAIのクライアントを初期化
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_41_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_41_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_41_ENDPOINT")
    )

    # システムプロンプトのファイルを開いて読み込む
    # 要約プロンプトファイルのパスを設定
    summarize_prompt_file_path = os.path.join(base_dir, prompts_dir, f"summarize_prompt.txt")
    with open(summarize_prompt_file_path, "r", encoding="utf-8") as pf:
        system_prompt = pf.read()



    # 文字起こしファイルを開いて要約を実行
    with open(file_path, "r", encoding="utf-8") as text_file:
        transcription_text = text_file.read()
        response = client.chat.completions.create(
            model="gpt-4.1",
            # model="gpt-4.1-mini",
            # messages=[
            #     {"role": "system",
            #      "content": (
            #         "あなたは有能なアシスタントです。\n"
            #         "以下の内容を要約してください。\n"
            #         "要点を簡潔にまとめてください。"
            #         )
            #     },
            #     {"role": "user", "content": transcription_text}
            # ],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": transcription_text}
            ],
            # max_tokens=500,
            temperature=0.7
        )
    
    return response.choices[0].message.content.strip()