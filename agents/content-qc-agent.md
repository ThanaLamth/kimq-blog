# Agent QC nội dung KimQ Tech

Agent kiểm và sửa bài trong `posts/` theo [CONTENT-QC.md](../CONTENT-QC.md) trước khi đăng. Có thể giao cho Codex, Claude Code hoặc bất kỳ agent nào đọc được repo, bằng câu lệnh: **"Đọc agents/content-qc-agent.md và QC bài posts/<slug>.md"**.

## Vai trò và giới hạn

- Agent làm trọn QC: kiểm tự động, chụp ảnh màn hình trang chính thức, đối chiếu số liệu, chấm EOT/SA, sửa bài, ghi báo cáo, commit. Không có bước người duyệt riêng.
- **Không bịa tên tác giả hay người duyệt.** Tác giả giữ "Đội sản phẩm KimQ".
- **Ảnh phải là ảnh chụp màn hình thật** của trang chính thức (trang sản phẩm, bảng giá, tài liệu, repo GitHub, kết quả). Không dùng ảnh AI tạo. Chú thích ghi đúng đó là trang gì, nguồn và ngày chụp. Không viết như thể KimQ đã tự dùng thử nếu không có kết quả thử thật.
- Không đổi `updated` nếu chỉ sửa chính tả, định dạng, thêm ảnh. Đổi `lastReviewed` mỗi lần QC.

## Chuẩn bị (một lần)

```bash
cd /tmp/shot && npm i puppeteer-core sharp   # thư mục công cụ ngoài repo
```

Trình duyệt chụp ảnh: một trình duyệt từ xa có CDP (đặt `BROWSER_WS_ENDPOINT=wss://...`) hoặc Chrome trên máy (đặt `CHROME_PATH`). Nhớ đóng phiên trình duyệt từ xa sau khi chụp.

## Quy trình cho mỗi bài

1. **Kiểm tự động**
   ```bash
   python3 scripts/content_qc.py posts/<slug>.md --check-links --report qc-reports
   ```

2. **Ảnh chụp màn hình (B1, cần ≥ 3)**
   - Thêm mục cho bài vào [data/screenshots.json](../data/screenshots.json): `url` (trang chính thức), `after` (dòng tiêu đề chính xác trong bài), `name`, `alt` (mô tả đúng nội dung ảnh), `captured` (ngày chụp). Tuỳ chọn: `scrollToText` (cuộn tới và tô nổi bật đoạn chữ cần chỉ, ví dụ "Vietnam" trong danh sách quốc gia), `scrollY`, `waitMs`.
   - Chụp: `BROWSER_WS_ENDPOINT=... PUPPETEER_PATH=/tmp/shot/node_modules node scripts/capture_screenshots.mjs <slug>` → `images/<slug>/<name>.webp`.
   - **Xem lại từng ảnh**: không bị popup/cookie che, không trang trống, không trang lỗi, đúng nội dung chú thích. Sai thì sửa thông số và chụp lại với `--force`.
   - Chèn: `python3 scripts/insert_images.py <slug>` (ảnh đặt sau đoạn đầu của mục, chú thích có link nguồn và ngày chụp).

3. **Đối chiếu số liệu (C1, C3, C4)**: lấy ít nhất 3 số liệu dễ sai nhất (giá, tên gói, phiên bản model, giới hạn gói miễn phí, số sao GitHub, số hiệu văn bản). So với nguồn chính thức, ưu tiên chính các ảnh vừa chụp. Ghi bảng vào `qc-reports/<slug>.md`:

   | Số liệu trong bài | Nguồn | Giá trị ở nguồn | Kết quả |
   |---|---|---|---|

   Sai thì sửa bài và cập nhật `dataDate`, `updated`. Không tìm được nguồn thì ghi "Chưa xác minh" và bỏ hoặc viết lại câu đó cho đúng mức chắc chắn. Không đoán.

4. **Sửa lỗi văn bản**: câu sáo, câu đệm (A1, A2), thời gian mơ hồ (C1), link về pillar và 2 bài cùng cluster (D, sửa cả chiều ngược lại), description 120–170 ký tự.

5. **Frontmatter và nhãn**: `lastReviewed: <hôm nay>`, `aiAssisted: true`, `sources:` (link nguồn chính thức dùng trong bài). Dòng cuối bài, trên mục "Về KimQ Tech":
   `> Bài viết có sử dụng AI hỗ trợ soạn thảo. Nội dung và số liệu được đối chiếu với nguồn chính thức ngày <dd/mm/yyyy>; ảnh là ảnh chụp màn hình trang chính thức, có ghi nguồn và ngày chụp.`

6. **Chấm EOT/SA** (1–5 mỗi mục, ghi lý do 1 câu; cần ≥ 15/20). Dưới 15 thì ghi cần bổ sung gì (bảng so sánh riêng, ví dụ thực tế cho doanh nghiệp Việt, mẫu câu lệnh đã thử…) và bổ sung luôn nếu làm được từ nguồn chính thức.

7. **Chạy lại** `python3 scripts/content_qc.py --report qc-reports`, rồi commit. Trước khi commit kiểm không có khoá API nào trong repo.

## Kết luận trong báo cáo

- `ĐẠT`: PASS tự động, số liệu khớp, EOT/SA ≥ 15.
- `ĐẠT CÓ GHI CHÚ`: chỉ còn FLAG không chặn (pillar chưa đủ 2.500 từ, từ khoá chờ chuyển sang bài con, site chặn kiểm tra link tự động).
- `CHƯA ĐẠT`: còn FAIL hoặc có số liệu chưa xác minh.

## Trả lời người giao việc

Tiếng Việt, ngắn: mỗi bài một dòng kết luận, số liệu đã sửa, việc còn lại, link báo cáo trên GitHub.
