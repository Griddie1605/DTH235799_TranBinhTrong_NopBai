from random import randrange

# 1. Khởi tạo
print("Chương trình xử lý List")
n = int(input("Nhập số phần tử: "))

# Tạo list với n phần tử 0
lst = [0] * n 

# 2. Tạo list ngẫu nhiên
for i in range(n):
    # Gán số ngẫu nhiên từ -100 đến 99
    lst[i] = randrange(-100, 100) 
    
print("List ngẫu nhiên là:")
print(lst)

# 3. Thêm phần tử
print("Mời bạn thêm số mới:")
value = int(input())
lst.append(value) # Thêm 'value' vào cuối list
print(lst)

# 4. Đếm phần tử
print("bạn muốn đếm số nào:")
k = int(input())
dem = lst.count(k) # Dùng hàm count() để đếm
print(k, "xuất hiện ", dem, "trong list")

# 5. Định nghĩa hàm kiểm tra số nguyên tố
def CheckPrime(n):
    """
    Hàm này đếm số ước của n.
    Trả về True nếu n có đúng 2 ước (là 1 và chính nó).
    """
    d = 0
    # Vòng lặp chạy từ 1 đến n
    for i in range(1, n + 1):
        if n % i == 0:
            d += 1
    return d == 2 # Trả về True nếu có đúng 2 ước

# 6. Xử lý số nguyên tố
demnt = 0
tongnt = 0
for x in lst:
    # Chỉ kiểm tra số dương > 1
    # (vì số 0, 1, và số âm không phải số nguyên tố)
    if x > 1 and CheckPrime(x):
        demnt += 1
        tongnt += x
        
print("Có ", demnt, "số nguyên tố trong list")
print("Tổng=", tongnt)

# 7. Sắp xếp list
lst.sort() # Sắp xếp list tăng dần
print("List sau khi sort:")
print(lst)

# 8. Xóa nội dung list
# del lst # Lỗi: Dòng này sẽ xóa biến và gây lỗi NameError ở dòng print()
lst.clear() # Sửa lỗi: Dùng .clear() để xóa SẠCH nội dung, list trở thành rỗng

print("List sau khi xóa (đã rỗng):")
print(lst) # In ra: []