#___№9___
a = 200
while a % 17 != 0:
    a += 1
print(a)
#___№10___
a = 600
while a % 28 != 0:
    a -= 1
print(a)
#___№11___
a = 10
count = 1
while a <= 20:
    a += a * 0.1
    count += 1
print(f"{a} ({count})")
#___№12___
a = 1
total = 0
n = int(input())
while a <= n:
    b = (2 * a - 1) / (2 * a)
    total += b
    a += 1
print(round(total, 4))
#___№13___
total = 1.0  
a = 1.0 
n = 2 
for i in range(1000):
    a = (-1) ** (n+1) / (2 ** (n-1))
    total += a
    n += 1
print(total)
#___№14___
a = 1
while a <= 100:
    if a % 11 == 0:
        print(a)
    a += 1





















