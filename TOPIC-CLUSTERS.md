# Sơ đồ chuyên đề (pillar và cluster)

Cập nhật 23/11/2026. Lượng tìm kiếm là tổng lượt tìm/tháng tại Việt Nam của nhóm từ khoá, lấy từ [data/keywords/2026-11-23](data/keywords/2026-11-23/) sau khi bỏ từ nhiễu. KD là độ khó trung bình.

## Quy tắc

- **Pillar** (`type: pillar`): bài tổng quan, nhắm từ khoá chính của chuyên đề, có bảng "Bài trong chuyên đề" link tới mọi cluster.
- **Cluster** (`pillar: <slug>` trong frontmatter): đào sâu một câu hỏi. Dòng đầu bài link về pillar, link chéo 2–3 cluster cùng chuyên đề.
- **Một từ khoá chỉ thuộc một bài.** Viết cluster mới thì chuyển từ khoá tương ứng khỏi pillar để tránh hai bài tranh nhau.
- Viết xong cluster: thêm vào bảng "Bài trong chuyên đề" của pillar, cập nhật file này và README.

## Tổng quan

| # | Pillar | Bài pillar | Lượng tìm ước tính | Cluster đã có | Cluster dự kiến | Sản phẩm KimQ liên quan |
|---|---|---|---|---|---|---|
| 1 | Phần mềm mã nguồn mở cho doanh nghiệp | [huong-dan-chon-phan-mem-ma-nguon-mo-cho-doanh-nghiep](posts/huong-dan-chon-phan-mem-ma-nguon-mo-cho-doanh-nghiep.md) | thấp (B2B, không có trong bộ từ khoá) | 5 | 1 | [AI Gateway](https://kimq.tech/san-pham/ai-gateway), [Tự động hoá](https://kimq.tech/san-pham/tu-dong-hoa) |
| 2 | Tạo video bằng AI | [top-cong-cu-tao-video-ai](posts/top-cong-cu-tao-video-ai.md) | ~180.000 | 0 | 6 | [AI Studio](https://kimq.tech/san-pham/ai-studio) |
| 3 | AI tạo và chỉnh sửa ảnh | [top-cong-cu-ai-chinh-sua-anh](posts/top-cong-cu-ai-chinh-sua-anh.md) | ~75.000 | 1 | 5 | [AI Studio](https://kimq.tech/san-pham/ai-studio) |
| 4 | Trợ lý AI và công cụ AI cho công việc | [huong-dan-dung-cong-cu-ai-pho-bien](posts/huong-dan-dung-cong-cu-ai-pho-bien.md) | ~150.000 | 3 | 6 | [Chatbot đa kênh](https://kimq.tech/san-pham/chatbot-da-kenh), [Trợ lý Zalo](https://kimq.tech/san-pham/tro-ly-zalo) |

Pillar 4 đồng thời là trang mục lục cho pillar 2 và 3 (bảng "Chuyên đề con").

## Pillar 1: Phần mềm mã nguồn mở cho doanh nghiệp

| Cluster | Trạng thái | Từ khoá chính | Lượng tìm | KD |
|---|---|---|---|---|
| [Top 10 framework AI Agent](posts/top-10-framework-ai-agent-ma-nguon-mo.md) | Đã viết | framework ai agent | – | – |
| [Top 7 AI Gateway](posts/top-7-ai-gateway-ma-nguon-mo.md) | Đã viết | ai gateway mã nguồn mở | – | – |
| [Top 7 repo chạy LLM nội bộ](posts/top-7-repo-chay-llm-noi-bo.md) | Đã viết | chạy llm nội bộ | – | – |
| [Top 8 công cụ tự động hoá quy trình](posts/top-8-cong-cu-tu-dong-hoa-quy-trinh-ma-nguon-mo.md) | Đã viết | tự động hoá mã nguồn mở, n8n | – | – |
| [Top 8 phần mềm ERP, kế toán](posts/top-8-phan-mem-erp-ke-toan-ma-nguon-mo.md) | Đã viết | erp mã nguồn mở | – | – |
| Top repo Claude Code, Claude skill | Dự kiến | everything claude code, claude skill, claude code | ~2.600 | 24 |

## Pillar 2: Tạo video bằng AI

Pillar giữ: tạo video ai, tạo video ai miễn phí, ai tạo video, làm video ai, cách tạo video ai, tạo video ai từ văn bản.

| Cluster | Trạng thái | Từ khoá chính | Lượng tìm | KD | Ưu tiên |
|---|---|---|---|---|---|
| Cách tạo video AI từ ảnh, làm video TikTok bằng hình ảnh | Dự kiến | tạo video ai miễn phí từ ảnh, tạo video ai từ hình ảnh, cách làm video tik tok bằng hình ảnh | ~12.400 | 27 | Cao. Chuyển các từ khoá "từ ảnh" khỏi pillar |
| Higgsfield AI là gì, cách dùng | Dự kiến | higgsfield ai | 12.100 | 15 | Cao (KD thấp) |
| Tạo nhạc bằng AI | Dự kiến | nhạc ai, tạo nhạc ai, ai tạo nhạc, tạo nhạc bằng ai miễn phí | ~21.600 | 22 | Cao |
| Giọng đọc AI tiếng Việt: Vbee, FPT AI, Viettel AI, Vclip | Dự kiến | vbee ai, vclip ai voice, fpt ai text to speech, giọng adam ai | ~20.000 | 22 | Trung bình. Gắn AI Studio |
| Viggle AI: cách dùng | Dự kiến | viggle ai | 74.000 | 27 | Trung bình. Từ khoá điều hướng, khó vượt trang chủ Viggle |
| Kling AI: hướng dẫn, gói miễn phí | Dự kiến | kling ai video, kling ai free, kling ai.com | ~5.300 | 25 | Thấp |

## Pillar 3: AI tạo và chỉnh sửa ảnh

Pillar giữ: ai chỉnh sửa ảnh, ai sửa ảnh, chỉnh sửa ảnh bằng ai miễn phí, phần mềm ai chỉnh sửa ảnh, ai photoshop. **Nên thêm** "ai tạo hình ảnh" (5.400, KD 14) vào pillar.

| Cluster | Trạng thái | Từ khoá chính | Lượng tìm | KD | Ưu tiên |
|---|---|---|---|---|---|
| [35 câu lệnh tạo ảnh, ghép ảnh trên Gemini](posts/cau-lenh-tao-anh-ghep-anh-gemini.md) | Đã viết | câu lệnh tạo ảnh/ghép ảnh trên gemini, xoá logo gemini | ~10.000 | 17 | – |
| Làm nét ảnh bằng AI | Dự kiến | làm nét ảnh ai | 4.400 | 12 | Cao (KD thấp nhất) |
| Ghép ảnh, ghép mặt bằng AI | Dự kiến | ai ghép ảnh, ghép ảnh ai online, ai ghép mặt | ~8.600 | 22 | Cao. Chuyển "ai ghép ảnh", "ghép ảnh ai online" khỏi pillar |
| Tạo logo bằng AI | Dự kiến | tạo logo bằng ai, tạo logo ai miễn phí, thiết kế logo bằng ai | ~6.100 | 26 | Trung bình |
| Mở rộng ảnh bằng AI | Dự kiến | mở rộng ảnh bằng ai, ai mở rộng ảnh | ~3.900 | 20 | Trung bình. Chuyển khỏi pillar |
| Phục hồi ảnh cũ, kiểm tra ảnh AI | Dự kiến | ai phục hồi ảnh cũ, check ảnh ai | ~1.100 | 23 | Thấp |

## Pillar 4: Trợ lý AI và công cụ AI cho công việc

Pillar giữ: công cụ ai, ai cho công việc, ứng dụng ai trong doanh nghiệp.

| Cluster | Trạng thái | Từ khoá chính | Lượng tìm | KD | Ưu tiên |
|---|---|---|---|---|---|
| [Chế độ AI của Google](posts/che-do-ai-google-ai-mode-la-gi.md) | Đã viết | chế độ ai, che do ai, chế độ ai google | ~44.500 | 26 | – |
| [Claude là gì, so sánh các gói](posts/claude-la-gi-so-sanh-cac-goi-claude.md) | Đã viết | claude pro, claude là gì, claude max, claude free | ~19.800 | 21 | – |
| [Claude Design là gì](posts/claude-design-la-gi.md) | Đã viết | claude design | 8.100 | 20 | – |
| Làm slide bằng AI | Dự kiến | slide ai, powerpoint ai, tạo slide bằng ai (miễn phí) | ~18.600 | 27 | Cao. Link Claude Design |
| Gemini cho sinh viên, Gemini Pro | Dự kiến | gemini sinh viên, gemini pro cho sinh viên, google ai plus cho sinh viên | ~9.500 | 23 | Cao. Chuyển các từ khoá này khỏi bài câu lệnh Gemini |
| Học AI bắt đầu từ đâu | Dự kiến | khóa học ai, học ai, học ai bắt đầu từ đâu, tự học ai | ~6.500 | 11 | Cao (KD rất thấp) |
| AI agency là gì | Dự kiến | ai agency | 9.900 | 18 | Trung bình. Cần xem SERP trước để chắc ý định tìm kiếm |
| Tạo chatbot AI miễn phí | Dự kiến | tạo chatbot, chatbot miễn phí, phần mềm chatbot | ~1.100 | 22 | Trung bình. Lượng tìm thấp nhưng sát sản phẩm Chatbot đa kênh |
| Hướng dẫn dùng ChatGPT | Dự kiến | hướng dẫn sử dụng chatgpt, cách vào chat gpt | ~1.100 | 28 | Thấp |

## Không làm

- **camera ai** (~14.500): thiết bị camera, ngoài phạm vi KimQ.
- **bing ai** (6.600): từ khoá điều hướng tới Microsoft.
- Các nhóm nhiễu đã ghi ở [KEYWORD-MAP.md](data/keywords/2026-11-23/KEYWORD-MAP.md).

## Thứ tự viết đề xuất

1. Làm nét ảnh bằng AI (P3)
2. Học AI bắt đầu từ đâu (P4)
3. Higgsfield AI (P2)
4. Làm slide bằng AI (P4)
5. Gemini cho sinh viên (P4)
6. Tạo video AI từ ảnh (P2)
7. Ghép ảnh, ghép mặt bằng AI (P3)
8. Tạo nhạc bằng AI (P2)

Nhóm đầu ưu tiên KD thấp để có thứ hạng sớm; sau đó tới nhóm lượng tìm cao.
