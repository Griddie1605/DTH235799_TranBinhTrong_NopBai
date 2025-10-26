from random import randrange

def TaoMaTran(m,n):
    D=[]
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(randrange(100))
        D.append(row)
    return D

def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element,end='\t')
        print()

def LayDong(r):
    # Lưu ý: Code này sẽ gây lỗi nếu biến 'D'
    # không được khai báo global.
    # Để an toàn, hàm này nên nhận D làm tham số: def LayDong(D, r):
    R=D[r]
    return R

def XuatList1Chieu(R):
    for element in R:
        print(element,end='\t')

def LayCot(c):
    # Tương tự hàm LayDong, hàm này cũng phụ thuộc
    # vào biến global 'D'
    C=[]
    for i in range(len(D)):
        C.append(D[i][c])
    return C

def MAX(D):
    max=D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if(max<D[i][j]):
                max=D[i][j]
    return max

# --- Chương trình chính ---
print("Nhập số dòng:")
m=int(input())
print("Nhập số cột:")
n=int(input())

D=TaoMaTran(m,n) # Biến 'D' toàn cục (global) được tạo ở đây
XuatMaTran(D)

print("Mời bạn nhập dòng muốn xuất:")
r=int(input())
XuatList1Chieu(LayDong(r))

print("\nMời bạn nhập cột muốn xuất:") # Thêm \n để xuống dòng
c=int(input())
XuatList1Chieu(LayCot(c))

max=MAX(D)
print("\nSố lớn nhất trong ma trận=",max) # Thêm \n để xuống dòng