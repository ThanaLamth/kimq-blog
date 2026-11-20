---
title: "Top 7 AI Gateway mã nguồn mở trên GitHub: quản lý chi phí và dữ liệu khi dùng nhiều mô hình AI (cập nhật 11/2026)"
slug: top-7-ai-gateway-ma-nguon-mo
path: /kien-thuc/top-7-ai-gateway-ma-nguon-mo
description: "7 AI Gateway mã nguồn mở: LiteLLM, Kong, Portkey, Bifrost, Helicone, Envoy AI Gateway, One API. AI Gateway là gì, so sánh tính năng, giấy phép và cách chọn cho doanh nghiệp."
category: AI Gateway
tags: [ai gateway, llm gateway, github, mã nguồn mở, litellm, quản lý chi phí ai]
author: Đội sản phẩm KimQ
published: 2026-11-20
updated: 2026-11-20
dataDate: 2026-11-20
status: ready
---

Khi một công ty có phòng kinh doanh dùng ChatGPT, phòng kỹ thuật dùng Claude, bộ phận chăm sóc khách hàng dùng Gemini, câu hỏi nhanh chóng xuất hiện: **tháng này mỗi phòng tiêu bao nhiêu tiền AI? Ai đã gửi dữ liệu khách hàng ra ngoài? Nếu một nhà cung cấp sập thì sao?**

**AI Gateway** (cổng AI) là lớp đứng giữa ứng dụng và các nhà cung cấp mô hình, giải quyết đúng các câu hỏi đó. Bài này tổng hợp **7 AI Gateway mã nguồn mở đáng chú ý trên GitHub**, số liệu lấy ngày **20/11/2026**.

## AI Gateway làm được gì?

- **Một cửa cho mọi mô hình:** ứng dụng gọi một API duy nhất (thường theo chuẩn OpenAI), gateway chuyển tới OpenAI, Anthropic, Google, mô hình nội bộ…
- **Quản lý khoá và ngân sách:** cấp khoá riêng cho từng phòng ban, đặt hạn mức chi tiêu, giới hạn số lượt gọi.
- **Dự phòng (fallback):** nhà cung cấp A lỗi hoặc chậm thì tự chuyển sang B.
- **Ghi nhật ký, đo chi phí:** biết ai gọi mô hình nào, tốn bao nhiêu token, bao nhiêu tiền.
- **Kiểm soát nội dung (guardrail):** chặn hoặc che dữ liệu nhạy cảm trước khi gửi ra ngoài.

## Tóm tắt nhanh

| # | Repo | Sao GitHub | Ngôn ngữ | Giấy phép | Hợp nhất với |
|---|---|---|---|---|---|
| 1 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | ~63,6 nghìn | Python | MIT, trừ thư mục `enterprise/` | Lựa chọn phổ biến nhất, hỗ trợ hơn 100 nhà cung cấp |
| 2 | [Kong/kong](https://github.com/Kong/kong) | ~44,4 nghìn | Lua | Apache 2.0 | Công ty đã dùng Kong làm API Gateway |
| 3 | [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | ~13,4 nghìn | TypeScript | MIT | Cần guardrail, định tuyến linh hoạt |
| 4 | [maximhq/bifrost](https://github.com/maximhq/bifrost) | ~9,8 nghìn | Go | Apache 2.0 | Tải lớn, cần độ trễ thấp |
| 5 | [Helicone/helicone](https://github.com/Helicone/helicone) | ~6,3 nghìn | TypeScript | Apache 2.0 | Theo dõi, đo chi phí, đánh giá chất lượng |
| 6 | [theagentrouter/agent-router](https://github.com/theagentrouter/agent-router) | ~2,4 nghìn | Go | Apache 2.0 | Hạ tầng Kubernetes, Envoy |
| 7 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | ~37,5 nghìn | Go, JavaScript | MIT | Chia khoá, chia hạn mức đơn giản |

*Số sao làm tròn, lấy từ GitHub API ngày 20/11/2026. Số sao cho biết mức độ quan tâm, không phải chất lượng.*

## Chúng tôi chọn thế nào

- **Chức năng chính là gateway:** đứng giữa ứng dụng và nhà cung cấp mô hình, không chỉ là thư viện gọi API.
- **Tự triển khai được** trên hạ tầng của doanh nghiệp.
- **Giấy phép cho phép dùng nội bộ;** phần tính năng doanh nghiệp có giấy phép riêng được ghi rõ.
- **Còn được bảo trì;** repo ít hoạt động được ghi chú.

## 1. LiteLLM: phổ biến nhất

**LiteLLM** gồm thư viện Python và máy chủ proxy, cho phép gọi hơn 100 nhà cung cấp mô hình bằng cùng định dạng API OpenAI. Bản proxy có khoá ảo theo người dùng, nhóm, ngân sách, giới hạn tốc độ, dự phòng và ghi nhật ký chi phí.

- **Điểm mạnh:** hỗ trợ rộng nhất; cộng đồng lớn; dễ dựng bằng Docker.
- **Lưu ý giấy phép:** phần chính là MIT; thư mục `enterprise/` (một số tính năng như SSO, kiểm soát nâng cao) có giấy phép riêng, cần mua để dùng.
- **Hợp với:** đa số doanh nghiệp muốn bắt đầu.

## 2. Kong: mở rộng từ API Gateway có sẵn

**Kong** là API Gateway lâu đời, có thêm các plugin AI (định tuyến tới nhiều nhà cung cấp, quản lý lời nhắc, giới hạn theo token). Nếu công ty đã dùng Kong cho API thông thường, thêm lớp AI là bước tự nhiên.

- **Điểm cần cân nhắc:** một số plugin AI nâng cao chỉ có ở bản doanh nghiệp; kiểm tra trước khi chọn.
- **Giấy phép:** Apache 2.0 (bản mã nguồn mở).

## 3. Portkey Gateway: guardrail tích hợp

**Portkey Gateway** là gateway gọn nhẹ, định tuyến tới rất nhiều mô hình, có sẵn cơ chế thử lại, dự phòng, cân bằng tải và **guardrail** kiểm tra đầu vào, đầu ra.

- **Hợp với:** ứng dụng cần kiểm soát nội dung trả về, ví dụ chatbot cho khách hàng.
- **Giấy phép:** MIT.

## 4. Bifrost: tốc độ cao

**Bifrost** viết bằng Go, tập trung vào hiệu năng và độ trễ thấp khi lưu lượng lớn. Ngoài vai trò LLM gateway còn làm cổng cho MCP (giao thức kết nối công cụ cho agent).

- **Hợp với:** hệ thống có nhiều lượt gọi mỗi giây, đội quen vận hành dịch vụ Go.
- **Giấy phép:** Apache 2.0.

## 5. Helicone: theo dõi và đo chi phí

**Helicone** thiên về **quan sát (observability)**: ghi lại mọi yêu cầu, thời gian phản hồi, chi phí, cho phép gắn nhãn theo người dùng hoặc tính năng và đánh giá chất lượng câu trả lời.

- **Hợp với:** đội cần biết rõ AI đang tốn tiền ở đâu trước khi tối ưu.
- **Giấy phép:** Apache 2.0.

## 6. Envoy AI Gateway (agent-router): cho hạ tầng Kubernetes

Repo **agent-router** (trước đây là dự án Envoy AI Gateway) xây trên Envoy Gateway, quản lý truy cập thống nhất tới các dịch vụ AI tạo sinh, hợp với môi trường Kubernetes.

- **Hợp với:** đội hạ tầng đã dùng Envoy, Kubernetes và muốn quản lý AI như mọi dịch vụ khác.
- **Giấy phép:** Apache 2.0.

## 7. One API: chia khoá và hạn mức đơn giản

**One API** là hệ thống quản lý và phân phối khoá API cho nhiều nhà cung cấp, có giao diện quản trị, hạn mức theo người dùng. Rất phổ biến trong cộng đồng tiếng Trung.

- **Lưu ý:** lần cập nhật mã gần nhất là **09/01/2026**, ít hoạt động hơn các lựa chọn khác; cân nhắc khi dùng lâu dài.
- **Giấy phép:** MIT.

## Đáng chú ý khác

- [langfuse/langfuse](https://github.com/langfuse/langfuse) (~37,6 nghìn sao): nền tảng theo dõi, đánh giá và quản lý lời nhắc cho ứng dụng LLM. Không phải gateway thuần nhưng thường dùng kèm gateway để phân tích chất lượng. Giấy phép MIT, trừ các thư mục `ee/`.

## Nên chọn cái nào?

| Tình huống | Gợi ý |
|---|---|
| Mới bắt đầu, cần hỗ trợ nhiều nhà cung cấp | LiteLLM |
| Đã dùng Kong cho API | Kong |
| Chatbot cho khách hàng, cần kiểm soát nội dung | Portkey Gateway |
| Lưu lượng lớn, cần độ trễ thấp | Bifrost |
| Muốn biết rõ chi phí và chất lượng trước | Helicone, kèm Langfuse |
| Hạ tầng Kubernetes, Envoy | Envoy AI Gateway (agent-router) |

## 5 chính sách nên cấu hình ngay khi triển khai

1. **Mỗi phòng ban một khoá, một ngân sách tháng.** Hết ngân sách thì cảnh báo hoặc chặn, tránh hoá đơn bất ngờ.
2. **Che dữ liệu nhạy cảm** (số CCCD, số tài khoản, số điện thoại, lương) trước khi gửi tới mô hình bên ngoài.
3. **Định tuyến theo mức nhạy cảm:** dữ liệu nội bộ quan trọng đi tới mô hình chạy nội bộ; việc thông thường đi tới mô hình đám mây.
4. **Bật dự phòng** ít nhất hai nhà cung cấp cho các tính năng quan trọng.
5. **Quy định rõ việc lưu nhật ký:** lưu những gì (chỉ số liệu, hay cả nội dung lời nhắc), lưu bao lâu, ai được xem.

## Tự dựng hay dùng dịch vụ có sẵn?

Tự dựng gateway mã nguồn mở cho bạn toàn quyền kiểm soát nhưng cần người vận hành: cập nhật phiên bản, sao lưu, giám sát, cấu hình bảo mật. Nếu doanh nghiệp muốn có ngay **báo cáo chi phí theo phòng ban, che dữ liệu nhạy cảm và tự chuyển nhà cung cấp khi lỗi** mà không tự vận hành, xem [KimQ AI Gateway](/san-pham/ai-gateway).

Đọc thêm: [Top 7 repo chạy LLM nội bộ](/kien-thuc/top-7-repo-chay-llm-noi-bo) và [Top 10 framework AI Agent mã nguồn mở](/kien-thuc/top-10-framework-ai-agent-ma-nguon-mo).

## Câu hỏi thường gặp

**AI Gateway khác API Gateway thông thường thế nào?**
API Gateway quản lý theo số lượt gọi. AI Gateway hiểu thêm về token, chi phí theo mô hình, định dạng lời nhắc, dự phòng giữa các nhà cung cấp và kiểm soát nội dung.

**Có làm chậm ứng dụng không?**
Gateway thêm một bước trung gian, thường chỉ vài mili giây, rất nhỏ so với thời gian mô hình trả lời (thường vài giây).

**Công ty nhỏ có cần AI Gateway không?**
Nếu chỉ một người dùng một mô hình thì chưa cần. Khi từ hai phòng ban hoặc hai nhà cung cấp trở lên, hoặc có dữ liệu khách hàng đi qua AI, gateway giúp kiểm soát chi phí và rủi ro.

**Gateway có lưu nội dung câu hỏi không?**
Tuỳ cấu hình. Hầu hết cho phép chọn chỉ lưu số liệu (token, chi phí, thời gian) hoặc lưu cả nội dung. Với dữ liệu nhạy cảm, nên tắt lưu nội dung hoặc che trước khi lưu.

---

*Số liệu lấy từ GitHub API ngày 20/11/2026 và có thể đã thay đổi. Nội dung giấy phép tóm tắt để tham khảo, không phải tư vấn pháp lý; hãy đọc tệp LICENSE gốc của từng repo trước khi dùng thương mại.*
