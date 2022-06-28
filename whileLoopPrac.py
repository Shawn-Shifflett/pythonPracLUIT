#Basic Loop Practice

#basic while loop
print("While Loop:")
i = 1 #set counter

while i <= 4:
    print(i)
    i += 1 #incr counter, so it's not an inf loop
    
print('-------------------------')
    
#basic for loop 
print("For Loop:")
colors = ['blue', 'green', 'red']
for c in colors:
    print(c)
    
print()

#Looping w/ dict    
ages = {'shawn': 24, 'tre':24, 'jordan':25} 
for key, value in ages.items():
    print(key, value)
    
print()

#Looping w/ a string
for l in 'Hello World!':
    print(l)
    
print('-------------------------')
#Nested Looping
num = 1
while num <= 25:
    if num % 3 == 0: #take number and see if its / by 4
        print(num)
    num +=1 #incr the number
    
print('-------------------------')
#Looping w/ else
for lis in [1, 2, 3, 4, 5]:
    print(lis)
else:
    print("Completed")
    
print()
    
max_color = ['r','b','o','p']
for o in max_color:
    if o == 'r':
        print("R is in the list")
        break
else:
    print("R is not in the list")
    
print('-------------------------')

#working w/ range
my_range = range(1, 11)
print(my_range)
range_list = list(my_range)
print(range_list)

print('-------------------------')

#List comprehensions
b = ['r', 'b', 'y'] #list of colors
u_b = [] #create empty list of uppercase colors
for y in b:
    u_b.append(y.upper()) #make colors uppercase
    
print(u_b)