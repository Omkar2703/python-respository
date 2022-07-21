def GCD(m, n):
    if (n>m):
        return GCD(n,m)
    elif (n==0):
        return m
    else:
        return GCD(n, m%n)
a = int (input("Please enter the number:"))
b = int (input("Please enter the number:"))
g = GCD(a, b)
l = (a*b)/g
print('GCD of the given number is',g)
print('LCM of the given number is', l)