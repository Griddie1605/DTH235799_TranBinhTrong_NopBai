def kiem_tra_nam_nhuan(nam):
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        return True
    return False

def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if kiem_tra_nam_nhuan(nam):
            return 29
        else:
            return 28
    else:
        # Trả về 0 nếu tháng không hợp lệ
        return 0

# --- Chương trình chính ---
try:
    # 1. Nhập dữ liệu
    ngay = int(input("Nhập ngày: "))
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))

    # 2. Kiểm tra ngày có hợp lệ không
    ngay_toi_da = so_ngay_trong_thang(thang, nam)
    
    if not (1 <= thang <= 12 and 1 <= ngay <= ngay_toi_da and nam > 0):
        print(f"Ngày {ngay}/{thang}/{nam} không hợp lệ!")
    else:
        # 3. Tìm ngày kế tiếp
        ngay_ke_tiep = ngay
        thang_ke_tiep = thang
        nam_ke_tiep = nam

        if ngay < ngay_toi_da:
            # TH1: Ngày bình thường (không phải cuối tháng)
            ngay_ke_tiep = ngay + 1
        else:
            # TH2: Ngày cuối tháng
            ngay_ke_tiep = 1
            if thang < 12:
                # TH2a: Cuối tháng (không phải tháng 12)
                thang_ke_tiep = thang + 1
            else:
                # TH2b: Cuối năm (ngày 31/12)
                thang_ke_tiep = 1
                nam_ke_tiep = nam + 1
        
        # 4. In kết quả
        print(f"Ngày vừa nhập: {ngay}/{thang}/{nam}")
        print(f"Ngày kế sau là: {ngay_ke_tiep}/{thang_ke_tiep}/{nam_ke_tiep}")

except ValueError:
    print("Lỗi: Vui lòng chỉ nhập số nguyên.")