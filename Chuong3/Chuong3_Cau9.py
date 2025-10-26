try:
    thang = int(input("Nhập vào tháng (1-12): "))

    if 1 <= thang <= 3:
        print(f"Tháng {thang} thuộc Quý 1.")
    elif 4 <= thang <= 6:
        print(f"Tháng {thang} thuộc Quý 2.")
    elif 7 <= thang <= 9:
        print(f"Tháng {thang} thuộc Quý 3.")
    elif 10 <= thang <= 12:
        print(f"Tháng {thang} thuộc Quý 4.")
    else:
        print("Lỗi: Tháng không hợp lệ, phải nằm trong khoảng 1-12.")

except ValueError:
    print("Lỗi: Vui lòng nhập một con số nguyên.")