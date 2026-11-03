# Study Ink — bản chạy thử Windows 10 và Android

Kho này dùng để thử bản Study Ink v0.7.5. Đây là **ứng dụng cài đặt**, không phải website.

## Build không cần cài Flutter

1. Tải ZIP mã nguồn `Study_Ink_v0.7.5_Windows10_Android_TwoPages_Pinch_Shapes_Source.zip` từ ChatGPT.
2. Tại trang repo, chọn **Add file → Upload files**, tải **ZIP gốc** lên thư mục gốc nhánh `main` và nhấn **Commit changes**.
3. GitHub Actions tự khởi chạy quy trình `Build Study Ink v0.7.5 preview`.
4. Khi cả Android và Windows thành công, vào tab **Releases** tải Android APK và Windows ZIP. Nếu lỗi, mở **Actions** để xem thông báo.
5. Android: bản `arm64-v8a` cho đa số điện thoại hiện đại; bản khác tùy máy. Windows 10 x64: giải nén toàn bộ ZIP rồi chạy `study_ink.exe` trong thư mục (không xóa DLL/thư mục data).

**Chú ý:** Bản thử nghiệm không được kiểm chứng trên thiết bị thật. Hãy sao lưu ghi chú; không lưu dữ liệu quan trọng duy nhất tại đây. Tệp Windows chưa ký số có thể bị SmartScreen cảnh báo. APK cài ngoài Google Play có thể bị Android yêu cầu cấp quyền. Chỉ cài từ repository của mình.
