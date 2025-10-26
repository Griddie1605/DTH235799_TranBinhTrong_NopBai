# Cần thêm 2 dòng này để code chạy đúng:
from random import randrange
lst = [] 

# --- Code gốc của bạn ---
print("Nhập số phần tử:")
n=int(input())
for i in range(n):
    lst.append(randrange(0,100))

print("List sau khi tạo ngẫu nhiên là:")
print(lst)

x=int(input("Mời bạn chèn thêm số mới"))
lst.append(x)
print("List sau khi chèn:")
print(lst)

k=int(input("Mời nhập số để xóa"))
while lst.count(k)>0:
    lst.remove(k)

print("List sau khi xóa:")
print(lst)

def CheckDoiXung(lst):
    # Vòng lặp này sẽ so sánh phần tử đầu với cuối,
    # rồi gần đầu với gần cuối, v.v.
    # Tối ưu: Lặp đến len(lst) // 2 là đủ
    for i in range(len(lst)): 
        if lst[i]!=lst[len(lst)-i-1]:
            return False
    return True

kt=CheckDoiXung(lst)
if kt==True:
    print("List đối xứng")
else:
    print("List không đối xứng")