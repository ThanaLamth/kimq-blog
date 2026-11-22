---
title: "Top 8 phần mềm ERP, kế toán mã nguồn mở trên GitHub cho doanh nghiệp Việt (cập nhật 11/2026)"
slug: top-8-phan-mem-erp-ke-toan-ma-nguon-mo
path: /kien-thuc/top-8-phan-mem-erp-ke-toan-ma-nguon-mo
description: "8 phần mềm ERP, kế toán, hoá đơn mã nguồn mở: Odoo, ERPNext, Dolibarr, Akaunting, Invoice Ninja, metasfresh, iDempiere, Tryton. So sánh giấy phép, mức hỗ trợ Việt Nam và cách chọn."
category: Quản trị doanh nghiệp
tags: [erp, phần mềm kế toán, mã nguồn mở, github, odoo, erpnext]
author: Đội sản phẩm KimQ
published: 2026-11-20
updated: 2026-11-20
dataDate: 2026-11-20
status: ready
---

> Thuộc chuyên đề: [Hướng dẫn chọn phần mềm mã nguồn mở cho doanh nghiệp](huong-dan-chon-phan-mem-ma-nguon-mo-cho-doanh-nghiep.md) · Bài viết của [KimQ Tech](https://kimq.tech)

Phần mềm ERP (quản trị nguồn lực doanh nghiệp) gom bán hàng, mua hàng, kho, kế toán, nhân sự vào một hệ thống. Bản thương mại thường đắt và khó tuỳ biến, nên nhiều doanh nghiệp vừa và nhỏ tìm tới **ERP mã nguồn mở**.

Bài này tổng hợp **8 phần mềm ERP, kế toán và hoá đơn mã nguồn mở trên GitHub**, kèm số liệu ngày **20/11/2026**, và đặc biệt chú ý một câu hỏi người Việt hay hỏi: **dùng ở Việt Nam có hợp chuẩn kế toán, thuế không?**

## Tóm tắt nhanh

| # | Repo | Sao GitHub | Ngôn ngữ | Giấy phép | Hợp nhất với |
|---|---|---|---|---|---|
| 1 | [odoo/odoo](https://github.com/odoo/odoo) | ~56,0 nghìn | Python | LGPL v3 (bản Community) | ERP đầy đủ, có sẵn module kế toán Việt Nam |
| 2 | [frappe/erpnext](https://github.com/frappe/erpnext) | ~41,5 nghìn | Python | GPL v3 | ERP mã nguồn mở hoàn toàn, sản xuất, phân phối |
| 3 | [invoiceninja/invoiceninja](https://github.com/invoiceninja/invoiceninja) | ~10,6 nghìn | PHP | Elastic License 2.0 | Báo giá, hoá đơn, chấm công dự án |
| 4 | [akaunting/akaunting](https://github.com/akaunting/akaunting) | ~10,3 nghìn | PHP | Business Source License 1.1 | Kế toán đơn giản cho hộ, công ty rất nhỏ |
| 5 | [Dolibarr/dolibarr](https://github.com/Dolibarr/dolibarr) | ~7,9 nghìn | PHP | GPL v3 | ERP + CRM nhẹ, dễ cài |
| 6 | [metasfresh/metasfresh](https://github.com/metasfresh/metasfresh) | ~2,5 nghìn | Java | GPL | Phân phối, thực phẩm, chuỗi cung ứng |
| 7 | [idempiere/idempiere](https://github.com/idempiere/idempiere) | ~0,7 nghìn | Java | GPL v2 | Doanh nghiệp cần hệ thống nhiều chi nhánh, tuỳ biến sâu |
| 8 | [tryton/tryton](https://github.com/tryton/tryton) | ~0,2 nghìn | Python | GPL v3 (theo dự án gốc) | Nền tảng ERP dạng module cho đội có lập trình viên |

*Số sao làm tròn, lấy từ GitHub API ngày 20/11/2026. iDempiere và Tryton phát triển chủ yếu ngoài GitHub (repo Tryton là bản sao), nên số sao thấp không phản ánh quy mô cộng đồng.*

## Chúng tôi chọn thế nào

- **Có phân hệ kế toán hoặc hoá đơn** dùng được thật, không chỉ quản lý dự án.
- **Còn được bảo trì:** có commit trong tháng 11/2026.
- **Tự cài được** trên máy chủ của doanh nghiệp.
- **Giấy phép rõ ràng;** các giấy phép "mở có điều kiện" (source-available) được ghi chú riêng.

## 1. Odoo: phổ biến nhất, có module Việt Nam

**Odoo** gồm hàng chục ứng dụng: bán hàng, mua hàng, kho, kế toán, sản xuất, nhân sự, website. Bản **Community** là mã nguồn mở; bản **Enterprise** trả phí có thêm nhiều tính năng (một phần kế toán nâng cao, ứng dụng di động…).

- **Hỗ trợ Việt Nam:** có module `l10n_vn` (Vietnam - Accounting) gồm hệ thống tài khoản theo **chuẩn mực kế toán Việt Nam (VAS), Thông tư 200/2014/TT-BTC**, danh sách ngân hàng Việt Nam và **mã VietQR trên hoá đơn**.
- **Lưu ý:** từ năm tài chính 2026, chế độ kế toán doanh nghiệp theo **Thông tư 99/2025/TT-BTC** thay thế Thông tư 200; cần kiểm tra module đã cập nhật hệ thống tài khoản mới chưa.
- **Giấy phép:** LGPL v3 cho bản Community.

## 2. ERPNext: mở hoàn toàn

**ERPNext** (trên nền Frappe Framework) có kế toán, kho, mua bán, sản xuất, dự án, nhân sự. Khác Odoo, **toàn bộ tính năng đều mã nguồn mở**, không chia bản trả phí.

- **Điểm mạnh:** tuỳ biến bằng giao diện (thêm trường, biểu mẫu) không cần sửa code nhiều.
- **Hỗ trợ Việt Nam:** chúng tôi chưa thấy module bản địa hoá Việt Nam chính thức trong repo; hệ thống tài khoản và mẫu báo cáo cần tự thiết lập.
- **Giấy phép:** GPL v3.

## 3. Invoice Ninja: báo giá và hoá đơn

**Invoice Ninja** tập trung vào báo giá, hoá đơn, thu tiền, chấm công theo dự án, cổng cho khách hàng xem và thanh toán.

- **Hợp với:** công ty dịch vụ, agency, freelancer cần lập hoá đơn gửi khách nhanh.
- **Lưu ý giấy phép:** **Elastic License 2.0** (mã nguồn công khai, không phải mã nguồn mở theo định nghĩa OSI). Được dùng nội bộ, nhưng **không được cung cấp phần mềm cho bên thứ ba dưới dạng dịch vụ lưu trữ hoặc quản lý**.

## 4. Akaunting: kế toán đơn giản

**Akaunting** là phần mềm kế toán trực tuyến gọn gàng: thu chi, hoá đơn, khách hàng, nhà cung cấp, báo cáo.

- **Lưu ý giấy phép quan trọng:** dùng **Business Source License 1.1**. Chỉ được dùng thật (production) miễn phí nếu **không quá 2 người dùng, 1 công ty, 1.000 hoá đơn**; không được gỡ thương hiệu để bán lại; không được dùng để cung cấp dịch vụ kế toán cho bên thứ ba. Vượt mức phải mua giấy phép.
- **Hợp với:** hộ kinh doanh, công ty rất nhỏ thử nghiệm.

## 5. Dolibarr: ERP + CRM nhẹ

**Dolibarr** gồm CRM, báo giá, đơn hàng, hoá đơn, kho, kế toán, nhân sự, dưới dạng module bật tắt tuỳ nhu cầu. Cài đặt đơn giản trên máy chủ PHP thông thường.

- **Hợp với:** doanh nghiệp nhỏ muốn ERP nhẹ, dễ triển khai.
- **Giấy phép:** GPL v3.

## 6. metasfresh: phân phối và chuỗi cung ứng

**metasfresh** là ERP viết bằng Java, mạnh ở mua bán, kho, phân phối, truy xuất lô hàng, thường dùng trong ngành thực phẩm và thương mại.

- **Giấy phép:** GPL (theo README; GitHub API không tự nhận diện được tệp giấy phép).

## 7. iDempiere: tuỳ biến sâu, nhiều chi nhánh

**iDempiere** (phát triển từ Compiere, ADempiere) là ERP Java với kiến trúc plugin, hỗ trợ nhiều công ty, nhiều chi nhánh trên một hệ thống.

- **Hợp với:** doanh nghiệp có đội kỹ thuật Java, cần tuỳ biến sâu.
- **Giấy phép:** GPL v2.

## 8. Tryton: nền tảng ERP dạng module

**Tryton** là nền tảng ERP viết bằng Python, chia module rõ ràng (kế toán, bán hàng, kho, sản xuất). Mã nguồn chính đặt tại `code.tryton.org`; repo GitHub là bản sao.

- **Hợp với:** đội có lập trình viên Python muốn xây ERP riêng trên nền vững.
- **Giấy phép:** GPL v3 theo dự án gốc; GitHub API không nhận diện được, hãy kiểm tra trên trang dự án.

## Nên chọn cái nào?

| Tình huống | Gợi ý |
|---|---|
| Cần ERP đầy đủ, muốn có sẵn hệ thống tài khoản Việt Nam | Odoo Community |
| Muốn mở hoàn toàn, không lo bản trả phí | ERPNext |
| Công ty dịch vụ, chủ yếu cần báo giá, hoá đơn | Invoice Ninja |
| Doanh nghiệp nhỏ, muốn ERP + CRM nhẹ | Dolibarr |
| Phân phối, thực phẩm, cần truy xuất lô | metasfresh |
| Có đội lập trình, cần tuỳ biến sâu | iDempiere, Tryton |

## Dùng ERP mã nguồn mở ở Việt Nam: cần lưu ý gì?

1. **Hệ thống tài khoản và báo cáo tài chính** phải theo chế độ kế toán Việt Nam. Từ năm 2026 là Thông tư 99/2025/TT-BTC (thay Thông tư 200). Hầu hết phần mềm nước ngoài cần cấu hình lại.
2. **Hoá đơn điện tử:** doanh nghiệp phải xuất hoá đơn qua nhà cung cấp hoá đơn điện tử được cơ quan thuế chấp nhận. ERP mã nguồn mở **không tự làm việc này**; cần tích hợp API của nhà cung cấp hoá đơn.
3. **Tờ khai thuế, báo cáo thuế:** thường vẫn lập trên phần mềm hỗ trợ kê khai của cơ quan thuế; ERP chỉ xuất số liệu.
4. **Giấy phép:** phân biệt mã nguồn mở thật (GPL, LGPL) với mã nguồn công khai có điều kiện (Elastic, BSL). Điều này quan trọng nếu bạn định cung cấp phần mềm cho khách hàng.
5. **Chi phí thật** gồm máy chủ, triển khai, đào tạo, bảo trì và nhân sự kỹ thuật, thường lớn hơn nhiều so với "phần mềm miễn phí".

## Không cần cả bộ ERP?

Nhiều doanh nghiệp chỉ đau một vài khâu: **theo dõi công nợ**, **kho và mua hàng**, hoặc **nhập hoá đơn đầu vào**. Khi đó, giải pháp chuyên biệt kết nối với phần mềm kế toán đang dùng thường nhanh hơn triển khai cả ERP. Xem các giải pháp của KimQ Tech: [Quản lý công nợ](https://kimq.tech/san-pham/cong-no), [Kho và mua hàng](https://kimq.tech/san-pham/kho-mua-hang), [Hoá đơn đầu vào](https://kimq.tech/san-pham/hoa-don-dau-vao).

Đọc thêm: [Top 8 công cụ tự động hoá quy trình mã nguồn mở](top-8-cong-cu-tu-dong-hoa-quy-trinh-ma-nguon-mo.md) để nối ERP với email, Zalo, bảng tính.

## Câu hỏi thường gặp

**Odoo Community có miễn phí không?**
Mã nguồn miễn phí theo LGPL v3. Bạn vẫn trả chi phí máy chủ, triển khai, tuỳ biến. Một số tính năng chỉ có ở bản Enterprise trả phí.

**ERP mã nguồn mở có xuất hoá đơn điện tử được không?**
Không trực tiếp. Cần tích hợp với nhà cung cấp hoá đơn điện tử tại Việt Nam qua API, hoặc dùng module do đối tác trong nước phát triển.

**Doanh nghiệp nhỏ nên chọn gì?**
Nếu chỉ cần hoá đơn và thu chi, chọn phần mềm gọn (Dolibarr, Invoice Ninja) hoặc giải pháp chuyên biệt. Nếu cần kho, mua bán, kế toán liên thông, Odoo hoặc ERPNext phù hợp hơn nhưng cần người triển khai.

**Có thể chuyển từ phần mềm kế toán đang dùng sang ERP không?**
Có, nhưng cần chuyển danh mục, số dư đầu kỳ, công nợ và đối chiếu kỹ. Nên chạy song song ít nhất một kỳ kế toán.


## Về KimQ Tech

[KimQ Tech](https://kimq.tech) xây giải pháp AI và tự động hoá vận hành cho doanh nghiệp Việt: [AI Gateway](https://kimq.tech/san-pham/ai-gateway), [Trợ lý AI trên Zalo](https://kimq.tech/san-pham/tro-ly-zalo), [Tự động hoá](https://kimq.tech/san-pham/tu-dong-hoa), [Công nợ](https://kimq.tech/san-pham/cong-no), [Kho và mua hàng](https://kimq.tech/san-pham/kho-mua-hang), [Hoá đơn đầu vào](https://kimq.tech/san-pham/hoa-don-dau-vao). Cần tư vấn chọn và triển khai? [Liên hệ KimQ Tech](https://kimq.tech/lien-he) hoặc email contact@kimq.tech.

---

*Số liệu lấy từ GitHub API ngày 20/11/2026 và có thể đã thay đổi. Nội dung giấy phép và quy định tóm tắt để tham khảo, không phải tư vấn pháp lý, thuế hay kế toán; hãy đọc tệp LICENSE gốc của từng repo và hỏi kế toán, luật sư trước khi áp dụng.*
