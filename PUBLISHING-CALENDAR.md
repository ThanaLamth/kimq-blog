# Lịch đăng bài và số lượng mỗi tháng

Cập nhật 24/11/2026. Lập theo khung hub–spoke, kế hoạch nội dung và quality gate của bộ kỹ năng [claude-seo](https://github.com/AgriciDaniel/claude-seo) (`seo-cluster`, `seo-plan`, `seo-content`, `seo-geo`). Đi kèm [TOPIC-CLUSTERS.md](TOPIC-CLUSTERS.md) và [DISTRIBUTION-PLAN.md](DISTRIBUTION-PLAN.md). Cột `dot_dang` trong [cluster-keyword-map.csv](data/keywords/2026-11-23/cluster-keyword-map.csv) ghi bài thuộc Stage nào. Mỗi Stage tương ứng khoảng 1 tháng.

## 1. Quy tắc lấy từ claude-seo

| Quy tắc | Giá trị | KimQ hiện tại | Việc cần làm |
|---|---|---|---|
| Thứ tự viết | Pillar trước, sau đó spoke theo volume giảm dần | 4 pillar đã có | Viết spoke theo volume (mục 3) |
| Độ dài pillar | 2.500–4.000 từ, link tới **mọi** spoke, có mục lục, schema ItemList | 1.200–2.300 từ | Mở rộng 4 pillar trong Stage 1 |
| Độ dài spoke | 1.200–1.800 từ, nội dung 100% riêng | 1.400–2.100 từ | Giữ nguyên |
| Link nội bộ của spoke | 1 link về pillar (bắt buộc) + 2–3 link bài cùng cluster | Đã có link pillar | Thêm 2–3 link bài cùng cluster khi bài đó lên |
| Số cluster mỗi pillar | 2–5 | P4 có 7 cluster | Tách P4 (mục 2) |
| Số bài mỗi cluster | 2–4 | C2.2 có 7, C3.2 có 6, C3.3 có 1 | Tách hoặc gộp (mục 2) |
| Tổng bài mỗi pillar | 5–21 | P4 có 23 | Tách P4 |
| Làm mới | Pillar mỗi quý hoặc khi có spoke mới | – | Mỗi bài mới: cập nhật bảng "Bài trong chuyên đề" của pillar |
| Rủi ro | Nội dung hàng loạt do AI viết, thiếu giá trị riêng, là lỗi E-E-A-T | – | Mỗi bài phải có ảnh chụp thao tác thật, thử nghiệm thật, ngày dữ liệu và người duyệt. **Không đăng hằng ngày cho đủ số** |
| GEO | Thương hiệu được nhắc tới tương quan với khả năng được AI trích dẫn mạnh hơn backlink. YouTube có tương quan mạnh nhất, sau đó Reddit, LinkedIn | Chưa có YouTube, Reddit | Đăng lại video TikTok lên YouTube Shorts; trả lời câu hỏi thật trên Reddit/Facebook group (không spam) |

## 2. Chỉnh cấu trúc cluster cho đúng khung (chờ duyệt)

| Hiện tại | Đề xuất |
|---|---|
| P4 Trợ lý AI: 7 cluster, 23 bài | **P4 Trợ lý AI**: C4.1 Claude, C4.2 Gemini/ChatGPT, C4.5 Tìm kiếm và kiến thức AI. **P5 AI cho học tập và công việc** (pillar mới): C4.3 Học tập, C4.4 Văn phòng, C4.6 Doanh nghiệp |
| C4.7 AI lập trình nằm trong P4 | Chuyển sang **P1 Mã nguồn mở và lập trình**, hợp với nhóm bài tiếng Anh cho dev |
| C2.2 Hướng dẫn từng công cụ video: 7 bài | Tách thành **C2.2a Công cụ quốc tế** (Kling, Luma, Vidu, Higgsfield) và **C2.2b Công cụ hot, miễn phí** (Viggle, Vclip, Grok Imagine) |
| C3.2 Sửa ảnh theo việc: 6 bài | Tách thành **C3.2a Chỉnh chất lượng** (làm nét, mở rộng, phục hồi ảnh cũ) và **C3.2b Ghép và kiểm tra ảnh** (ghép ảnh, ghép mặt, kiểm tra ảnh AI) |
| C3.3 Thiết kế bằng AI: 1 bài | Gộp vào C3.1, hoặc thêm 1 bài (ví dụ "Thiết kế banner bằng AI") khi có từ khoá |

Sau khi tách: 5 pillar, 18 cluster. Mỗi pillar có 2–5 cluster, mỗi cluster có 2–4 bài.

## 3. Số lượng mỗi tháng

### Blog gốc (GitHub `kimq-blog`, sau này là kimq.tech/kien-thuc)

| Loại | Số lượng/tháng | Ghi chú |
|---|---|---|
| Bài spoke mới (tiếng Việt) | **12** (3 bài/tuần) | 42 bài dự kiến → 3,5 tháng (Stage 1–4) |
| Mở rộng hoặc làm mới pillar | 1–2 | Stage 1: mở rộng cả 4 pillar lên 2.500+ từ; viết pillar P5 nếu duyệt mục 2 |
| Cập nhật bài cũ | 2–4 | Giá, gói, phiên bản model, số sao GitHub. Cập nhật trường `updated` |

12 bài/tháng là mức đội nhỏ giữ được chất lượng (tự thử công cụ, tự chụp ảnh). Tăng lên 16–20 chỉ khi có thêm người viết và người duyệt.

### Phân phối ra các nền tảng

| Nền tảng | Số lượng/tháng | Lấy từ đâu |
|---|---|---|
| Facebook | 12 tóm tắt + 4–8 mẹo ngắn | Mỗi bài mới 1 tóm tắt |
| Threads | 12 chuỗi + 8 bài ngắn | Mỗi bài mới 1 chuỗi; mẹo, số liệu lấy lại từ bài cũ |
| Instagram | 6–8 carousel | Bài P2, P3, C4.4 (câu lệnh, trước–sau) |
| TikTok | 8 video | Bài P2, P3, C4.3; quay màn hình thao tác |
| YouTube Shorts (đề xuất thêm) | 8 | Đăng lại video TikTok, không cần làm mới |
| LinkedIn | 4–6 | P1, C4.5, C4.6, bài doanh nghiệp |
| Substack | 2 bản tin | Mỗi bản tin gom 6 bài mới, mỗi bài 2–3 câu + link |
| dev.to (gốc EN) | 2 | 5 bài P1 + 3 bài C4.7 viết lại tiếng Anh → khoảng 4 tháng |
| Hashnode, HackerNoon, Medium, Plain English | 2 mỗi nền tảng | Bản sao của 2 bài dev.to trong tháng, canonical về dev.to |
| DZone | 1 (từ Stage 2) | Kỹ sư KimQ tự viết, không dùng bài AI |
| GitHub KimQ-Tech | 1 cập nhật | Danh sách repo (awesome list) cập nhật số liệu |
| Product Hunt | 0 | Chỉ khi ra mắt sản phẩm |

## 4. Lịch bài spoke theo Stage

Sắp theo volume giảm dần, đúng thứ tự của claude-seo. Bài thương hiệu có volume cao nhưng ý định điều hướng (Viggle, Vclip) vẫn viết sớm, nhưng phải có giá trị riêng: hướng dẫn tiếng Việt, ảnh thao tác, giới hạn gói miễn phí.

**Stage 1 còn có thêm:** chốt cấu trúc mục 2, mở rộng 4 pillar, thống nhất hồ sơ 14 nền tảng.

### Stage 1 (12 bài, 209,250 lượt tìm/tháng)

| # | Bài | Cluster | Volume | KD |
|---|---|---|---|---|
| 1 | Viggle AI là gì, cách dùng | C2.2 Hướng dẫn từng công cụ video | 74,000 | 27 |
| 2 | Giọng đọc AI tiếng Việt: Vbee, FPT AI, Viettel AI, Vclip | C2.3 Âm thanh cho video | 23,760 | 23 |
| 3 | Tạo nhạc bằng AI | C2.3 Âm thanh cho video | 19,800 | 24 |
| 4 | Làm slide bằng AI | C4.4 Làm việc văn phòng với AI | 18,580 | 26 |
| 5 | Higgsfield AI là gì, cách dùng | C2.2 Hướng dẫn từng công cụ video | 12,100 | 15 |
| 6 | AI agency là gì | C4.6 AI cho doanh nghiệp | 9,900 | 18 |
| 7 | Cách tạo video AI từ ảnh | C2.1 Tạo video theo đầu vào | 9,640 | 26 |
| 8 | Gemini cho sinh viên: nhận gói miễn phí | C4.2 Gemini, ChatGPT và app AI miễn phí | 9,500 | 22 |
| 9 | Check đạo văn AI: cách phát hiện văn bản do AI viết | C4.3 AI cho học tập | 8,400 | 24 |
| 10 | Ghép ảnh bằng AI | C3.2 Sửa ảnh theo việc | 8,350 | 25 |
| 11 | Vclip AI là gì, cách dùng | C2.2 Hướng dẫn từng công cụ video | 8,100 | 30 |
| 12 | AI tạo hình ảnh: công cụ và cách dùng | C3.1 Tạo ảnh bằng AI | 7,120 | 17 |

### Stage 2 (12 bài, 51,740 lượt tìm/tháng)

| # | Bài | Cluster | Volume | KD |
|---|---|---|---|---|
| 1 | Học AI bắt đầu từ đâu: lộ trình, khoá học | C4.3 AI cho học tập | 6,830 | 13 |
| 2 | Tạo logo bằng AI | C3.3 Thiết kế bằng AI | 5,830 | 28 |
| 3 | Kling AI: hướng dẫn, gói miễn phí | C2.2 Hướng dẫn từng công cụ video | 5,300 | 26 |
| 4 | AI giải bài tập: AI Hay, Gauth và cách dùng đúng | C4.3 AI cho học tập | 4,940 | 24 |
| 5 | Làm nét ảnh bằng AI | C3.2 Sửa ảnh theo việc | 4,400 | 12 |
| 6 | Prompt AI: cách viết câu lệnh hiệu quả | C4.4 Làm việc văn phòng với AI | 4,400 | 26 |
| 7 | Mở rộng ảnh bằng AI | C3.2 Sửa ảnh theo việc | 3,870 | 20 |
| 8 | Vidu AI: hướng dẫn | C2.2 Hướng dẫn từng công cụ video | 3,740 | 29 |
| 9 | Các model Claude: Fable, Opus, Sonnet khác nhau thế nào | C4.1 Claude | 3,630 | 21 |
| 10 | AI engineer là gì, học gì | C4.7 AI lập trình | 3,000 | 22 |
| 11 | Cách làm video TikTok bằng hình ảnh | C2.1 Tạo video theo đầu vào | 2,900 | 28 |
| 12 | Luma AI: hướng dẫn | C2.2 Hướng dẫn từng công cụ video | 2,900 | 28 |

### Stage 3 (12 bài, 22,000 lượt tìm/tháng)

| # | Bài | Cluster | Volume | KD |
|---|---|---|---|---|
| 1 | Ghép mặt bằng AI: công cụ và lưu ý pháp lý | C3.2 Sửa ảnh theo việc | 2,900 | 15 |
| 2 | Ứng dụng AI miễn phí đáng dùng | C4.2 Gemini, ChatGPT và app AI miễn phí | 2,560 | 24 |
| 3 | AI trong marketing: ứng dụng và cảnh báo lừa đảo | C4.6 AI cho doanh nghiệp | 2,390 | 17 |
| 4 | Tạo video AI từ văn bản: mẫu câu lệnh | C2.1 Tạo video theo đầu vào | 2,180 | 28 |
| 5 | Top repo Claude Code, Claude skill trên GitHub | C1.1 AI mã nguồn mở | 2,000 | 24 |
| 6 | Gen AI (AI tạo sinh) là gì | C4.5 Tìm kiếm và kiến thức AI | 1,900 | 23 |
| 7 | Kiro AI là gì | C4.7 AI lập trình | 1,900 | 28 |
| 8 | Gemini 3.5 Pro và Flash: khác nhau, giá | C4.2 Gemini, ChatGPT và app AI miễn phí | 1,550 | 27 |
| 9 | AI viết văn: dùng thế nào cho đúng | C4.3 AI cho học tập | 1,470 | 24 |
| 10 | Grok Imagine: tạo video bằng Grok | C2.2 Hướng dẫn từng công cụ video | 1,300 | 22 |
| 11 | Hướng dẫn dùng ChatGPT | C4.2 Gemini, ChatGPT và app AI miễn phí | 1,070 | 28 |
| 12 | Claude for Excel: phân tích bảng tính | C4.1 Claude | 780 | 22 |

### Stage 4 (6 bài, 3,360 lượt tìm/tháng)

| # | Bài | Cluster | Volume | KD |
|---|---|---|---|---|
| 1 | Tạo chatbot AI miễn phí cho website, Zalo, Facebook | C4.6 AI cho doanh nghiệp | 770 | 19 |
| 2 | Cách kiểm tra ảnh có phải AI tạo | C3.2 Sửa ảnh theo việc | 720 | 20 |
| 3 | Tạo ảnh AI trên Zalo | C3.1 Tạo ảnh bằng AI | 700 | 20 |
| 4 | Claude Code là gì | C4.7 AI lập trình | 640 | 23 |
| 5 | Phục hồi ảnh cũ bằng AI | C3.2 Sửa ảnh theo việc | 460 | 26 |
| 6 | Tạo phụ đề tự động cho video | C2.3 Âm thanh cho video | 70 | 15 |
## 5. Quy trình mỗi tuần

| Ngày | Việc |
|---|---|
| Thứ 2, 4, 6 | Đăng 1 bài spoke lên repo. Cập nhật bảng bài trong pillar, CSV, TOPIC-CLUSTERS.md. Thêm link 2–3 bài cùng cluster vào bài mới và sửa bài cũ để link ngược lại |
| Cùng ngày đăng | Facebook tóm tắt + Threads chuỗi |
| Trong tuần | 2 video TikTok/Shorts, 1–2 carousel Instagram, 1 bài LinkedIn |
| 2 tuần/lần | Bản tin Substack; 1 bài tiếng Anh dev.to, rồi các bản sao sau khi dev.to được lập chỉ mục |
| Cuối tháng | Cập nhật 2–4 bài cũ; xem Search Console (khi blog lên kimq.tech): bài nào có lượt hiển thị nhưng ít click thì sửa title/description |
