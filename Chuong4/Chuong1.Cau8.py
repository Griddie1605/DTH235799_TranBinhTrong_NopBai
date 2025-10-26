import math # Thêm thư viện math để dùng hàm log

# --- Chương trình chính ---
try:
    # 1. Nhập x và a
    x = float(input("Nhập giá trị x (x > 0): "))
    a = float(input("Nhập cơ số a (a > 0 và a != 1): "))

    # 2. Kiểm tra các điều kiện
    if x <= 0:
        print(f"Lỗi: x = {x} không hợp lệ. x phải lớn hơn 0.")
    elif a <= 0:
        print(f"Lỗi: a = {a} không hợp lệ. a phải lớn hơn 0.")
    elif a == 1:
        print(f"Lỗi: a = {a} không hợp lệ. Cơ số a phải khác 1.")
    else:
        # 3. Tính toán theo công thức loga(x) = lnx / lna
        # math.log(num) sẽ tính ln(num)
        ln_x = math.log(x)
        ln_a = math.log(a)
        
        ket_qua = ln_x / ln_a
        
        # 4. In kết quả
        print(f"Giá trị của log cơ số {a} của {x} là: {ket_qua}")

except ValueError:
    print("Lỗi: Vui lòng chỉ nhập các con số.")