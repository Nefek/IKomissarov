from math import sqrt
#___№1___
a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
if a == b:
    print("Ваши числа равны")
else:
    print(f"Большее число: {max(a, b)}  Меньшее число: {min(a, b)}")
#
#
#___№2___
a, b = int(input("Введите сторону квадрата: ")), int(input("Введите радиус круга: "))
if a >= 2 * b:
    print("Круг впишется в квадрат")
else:
    print("Круг не впишется в квадрат")
#
#
#___№3___
x = int(input("Введите х: "))
if x > 0:
    print(f"y=x² y={x ** 2}")
elif x == 0:
    print("x не может быть равен 0")
else:
    print(f"y=1/x² y={1 / x ** 2}")
#
#
#___№4___
a, b = int(input("Введите сторону квадрата: ")), int(input("Введите радиус круга: "))
if a <= b * sqrt(2):
    print("Квадрат впишется в круг")
else:
    print("Квадрат не впишется в кргу")
#
#
#___№5___
a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
if a == b:
    print("Ваши числа равны")
elif a > b:
    print(f"Число {a} больше числа {b}")
else:
    print(f"Число {b} больше числа {a}")
#
#
#___№7___
a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
if a == b:
    print("Ваши числа равны")
elif a > b:
    print(f"Число {b} меньше числа {a}")
else:
    print(f"Число {a} меньше числа {b}")
#
#
#___№8___
a1, b1 = int(input("Введите время (в сек): ")), int(input("Введите скорость (в м/с): "))
a2, b2 = int(input("Введите время (в сек): ")), int(input("Введите скорость (в м/с): "))
if a1 * b1 == a2 * b2:
    print("Расстояния одинаковы")
elif a1 * b1 > a2 * b2:
    print("Первое расстояние больше")
else:
    print("Второе расстояние больше")







