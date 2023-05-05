#___№1___
for i in range(10, 23):
    print(i * 2.54)

#___№2___
a = float(input("Введите значение текущего курса: "))
for i in range(1, 21):
    print(i * a)

#___№3___
a = int(input("Введите цифру, степени которой хотите вычислить: "))
for i in range(1, 21):
    print(a ** i)

#___№4___
for i in range(21):
    print(1.1 + i)

#___№5___
for i in range(1, 10):
    print(2 + i / 10)

#___№6___
for i in range(10):
    print(2 * i)

#___№7___
for i in range(1, 16):
    print(-1 + 2 * i)

#___№8___
for i in range(2, 21, 2):
    print(i ** 0.5)

#___№9___
a = int(input("Цена за 1 кг конфет: "))
for i in range(2, 11):
    print(f"Цена за {i} кг = {i * a}")

#___№10___
for i in range(int(input("Введите точку начала отрезка(a): ")), int(input("Введите точку конца отрезка(b): ")) + 1):
    print(f"y = {i ** 0.5}")

