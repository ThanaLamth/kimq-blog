# Agent QC nội dung KimQ Tech

Agent kiểm bài trong `posts/` theo [CONTENT-QC.md](../CONTENT-QC.md) trước khi đăng. Có thể giao cho Codex, Claude Code hoặc bất kỳ agent nào đọc được repo, bằng câu lệnh: **"Đọc agents/content-qc-agent.md và QC bài posts/<slug>.md"**.

## Vai trò và giới hạn

- Agent làm **QC sơ bộ**: chạy kiểm tự động, kiểm link, đối chiếu số liệu với nguồn, chấm EOT/SA, sửa các lỗi văn bản an toàn, ghi báo cáo.
- Agent **không phải người duyệt**. Không bao giờ ghi tên agent hoặc tên bịa vào `reviewer`, vì Google coi tác giả/người duyệt giả là vi phạm. Trường `reviewer` chỉ do người thật của KimQ điền sau khi đọc báo cáo.
- Agent **không tạo ảnh chụp màn hình giả** và không dùng ảnh AI thay cho ảnh thao tác. Thiếu ảnh thì ghi vào báo cáo để người làm chụp.
- Agent **không đổi `updated`** nếu chỉ sửa chính tả hoặc định dạng.

## Quy trình cho mỗi bài

1. **Chạy kiểm tự động**
   ```bash
   python3 scripts/content_qc.py posts/<slug>.md --check-links --report qc-reports
   ```
   Mở `qc-reports/<slug>.md`.

2. **Sửa ngay các lỗi an toàn** (không đổi ý nghĩa):
   - Câu sáo, câu đệm (A1, A2): viết lại câu đó.
   - Thời gian mơ hồ (C1): thay bằng ngày cụ thể lấy từ nguồn. Không có nguồn thì bỏ câu.
   - Link về pillar hoặc link bài cùng cluster còn thiếu (D): thêm vào đúng ngữ cảnh. Sửa cả pillar và bài cùng cluster để có link ngược lại.
   - Dòng nhãn AI hỗ trợ cuối bài (B4), ngay trên mục "Về KimQ Tech":
     `> Bài viết có sử dụng AI hỗ trợ soạn thảo. Nội dung, số liệu và ảnh thao tác do <reviewer> kiểm tra ngày <lastReviewed>.`
     Khi chưa có reviewer, giữ nguyên `<reviewer>` để bài trượt QC đến khi người thật điền.
   - Thêm các trường `aiAssisted: true`, `sources:` (liệt kê link nguồn chính thức đã dùng trong bài). Chỉ ghi `tested: true` khi người làm xác nhận đã dùng thử.

3. **Kiểm số liệu (C1, C3, C4)**: chọn ít nhất 3 số liệu dễ sai nhất (giá, giới hạn gói miễn phí, số sao GitHub, ngày ra mắt, số hiệu văn bản). Mở nguồn chính thức (trang giá của hãng, tài liệu, trang GitHub, văn bản pháp luật) và ghi vào báo cáo:

   | Số liệu trong bài | Nguồn đã mở | Giá trị ở nguồn | Kết quả |
   |---|---|---|---|

   - Đúng: ghi "Khớp".
   - Sai: sửa trong bài, cập nhật `dataDate` và ghi "Đã sửa".
   - Không tìm được nguồn: ghi "Chưa xác minh" và đánh FAIL. Không đoán.

4. **Chấm EOT/SA** (mỗi mục 1–5, ghi lý do 1 câu):
   - Effort: có ảnh thật, kết quả thử thật không.
   - Originality: có bảng so sánh riêng, góc nhìn doanh nghiệp Việt, dữ liệu tự thu không. Nếu không có gì khác so với 3 bài top Google, ghi rõ cần thêm gì.
   - Talent: đúng chuyên môn người duyệt cần có (P1, C4.7 cần kỹ sư).
   - Accuracy: kết quả bước 3.

5. **Ghi kết luận vào `qc-reports/<slug>.md`**:
   - `SẴN SÀNG CHỜ DUYỆT`: không còn lỗi, chỉ chờ người thật điền `reviewer`, `lastReviewed`.
   - `CẦN NGƯỜI LÀM`: thiếu ảnh thao tác, chưa dùng thử, cần chuyên gia.
   - `TRẢ VỀ VIẾT LẠI`: EOT/SA < 15/20, hoặc sai số liệu không sửa được.

6. **Chạy lại** `python3 scripts/content_qc.py --report qc-reports` để cập nhật [qc-reports/README.md](../qc-reports/README.md), rồi commit.

## Khi QC cả loạt bài

Chạy `python3 scripts/content_qc.py --check-links --report qc-reports`. Xử lý theo thứ tự: pillar trước, rồi bài trong Stage hiện tại của [PUBLISHING-CALENDAR.md](../PUBLISHING-CALENDAR.md).

## Kết quả trả cho người giao việc

Trả lời ngắn bằng tiếng Việt:
- Mỗi bài một dòng: kết luận và việc còn lại cho người thật làm (chụp ảnh nào, ai duyệt).
- Số liệu đã sửa.
- Link báo cáo trên GitHub.
