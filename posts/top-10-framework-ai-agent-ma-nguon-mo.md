---
title: "Top 10 framework AI Agent mã nguồn mở trên GitHub (cập nhật 11/2026)"
slug: top-10-framework-ai-agent-ma-nguon-mo
path: /kien-thuc/top-10-framework-ai-agent-ma-nguon-mo
description: "10 repo GitHub mã nguồn mở để xây AI Agent: Dify, LangChain, LangGraph, CrewAI, LlamaIndex… So sánh số sao, ngôn ngữ, giấy phép và nên chọn cái nào."
category: AI Agent
tags: [ai agent, github, mã nguồn mở, langchain, dify, crewai]
author: Đội sản phẩm KimQ
published: 2026-11-20
updated: 2026-11-20
dataDate: 2026-11-20
status: ready
---

AI Agent là chương trình dùng mô hình ngôn ngữ (LLM) để tự lên kế hoạch, gọi công cụ (tra dữ liệu, gửi email, tạo phiếu…) và hoàn thành một việc nhiều bước. Thay vì tự viết từ đầu, phần lớn đội kỹ thuật bắt đầu từ một framework mã nguồn mở.

Bài này tổng hợp **10 framework AI Agent đáng chú ý nhất trên GitHub**, kèm số liệu thật lấy ngày **20/11/2026**, giấy phép, và gợi ý nên chọn cái nào.

## Tóm tắt nhanh

| # | Repo | Sao GitHub | Ngôn ngữ | Giấy phép | Hợp nhất với |
|---|---|---|---|---|---|
| 1 | [langgenius/dify](https://github.com/langgenius/dify) | ~161,5 nghìn | Python, TypeScript | Apache 2.0 có điều kiện thêm | Làm agent bằng giao diện kéo thả, không cần nhiều code |
| 2 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | ~149,9 nghìn | Python | MIT | Hệ sinh thái lớn nhất, nhiều tích hợp |
| 3 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | ~61,1 nghìn | Python | MIT | Nhiều agent đóng vai, phối hợp theo nhóm |
| 4 | [run-llama/llama_index](https://github.com/run-llama/llama_index) | ~53,0 nghìn | Python | MIT | Agent làm việc với tài liệu, RAG |
| 5 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | ~45,2 nghìn | Python | MIT | Quy trình agent phức tạp, cần kiểm soát từng bước |
| 6 | [agno-agi/agno](https://github.com/agno-agi/agno) | ~43,2 nghìn | Python | Apache 2.0 | Agent gọn, chạy nhanh, có sẵn bộ nhớ |
| 7 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | ~30,8 nghìn | Python | MIT | Bắt đầu nhanh, nhiều agent chuyển việc cho nhau |
| 8 | [huggingface/smolagents](https://github.com/huggingface/smolagents) | ~30,5 nghìn | Python | Apache 2.0 | Agent tối giản, "nghĩ bằng code" |
| 9 | [mastra-ai/mastra](https://github.com/mastra-ai/mastra) | ~29,7 nghìn | TypeScript | Apache 2.0, trừ thư mục `ee/` | Đội dùng TypeScript, Node.js |
| 10 | [google/adk-python](https://github.com/google/adk-python) | ~22,3 nghìn | Python | Apache 2.0 | Hệ sinh thái Google Cloud, Gemini |

*Số sao làm tròn, lấy từ GitHub API ngày 20/11/2026. Số sao cho biết mức độ quan tâm, không phải chất lượng.*

## Chúng tôi chọn thế nào

- **Còn được bảo trì:** có commit trong tháng 11/2026. Repo đã lưu trữ (archived) bị loại.
- **Dùng được cho doanh nghiệp:** giấy phép cho phép dùng nội bộ; điều kiện thương mại được ghi rõ.
- **Cộng đồng đủ lớn:** trên 20 nghìn sao, nhiều người đóng góp, tài liệu đầy đủ.
- **Đa dạng cách tiếp cận:** có công cụ kéo thả, có thư viện code, có lựa chọn cho Python và TypeScript.

## 1. Dify: xây agent bằng giao diện

**Dify** là nền tảng có giao diện web để dựng chatbot, agent và quy trình RAG mà không cần viết nhiều code. Bạn chọn mô hình, nạp tài liệu, kéo các bước vào luồng xử lý rồi xuất ra API hoặc trang chat.

- **Điểm mạnh:** nhanh nhất để có bản chạy thử; hỗ trợ nhiều nhà cung cấp mô hình; có quản lý tài liệu, lịch sử hội thoại, nhật ký.
- **Lưu ý giấy phép:** dựa trên Apache 2.0 nhưng **thêm điều kiện**: không được dùng mã nguồn để vận hành dịch vụ nhiều khách thuê (multi-tenant) và không được gỡ logo, bản quyền trên giao diện nếu chưa mua giấy phép thương mại. Dùng nội bộ một công ty thường không vướng.
- **Hợp với:** doanh nghiệp muốn thử nhanh trợ lý nội bộ trên tài liệu của mình.

## 2. LangChain: hệ sinh thái lớn nhất

**LangChain** là thư viện phổ biến nhất để ghép LLM với dữ liệu và công cụ. Gần như mọi mô hình, cơ sở dữ liệu vector hay API phổ biến đều đã có tích hợp sẵn.

- **Điểm mạnh:** nhiều ví dụ, nhiều tích hợp, dễ tìm người đã dùng.
- **Điểm cần cân nhắc:** nhiều lớp trừu tượng; dự án nhỏ có thể thấy nặng. Với agent nhiều bước cần kiểm soát chặt, đội LangChain có thêm LangGraph (mục 5).
- **Giấy phép:** MIT.

## 3. CrewAI: nhóm agent đóng vai

**CrewAI** cho bạn định nghĩa nhiều agent với vai trò riêng (ví dụ "người nghiên cứu", "người viết", "người kiểm tra") và để chúng phối hợp hoàn thành một nhiệm vụ.

- **Điểm mạnh:** cách mô tả gần với cách giao việc cho một nhóm người; dễ hiểu với người không chuyên.
- **Điểm cần cân nhắc:** nhiều agent đồng nghĩa nhiều lần gọi mô hình, chi phí tăng nhanh. Nên đặt giới hạn số bước.
- **Giấy phép:** MIT.

## 4. LlamaIndex: agent làm việc với tài liệu

**LlamaIndex** mạnh nhất ở phần đọc, chia nhỏ, đánh chỉ mục và truy vấn tài liệu (PDF, Word, bảng tính). Repo tự mô tả là "nền tảng xử lý tài liệu cho AI".

- **Hợp với:** trợ lý trả lời theo quy chế công ty, hợp đồng, hồ sơ sản phẩm; tra cứu văn bản pháp luật nội bộ.
- **Giấy phép:** MIT.

## 5. LangGraph: kiểm soát từng bước của agent

**LangGraph** (cùng đội LangChain) mô tả agent dưới dạng đồ thị: mỗi nút là một bước, mỗi cạnh là điều kiện chuyển bước. Có lưu trạng thái, dừng chờ người duyệt rồi chạy tiếp.

- **Điểm mạnh:** hợp với nghiệp vụ cần **người xác nhận trước khi ghi dữ liệu**, ví dụ duyệt báo giá, duyệt chi.
- **Giấy phép:** MIT.

## 6. Agno: gọn và nhanh

**Agno** tập trung vào agent nhẹ, khởi tạo nhanh, có sẵn bộ nhớ, kiến thức và công cụ. Phù hợp khi cần chạy nhiều agent cùng lúc.

- **Giấy phép:** Apache 2.0.

## 7. OpenAI Agents SDK: bắt đầu nhanh

**openai-agents-python** là bộ công cụ chính thức của OpenAI, ít khái niệm: agent, công cụ, chuyển giao (handoff) giữa các agent, và kiểm tra đầu vào/đầu ra (guardrail).

- **Điểm mạnh:** đơn giản, tài liệu rõ; có hỗ trợ cả mô hình ngoài OpenAI.
- **Giấy phép:** MIT.

## 8. smolagents: tối giản

**smolagents** của Hugging Face để agent viết và chạy đoạn code Python thay vì chỉ gọi công cụ dạng JSON. Mã nguồn lõi nhỏ, dễ đọc hiểu.

- **Lưu ý:** agent chạy code cần môi trường cách ly (sandbox) để an toàn.
- **Giấy phép:** Apache 2.0.

## 9. Mastra: cho đội TypeScript

**Mastra** là framework agent viết bằng TypeScript, hợp với đội đang làm web bằng Node.js, Next.js.

- **Giấy phép:** Apache 2.0, trừ các thư mục `ee/` (tính năng doanh nghiệp) có giấy phép riêng.

## 10. Google ADK: hệ sinh thái Google

**Agent Development Kit** của Google là bộ công cụ viết agent bằng code, có sẵn phần đánh giá (evaluation) và triển khai. Dùng tốt nhất với Gemini và Google Cloud nhưng không bắt buộc.

- **Giấy phép:** Apache 2.0.

## Đáng chú ý khác

- [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (~21,3 nghìn sao, MIT): agent có kiểu dữ liệu chặt chẽ, hợp với đội đã dùng Pydantic.
- [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) (~28,8 nghìn sao, MIT): lựa chọn cho đội dùng C# và .NET.

**Đã ngừng bảo trì, không nên dùng cho dự án mới:**
- **microsoft/autogen**: README ghi repo đã lưu trữ, Microsoft không còn sửa lỗi hay vá bảo mật.
- **FlowiseAI/Flowise**: repo đã ở trạng thái lưu trữ (archived) trên GitHub.

## Nên chọn cái nào?

| Tình huống | Gợi ý |
|---|---|
| Chưa có lập trình viên AI, cần bản chạy thử nhanh | Dify |
| Trợ lý trả lời theo tài liệu nội bộ | LlamaIndex hoặc Dify |
| Nghiệp vụ nhiều bước, cần người duyệt trước khi ghi | LangGraph |
| Nhiều agent phối hợp theo vai trò | CrewAI |
| Đội dùng TypeScript | Mastra |
| Muốn ít khái niệm, bắt đầu nhanh bằng code | OpenAI Agents SDK, Agno, smolagents |

## 5 điều cần làm trước khi đưa agent vào chạy thật

1. **Agent chỉ đề xuất, người duyệt mới ghi.** Không để agent tự sửa sổ sách, tự gửi báo giá.
2. **Chạy đúng quyền người dùng.** Agent không được xem dữ liệu mà người đang hỏi không có quyền xem.
3. **Ghi nhật ký** mọi lần gọi mô hình và mọi thao tác.
4. **Giới hạn chi phí:** số bước tối đa, số lần gọi mô hình, ngân sách theo phòng ban.
5. **Che dữ liệu nhạy cảm** (số CCCD, số tài khoản, lương) trước khi gửi tới nhà cung cấp mô hình.

KimQ Tech áp dụng các nguyên tắc này trong [Trợ lý AI trên Zalo](/san-pham/tro-ly-zalo) và [KimQ AI Gateway](/san-pham/ai-gateway). Nếu doanh nghiệp cần quản lý chi phí và dữ liệu khi nhiều phòng ban cùng dùng AI, xem thêm bài [Top 7 AI Gateway mã nguồn mở](/kien-thuc/top-7-ai-gateway-ma-nguon-mo).

## Câu hỏi thường gặp

**Số sao GitHub có nói lên chất lượng không?**
Không hẳn. Số sao cho biết mức độ quan tâm. Nên xem thêm: lần commit gần nhất, số issue đang mở, tốc độ phản hồi, tài liệu và giấy phép.

**Framework mã nguồn mở có miễn phí hoàn toàn không?**
Mã nguồn thường miễn phí, nhưng bạn vẫn trả tiền gọi mô hình, tiền máy chủ và công vận hành. Một số repo (Dify, phần `ee/` của Mastra) có điều kiện riêng khi dùng thương mại.

**Có cần GPU không?**
Không, nếu gọi mô hình qua API (OpenAI, Gemini, Claude…). Chỉ cần GPU khi tự chạy mô hình tại chỗ; xem bài [Top 7 repo chạy LLM nội bộ](/kien-thuc/top-7-repo-chay-llm-noi-bo).

---

*Số liệu lấy từ GitHub API ngày 20/11/2026 và có thể đã thay đổi. Nội dung giấy phép tóm tắt để tham khảo, không phải tư vấn pháp lý; hãy đọc tệp LICENSE gốc của từng repo trước khi dùng thương mại.*
