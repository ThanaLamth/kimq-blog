# KimQ Tech: bài blog chuyên mục Kiến thức

Bài viết dạng top/list cho mục `/kien-thuc` trên [kimq.tech](https://kimq.tech).

## Danh sách bài

| # | Bài | Đường dẫn trên site | Gợi ý thứ tự đăng |
|---|---|---|---|
| 1 | [Top 10 framework AI Agent mã nguồn mở](posts/top-10-framework-ai-agent-ma-nguon-mo.md) | `/kien-thuc/top-10-framework-ai-agent-ma-nguon-mo` | 1 |
| 2 | [Top 7 AI Gateway mã nguồn mở](posts/top-7-ai-gateway-ma-nguon-mo.md) | `/kien-thuc/top-7-ai-gateway-ma-nguon-mo` | 2 |
| 3 | [Top 7 repo chạy LLM nội bộ](posts/top-7-repo-chay-llm-noi-bo.md) | `/kien-thuc/top-7-repo-chay-llm-noi-bo` | 3 |
| 4 | [Top 8 công cụ tự động hoá quy trình mã nguồn mở](posts/top-8-cong-cu-tu-dong-hoa-quy-trinh-ma-nguon-mo.md) | `/kien-thuc/top-8-cong-cu-tu-dong-hoa-quy-trinh-ma-nguon-mo` | 4 |
| 5 | [Top 8 phần mềm ERP, kế toán mã nguồn mở](posts/top-8-phan-mem-erp-ke-toan-ma-nguon-mo.md) | `/kien-thuc/top-8-phan-mem-erp-ke-toan-ma-nguon-mo` | 5 |

Bài 1–3 liên kết chéo với nhau, nên đăng gần nhau để không có liên kết hỏng.

## Định dạng

- Markdown, có frontmatter: `title`, `slug`, `path`, `description`, `category`, `tags`, `author`, `published`, `updated`, `dataDate`, `status`.
- Thân bài: mở đầu → bảng tóm tắt → cách chọn → từng mục → đáng chú ý khác → bảng "Nên chọn cái nào?" → mẹo thực tế → liên kết nội bộ → FAQ → ghi chú nguồn.
- Liên kết nội bộ dùng đường dẫn tương đối (`/san-pham/...`, `/kien-thuc/...`).

## Quy tắc số liệu

- Số sao, ngôn ngữ, giấy phép, ngày cập nhật lấy từ GitHub API ngày **20/11/2026** (`dataDate`). Dữ liệu gốc: [data/github-repos-2026-11-20.json](data/github-repos-2026-11-20.json).
- Khi cập nhật số liệu: sửa `updated` và `dataDate`, không sửa `published`.
- Tóm tắt giấy phép chỉ để tham khảo, không phải tư vấn pháp lý.
