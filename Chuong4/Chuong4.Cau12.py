def oscillate(start, stop):    
    for i in range(abs(start)):
        
        inner_start = start + i
        
        inner_stop = stop - (abs(start) - 1) + i
        
        for j in range(inner_start, inner_stop):
            yield j

print("Kết quả chạy hàm:")

for n in oscillate(-3, 5):
    print(n, end=' ')

print()