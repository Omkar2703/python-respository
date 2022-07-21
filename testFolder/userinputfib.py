n=int(input("Enter number till you want the series:"))
x, y=0, 1
while (x<n):
    print(x, end=',')
    x, y= y, x + y