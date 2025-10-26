import math

def kiem_tra_nguyen_to(n):
    """
    Hàm kiểm tra số n có phải là số nguyên tố hay không.
    """
    if n < 2:
        return False
    # Chỉ cần kiểm tra ước từ 2 đến căn bậc hai của n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# --- Chương trình chính ---

# 1. Nhập mảng (List)
# Dùng mảng ví dụ trong đề bài
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 8]

print(f"Mảng đã nhập: {M}\n")

# 2. Khởi tạo các list con
so_le = []
so_chan = []
so_nguyen_to = []
khong_nguyen_to = []

# 3. Phân loại
for num in M:
    # 3a. Chẵn / Lẻ
    if num % 2 == 0:
        so_chan.append(num)
    else:
        so_le.append(num)
        
    # 3b. Nguyên tố / Không nguyên tố
    if kiem_tra_nguyen_to(num):
        so_nguyen_to.append(num)
    else:
        khong_nguyen_to.append(num)

# 4. In kết quả 4 dòng
print(f"Dòng 1: {so_le} -> Tổng cộng {len(so_le)} số lẻ")
print(f"Dòng 2: {so_chan} -> Tổng cộng {len(so_chan)} số chẵn")
print(f"Dòng 3: {so_nguyen_to} -> Tổng cộng {len(so_nguyen_to)} số nguyên tố")
print(f"Dòng 4: {khong_nguyen_to} -> Tổng cộng {len(khong_nguyen_to)} số không phải nguyên tố")