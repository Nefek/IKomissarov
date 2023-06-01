def bank(a, years):
    for i in range(1, years + 1):
        a += a * 0.1
    return(a)

a, b = input(),input()
x, y = a.isdigit(), b.isdigit()
if x == True and y == True: print(bank(int(a), int(b)))
else: print("Not numbers")
