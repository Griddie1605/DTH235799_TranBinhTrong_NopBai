import os

def lay_ten_file_day_du(path):
    # os.path.basename() trích xuất tên file từ đường dẫn
    return os.path.basename(path)

def lay_ten_file_khong_mo_rong(path):
    """
    Hàm 2: Lấy ra tên file (không bao gồm phần mở rộng).
    Ví dụ: muabuoi
    """
    # 1. Lấy tên file đầy đủ
    basename = os.path.basename(path)
    
    # 2. Tách tên file và phần mở rộng
    # os.path.splitext("muabuoi.mp3") -> trả về ("muabuoi", ".mp3")
    ten_file, _ = os.path.splitext(basename)
    
    return ten_file

path_vi_du = "d:/music/muabuoi.mp3"

# Thử với đường dẫn kiểu Windows
path_windows = "C:\\Users\\Admin\\Documents\\baitap.docx"
print(f"--- Ví dụ 1: {path_vi_du} ---")
print(f"Hàm 1 (Tên đầy đủ): {lay_ten_file_day_du(path_vi_du)}")
print(f"Hàm 2 (Tên file):    {lay_ten_file_khong_mo_rong(path_vi_du)}")

print(f"\n--- Ví dụ 2 (Windows): {path_windows} ---")
print(f"Hàm 1 (Tên đầy đủ): {lay_ten_file_day_du(path_windows)}")
print(f"Hàm 2 (Tên file):    {lay_ten_file_khong_mo_rong(path_windows)}")

