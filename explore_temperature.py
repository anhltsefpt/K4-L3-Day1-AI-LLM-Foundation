"""
Câu 1.1 — Khám phá độ nhạy của temperature.

Gọi call_openai với cùng một prompt nhưng 4 mức temperature khác nhau,
in kết quả ra để bạn quan sát và tự viết nhận xét vào exercises.md.

Chạy:  python explore_temperature.py
"""

import os
import sys

# Nạp hàm call_openai đã hoàn chỉnh trong solution/solution.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "solution"))
from solution import call_openai  # noqa: E402

PROMPT = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."

for temp in (0.0, 0.5, 1.0, 1.5):
    print("=" * 70)
    print(f"temperature = {temp}")
    print("-" * 70)
    text, latency = call_openai(PROMPT, temperature=temp)
    print(text)
    print(f"\n(latency: {latency:.2f}s)\n")
