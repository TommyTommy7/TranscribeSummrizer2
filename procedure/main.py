# %%
import os
from glob import glob
from dotenv import load_dotenv
import time

# %%
# ------------------------------------------------------------
# 環境データの準備
# ------------------------------------------------------------
from config import base_dir, source_dir, out_transcribe_dir, out_summarize_dir
from s1_transcribe import transcribe_audio
from s2_summarize import summarize_transcription

# %%
load_dotenv()  # .envファイルから環境変数を読み込む
# ------------------------------------------------------
# 各種ファイルのパスを取得
# ------------------------------------------------------
# 音声ファイルのパスを取得
source_path = os.path.join(base_dir, source_dir)
source_files = glob(os.path.join(source_path, "*.mp3"))
source_files.sort()
# 文字起こしファイルの出力パス
out_transcribe_path = os.path.join(base_dir, out_transcribe_dir)
os.makedirs(out_transcribe_path, exist_ok=True)
# 要約ファイルの出力パス
out_summarize_path = os.path.join(base_dir, out_summarize_dir)
os.makedirs(out_summarize_path, exist_ok=True)

# %%
# ----------------------------------------------------------
# <main関数>
# ----------------------------------------------------------
def main():
    # ------------------------------------------------------
    # 音声ファイルの数だけループして処理
    # ------------------------------------------------------
    for file_path in source_files:
        start_time = time.perf_counter()    # 開始時間を記録
        # ファイル名を取得
        file_name = os.path.basename(file_path)
        print(f"-- << Processing file: {file_name} >> --")
        print("文字起こし中...")

        # --- <<STEP1 - 音声ファイルを文字起こし>> ---
        transcribe_data = transcribe_audio(file_path)
        transcribe_data = transcribe_data.strip()  # 前後の空白を削除
        # 文字起こし結果をファイルに保存
        transcribe_file_path = os.path.join(out_transcribe_path, f"transe_{file_name}.txt")
        with open(transcribe_file_path, "w", encoding="utf-8") as f:
            f.write(transcribe_data)

        # --- <<STEP2 - 文字起こし結果を要約>> ---
        print("finish!!\n要約中...")
        # ファイルから文字起こし結果を再度読み込む
        with open(transcribe_file_path, "r", encoding="utf-8") as f:
            transcribe_data = f.read()
        summarize_data = summarize_transcription(transcribe_file_path)
        # 要約結果をファイルに保存
        summarize_file_path = os.path.join(out_summarize_path, f"summary_{file_name}.txt")
        with open(summarize_file_path, "w", encoding="utf-8") as f:
            f.write(summarize_data)

        print("finish!!\n")
        elapsed_time = time.perf_counter() - start_time  # 経過時間を計算
        print(f"処理時間: {elapsed_time:.2f}秒\n")

# %%
# ----------------------------------------------------------
# <実行>
# ----------------------------------------------------------

if __name__ == "__main__":
    main()
