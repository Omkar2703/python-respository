n = int(input("Enter the number:"))
s=0
temp=n
while temp>0:
    d = temp%10
    s += d ** 3
    temp //= 10
if (n == s):
    print('Entered number is Armstrong number.')
else:
    print('Entered number is not Armstrong number.')