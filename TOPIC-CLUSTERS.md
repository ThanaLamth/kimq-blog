# Sơ đồ chuyên đề: pillar → cluster → bài

Cập nhật 23/11/2026. Lượng tìm là tổng lượt tìm/tháng tại Việt Nam của các từ khoá gán cho bài. KD là độ khó trung bình theo lượng tìm. Nguồn: [data/keywords/2026-11-23](data/keywords/2026-11-23/). Bảng đầy đủ dạng CSV: [cluster-keyword-map.csv](data/keywords/2026-11-23/cluster-keyword-map.csv).

## Quy tắc

- **Pillar** (`type: pillar`): bài tổng quan, giữ từ khoá chung của chuyên đề, có bảng "Bài trong chuyên đề" link tới mọi bài.
- **Cluster**: nhóm bài cùng một mảng nhỏ trong pillar. Bài trong cùng cluster link chéo với nhau.
- **Bài** (`pillar: <slug>` trong frontmatter): dòng đầu link về pillar.
- **Một từ khoá chỉ thuộc một bài.** Từ khoá trong bảng dưới đây đã được chia không trùng. Khi viết bài mới, xoá từ khoá đó khỏi frontmatter bài cũ (xem cột Ghi chú).
- Viết xong: thêm bài vào bảng "Bài trong chuyên đề" của pillar, đổi trạng thái ở file này, CSV và README.

## Tổng quan

| Pillar | Bài pillar | Cluster | Số bài (đã viết/tổng) | Lượng tìm cả chuyên đề |
|---|---|---|---|---|
| P1 Phần mềm mã nguồn mở cho doanh nghiệp | [huong-dan-chon-phan-mem-ma-nguon-mo-cho-doanh-nghiep](posts/huong-dan-chon-phan-mem-ma-nguon-mo-cho-doanh-nghiep.md) | 2 | 5/6 | thấp (B2B) |
| P2 Tạo video bằng AI | [top-cong-cu-tao-video-ai](posts/top-cong-cu-tao-video-ai.md) | 3 | 2/13 | 219.650 |
| P3 AI tạo và chỉnh sửa ảnh | [top-cong-cu-ai-chinh-sua-anh](posts/top-cong-cu-ai-chinh-sua-anh.md) | 3 | 1/10 | 58.780 |
| P4 Trợ lý AI và công cụ AI cho công việc | [huong-dan-dung-cong-cu-ai-pho-bien](posts/huong-dan-dung-cong-cu-ai-pho-bien.md) | 7 | 3/22 | 156.940 |

## P1. Phần mềm mã nguồn mở cho doanh nghiệp

**Pillar:** [huong-dan-chon-phan-mem-ma-nguon-mo-cho-doanh-nghiep](posts/huong-dan-chon-phan-mem-ma-nguon-mo-cho-doanh-nghiep.md). Từ khoá giữ ở pillar: không có trong bộ từ khoá (chủ đề B2B).

### C1.1 AI mã nguồn mở

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| [Top 10 framework AI Agent mã nguồn mở](posts/top-10-framework-ai-agent-ma-nguon-mo.md) | Đã viết | – | – | – | – | – |  |
| [Top 7 AI Gateway mã nguồn mở](posts/top-7-ai-gateway-ma-nguon-mo.md) | Đã viết | – | – | – | – | – |  |
| [Top 7 repo chạy LLM nội bộ](posts/top-7-repo-chay-llm-noi-bo.md) | Đã viết | – | – | – | – | – |  |
| Top repo Claude Code, Claude skill trên GitHub | Dự kiến | Trung bình | everything claude code | claude skill | 2.000 | 24 | Link sang bài Claude Code là gì (C4.7) |

### C1.2 Phần mềm vận hành

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| [Top 8 công cụ tự động hoá quy trình](posts/top-8-cong-cu-tu-dong-hoa-quy-trinh-ma-nguon-mo.md) | Đã viết | – | – | – | – | – |  |
| [Top 8 phần mềm ERP, kế toán](posts/top-8-phan-mem-erp-ke-toan-ma-nguon-mo.md) | Đã viết | – | – | – | – | – |  |

## P2. Tạo video bằng AI

**Pillar:** [top-cong-cu-tao-video-ai](posts/top-cong-cu-tao-video-ai.md). Từ khoá giữ ở pillar: tạo video ai, tạo video ai miễn phí, ai tạo video, tạo video ai free, làm video ai, ai video, làm video ai miễn phí, cách tạo video ai, tạo video bằng ai miễn phí, ai tạo video free, video ai miễn phí, làm video bằng ai miễn phí, web tạo video ai miễn phí, làm video bằng ai, ai tạo video ngắn, app làm video miễn phí (53.860 lượt/tháng, KD 27).

### C2.1 Tạo video theo đầu vào

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| Cách tạo video AI từ ảnh | Dự kiến | Cao | tạo video ai miễn phí từ ảnh | tạo video ai từ hình ảnh, tạo video ai từ ảnh, tạo video từ ảnh bằng ai, tạo ảnh thành video, tạo video bằng ảnh, tạo video từ ảnh free, tạo video từ ảnh trực tuyến, tạo video từ ảnh online, tạo video online từ ảnh | 9.640 | 26 | Chuyển các từ khoá "từ ảnh" khỏi pillar |
| Cách làm video TikTok bằng hình ảnh | Dự kiến | Trung bình | cách làm video tik tok bằng hình ảnh | – | 2.900 | 28 | Ý định: video trình chiếu ảnh có nhạc; link bài "từ ảnh" |
| Tạo video AI từ văn bản: mẫu câu lệnh | Dự kiến | Trung bình | tạo video ai từ văn bản | tạo video ai từ văn bản miễn phí | 2.180 | 28 | Chuyển từ khoá "từ văn bản" khỏi pillar |

### C2.2 Hướng dẫn từng công cụ video

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| [Viggle AI là gì, cách dùng](posts/viggle-ai-la-gi.md) | Đã viết | – | viggle ai | – | 74.000 | 27 | Từ khoá điều hướng, khó vượt trang chủ Viggle |
| Higgsfield AI là gì, cách dùng | Dự kiến | Cao | higgsfield ai | – | 12.100 | 15 |  |
| Vclip AI là gì, cách dùng | Dự kiến | Trung bình | vclip ai | – | 8.100 | 30 | Điều hướng |
| Kling AI: hướng dẫn, gói miễn phí | Dự kiến | Cao | kling ai.com | kling ai video, kling ai free, kling ai 3.0 | 5.300 | 26 | Chuyển "kling ai video" khỏi pillar |
| Vidu AI: hướng dẫn | Dự kiến | Trung bình | vidu ai | vidu studio | 3.740 | 29 | Chuyển "vidu ai" khỏi pillar |
| Luma AI: hướng dẫn | Dự kiến | Trung bình | luma ai | – | 2.900 | 28 | Điều hướng |
| Grok Imagine: tạo video bằng Grok | Dự kiến | Trung bình | grok ai video | – | 1.300 | 22 | Chuyển khỏi pillar |

### C2.3 Âm thanh cho video

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| [Giọng đọc AI tiếng Việt: Vbee, FPT AI, Viettel AI, Vclip](posts/giong-doc-ai-tieng-viet.md) | Đã viết | – | vbee ai | vclip.ai voice, vclip ai voice, clip ai voice, giọng adam ai, giọng ai adam, fpt ai text to speech, viettel ai text to speech, fpt voice ai | 23.760 | 23 | Gắn AI Studio |
| Tạo nhạc bằng AI | Dự kiến | Cao | nhạc ai | tạo nhạc ai, ai tạo nhạc, tạo nhạc bằng ai miễn phí, làm nhạc ai, tạo nhạc bằng ai, ai nhạc | 19.800 | 24 |  |
| Tạo phụ đề tự động cho video | Dự kiến | Thấp | tạo phụ đề tự động cho video | – | 70 | 15 | Gắn AI Studio |

## P3. AI tạo và chỉnh sửa ảnh

**Pillar:** [top-cong-cu-ai-chinh-sua-anh](posts/top-cong-cu-ai-chinh-sua-anh.md). Từ khoá giữ ở pillar: ai chỉnh sửa ảnh, ai sửa ảnh, sửa ảnh ai, chỉnh sửa ảnh bằng ai miễn phí, sửa ảnh bằng ai, chỉnh ảnh bằng ai, ai chỉnh ảnh, phần mềm ai chỉnh sửa ảnh, ai photoshop, chỉnh ảnh ai online, al chỉnh ảnh, chinh sua anh ai (14.110 lượt/tháng, KD 27).

### C3.1 Tạo ảnh bằng AI

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| AI tạo hình ảnh: công cụ và cách dùng | Dự kiến | Cao | ai tạo hình ảnh | ai hình ảnh, ảnh trí tuệ nhân tạo, vẽ tranh ai, krea ai | 7.120 | 17 |  |
| [35 câu lệnh tạo ảnh, ghép ảnh trên Gemini](posts/cau-lenh-tao-anh-ghep-anh-gemini.md) | Đã viết | – | câu lệnh tạo ảnh trên gemini | câu lệnh ghép ảnh trên gemini, xoá logo gemini, xóa logo gemini trên ảnh | 10.320 | 17 | Bỏ nhóm "gemini sinh viên" khỏi bài này (sang C4.2) |
| Tạo ảnh AI trên Zalo | Dự kiến | Thấp | zalo ai avatar | cách tạo ảnh ai trên zalo | 700 | 20 |  |

### C3.2 Sửa ảnh theo việc

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| Làm nét ảnh bằng AI | Dự kiến | Cao | làm nét ảnh ai | – | 4.400 | 12 |  |
| Ghép ảnh bằng AI | Dự kiến | Cao | ai ghép ảnh | ghép ảnh ai online, ghép ảnh bằng ai, ghép ảnh ai, ghép hình ai, cách ghép ảnh bằng ai | 8.350 | 25 | Chuyển khỏi pillar |
| Ghép mặt bằng AI: công cụ và lưu ý pháp lý | Dự kiến | Cao | ai ghép mặt | ghép mặt ai | 2.900 | 15 | Nhấn mạnh deepfake, xin phép người trong ảnh |
| Mở rộng ảnh bằng AI | Dự kiến | Trung bình | mở rộng ảnh bằng ai | mở rộng ảnh ai, ai mở rộng ảnh, mở rộng ảnh ai online | 3.870 | 20 | Chuyển khỏi pillar |
| Phục hồi ảnh cũ bằng AI | Dự kiến | Thấp | ai phục hồi ảnh cũ | ai phục hồi ảnh | 460 | 26 | Chuyển khỏi pillar |
| Cách kiểm tra ảnh có phải AI tạo | Dự kiến | Thấp | check ảnh ai | – | 720 | 20 | Link bài phát hiện văn bản AI (C4.3) |

### C3.3 Thiết kế bằng AI

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| Tạo logo bằng AI | Dự kiến | Trung bình | tạo logo bằng ai | tạo logo ai miễn phí, thiết kế logo bằng ai, thiết kế logo ai, thiet ke logo bang ai, tạo logo ai, làm logo bằng ai, cách tạo logo bằng ai | 5.830 | 28 |  |

## P4. Trợ lý AI và công cụ AI cho công việc

**Pillar:** [huong-dan-dung-cong-cu-ai-pho-bien](posts/huong-dan-dung-cong-cu-ai-pho-bien.md). Từ khoá giữ ở pillar: công cụ ai, ai assistant, cách dùng ai, ứng dụng ai trong doanh nghiệp (2.920 lượt/tháng, KD 23).

### C4.1 Claude

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| [Claude là gì? So sánh các gói](posts/claude-la-gi-so-sanh-cac-goi-claude.md) | Đã viết | – | claude pro | claude ai pro, claude là gì, claude max, claude free, claude team, mua tài khoản claude, giá claude, claude ai tiếng việt | 17.210 | 21 |  |
| Các model Claude: Fable, Opus, Sonnet khác nhau thế nào | Dự kiến | Trung bình | claude fable 5 | claude opus, claude opus 4.6, claude 3.5 sonnet, claude sonnet 5, claude fable 5 mở lại | 3.630 | 21 | Chuyển "claude fable 5" khỏi bài so sánh gói |
| [Claude Design là gì](posts/claude-design-la-gi.md) | Đã viết | – | claude design | – | 8.100 | 20 |  |
| Claude for Excel: phân tích bảng tính | Dự kiến | Thấp | claude excel | claude for excel | 780 | 22 |  |

### C4.2 Gemini, ChatGPT và app AI miễn phí

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| Gemini cho sinh viên: nhận gói miễn phí | Dự kiến | Cao | gemini sinh viên | gemini pro cho sinh viên, gemini pro sinh viên, gemini cho sinh viên, google ai plus cho sinh viên | 9.500 | 22 | Chuyển khỏi bài câu lệnh Gemini |
| Gemini 3.5 Pro và Flash: khác nhau, giá | Dự kiến | Trung bình | gemini pro giá | gemini 3.5 flash, gemini 3.5 pro | 1.550 | 27 | Chờ số liệu chính thức |
| Hướng dẫn dùng ChatGPT | Dự kiến | Trung bình | hướng dẫn sử dụng chat gpt | hướng dẫn sử dụng chatgpt, cách vào chat gpt, hướng dẫn chat gpt, sử dụng chat gpt trên điện thoại | 1.070 | 28 |  |
| Ứng dụng AI miễn phí đáng dùng | Dự kiến | Trung bình | phần mềm ai miễn phí | các ứng dụng ai miễn phí, hỏi ai miễn phí, tải phần mềm ai miễn phí, tải ai miễn phí | 2.560 | 24 |  |

### C4.3 AI cho học tập

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| Học AI bắt đầu từ đâu: lộ trình, khoá học | Dự kiến | Cao | khóa học ai | học ai, học ai bắt đầu từ đâu, học ai ở đâu, tự học ai trí tuệ nhân tạo, học ai cho người mới bắt đầu, học ai cơ bản, khóa học ai miễn phí, học về ai, tự học ai, khóa học về ai, học ai miễn phí, học công nghệ ai, cách học ai, học ai online, hướng dẫn học ai, học ai từ a đến z, khóa học ai online, học sử dụng ai, lộ trình học ai, khoá học ai trí tuệ nhân tạo | 6.830 | 13 |  |
| Check đạo văn AI: cách phát hiện văn bản do AI viết | Dự kiến | Cao | check đạo văn ai | check ai đạo văn, phát hiện ai, kiểm tra ai | 8.400 | 24 | "kiểm tra ai" có lẫn ý định khác, xem SERP |
| AI giải bài tập: AI Hay, Gauth và cách dùng đúng | Dự kiến | Cao | ai hay giải bài tập | gauth ai, ứng dụng ai trong học tập | 4.940 | 24 |  |
| AI viết văn: dùng thế nào cho đúng | Dự kiến | Trung bình | ai viết văn | ai viết văn hay | 1.470 | 24 |  |

### C4.4 Làm việc văn phòng với AI

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| Làm slide bằng AI | Dự kiến | Cao | slide ai | powerpoint ai, tạo slide bằng ai, làm slide bằng ai, tạo slide bằng ai miễn phí, tạo slide thuyết trình bằng ai, làm powerpoint bằng ai, thiết kế powerpoint bằng ai | 18.580 | 26 | Link Claude Design |
| Prompt AI: cách viết câu lệnh hiệu quả | Dự kiến | Cao | prompt ai | – | 4.400 | 26 | Link các bài câu lệnh |

### C4.5 Tìm kiếm và kiến thức AI

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| [Chế độ AI của Google](posts/che-do-ai-google-ai-mode-la-gi.md) | Đã viết | – | chế độ ai | che do ai, chế độ ai google, chế độ ai của google | 44.500 | 27 |  |
| Gen AI (AI tạo sinh) là gì | Dự kiến | Trung bình | gen ai | – | 1.900 | 23 |  |

### C4.6 AI cho doanh nghiệp

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| Tạo chatbot AI miễn phí cho website, Zalo, Facebook | Dự kiến | Trung bình | tao chatbot | tạo chatbot, chatbot miễn phí, ai chatbot là gì, phần mềm chatbot miễn phí, phần mềm chatbot, trợ lý ảo ai | 770 | 19 | Gắn Chatbot đa kênh, Trợ lý Zalo |
| AI agency là gì | Dự kiến | Cao | ai agency | – | 9.900 | 18 | Xem SERP trước |
| AI trong marketing: ứng dụng và cảnh báo lừa đảo | Dự kiến | Trung bình | ai marketing lừa đảo | ai marketing, ai seo, ai trong marketing, viết content bằng ai, ứng dụng ai trong marketing | 2.390 | 17 |  |

### C4.7 AI lập trình

| Bài | Trạng thái | Ưu tiên | Từ khoá chính | Từ khoá phụ | Lượng tìm | KD | Ghi chú |
|---|---|---|---|---|---|---|---|
| Claude Code là gì | Dự kiến | Thấp | claude code là gì | claude code pro | 640 | 23 | Link Top repo Claude Code (C1.1) |
| Kiro AI là gì | Dự kiến | Trung bình | kiro ai | – | 1.900 | 28 |  |
| AI engineer là gì, học gì | Dự kiến | Trung bình | ai engineer | ai engineer là gì, lập trình ai, ai lập trình | 3.000 | 22 | Bỏ các biến thể "tuyển dụng" |

## Thứ tự viết đề xuất (nhóm ưu tiên Cao)

Xếp theo lượng tìm chia cho độ khó, nên bài vừa nhiều lượt tìm vừa dễ lên top được viết trước.

| # | Bài | Pillar / Cluster | Lượng tìm | KD |
|---|---|---|---|---|
| 1 | [Giọng đọc AI tiếng Việt: Vbee, FPT AI, Viettel AI, Vclip](posts/giong-doc-ai-tieng-viet.md) (đã viết) | P2 / C2.3 Âm thanh cho video | 23.760 | 23 |
| 2 | Tạo nhạc bằng AI | P2 / C2.3 Âm thanh cho video | 19.800 | 24 |
| 3 | Higgsfield AI là gì, cách dùng | P2 / C2.2 Hướng dẫn từng công cụ video | 12.100 | 15 |
| 4 | Làm slide bằng AI | P4 / C4.4 Làm việc văn phòng với AI | 18.580 | 26 |
| 5 | AI agency là gì | P4 / C4.6 AI cho doanh nghiệp | 9.900 | 18 |
| 6 | Học AI bắt đầu từ đâu: lộ trình, khoá học | P4 / C4.3 AI cho học tập | 6.830 | 13 |
| 7 | Gemini cho sinh viên: nhận gói miễn phí | P4 / C4.2 Gemini, ChatGPT và app AI miễn phí | 9.500 | 22 |
| 8 | AI tạo hình ảnh: công cụ và cách dùng | P3 / C3.1 Tạo ảnh bằng AI | 7.120 | 17 |
| 9 | Cách tạo video AI từ ảnh | P2 / C2.1 Tạo video theo đầu vào | 9.640 | 26 |
| 10 | Check đạo văn AI: cách phát hiện văn bản do AI viết | P4 / C4.3 AI cho học tập | 8.400 | 24 |
| 11 | Ghép ảnh bằng AI | P3 / C3.2 Sửa ảnh theo việc | 8.350 | 25 |
| 12 | Làm nét ảnh bằng AI | P3 / C3.2 Sửa ảnh theo việc | 4.400 | 12 |
| 13 | Kling AI: hướng dẫn, gói miễn phí | P2 / C2.2 Hướng dẫn từng công cụ video | 5.300 | 26 |
| 14 | AI giải bài tập: AI Hay, Gauth và cách dùng đúng | P4 / C4.3 AI cho học tập | 4.940 | 24 |
| 15 | Ghép mặt bằng AI: công cụ và lưu ý pháp lý | P3 / C3.2 Sửa ảnh theo việc | 2.900 | 15 |
| 16 | Prompt AI: cách viết câu lệnh hiệu quả | P4 / C4.4 Làm việc văn phòng với AI | 4.400 | 26 |

Sau nhóm Cao: viết nhóm Trung bình theo cùng cách xếp; nhóm Thấp để cuối hoặc gộp vào bài lớn hơn.

## Không làm

- **camera ai** (~14.500): thiết bị camera, ngoài phạm vi KimQ.
- **bing ai** (6.600): người tìm chủ yếu muốn vào thẳng Bing của Microsoft.
- **tuyển dụng ai engineer** và các biến thể: ý định tìm việc.
- **thư vũ gemini, gemini hùng huỳnh, cung gemini**: không liên quan công cụ AI.
- Các nhóm nhiễu khác ghi ở [KEYWORD-MAP.md](data/keywords/2026-11-23/KEYWORD-MAP.md).
