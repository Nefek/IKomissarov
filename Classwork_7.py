#___№1___
a, n = 1, 3.14  
while a ** 0.5 <= n:
    if a ** 0.5 < 3.14:
        print(f"{a ** 0.5} ({a})")
    a += 1
#___№2___ 
a, b = int(input()), int(input())     
while a < b:
    a += 1
    print(a)
#___№3___ 
a, b = int(input()), int(input())     
while a < b:
    b -= 1
    print(b)
#___№4___
n, a = int(input()), 1
while a * 3 < n:
    a += 1
print(a, a * 3)
#___№5___
n, a = int(input()), 1
while a * 3 < n:
    a += 1
if a * 3 > n:
    print(a - 1)
else:
    print(a)


