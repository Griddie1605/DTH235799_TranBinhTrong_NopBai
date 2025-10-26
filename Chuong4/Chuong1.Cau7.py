import math 

# --- Chương trình chính ---
try:
    # 1. Nhập tọa độ cho điểm A
    print("--- Nhập tọa độ điểm A ---")
    xA = float(input("Nhập xA: "))
    yA = float(input("Nhập yA: "))
    
    # 2. Nhập tọa độ cho điểm B
    print("\n--- Nhập tọa độ điểm B ---")
    xB = float(input("Nhập xB: "))
    yB = float(input("Nhập yB: "))
    
    # 3. Tính toán theo công thức
    # (xB - xA)**2 tương đương với (xB - xA) bình phương
    # math.sqrt() là hàm lấy căn bậc hai
    do_dai_AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)
    
    # 4. In kết quả
    print(f"\nTọa độ A({xA}, {yA})")
    print(f"Tọa độ B({xB}, {yB})")
    print(f"-> Độ dài đoạn thẳng AB là: {do_dai_AB}")

except ValueError:
    print("Lỗi: Vui lòng chỉ nhập các con số cho tọa độ.")