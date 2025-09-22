#Câu 3: Tính điểm trung bình
'''
Yêu cầu:
Viết chương trình nhập vào điểm ba môn Toán, Lý, Hóa của một học sinh. In ra
điểm trung bình của học sinh đó với hai số lẻ thập phân.
'''
print("Chuong trinh tinh diem trung binh!")
toan=float(input("nhap diem toan: "))
ly=float(input("Nhap diem ly: "))
hoa=float(input("Nhap diem hoa: "))
dtb=(toan+ly+hoa)/3
print("Diem trung binh = ",dtb)
print("Diem trung binh = ",round(dtb,2))