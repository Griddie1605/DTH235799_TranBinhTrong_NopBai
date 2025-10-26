def toi_uu_chuoi(s):
    """
    Hàm chuẩn hóa chuỗi danh từ:
    1. Xóa khoảng trắng thừa ở đầu/cuối.
    2. Tách các từ.
    3. Viết hoa chữ cái đầu mỗi từ, viết thường các chữ còn lại.
    4. Nối các từ lại bằng một dấu cách.
    """
    
    tu_list = s.strip().split()
    
    tu_list_da_xu_ly = [word.capitalize() for word in tu_list]
    
    ket_qua = " ".join(tu_list_da_xu_ly)
    
    return ket_qua

input_s = "   TrẦn     duY    thAnH   "
output_s = toi_uu_chuoi(input_s)

print(f"Input:  '{input_s}'")
print(f"Output: '{output_s}'")