def nhap_day_so_tang_dan():
    """
    Hàm yêu cầu người dùng nhập dãy số tăng dần.
    """
    lst = []
    
    try:
        n = int(input("Bạn muốn nhập bao nhiêu số? "))
        if n <= 0:
            print("Số lượng phải là số dương.")
            return []

        # 1. Nhập số đầu tiên để làm mốc
        # Dùng float() để chấp nhận cả số nguyên và số thực
        so_dau_tien = float(input("Nhập số thứ 1: "))
        lst.append(so_dau_tien)
        
        # Mốc so sánh là số cuối cùng vừa nhập
        so_cuoi_cung = so_dau_tien

        # 2. Lặp n-1 lần để nhập các số còn lại
        for i in range(1, n):
            # Dùng vòng lặp while True để bắt nhập lại nếu sai
            while True:
                prompt = f"Nhập số thứ {i + 1} (phải > {so_cuoi_cung}): "
                so_moi = float(input(prompt))
                
                # 3. Kiểm tra điều kiện
                if so_moi > so_cuoi_cung:
                    lst.append(so_moi)
                    so_cuoi_cung = so_moi # Cập nhật mốc so sánh
                    break # Thoát vòng lặp while True, đi tiếp vòng for
                else:
                    print(f"Nhập sai! {so_moi} không lớn hơn {so_cuoi_cung}. Vui lòng nhập lại.")
        
        return lst

    except ValueError:
        print("Lỗi: Vui lòng nhập một con số hợp lệ.")
        return lst

# --- Chương trình chính ---
print("--- Bắt đầu nhập dãy số tăng dần ---")
day_so_da_nhap = nhap_day_so_tang_dan()

if day_so_da_nhap: # Chỉ in nếu list không rỗng
    print("\n--- Dãy số bạn đã nhập là ---")
    print(day_so_da_nhap)