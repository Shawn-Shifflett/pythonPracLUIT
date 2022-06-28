value = int(input("Enter number: "))
print("Number enetered:",value)

if value % 5 == 0 and value % 3 == 0:
    print(value,"is div by both 3 & 5")
elif value % 5 == 0: 
    print(value, "is div by 5")
elif value % 3 == 0:
    print(value, "is div by 3")
else: 
    print(value, "is not div by 3 nor 5")