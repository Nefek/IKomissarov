from math import pi, sin, cos

arr = ["0","1","2","3","4","5","6","7","8","9"]
x = input("Введите значение x: ")
if x not in arr:
    
    while x not in arr:
        x = input("Неверный тип данных, ведите значение в числовом типе: ")
        continue

else: 
    x = int(x)
    if x <= pi / 4:
        print(f"y = sinx  y = {sin(x)}")
    else:
        print(f"y = cosx  y = {cos(x)}")
