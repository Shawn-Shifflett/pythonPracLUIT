#basic function practice
def printName(name):
    print("Name is:", name)
    
printName("Shawn")

def add_two(num):
    return num + 2
print(add_two(4))

def add(num1, num2):
    print(num1 + num2)
add(3,5)
add(7,7)

def canDrive(age, drivingAge = 16):
    return age >= drivingAge
print("You are old enough to drive:" , canDrive(14))
print("You are old enough to drive:" , canDrive(24))
print("You are old enough to drive:" , canDrive(15,16))