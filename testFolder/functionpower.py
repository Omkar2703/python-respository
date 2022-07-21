def power(x, n):
    if (n == 0):
        return 1
    elif (n == 1):
        return x
    else:
        return x*power(x,n-1)
x = int(input("Enter the value of X:"))
n = int(input("Enter the power value:"))
p=power(x,n)
print('Result is',p)