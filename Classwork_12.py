def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True
a = int(input())
print(is_prime(a))
        



def date(day, month, year):
    if month < 1 or month > 12: return False

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        if month == 2:
            if day > 29: return False
    
    if month == 2: 
        if day > 29: return False
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30: return False
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day > 31: return False

    return True
day, month, year = int(input("день: ")), int(input("месяц: ")), int(input("год: "))
print(date(day, month, year))


