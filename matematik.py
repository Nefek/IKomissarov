def factorial(n):
    factorial = 1
    for j in range(1, n + 1):
        k = 1
        k *= j
        factorial *= k
    return factorial

pi = 3.141592653589793

#Вычисление sin и cos через ряд Тейлора

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
