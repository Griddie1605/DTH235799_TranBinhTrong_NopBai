# --- Câu 4 ---
print("--- Kết quả Câu 4 ---")

# Khởi tạo
lst = [3, 0, 1, 5, 2]
x = 2

print(f"Cho lst = {lst}")
print(f"Cho x = {x}\n")

# (a) lst[0]?
print(f"(a) lst[0]:     {lst[0]}")

# (b) lst[3]?
print(f"(b) lst[3]:     {lst[3]}")

# (c) lst[x]?
# Tương đương lst[2]
print(f"(c) lst[x]:     {lst[x]}")

# (d) lst[-x]?
# Tương đương lst[-2]
print(f"(d) lst[-x]:    {lst[-x]}")

# (e) lst[x + 1]?
# Tương đương lst[2 + 1] -> lst[3]
print(f"(e) lst[x + 1]: {lst[x + 1]}")

# (f) lst[x] + 1?
# Tương đương lst[2] + 1 -> 1 + 1
print(f"(f) lst[x] + 1: {lst[x] + 1}")

# (g) lst[lst[x]]?
# Tương đương lst[lst[2]] -> lst[1]
print(f"(g) lst[lst[x]]: {lst[lst[x]]}")

# (h) lst[lst[lst[x]]]?
# Tương đương lst[lst[lst[2]]] -> lst[lst[1]] -> lst[0]
print(f"(h) lst[lst[lst[x]]]: {lst[lst[lst[x]]]}")