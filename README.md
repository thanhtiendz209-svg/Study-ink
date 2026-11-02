# Study Ink — Windows 10 & Android

**Mục tiêu:** ứng dụng ghi chú viết tay chạy độc lập trên Windows 10 (64-bit) và Android. Repository này dành riêng cho Study Ink, không liên quan repository trắc nghiệm tính cách.

## Quy trình GitHub Releases (miễn phí trên repository công khai)

1. Tải mã nguồn ZIP **`Study_Ink_v0.6_Windows10_Android_Source.zip`** từ cuộc trò chuyện ChatGPT đang phát triển Study Ink.
2. Tại repository này, bấm **Add file → Upload files**, chọn **tệp ZIP gốc (không giải nén)**, bấm **Commit changes** lên nhánh `main`.
3. Mở **Actions → Build and publish Study Ink preview → Run workflow**. Giữ `source_zip` mặc định và đặt `release_tag` (chẳng hạn `v0.6.0-beta.1`).
4. Theo dõi cả hai job **Android** và **Windows**. Sau khi **cả hai build thành công**, job `release` sẽ tạo GitHub Release **prerelease** chứa APK và ZIP Windows.
5. Vào mục **Releases** của repository để tải tệp. Giải nén ZIP Windows và chạy `study_ink.exe` trong thư mục giải nén (giữ nguyên các DLL và thư mục `data`). Trên Android, mở tệp APK để cài thử.

**Lưu ý:** Đây là mã nguồn thử nghiệm và chưa được xác nhận build thành công trên GitHub Actions. Nếu job báo lỗi, tải logs để sửa trước khi phát hành. Chưa có chữ ký số Windows và không có bộ cài EXE/MSI chính thức. Bản Android preview có thể dùng chữ ký debug tạm thời của CI; trước khi phân phối rộng rãi cần cấu hình khóa ký phát hành ổn định, nếu không những bản sau có thể không cập nhật đè được. Không dùng như nơi lưu bản duy nhất của ghi chú quan trọng.

### Links

- [Build & publish workflow](.github/workflows/release.yml)
- [GitHub Actions](../../actions)
- [GitHub Releases](../../releases)

## Thiết lập và sửa lỗi

Flutter được cài tự động trên GitHub Actions. Workflow giải nén mã nguồn, tạo cấu trúc project native bằng `flutter create`, chạy `flutter analyze`, `flutter test`, sau đó biên dịch ứng dụng. Workflow chỉ chạy khi bạn nhấn **Run workflow**, không tự phát hành mã chưa được kiểm tra.

**Cập nhật:** Khi có phiên bản ZIP mới, tải lên repository, đổi giá trị `source_zip` trong màn hình chạy Actions và dùng một `release_tag` mới. Không đưa mật khẩu hoặc khóa API vào repository công khai.