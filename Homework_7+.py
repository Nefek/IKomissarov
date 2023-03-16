from math import pi, sin, cos

a = input("Введите значение x: ")
x = a.isdigit()

while x != True or x == "":
        if a == "":
            a = input("Вы ничего не ввели, попробуйте еще раз: ")
            x = a.isdigit()
        else:
            a = input("Неверный тип данных, ведите значение в числовом типе: ")
            x = a.isdigit()

a = int(a)
if a <= pi / 4:
    print(f"y = sinx  y = {sin(a)}")
else:
    print(f"y = cosx  y = {cos(a)}")