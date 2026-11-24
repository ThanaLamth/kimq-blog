# Kế hoạch đăng bài lên các nền tảng theo cluster

Cập nhật 24/11/2026. Đi kèm [TOPIC-CLUSTERS.md](TOPIC-CLUSTERS.md). Cột `kenh` trong [cluster-keyword-map.csv](data/keywords/2026-11-23/cluster-keyword-map.csv) ghi kênh đăng cho từng bài.

## 1. Nguyên tắc chung

1. **Một bản gốc, nhiều bản sao có canonical.** Bản gốc tiếng Việt: repo này (sau này là `kimq.tech/kien-thuc/...`). Bản sao đăng đầy đủ chỉ ở nền tảng cho đặt canonical (đánh dấu bản gốc). Nền tảng không cho đặt canonical: chỉ đăng tóm tắt và link về bản gốc.
2. **Đúng ngôn ngữ, đúng người đọc.** Nhóm công cụ AI phổ biến (P2, P3, phần lớn P4) nhắm người Việt, nên đăng lên mạng xã hội tiếng Việt. Nhóm kỹ thuật (P1, C4.7) viết lại bằng tiếng Anh cho các nền tảng dev. Bản tiếng Anh viết lại không bị coi là trùng nội dung với bản tiếng Việt.
3. **Bản gốc tiếng Anh:** khi kimq.tech chưa có `/en/` (Q4 đang chờ Owner), dev.to `@kimqtech` là bản gốc. Hashnode, HackerNoon đặt canonical về dev.to. Khi có `kimq.tech/en/...`, sửa canonical mọi bản về đó.
4. **Đăng bản gốc trước, chờ Google lập chỉ mục, rồi mới đăng bản sao.**
5. **Link về KimQ:** mỗi bài có tối đa 1–2 link sản phẩm liên quan thật sự và 1 link trang chủ. Nhiều nền tảng gắn `nofollow`/`ugc` cho link trong bài, nên giá trị chính là thương hiệu, lượt truy cập giới thiệu và khả năng được AI trích dẫn, không phải điểm link.
6. **Hồ sơ đồng nhất:** cùng tên "KimQ Tech", cùng logo, cùng mô tả một câu, link `https://kimq.tech` và email `contact@kimq.tech` trên mọi nền tảng.

## 2. Quy định từng nền tảng

| Nền tảng | Ngôn ngữ | Đăng gì | Canonical | Lưu ý |
|---|---|---|---|---|
| [dev.to/kimqtech](https://dev.to/kimqtech) | Anh | Bài đầy đủ, **bản gốc tiếng Anh** | Có, trường `canonical_url` | Tối đa 4 thẻ; có thể dùng tài khoản tổ chức |
| [hashnode.com/@kimqtech](https://hashnode.com/@kimqtech) | Anh | Bài đầy đủ, bản sao | Có, mục "Are you republishing?" | Đăng **sau** dev.to, nếu không Hashnode thành bản gốc |
| [hackernoon.com/u/kimqtech](https://hackernoon.com/u/kimqtech) | Anh | Bài đầy đủ, bản sao | Có, mục "First Seen At" | Biên tập viên duyệt. Phải điền nguồn nếu đã đăng nơi khác, nếu không bị coi là đạo văn. Phải nêu rõ lợi ích liên quan khi nhắc sản phẩm KimQ. Canonical về trang công ty có thể bị gỡ nếu không tham gia chương trình thương hiệu của họ |
| [plainenglish.io/author/kimq-tech](https://plainenglish.io/author/kimq-tech) | Anh | Bài đầy đủ 1.000–1.500+ từ | Kiểm tra khi nộp | Chỉ nhận chủ đề lập trình, công nghệ. Kênh "guest post/syndication" đi qua Circuit, cần kiểm tra có tính phí không |
| [dzone.com](https://dzone.com/users/5641567/kimqtech.html) | Anh | **Bài viết riêng, chưa đăng ở đâu**, ≥ 800 từ | DZone là bản gốc; đăng lại nơi khác sau ≥ 1 tuần, canonical về DZone | **Cấm nội dung do AI tạo**, cấm quảng cáo. Kỹ sư KimQ tự viết từ kinh nghiệm thật. Không dùng bản dịch từ repo này |
| [medium.com/@social_76509](https://medium.com/@social_76509) | Anh (chính); Việt cho bài B2B nếu cần | Bài đầy đủ, bản sao | Có: "Import a story" tự đặt canonical, hoặc More settings → Advanced settings → "This story was originally published elsewhere" | Đăng sau dev.to. Có thể gửi bài vào publication (ví dụ Plain English trên Medium). Link trong bài là `nofollow`. Nên đổi tên hồ sơ thành "KimQ Tech" và handle thành `@kimqtech` cho đồng nhất |
| [substack.com/@kimqtech](https://substack.com/@kimqtech) | Anh hoặc Việt | Bản tin tổng hợp + link | **Không** đặt được | Không đăng nguyên bài; tóm tắt 3–5 ý và link về bản gốc |
| [LinkedIn KimQ](https://www.linkedin.com/company/kimq/) | Việt (B2B) | Bài ngắn 150–300 từ + link | Không | Chủ đề doanh nghiệp: P1, C4.6, AI Mode |
| [Facebook](https://www.facebook.com/share/19ud5Stik8/?mibextid=wwXIfr) | Việt | Tóm tắt 150–300 từ + 1 ảnh + link | Không cần (không đăng nguyên bài) | Link đặt ở thân bài hoặc bình luận đầu |
| [Threads @kimqtech](https://www.threads.com/@kimqtech) | Việt | Chuỗi 3–6 ý ngắn, ý cuối có link | Không cần | Mẹo nhanh, so sánh, số liệu |
| [Instagram @kimqtech](https://www.instagram.com/kimqtech/) | Việt | Carousel 6–8 ảnh, link ở bio | Không cần | Hợp bài top/list, câu lệnh, trước–sau khi sửa ảnh |
| [TikTok @kimqaitech](https://www.tiktok.com/@kimqaitech) | Việt | Video 30–60 giây quay màn hình thao tác | Không cần | Hợp P2, P3; có thể làm bằng [AI Studio](https://kimq.tech/san-pham/ai-studio) |
| [GitHub KimQ-Tech](https://github.com/KimQ-Tech) | Anh + Việt | Repo danh sách (awesome list), dữ liệu, mã mẫu | – | Nên chuyển repo `kimq-blog` sang tổ chức này để đúng thương hiệu |
| [Product Hunt @kimq_tech](https://www.producthunt.com/@kimq_tech) | Anh | **Chỉ ra mắt sản phẩm**, không đăng bài | – | AI Studio, Chatbot đa kênh, AI Gateway khi có bản tiếng Anh |

dev.to, hashnode, plainenglish lặp lại trong danh sách gốc, ở đây đã gộp.

## 3. Cluster → kênh

| Cluster | Người đọc | Kênh chính | Kênh phụ | Định dạng |
|---|---|---|---|---|
| C1.1 AI mã nguồn mở | Dev, CTO | dev.to (gốc EN) → Hashnode, HackerNoon | Medium, Plain English, LinkedIn, GitHub KimQ-Tech | Viết lại bằng tiếng Anh, tập trung góc nhìn doanh nghiệp Việt/Đông Nam Á |
| C1.2 Phần mềm vận hành | Chủ DN, kế toán | LinkedIn, Facebook | dev.to (chỉ bài tự động hoá) | Bài ERP gắn chế độ kế toán Việt Nam, chỉ đăng tiếng Việt |
| C2.1 Tạo video theo đầu vào | Người làm nội dung | TikTok, Facebook | Threads, Instagram | Video thao tác từ ảnh → video |
| C2.2 Hướng dẫn từng công cụ video | Người làm nội dung | TikTok, Threads | Facebook | Mỗi công cụ 1 video demo + chuỗi Threads |
| C2.3 Âm thanh cho video | Người bán hàng, người làm nội dung | TikTok, Facebook | Instagram | So sánh giọng đọc (nghe thử); gắn AI Studio |
| C3.1 Tạo ảnh bằng AI | Đại chúng | Instagram, Facebook | Threads, TikTok | Carousel câu lệnh + ảnh kết quả |
| C3.2 Sửa ảnh theo việc | Đại chúng | Instagram, TikTok | Facebook | Ảnh trước–sau |
| C3.3 Thiết kế bằng AI | Chủ shop, DN nhỏ | Facebook, Instagram | Threads | Carousel logo mẫu + câu lệnh |
| C4.1 Claude | Dân văn phòng, dev | Facebook, Threads | LinkedIn | Bảng so sánh gói; ảnh tóm tắt |
| C4.2 Gemini, ChatGPT, app miễn phí | Sinh viên, văn phòng | Facebook, TikTok | Threads | Hướng dẫn từng bước; ưu đãi sinh viên |
| C4.3 AI cho học tập | Sinh viên | TikTok, Facebook | Threads, Instagram | Video ngắn; nhấn mạnh dùng đúng, không gian lận |
| C4.4 Văn phòng (slide, prompt) | Dân văn phòng | Facebook, LinkedIn | Threads, Instagram | Carousel mẫu prompt |
| C4.5 Tìm kiếm và kiến thức AI | Chủ DN, marketer | LinkedIn, Facebook | Substack | Bài "doanh nghiệp cần làm gì" |
| C4.6 AI cho doanh nghiệp | Chủ DN | LinkedIn, Facebook | Substack | Gắn Chatbot đa kênh, Trợ lý Zalo |
| C4.7 AI lập trình | Dev | dev.to (gốc EN) → Hashnode | HackerNoon, Medium, Plain English, GitHub KimQ-Tech | Viết lại bằng tiếng Anh, có ví dụ cấu hình |

**Substack:** bản tin định kỳ gom 3–5 bài mới trong kỳ, mỗi bài 2–3 câu + link. **DZone:** không lấy từ cluster; kỹ sư KimQ tự viết bài kinh nghiệm thật (ví dụ: vận hành AI Gateway, chạy LLM nội bộ, tích hợp Zalo OA), mỗi bài một chủ đề chưa đăng ở đâu.

## 4. Bài tiếng Anh dự kiến cho nền tảng dev

| Bài gốc (VI) | Tiêu đề tiếng Anh dự kiến | Bản gốc EN | Bản sao |
|---|---|---|---|
| [Hướng dẫn chọn phần mềm mã nguồn mở](posts/huong-dan-chon-phan-mem-ma-nguon-mo-cho-doanh-nghiep.md) | How to choose open-source software for your business: licenses, real costs, build vs buy | dev.to | Hashnode, HackerNoon, Medium |
| [Top 10 framework AI Agent](posts/top-10-framework-ai-agent-ma-nguon-mo.md) | 10 open-source AI agent frameworks compared for production use | dev.to | Hashnode, Medium, Plain English |
| [Top 7 AI Gateway](posts/top-7-ai-gateway-ma-nguon-mo.md) | 7 open-source AI gateways to control LLM cost, keys and logs | dev.to | Hashnode, HackerNoon, Medium |
| [Top 7 repo chạy LLM nội bộ](posts/top-7-repo-chay-llm-noi-bo.md) | 7 open-source tools to run LLMs on your own servers | dev.to | Hashnode, Medium, Plain English |
| [Top 8 công cụ tự động hoá](posts/top-8-cong-cu-tu-dong-hoa-quy-trinh-ma-nguon-mo.md) | 8 open-source workflow automation tools (n8n alternatives included) | dev.to | Hashnode, Medium |
| Top repo Claude Code (dự kiến) | Best Claude Code repos and skills on GitHub | dev.to | Hashnode, Medium, Plain English |
| Claude Code là gì (dự kiến) | Viết bài tiếng Việt cho repo; bản EN chỉ khi có góc nhìn riêng | – | – |

Số liệu GitHub (sao, ngày cập nhật) phải lấy lại vào ngày đăng bản tiếng Anh.

## 5. Quy trình cho mỗi bài

1. Bài lên repo (bản gốc tiếng Việt).
2. Facebook, Threads, LinkedIn: đăng tóm tắt + link ngay.
3. Instagram, TikTok: làm carousel/video theo bảng mục 3.
4. Bài thuộc C1.x, C4.7: viết lại tiếng Anh → dev.to → chờ lập chỉ mục → Hashnode (canonical dev.to) → HackerNoon (First Seen At = dev.to) → Medium (Import a story từ link dev.to) → Plain English.
5. Kiểm tra canonical trên từng bản sao: mở mã nguồn trang, tìm `rel="canonical"`.
6. Ghi link đã đăng vào frontmatter bài gốc, trường `published_on` (ví dụ `published_on: {devto: ..., hashnode: ..., medium: ...}`).

## 6. Theo giai đoạn

| Giai đoạn | Việc |
|---|---|
| Stage 1 | Thống nhất hồ sơ trên 14 nền tảng (tên, logo, mô tả, link, email). Thêm các link mạng xã hội vào footer và `sameAs` trên kimq.tech (đang mở trong tracker). Chuyển `kimq-blog` sang GitHub KimQ-Tech. Đăng tóm tắt 9 bài đã có lên Facebook, Threads, LinkedIn |
| Stage 2 | Đăng 5 bài tiếng Anh nhóm P1 lên dev.to rồi các bản sao (Hashnode, HackerNoon, Medium, Plain English). Làm carousel/video cho bài P2, P3, P4. Bắt đầu bản tin Substack |
| Stage 3 | Kỹ sư viết bài riêng cho DZone. Ra mắt sản phẩm trên Product Hunt khi có bản tiếng Anh. Khi kimq.tech có `/kien-thuc` và `/en/`: đổi canonical tất cả bản sao về kimq.tech, thay bản đầy đủ trên GitHub bằng tóm tắt + link |
