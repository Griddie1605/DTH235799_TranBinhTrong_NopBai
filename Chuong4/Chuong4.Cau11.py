def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s
def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s
def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s

'''
Trường hợp 1: 
kq: 
5
5
0
'''

'''
Trường hợp 2:
kq:
5
5
5
'''

'''
Trường hợp 3:
kq:
5
5
0
'''