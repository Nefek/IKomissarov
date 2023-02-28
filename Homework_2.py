a = int(input("Введите 3х значное число: "))
if a > 99 and a < 1000:
    a1 = a // 100
    a3 = a % 10
    if a1 == a3:
        print("число пaлиндром")
    else:
        print("число не пakиндром")
else:
    print("плохое число")
