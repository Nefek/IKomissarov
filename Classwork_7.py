#___№1___
for i in range(2, 101):
    if i ** 0.5 < 3.14:
        print(f"{i ** 0.5} ({i})")
#___№2___ 
a, b = int(input()), int(input())     
for i in range(a + 1, b):
    print(i)
#___№3___ 
a, b = int(input()), int(input())     
for i in range(b - 1, a, -1):
    print(i)
#___№4___
n = int(input())
for i in range(1, 1000000):
    if i * 3 >= n:
        print(i, i * 3)
        break
#___№5___
n = int(input())
for i in range(1, 1000000):
    if i * 3 <= n:
        print(i, i * 3)
        break



