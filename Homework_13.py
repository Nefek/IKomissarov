def season(a):
    if a == 12 or a == 1 or a == 2: return "Winter"
    elif a in range(3, 6): return "Spring"
    elif a in range(6, 9): return "Summer"
    elif a in range(9, 12): return "Autumn"
    else: return "not month number"
print(season(int(input("Enter the month number: "))))
    
