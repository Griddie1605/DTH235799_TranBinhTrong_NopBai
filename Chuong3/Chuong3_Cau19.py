import math

def tinh_S(x, n):
    
    S = 0.0
    
    for k in range(n + 1):
        
        
        so_mu = 2 * k + 1
        
        tu_so = math.pow(x, so_mu)
        
        mau_so = math.factorial(so_mu)
        
        so_hang = tu_so / mau_so
        S = S + so_hang
        
    return S

try:
    x_input = float(input("Nhập giá trị x: "))
    n_input = int(input("Nhập giá trị n (nguyên, >= 0): "))

    if n_input < 0:
        print("Lỗi: n phải là số nguyên không âm (>= 0).")
    else:
        ket_qua = tinh_S(x_input, n_input)
        print(f"Giá trị của S({x_input}, {n_input}) là: {ket_qua}")

except ValueError:
    print("Lỗi: Vui lòng nhập đúng định dạng (x là số thực, n là số nguyên).")