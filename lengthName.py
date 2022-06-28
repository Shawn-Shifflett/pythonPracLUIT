name = input("Enter name: ")

print("Name entered:",name)


if len(name) >= 6:
    print(name , "is a long name.")
elif len(name) == 5:
    print(name , "is 5 char. long.")
elif len(name) >= 4:
    print(name, "is greater than 4 char. long.")
else:
    print(name, "is a short name.")