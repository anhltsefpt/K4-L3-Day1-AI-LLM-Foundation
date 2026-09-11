"""Câu 2.1 & 2.2 — lấy số liệu thật để viết câu trả lời."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "solution"))
from solution import chat_with_system_prompt, count_tokens  # noqa: E402

# ----- Câu 2.1: hai persona khác nhau, cùng câu hỏi -----
QUESTION = "Giải thích blockchain là gì?"
personas = {
    "Giáo viên tiểu học": "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi.",
    "Chuyên gia tài chính": "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật.",
}
for name, system in personas.items():
    print("=" * 70)
    print(f"PERSONA: {name}")
    print("-" * 70)
    text, _ = chat_with_system_prompt(system, QUESTION)
    print(text)
    print(f"\n[số từ: {len(text.split())} | số token: {count_tokens(text)}]\n")

# ----- Câu 2.2: tiktoken vs ước lượng số-từ/0.75 -----
doan_van = (
    "Việt Nam là một quốc gia nằm ở khu vực Đông Nam Á với đường bờ biển dài "
    "hơn ba nghìn cây số. Đất nước này nổi tiếng với nền văn hóa lâu đời, ẩm "
    "thực phong phú và cảnh quan thiên nhiên tươi đẹp. Từ những thửa ruộng bậc "
    "thang ở vùng núi phía bắc cho đến những bãi biển cát trắng ở miền trung, "
    "mỗi vùng miền đều mang một vẻ đẹp riêng. Người dân Việt Nam thân thiện, "
    "cần cù và luôn tự hào về lịch sử dựng nước và giữ nước hào hùng của dân "
    "tộc mình qua hàng nghìn năm lịch sử đầy biến động và thử thách lớn lao."
)
so_tu = len(doan_van.split())
uoc_luong = so_tu / 0.75
token_that = count_tokens(doan_van)
chenh = (token_that - uoc_luong) / uoc_luong * 100

print("=" * 70)
print("CÂU 2.2 — tiktoken vs ước lượng")
print("-" * 70)
print(f"Số từ:                 {so_tu}")
print(f"Ước lượng (từ/0.75):   {uoc_luong:.1f} token")
print(f"tiktoken (thật):       {token_that} token")
print(f"Chênh lệch:            {chenh:+.1f}%")
