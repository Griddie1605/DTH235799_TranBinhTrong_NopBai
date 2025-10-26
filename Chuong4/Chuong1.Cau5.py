def fibonacci(n):
    if n<=2 :
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def listfibo(n):
    for i in range(1,n+1):
        print(fibonacci(i),end='\t')

# ----- chạy chương trình -----
    n = int(input('Nhap mot so nguyen duong: '))
    print("Tổng các số fib là: ",fibonacci(n))
    print("Dãy fib: ")
    listfibo(n)
