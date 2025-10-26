import random

def tao_list_khong_trung(n, gioi_han_tren):
    """
    Tạo một list gồm n số ngẫu nhiên không trùng nhau.
    Các số được lấy từ 0 đến gioi_han_tren - 1.
    """
    
    if n > gioi_han_tren:
        print(f"Lỗi: Không thể lấy {n} số không trùng nhau")
        print(f"từ khoảng 0 đến {gioi_han_tren - 1}.")
        return None
    
    population = range(gioi_han_tren)
    
    lst = random.sample(population, n)
    
    return lst

# --- Chương trình chính ---
try:
    n = int(input("Nhập số N (số lượng phần tử): "))
    
    gioi_han = int(input("Nhập giới hạn trên (ví dụ 100, số ngẫu nhiên sẽ từ 0-99): "))
    
    if n < 0 or gioi_han <= 0:
        print("Lỗi: N và giới hạn trên phải là số dương.")
    else:
        ket_qua = tao_list_khong_trung(n, gioi_han)
        if ket_qua is not None:
            print(f"List {n} số ngẫu nhiên không trùng nhau là:")
            print(ket_qua)

except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")