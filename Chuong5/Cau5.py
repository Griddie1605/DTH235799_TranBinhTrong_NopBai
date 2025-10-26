# 1. Khởi tạo các biến đếm
hoa = 0
thuong = 0
so = 0
dac_biet = 0
khoang_trang = 0
nguyen_am = 0
phu_am = 0

# Định nghĩa một tập hợp các nguyên âm (cả hoa và thường)
# Chúng ta dùng tập hợp (set) để kiểm tra nhanh hơn
NGUYEN_AM_SET = "aeiouAEIOU"

# 2. Nhập chuỗi từ người dùng
try:
    chuoi = input("Nhập vào một chuỗi bất kỳ: ")
    
    # 3. Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi:
        
        # 3a. Phân loại chính (Chữ, Số, Khoảng trắng, Đặc biệt)
        if ky_tu.isalpha():
            # Nếu là chữ cái, kiểm tra hoa/thường
            if ky_tu.isupper():
                hoa += 1
            else:
                thuong += 1
                
            # Cũng kiểm tra xem nó là nguyên âm hay phụ âm
            if ky_tu in NGUYEN_AM_SET:
                nguyen_am += 1
            else:
                phu_am += 1
                
        elif ky_tu.isdigit():
            # Nếu là chữ số
            so += 1
            
        elif ky_tu.isspace():
            # Nếu là khoảng trắng (space, tab, newline)
            khoang_trang += 1
            
        else:
            # Nếu không phải các trường hợp trên
            dac_biet += 1
            
    # 4. In kết quả
    print("\n--- Kết quả phân tích chuỗi ---")
    print(f"Số lượng chữ IN HOA: {hoa}")
    print(f"Số lượng chữ in thường: {thuong}")
    print(f"Số lượng chữ số: {so}")
    print(f"Số lượng ký tự đặc biệt: {dac_biet}")
    print(f"Số lượng khoảng trắng: {khoang_trang}")
    print(f"Số lượng Nguyên Âm: {nguyen_am}")
    print(f"Số lượng Phụ âm: {phu_am}")

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")