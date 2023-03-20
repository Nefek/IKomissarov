#В файле matematik содержатся функции sin и cos, а так же переменная pi

from matematik import *

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
    print(f"y = sin(x)  y = {sin(a)}")
else:
    print(f"y = cos(x)  y = {cos(a)}")