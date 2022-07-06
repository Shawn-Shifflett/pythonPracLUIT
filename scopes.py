# testing name hiding
# testing inner and outter values

# not good to name hide, but for practice this is fine

y = 5

def setX(y):
    print("Inner y:" , y)
    x = y
    y = x
    
setX(10)
    
print("Outter y:", y)
