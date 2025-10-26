def nhap_va_sap_xep_giam_dan():
    """
    Hàm nhập n số thực và trả về list đã sắp xếp giảm dần.
    """
    M = []
    try:
        n = int(input("Nhập số lượng phần tử N: "))
        if n <= 0:
            print("N phải là số dương.")
            return None

        # 1. Vòng lặp để nhập N số thực
        print(f"Vui lòng nhập {n} số thực:")
        for i in range(n):
            so = float(input(f"Nhập số M[{i}]: "))
            M.append(so)
            
        print(f"\nDãy số đã nhập: {M}")
        
        # 2. Sắp xếp list giảm dần
        # .sort(reverse=True) sẽ sắp xếp list gốc (in-place)
        M.sort(reverse=True)
        
        return M

    except ValueError:
        print("Lỗi: Vui lòng nhập một con số hợp lệ.")
        return None

# --- Chương trình chính ---
print("--- Chương trình sắp xếp giảm dần ---")
day_so_sap_xep = nhap_va_sap_xep_giam_dan()

if day_so_sap_xep is not None:
    print(f"Dãy số sau khi sắp xếp giảm dần:")
    print(day_so_sap_xep)