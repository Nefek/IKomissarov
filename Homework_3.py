#___Задания_№7_№8___
#
#_____№7_____
a = int(input("Введите трёхзначное число: "))
if a >= 100 and a < 1000:
    a1 = a // 100
    a2 = a // 10 % 10
    a3 = a % 10
    if a1 + a2 + a3 > 9 and a1 + a2 + a3 < 100:
        print("сумма - двузначное")
    else:
        print("сумма - не двузначное")
    if a1 * a2 * a3 > 99 and a1 * a2 * a3 < 1000:
        print("произведение - трехзначное")
    else:
        print("произведение - не трехзначное")
    if a1 * a2 * a3 > a:
        print("произведение больше а")
    else:
        print("произведение меньше а")
    if a1 + a2 + a3 % 5 == 0:
        print("кратна 5")
    else:
        print("не кратна 5")
    if a1 + a2 + a3 % a == 0:
        print("кратна а")
    else:
        print("не кратна а")
else:
    print("число не трехзначное")
#
#
#_____№8_____
a = int(input("Введите 4х значное число: "))
if a > 999 and a < 10000:
    a1 = a // 1000
    a2 = a // 100 % 10
    a3 = a // 10 % 10
    a4 = a % 10
    if a1 + a2 == a3 + a4:
        print("Сумма первых двух цифр равна сумме двух последних чисел", a)
    else:
        print("Сумма первых двух цифр НЕ равна сумме двух последних чисел", a)
    if (a1 + a2 + a3 + a4) % 3 == 0:
        print("Сумма цифр", a, "кратна трем")
    else:
        print("Сумма цифр", a, "НЕ кратна трем")
    if (a1 * a2 * a3 * a4) % 4 == 0:
        print("Произведение цифр", a, "кратно четырем")
    else:
        print("Произведение цифр", a, "НЕ кратно четырем")
    if (a1 * a2 * a3 * a4) % a == 0:
        print("Произведение цифр", a, "кратно числу а" )
    else:
        print("Произведение цифр", a, "НЕ кратно числу", a)
else:
    print("число не 4х значное")