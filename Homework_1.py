a = int(input())
b = int(input())
if a > b:
    c = a - b
elif a < b:
    c = b + a
else:
    c = a
print(c)

a = input()
b = input()
if a == "красный":
    if a == b:
        print("красный")
    elif b == "синий":
        print ("фиолетовый")
    elif b == "желтый":
        print("оранжевый")
    else:
        print ("ошибка цвета")
elif a == "синий":
    if a == b:
        print("синий")
    elif b == "красный":
        print("фиолетовый")
    elif b == "желтый":
        print("зеленый")
    else:
        print("ошибка цвета")
elif a == "желтый":
    if a == b:
        print("желтый")
    elif b == "красный":
        print("оранжевый")
    elif b == "синий":
        print("зеленый")
    else:
        print("ошибка цвета")
else:
    print("ошибка цвета")
