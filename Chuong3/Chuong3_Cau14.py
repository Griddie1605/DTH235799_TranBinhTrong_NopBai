a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print('*', end='')
        b += 1
    print() # In xuống dòng, tạo ra dòng mới
    a += 1
    
    #kết quả là 2000 dấu *