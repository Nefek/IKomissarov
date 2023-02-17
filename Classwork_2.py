# №1
a = int(input())
if a > 0:
    print("Больше нуля")

# №2
if a > 0:
    print("1")
else:
    print("-1")

# №3 на вход даны 3 переменных, построить их в порядке убывания:
A = int(input())
B = int(input())
C = int(input())
Min = min(A, B, C)
Max = max(A, B, C)
if A == Min:
    if B == Max:
        Mid = C
    else:
        Mid = B
elif B == Min:
    if A == Max:
        Mid = C
    else:
        Mid = A
elif C == Min:
    if A == Max:
        Mid = B
    else:
        Mid = A
print(Max, Mid, Min, sep="\n")


