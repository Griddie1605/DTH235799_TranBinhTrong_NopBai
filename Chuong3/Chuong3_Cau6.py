def doc_so_hai_chu_so(n):
    """
    Hàm đọc số nguyên từ 0-99 sang dạng chữ Tiếng Việt.
    """
    
  
    doc_don_vi_std = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
    # Kiểm tra n có nằm trong khoảng 0-99 không
    if not (0 <= n <= 99):
        return "Số không hợp lệ (chỉ chấp nhận 0-99)."
        
    # Tách số
    chuc = n // 10
    don_vi = n % 10
    
    ket_qua = ""
    
    if chuc == 0:
        # Trường hợp số 0-9
        ket_qua = doc_don_vi_std[don_vi]
    
    elif chuc == 1:
        # Trường hợp 10-19
        ket_qua = "Mười"
        if don_vi == 0:
            pass  
        elif don_vi == 5:
            ket_qua += " lăm" # 15 = Mười lăm
        else:
            ket_qua += " " + doc_don_vi_std[don_vi] # 11, 12, 13, 14...
            
    else:
        # Trường hợp 20-99
        ket_qua = doc_don_vi_std[chuc] + " mươi" # Hai mươi, Ba mươi...
        
        # Xử lý các trường hợp đặc biệt của hàng đơn vị
        if don_vi == 1:
            ket_qua += " mốt" # 21 = Hai mươi mốt
        elif don_vi == 4:
            ket_qua += " tư"  # 24 = Hai mươi tư
        elif don_vi == 5:
            ket_qua += " lăm" # 35 = Ba mươi lăm
        elif don_vi != 0:
            ket_qua += " " + doc_don_vi_std[don_vi] # 22, 33, 46...

# --- Chạy chương trình ---
try:
    n_input = int(input("Nhập một số n (0-99): "))
    
    # Gọi hàm và in kết quả
    cach_doc = doc_so_hai_chu_so(n_input)
    print(f"n = {n_input} => {cach_doc}")
    
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")