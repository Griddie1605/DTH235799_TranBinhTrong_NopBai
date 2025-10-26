from random import randrange
while True:
    somay=randrange(1,101)
    solandoan=0
    win=False
    while solandoan<7:
        solandoan+=1
        songuoi=int(input(" Số ngẫu nhiên là [1..100], mời bạn đoán:"))
        print("Bạn đoán lần thứ ",solandoan)
        if somay==songuoi:
            print("Chúc mừng bạn đoán đúng, số chính xác là=",somay)
            win=True
            break
        if somay>songuoi:
            print("Bạn đoán sai, số chính xác là > số bạn đoán")
        elif somay<songuoi:
            print("Bạn đoán sai, số chính xác là < số bạn đoán")
        if win==False:
            print("GAME OVER!, số chính xác là =",somay)
            hoi=input("Bạn muốn chơi tiếp không?")
        if hoi=="k":
            break
print("Cám ơn bạn đã chơi Game!")
