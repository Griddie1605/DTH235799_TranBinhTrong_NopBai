import random
print("--- Chạy thử hàm random.randrange(0, 100) ---")

print("Kết quả của 20 lần chạy:")

for i in range(20):
    so_ngau_nhien = random.randrange(0, 100)
    
    print(so_ngau_nhien, end=" ")

print("\n\n--- Kết luận  ---")
print("-> Kết quả luôn là số nguyên (không thể là 4.5).")
print("-> Kết quả không bao giờ < 0 (không thể là -1).")
print("-> Kết quả không bao giờ >= 100 (không thể là 100).")
print("-> Kết quả CÓ THỂ là 0, 34, hoặc 99 (và nhiều số nguyên khác).")