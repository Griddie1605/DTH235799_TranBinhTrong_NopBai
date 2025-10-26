def ve_hinh_1(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("* ", end="") 
            else:
                print("  ", end="")
        
        print()

def ve_hinh_2(n):
    print("\n--- Hình 2 ---")
    for i in range(1, n + 1):
        for k in range(n - i):
            print("  ", end="")
        
        for j in range(i):
            print("* ", end="")
        print()


try:
    n_input = int(input("Nhập chiều cao n (ví dụ 4): "))
    
    if n_input <= 0:
        print("Lỗi: Vui lòng nhập một số nguyên dương.")
    else:
        ve_hinh_1(n_input)
        ve_hinh_2(n_input)
        
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")