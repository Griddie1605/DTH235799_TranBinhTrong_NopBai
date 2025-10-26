def tinh_tong_uoc_so(n):
    """
    Hàm này tính tổng các ước số của n, KHÔNG bao gồm chính n.
    """
    # Xử lý trường hợp n nhỏ hơn hoặc bằng 1
    if n <= 1:
        return 0
        
    tong_uoc = 0
    # Vòng lặp chỉ cần chạy từ 1 đến n-1
    # range(1, n) sẽ tạo ra dãy: 1, 2, ..., (n-1)
    for i in range(1, n):
        if n % i == 0:
            # i là một ước số của n
            tong_uoc += i
            
    return tong_uoc

# --- Yêu cầu (a) ---
def kiem_tra_so_hoan_thien(n):
    """
    Kiểm tra n có phải là số hoàn thiện (Perfect number) không.
    Tổng ước số (không kể n) == n
    """
    tong = tinh_tong_uoc_so(n)
    if n > 0 and tong == n:
        return True
    else:
        return False

# --- Yêu cầu (b) ---
def kiem_tra_so_thinh_vuong(n):
    """
    Kiểm tra n có phải là số thịnh vượng (Abundant number) không.
    Tổng ước số (không kể n) > n
    """
    tong = tinh_tong_uoc_so(n)
    if n > 0 and tong > n:
        return True
    else:
        return False

# --- Chương trình chính để kiểm tra ---
try:
    n_input = int(input("Nhập một số nguyên dương n: "))

    if n_input <= 0:
        print("Lỗi: Vui lòng nhập số nguyên dương.")
    else:
        # Kiểm tra (a)
        if kiem_tra_so_hoan_thien(n_input):
            print(f"(a) {n_input} LÀ số hoàn thiện.")
        else:
            print(f"(a) {n_input} KHÔNG phải là số hoàn thiện.")
            
        # Kiểm tra (b)
        if kiem_tra_so_thinh_vuong(n_input):
            print(f"(b) {n_input} LÀ số thịnh vượng.")
        else:
            print(f"(b) {n_input} KHÔNG phải là số thịnh vượng.")

except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")