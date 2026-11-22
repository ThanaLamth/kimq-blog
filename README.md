# KimQ Tech: Kiến thức phần mềm mã nguồn mở cho doanh nghiệp

Chuyên đề do [KimQ Tech](https://kimq.tech) biên soạn: cách chọn, đánh giá và triển khai phần mềm mã nguồn mở trên GitHub cho doanh nghiệp Việt Nam. Liên hệ: contact@kimq.tech.

## Bắt đầu từ đây

**[Hướng dẫn chọn phần mềm mã nguồn mở cho doanh nghiệp](posts/huong-dan-chon-phan-mem-ma-nguon-mo-cho-doanh-nghiep.md)**: cách đánh giá repo, đọc giấy phép, tính chi phí thật, tự dựng hay dùng giải pháp có sẵn.

## AI mã nguồn mở cho doanh nghiệp

- [Top 10 framework AI Agent mã nguồn mở](posts/top-10-framework-ai-agent-ma-nguon-mo.md)
- [Top 7 AI Gateway mã nguồn mở](posts/top-7-ai-gateway-ma-nguon-mo.md)
- [Top 7 repo chạy LLM nội bộ](posts/top-7-repo-chay-llm-noi-bo.md)

## Phần mềm mã nguồn mở cho vận hành

- [Top 8 công cụ tự động hoá quy trình mã nguồn mở](posts/top-8-cong-cu-tu-dong-hoa-quy-trinh-ma-nguon-mo.md)
- [Top 8 phần mềm ERP, kế toán mã nguồn mở](posts/top-8-phan-mem-erp-ke-toan-ma-nguon-mo.md)

---

## Ghi chú biên tập (nội bộ)

**Cấu trúc:** một trang trụ cột (`type: pillar`) + các bài vệ tinh. Mỗi bài vệ tinh có dòng "Thuộc chuyên đề" link về trang trụ cột, link chéo 2–3 bài liên quan và mục "Về KimQ Tech" ở cuối.

**Link:**
- Giữa các bài: link tương đối tới file `.md` trong repo.
- Sản phẩm, liên hệ: link tuyệt đối `https://kimq.tech/...`.

**Khi chuyển lên blog kimq.tech** (frontmatter `path` là URL dự kiến trên site):
1. Đổi `xxx.md` thành `/kien-thuc/xxx` và `https://kimq.tech/san-pham/...` thành `/san-pham/...`.
2. Bỏ dòng "Thuộc chuyên đề…" dạng trích dẫn nếu site có breadcrumb riêng.
3. Tránh trùng nội dung: sau khi bài lên site, thay bản đầy đủ trên GitHub bằng tóm tắt 3–5 dòng + link "Đọc đầy đủ tại kimq.tech", hoặc cập nhật bản trên site sâu hơn hẳn bản GitHub.

**Số liệu:** lấy từ GitHub API, ghi ở `dataDate`; dữ liệu gốc [data/github-repos-2026-11-20.json](data/github-repos-2026-11-20.json). Khi cập nhật: sửa `updated` và `dataDate`, giữ `published`. Tóm tắt giấy phép không phải tư vấn pháp lý.
