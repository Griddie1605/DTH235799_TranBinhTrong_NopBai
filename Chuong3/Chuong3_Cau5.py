def check_values(i_val, j_val, k_val):
    # Gán giá trị để không làm thay đổi giá trị gốc
    i, j, k = i_val, j_val, k_val
    
    if j < k:
        if j < i:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    
    # Dùng f-string để in kết quả
    print(f"Trường hợp (i={i_val}, j={j_val}, k={k_val}): \t Kết quả -> {i} {j} {k}")

# (a)
check_values(3, 5, 7)
# (b)
check_values(3, 7, 5)
# (c)
check_values(5, 3, 7)
# (d)
check_values(5, 7, 3)
# (e)
check_values(7, 3, 5)
# (f)
check_values(7, 5, 3)