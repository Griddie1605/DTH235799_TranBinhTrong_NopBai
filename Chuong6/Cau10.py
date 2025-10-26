import random

def tao_matrix_ngau_nhien(m, n):
    """Tạo ra một ma trận m x n với các số ngẫu nhiên 0-99."""
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(0, 99))
        matrix.append(row)
    return matrix

def xuat_matrix(M):
    """In ma trận ra màn hình cho đẹp."""
    if not M:
        print("[]")
        return
        
    # Tìm độ rộng cột lớn nhất để căn lề
    max_len = max(len(str(item)) for row in M for item in row)
    
    for row in M:
        for element in row:
            # {element:<{max_len}} căn lề trái
            print(f"{element:<{max_len}}", end="  ")
        print() # Xuống dòng

def cong_matrix(A, B):
    """Cộng hai ma trận A và B."""
    # Kiểm tra kích thước ma trận
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Lỗi: Không thể cộng 2 ma trận khác kích thước.")
        return None
        
    # Lấy kích thước
    m = len(A)
    n = len(A[0])
    
    # Tạo ma trận kết quả (C)
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            tong = A[i][j] + B[i][j]
            row.append(tong)
        C.append(row)
    return C

def chuyen_vi_matrix(A):
    """
    Tìm ma trận chuyển vị (hoán vị) của A.
    Hàng của A -> Cột của T
    """
    m_A = len(A)      # Số hàng của A
    n_A = len(A[0])   # Số cột của A
    
    # Ma trận chuyển vị T sẽ có kích thước n x m
    T = []
    for j in range(n_A): # Lặp qua các cột của A (sẽ là hàng của T)
        row = []
        for i in range(m_A): # Lặp qua các hàng của A (sẽ là cột của T)
            row.append(A[i][j])
        T.append(row)
    return T

# --- Chương trình chính ---
try:
    m = int(input("Nhập số dòng m: "))
    n = int(input("Nhập số cột n: "))

    if m <= 0 or n <= 0:
        print("Số dòng và cột phải là số dương.")
    else:
        # 1. Tạo 2 ma trận A và B
        print("\n--- Ma trận A ---")
        A = tao_matrix_ngau_nhien(m, n)
        xuat_matrix(A)
        
        print("\n--- Ma trận B ---")
        B = tao_matrix_ngau_nhien(m, n)
        xuat_matrix(B)
        
        # 2. Cộng ma trận
        print("\n--- Tổng A + B ---")
        C = cong_matrix(A, B)
        if C: # Chỉ in nếu phép cộng thành công
            xuat_matrix(C)
            
        # 3. Chuyển vị (Hoán vị)
        print("\n--- Ma trận chuyển vị của A ---")
        T_A = chuyen_vi_matrix(A)
        xuat_matrix(T_A)
        
        print("\n--- Ma trận chuyển vị của B ---")
        T_B = chuyen_vi_matrix(B)
        xuat_matrix(T_B)

except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")