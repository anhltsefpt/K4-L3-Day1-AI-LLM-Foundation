# K4 — Ngày 1: Bài Tập & Phản Ánh

## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 4 tiếng
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature

Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)

>  Temperature càng cao thì phản hồi càng đa dạng và ngẫu nhiên. Ở temperature 0.0 và 1.0, model đều kể về Hang Sơn Đoòng với nội dung ổn định, gần như lặp lại; nhưng ở 0.5 model lại đổi hẳn chủ đề sang cà phê Việt Nam, còn ở 1.5 cách diễn đạt bay bổng hơn (ví dụ ví hang động chứa được "cả một khu phố New York"). Nhìn chung, temperature thấp cho kết quả nhất quán, dễ lặp lại; temperature cao cho kết quả phong phú, sáng tạo nhưng khó đoán hơn.



### Câu 1.2 — Chọn temperature cho sản phẩm

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**

> Tôi sẽ đặt temperature thấp, khoảng 0.0–0.3, cho chatbot hỗ trợ khách hàng. Lý do là dịch vụ khách hàng cần câu trả lời nhất quán, chính xác và đáng tin cậy; cùng một câu hỏi nên nhận được câu trả lời giống nhau. Temperature cao dễ khiến model "sáng tạo" ra thông tin sai (hallucinate) hoặc trả lời lệch, điều rất nguy hiểm khi tư vấn về chính sách, giá cả hay quy trình.



### Câu 1.3 — Đánh đổi chi phí

Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**

> Workload: 10.000 người × 3 lần × 350 token output = 10,5 triệu token output/ngày. Với đơn giá output GPT-4o $0.010/1K và GPT-4o-mini $0.0006/1K: GPT-4o tốn ~$105/ngày, còn mini chỉ ~$6,3/ngày → GPT-4o đắt hơn khoảng 16,7 lần (tỷ lệ đơn giá 0.010/0.0006). Nên dùng GPT-4o cho tác vụ đòi hỏi lý luận phức tạp, độ chính xác cao (ví dụ phân tích hợp đồng pháp lý, hỗ trợ y tế). Nên dùng mini cho tác vụ đơn giản, khối lượng lớn (ví dụ phân loại email, trả lời FAQ, tóm tắt ngắn) để tiết kiệm chi phí.

---



## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)



### Câu 2.1 — Sức mạnh của persona

Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:

- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)

> Hai phản hồi khác nhau rõ rệt. Bản "giáo viên tiểu học" ngắn hơn (140 từ / 173 token), dùng từ ngữ đơn giản và ẩn dụ đời thường ("cuốn sổ lớn mà ai cũng xem được", "chữ ký"). Bản "chuyên gia tài chính" dài hơn (192 từ / 256 token), dùng nhiều thuật ngữ kỹ thuật (hash, phi tập trung, nodes, bất biến) và trình bày có cấu trúc đánh số. Điều này cho thấy system prompt định hình mạnh mẽ vai trò, độ dài, vốn từ và độ sâu chuyên môn của model — dù câu hỏi của người dùng hoàn toàn giống nhau.



### Câu 2.2 — tiktoken vs đếm từ

Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**

> Với một đoạn ~115 từ tiếng Việt: ước lượng theo công thức số-từ/0.75 cho ~153 token, còn count_tokens (tiktoken) đếm được 145 token — chênh khoảng 5%. Tiếng Việt thường tốn nhiều token hơn tiếng Anh cùng độ dài vì tokenizer BPE được tối ưu cho tiếng Anh: các ký tự có dấu thanh (ă, ơ, ệ, ố...) không nằm trong từ vựng token phổ biến nên bị tách thành nhiều token con, khiến mỗi âm tiết tiếng Việt thường tốn 2–3 token, trong khi một từ tiếng Anh thông dụng chỉ tốn 1 token.

---



## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)



### Câu 3.1 — Trải nghiệm người dùng với streaming

**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)

> Streaming quan trọng nhất trong các ứng dụng tương tác thời gian thực với con người, đặc biệt khi câu trả lời dài — như chatbot hay trợ lý viết văn — vì người dùng thấy chữ hiện ra ngay lập tức thay vì phải chờ toàn bộ phản hồi, giúp giảm cảm giác chờ đợi dù tổng thời gian xử lý không đổi. Ngược lại, non-streaming phù hợp hơn khi chương trình cần nhận trọn vẹn kết quả trước khi xử lý tiếp — ví dụ parse JSON, gọi hàm dựa trên output, chạy batch job nền, hoặc khi cần kiểm duyệt/lọc nội dung trước khi hiển thị.



### Câu 3.2 — Vì sao backoff theo cấp số nhân?

**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**

> So với delay cố định, exponential backoff tăng dần thời gian chờ sau mỗi lần thất bại (0.1s → 0.2s → 0.4s...), cho server bị quá tải thời gian hồi phục thay vì bị dội request liên tục. Nếu hàng nghìn client cùng retry với delay cố định giống nhau, tất cả sẽ gửi lại request cùng một thời điểm, tạo ra các đợt tải đồng loạt ("thundering herd") khiến server vốn đang quá tải càng dễ sập hẳn. (Thực tế nên thêm một chút ngẫu nhiên — jitter — để các client không đồng bộ với nhau.)

---



## Block 4 — Mini-Project (trả lời sau Checkpoint 4)



### Câu 4.1 — Thiết kế persona

**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**

>  Persona tôi chọn: "Bạn là trợ giảng thân thiện của khóa AI, trả lời ngắn gọn bằng tiếng Việt." Hai lựa chọn từ ngữ quan trọng: (1) "trả lời ngắn gọn" — buộc model giữ câu trả lời súc tích, vừa hợp với giao diện terminal vừa tiết kiệm token output nên giảm chi phí; (2) "bằng tiếng Việt" — chỉ định rõ ngôn ngữ để model không trả lời lẫn tiếng Anh, đảm bảo đúng đối tượng học viên Việt Nam. Cụm "trợ giảng thân thiện" đặt giọng điệu gần gũi, khuyến khích người học đặt câu hỏi.



### Câu 4.2 — Hạn chế & cải thiện

**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**

> Hạn chế lớn nhất hiện tại là history chỉ giữ 3 lượt gần nhất (6 message) — trợ lý sẽ "quên" những gì đã nói ở đầu phiên, nên không xử lý tốt cuộc trò chuyện dài có tham chiếu ngược. Một cải thiện cụ thể: thay vì cắt cứng history, khi vượt quá 3 lượt thì gọi model tóm tắt các lượt cũ thành một đoạn ngắn và chèn đoạn tóm tắt đó vào đầu messages (dưới role system). Cách này giữ được bối cảnh quan trọng mà vẫn kiểm soát được số token input, tránh chi phí tăng vô hạn theo độ dài hội thoại.

---



## Danh Sách Kiểm Tra Nộp Bài

- [x] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [x] Cả 4 checkpoint pytest đều pass
- [x] Tất cả 9 câu trong file này đã được trả lời
- [x] Đã copy bài làm vào folder `solution/`, push lên fork và dán link trên trang bài Lab ở VLearn trước 23:59 ngày 11/09/2026