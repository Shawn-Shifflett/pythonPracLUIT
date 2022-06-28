num = int(input("Enter number of range: "))

print("Range Limit:", num)

for n in range(1, num + 1):
    if n % 5 == 0 and n % 3 == 0:
        print(n,"is div by both 3 & 5")
    elif n % 3 == 0:
        print(n,"is div by 3")
    elif n % 5 == 0:
        print(n, "is div by 5")
    else: 
        print(n)