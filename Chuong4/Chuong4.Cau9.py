import math # Dùng thư viện math để lấy hàm căn bậc 2

def tinh_S(n):
    if n <= 0:
        return 0.0
        
    S = 0.0 # Khởi tạo S ban đầu
    
    # Lặp lại n lần
    for i in range(n):
        S = math.sqrt(2 + S)
        
    return S

# --- Chạy chương trình Câu 9 ---
try:
    n_input_9 = int(input("Câu 9: Nhập số n (số dấu căn lồng nhau): "))
    if n_input_9 < 0:
        print("Lỗi: n phải là số nguyên không âm.")
    else:
        ket_qua_9 = tinh_S(n_input_9)
        print(f"Giá trị của S({n_input_9}) là: {ket_qua_9}")

except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")