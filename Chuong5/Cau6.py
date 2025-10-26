import re

def NegativeNumberInStrings(s):
    """
    Hàm tìm và in ra tất cả các số nguyên âm trong chuỗi.
    """
    print(f"--- Phân tích chuỗi: '{s}' ---")
    
    pattern = r"-\d+"
    
    so_am = re.findall(pattern, s)
    
    if not so_am:
        print("Không tìm thấy số nguyên âm nào.")
    else:
        print(f"Các số nguyên âm tìm thấy: {', '.join(so_am)}")


s_de_bai = "aBc-5xyz.12k-9" 
NegativeNumberInStrings(s_de_bai)

s_typo = "aBc-5xyz-12k-9"
NegativeNumberInStrings(s_typo)

s_khac = "Nhiệt độ là -10 độ C. Số dư: -15000 vnd."
NegativeNumberInStrings(s_khac)