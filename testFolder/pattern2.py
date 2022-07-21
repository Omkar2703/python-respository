n = int ( input ("Enter the number of lines:"))
for i in range(1,n):
    for j in range(1,(n+1)-i):
        print("*", end=' ')
    print()