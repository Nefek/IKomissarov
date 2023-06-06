def schet(a):
    a = str(a)
    if len(a) != 4: print("Не 4х значеное число")
    else:
        summ = int(a[0]) + int(a[1]) + int(a[2]) + int(a[3])
        proizv = int(a[0]) * int(a[1]) * int(a[2]) * int(a[3])
    return(summ, proizv)
print(schet(int(input("введите 4х значное число: "))))

def last(a):
    a = str(a)
    if len(a) != 5: print("Не 5 значеное число")
    else: return a[3], a[4]
print(last(int(input("Введите 5 значное число: "))))

def obrat(a):
    a = str(a)
    if len(a) != 3: print("Не 3 значеное число")
    else: 
        b = a[2] + a[1] + a[0]
    return int(a) - int(b)
print(obrat(int(input("Введите 3х значное число: "))))

def chisla(a):
    a = str(a)
    v = len(a)
    m = ""
    for i in range(v):
        m += a[i] + " "
    return m
print(chisla(int(input("Введите число: "))))
    
def dva(a):
    a = str(a)
    l = len(a)
    flag = False
    for i in range(l):
        if int(a[i]) == 2:
            flag = True
    return flag
print(dva(int(input("Введите число: "))))

