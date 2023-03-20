#Блок функций и переменных

pi = 3.141592653589793

def sin(x):
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    return +s

def cos(x):
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    return +s

#Блок с задачей

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