#fib seq
# 1, 1, 2, 3, 5, 8 ...

def fib(n):
    if n == 0: #base case1
        return 0
    elif n == 1: #base case2
        return 1
    else:
        return fib(n- 2) + fib(n - 1)
        
find = int(input("Enter item to caluclate: ")) #finds value at the _ index 

print(fib(find))
#run time too long ctl + c will kill it