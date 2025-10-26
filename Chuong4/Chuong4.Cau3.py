import math

def BMI(height, weight):
    return weight / (height ** 2)

def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi <= 24.9:
        return "Bình thường"
    elif bmi <= 29.9:
        return "Hơi Béo"
    elif bmi <= 34.9:
        return "Béo Phì Cấp Độ 1"
    elif bmi <= 39.9:
        return "Béo Phì Cấp Độ 2"
    else:
        return "Béo Phì Cấp độ 3"

def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Thấp"
    elif bmi <= 24.9:
        return "Trung bình"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 39.9:
        return "Rất cao"
    else:
        return "Nguy Hiểm"

try:
    height = float(input("Nhập vào chiều cao (ví dụ: 1.70): "))
    weight = float(input("Nhập vào cân nặng (ví dụ: 65): "))

    if height <= 0 or weight <= 0:
        print("Lỗi: Chiều cao và cân nặng phải là số dương.")
    else:
        bmi = BMI(height, weight)
        
        phan_loai = PhanLoai(bmi)
        
        nguy_co = NguyCoBenh(bmi)
        
        print(f"\nBMI của bạn= {bmi:.2f}")
        print(f"Phân loại bạn= {phan_loai}")
        print(f"Nguy cơ bệnh của bạn= {nguy_co}")

except ValueError:
    print("Lỗi: Vui lòng chỉ nhập số (ví dụ: 1.70 hoặc 65).")