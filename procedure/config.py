import os
from pathlib import Path

# --- <<パスデータ>> ---
# このファイルの親フォルダ(procedure)
base_dir = Path(__file__).parent
# 音源データフォルダ
source_dir = os.path.join(base_dir.parent, "speech_source")
# プロンプトファイルフォルダ
prompts_dir = os.path.join(base_dir.parent, "prompts")
# 出力先フォルダ
out_dir = os.path.join(base_dir.parent, "output")
# 文字起こしファイルの出力先フォルダ
out_transcribe_dir = os.path.join(out_dir, "transcribe")
# 要約ファイルの出力先フォルダ
out_summarize_dir = os.path.join(out_dir, "summarize")
