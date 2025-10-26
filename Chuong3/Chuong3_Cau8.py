try:
    a = float(input("Nhập giá trị a: "))
    b = float(input("Nhập giá trị b: "))
    
    phep_toan = input("Nhập phép toán (+, -, *, /): ").strip()

    if phep_toan == '+':
        ket_qua = a + b
        print(f"Kết quả: {a} + {b} = {ket_qua}")
        
    elif phep_toan == '-':
        ket_qua = a - b
        print(f"Kết quả: {a} - {b} = {ket_qua}")
        
    elif phep_toan == '*':
        ket_qua = a * b
        print(f"Kết quả: {a} * {b} = {ket_qua}")
        
    elif phep_toan == '/':
        if b == 0:
            print("Lỗi: Không thể chia cho 0!")
        else:
            ket_qua = a / b
            print(f"Kết quả: {a} / {b} = {ket_qua}")
            
    else:
        print(f"Lỗi: Phép toán '{phep_toan}' không được hỗ trợ.")

except ValueError:
    print("Lỗi: 'a' và 'b' phải là các con số. Vui lòng chạy lại.")