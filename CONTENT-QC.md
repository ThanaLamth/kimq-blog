# Quy chuẩn viết và QC bài trước khi đăng

Cập nhật 24/11/2026. Chuyển từ bộ QC trong repo [Google-Update](https://github.com/ThanaLamth/Google-Update) (dự án 14 site trên Railway, file `CONTENT-FLOW-TICKETS.md`, `SEO-HANDOFF-2026-10-29.md`, `EDITORIAL-CREDITS-RESEARCH.md`), chỉnh cho blog KimQ Tech: bài tiếng Việt về công cụ AI và phần mềm mã nguồn mở. Đi kèm [PUBLISHING-CALENDAR.md](PUBLISHING-CALENDAR.md).

## 1. Vì sao phải QC kỹ

Repo Google-Update ghi lại các tín hiệu Google năm 2026 mà 14 site đã bị ảnh hưởng:

| Tín hiệu | Ý nghĩa với KimQ |
|---|---|
| Spam Update tháng 8 và tháng 9/2026 nhắm vào **scaled content**, nội dung AI không có giá trị riêng, bài review mỏng | Không đăng hàng loạt. Giữ khoảng 12 bài/tháng, mỗi bài có thứ site khác không có |
| Gary Illyes (5/10/2026): nội dung số lượng lớn, ít công sức nay là vấn đề lớn hơn spam link | Mỗi bài phải có công sức thật: tự thử, tự chụp, tự so sánh |
| Yêu cầu bắt buộc kiểm chứng thủ công nội dung có AI hỗ trợ (1/10/2026) | Mỗi bài kiểm 3 số liệu; có người duyệt khác người viết |
| Khung EOT/SA: Effort, Originality, Talent, Accuracy | Dùng làm 4 tiêu chí chấm điểm (mục 4) |
| Ghi tác giả giả là vi phạm chính sách lừa dối (8/10/2026) | **Không bịa tên tác giả.** Chỉ ghi người thật của KimQ hoặc "Đội sản phẩm KimQ" |
| `lastmod` sai còn tệ hơn không có (16/7/2026) | Chỉ đổi `updated` khi nội dung thay đổi thật |
| John Mueller: site bị lo ngại chất lượng sẽ bị giảm lập chỉ mục ("crawled, not indexed") | Chất lượng toàn site quyết định số trang được lập chỉ mục khi blog lên kimq.tech |

Các mốc trên lấy từ repo Google-Update. Trích dẫn gốc ở file `SEO-HANDOFF-2026-10-29.md` của repo đó.

## 2. Frontmatter bắt buộc thêm

```yaml
author: Đội sản phẩm KimQ        # hoặc tên người thật, có trang hồ sơ
reviewer: <tên người duyệt thật>  # khác người viết
lastReviewed: 2026-11-24         # ngày rà soát nội dung gần nhất
dataDate: 2026-11-24             # ngày lấy giá, gói, số sao GitHub
tested: true                     # đã tự dùng thử công cụ trong bài
aiAssisted: true                 # có dùng AI hỗ trợ viết
sources:                         # nguồn chính thức đã kiểm
  - https://...
```

Cuối bài, trên mục "Về KimQ Tech", thêm 1 dòng:

> Bài viết có sử dụng AI hỗ trợ soạn thảo. Nội dung, số liệu và ảnh thao tác do <reviewer> kiểm tra ngày <lastReviewed>.

## 3. Cách viết từng dạng bài

### Dạng "X là gì, cách dùng" (Viggle, Higgsfield, Kling, Claude Code…)

1. **Mở bài 2–3 câu:** X làm được gì, cho ai, miễn phí hay trả phí. Không định nghĩa chung chung.
2. **Bảng thông tin nhanh:** nhà phát triển, nền tảng, gói miễn phí (giới hạn cụ thể), giá gói trả phí, có tiếng Việt không, ngày kiểm tra.
3. **Hướng dẫn từng bước** có ảnh chụp màn hình thật (tối thiểu 3 ảnh), làm trên tài khoản KimQ.
4. **Kết quả thử thật:** đầu vào, đầu ra, thời gian chạy, lỗi gặp phải.
5. **Giới hạn và rủi ro:** bản quyền, dữ liệu cá nhân, watermark, điều khoản thương mại.
6. **So sánh với 2–3 công cụ cùng cluster**, link sang bài tương ứng.
7. **Câu hỏi thường gặp:** 3–5 câu lấy từ từ khoá phụ trong CSV.

### Dạng top/list (Top công cụ, Top repo)

1. **Nêu tiêu chí chọn** và vì sao số lượng là N. Nếu danh sách có 7 mục trở lên mà không giải thích lý do chọn thì bị trượt QC.
2. **Bảng so sánh tổng:** tên, phù hợp với ai, giá, điểm mạnh, điểm yếu, ngày dữ liệu.
3. **Mỗi mục có:** đã thử gì, kết quả, ai nên dùng, ai không nên dùng.
4. **Với repo GitHub:** số sao, ngày commit gần nhất, giấy phép, lấy vào ngày đăng.
5. **Gợi ý chọn theo tình huống**, thay cho phần "Kết luận" chỉ tóm tắt lại.

### Dạng hướng dẫn tác vụ (làm slide, tạo nhạc, ghép ảnh, giọng đọc…)

1. **Kết quả mẫu đầu bài:** ảnh, file nghe thử, slide mẫu.
2. **Chọn công cụ theo nhu cầu:** bảng 3–5 công cụ.
3. **Quy trình từng bước** với 1 công cụ chính, có ảnh thật.
4. **Mẫu câu lệnh (prompt)** đã thử, kèm kết quả.
5. **Lỗi thường gặp và cách sửa.**

## 4. Checklist QC trước khi đăng

### Phần A: Dấu vết văn AI (trượt bất kỳ mục nào thì trả về người viết)

- [ ] Description không phải câu đầu bài chép lại, không có cụm kiểu "Bài viết này sẽ…", không bị cắt cụt.
- [ ] Không mở bài bằng "Trong bài viết này", "Ngày nay", "Trong những năm gần đây", "Trong kỷ nguyên số", "Hãy cùng tìm hiểu".
- [ ] Không có câu đệm: "Đáng chú ý là", "Cần lưu ý rằng", "Như đã đề cập".
- [ ] Không có placeholder: `[CẦN…]`, `[LINK]`, `TODO`.
- [ ] Không có "các chuyên gia cho rằng…" mà không nêu tên.
- [ ] Không có phần "Kết luận"/"Tóm lại" chỉ lặp lại ý.
- [ ] Không có "gần đây", "mới đây", "vừa qua" mà thiếu ngày cụ thể.

### Phần B: E-E-A-T

- [ ] **B1. Trải nghiệm thật:** ít nhất 3 ảnh chụp thao tác thật, hoặc kết quả thử nghiệm có số liệu.
- [ ] **B2. Người duyệt:** có `reviewer` khác người viết. Bài kỹ thuật (P1, C4.7) cần người duyệt là kỹ sư.
- [ ] **B3. Nguồn:** ít nhất 2 link nguồn chính thức (trang hãng, tài liệu, GitHub, văn bản pháp luật). Không có link hỏng.
- [ ] **B4. Minh bạch:** nhãn AI hỗ trợ cuối bài. Nếu nhắc sản phẩm KimQ (AI Studio, Chatbot, AI Gateway) thì ghi rõ "sản phẩm của KimQ Tech".

### Phần C: Độ chính xác và độ mới

- [ ] **C1.** Chọn 3 số liệu (giá, giới hạn gói, số sao, ngày) và đối chiếu nguồn gốc. Sai 1/3 thì trượt cả bài.
- [ ] **C2.** Có `dataDate`. Giá và gói ghi "tại ngày …".
- [ ] **C3.** Tên sản phẩm, tên công ty, tên model đúng chính tả của hãng.
- [ ] **C4.** Văn bản pháp luật (thông tư, nghị định) có số hiệu và link nguồn chính thức.

### Phần D: SEO cluster

- [ ] Từ khoá chính đúng như cột `main_kw` trong CSV, không trùng bài khác.
- [ ] Có link về pillar và 2–3 bài cùng cluster. Sửa các bài đó để link ngược lại.
- [ ] Cập nhật bảng "Bài trong chuyên đề" của pillar, cập nhật `TOPIC-CLUSTERS.md` và CSV.

### Kết quả QC

| Kết quả | Xử lý |
|---|---|
| Đạt tất cả | Đăng |
| Lỗi nhỏ 1–2 mục B/D | Người duyệt sửa luôn rồi đăng |
| Trượt bất kỳ mục A hoặc C1 | Trả người viết |
| Sai số liệu hoặc còn placeholder | Không đăng |

### Chấm điểm EOT/SA (mỗi tiêu chí 1–5, cần tổng ≥ 15/20)

| Tiêu chí | Câu hỏi |
|---|---|
| Effort | Có tự thử, tự chụp, tự so sánh không? |
| Originality | Có điều gì site khác chưa có không (kết quả thử, bảng so sánh riêng, góc nhìn doanh nghiệp Việt)? Nếu không có thì không đăng |
| Talent | Người viết hoặc duyệt có đúng chuyên môn không? |
| Accuracy | Số liệu, giá, tên đã kiểm hết chưa? |

## 5. Sau khi đăng

- **Rà soát định kỳ:** bài về giá và gói công cụ AI rà lại mỗi 3 tháng; pillar rà lại mỗi quý.
- **Khi cập nhật:** chỉ đổi `updated`/`lastReviewed` khi nội dung đổi thật. Ghi 1 dòng "Cập nhật ngày …: …" đầu bài.
- **Bài không còn đúng** (công cụ đóng cửa, đổi tên): sửa hoặc gộp, không để nguyên.

## 6. Kết quả QC 13 bài hiện có (24/11/2026)

Quét tự động phần A, B1, B3, B4 và B2. Chưa kiểm C1 thủ công.

| Bài | Nguồn ngoài | Ảnh thật | Lỗi A | Thiếu |
|---|---|---|---|---|
| [cau-lenh-tao-anh-ghep-anh-gemini](posts/cau-lenh-tao-anh-ghep-anh-gemini.md) | 2 | 0 | – | Ảnh, nhãn AI, người duyệt |
| [che-do-ai-google-ai-mode-la-gi](posts/che-do-ai-google-ai-mode-la-gi.md) | 1 | 0 | 1 câu thời gian mơ hồ | Nguồn, ảnh, nhãn AI, người duyệt |
| [claude-design-la-gi](posts/claude-design-la-gi.md) | 1 | 0 | – | Nguồn, ảnh, nhãn AI, người duyệt |
| [claude-la-gi-so-sanh-cac-goi-claude](posts/claude-la-gi-so-sanh-cac-goi-claude.md) | 2 | 0 | – | Ảnh, nhãn AI, người duyệt |
| [huong-dan-chon-phan-mem-ma-nguon-mo-cho-doanh-nghiep](posts/huong-dan-chon-phan-mem-ma-nguon-mo-cho-doanh-nghiep.md) (pillar) | 0 | 0 | – | Nguồn, ảnh, nhãn AI, người duyệt |
| [huong-dan-dung-cong-cu-ai-pho-bien](posts/huong-dan-dung-cong-cu-ai-pho-bien.md) (pillar) | 0 | 0 | – | Nguồn, ảnh, nhãn AI, người duyệt |
| [top-10-framework-ai-agent-ma-nguon-mo](posts/top-10-framework-ai-agent-ma-nguon-mo.md) | 12 | 0 | – | Ảnh, nhãn AI, người duyệt |
| [top-7-ai-gateway-ma-nguon-mo](posts/top-7-ai-gateway-ma-nguon-mo.md) | 8 | 0 | – | Ảnh, nhãn AI, người duyệt |
| [top-7-repo-chay-llm-noi-bo](posts/top-7-repo-chay-llm-noi-bo.md) | 8 | 0 | 1 câu đệm | Ảnh, nhãn AI, người duyệt |
| [top-8-cong-cu-tu-dong-hoa-quy-trinh-ma-nguon-mo](posts/top-8-cong-cu-tu-dong-hoa-quy-trinh-ma-nguon-mo.md) | 10 | 0 | – | Ảnh, nhãn AI, người duyệt |
| [top-8-phan-mem-erp-ke-toan-ma-nguon-mo](posts/top-8-phan-mem-erp-ke-toan-ma-nguon-mo.md) | 8 | 0 | – | Ảnh, nhãn AI, người duyệt; kiểm Thông tư 99/2025 |
| [top-cong-cu-ai-chinh-sua-anh](posts/top-cong-cu-ai-chinh-sua-anh.md) (pillar) | 10 | 0 | – | Ảnh, nhãn AI, người duyệt |
| [top-cong-cu-tao-video-ai](posts/top-cong-cu-tao-video-ai.md) (pillar) | 5 | 0 | – | Ảnh, người duyệt |

**Việc cần làm trước khi đăng thêm bài mới:**
1. Chốt người duyệt thật của KimQ: 1 người cho nhóm công cụ AI, 1 kỹ sư cho P1 và C4.7.
2. Bổ sung 3+ ảnh thao tác thật cho từng bài, ưu tiên 4 pillar.
3. Thêm nguồn chính thức cho 4 bài có dưới 2 nguồn.
4. Thêm frontmatter mục 2 và dòng nhãn AI hỗ trợ vào 13 bài.
5. Kiểm C1 các điểm chưa xác minh: Thông tư 99/2025; HeyGen/Synthesia hỗ trợ tiếng Việt; Seedance, Hailuo, Luma, Canva, Remini; quảng cáo và số liệu AI Mode trong Search Console.
