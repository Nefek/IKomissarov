from math import sqrt
#___№1___
a, b, c = int(input("Первое снование трапеции: ")), int(input("Второе снование трапеции: ")), int(input("Высота трапеции: "))
print("Периметр трапеции равен =", a + b + 2 * c)
#
#
#___№2___
a, b = int(input("Масса вещества: ")), int(input("Объем вещества: "))
print("Плотность вещества =", a / b)
#
#
#___№3___
a, b = int(input("Первое число: ")), int(input("Второе число: "))
print(f"Сумма чисел = {a + b} Разность чисел = {a - b} Произведение чисел = {a * b} Частное чисел = {a / b}")
#
#
#___№4___
a, b = int(input("Введите положительное число: ")), int(input("Еще одно положительное число: "))
while a <= 0 or b <= 0:
    if a < 0 or b < 0:
        print("Числа не подходят")
        a, b = int(input("Введите положительное число: ")), int(input("Еще одно положительное число: "))
print(f"Среднее арифметическое = {(a + b) / 2} Среднее геометрическое = {sqrt(a * b)}")
#
#
#___№5___
a, b = int(input("Введите численность населения территории: ")), int(input("Введите площадь территории (в км²): "))
print(f"Плотность населения = {a / b} человек/км²")
#
#
#___№6___
a, b, c = int(input("Первое ребро (в см): ")), int(input("Второе ребро (в см): ")), int(input("Третье ребро (в см): "))
print(f"Площадь поверхности прямоугольного параллелепипеда = {2 * (a * b + b * c + a * c)} см²")
print(f"Объем прямоугольного параллелепипеда = {a * b * c} см³")



