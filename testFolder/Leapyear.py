from calendar import leapdays


def year(n):
    if n % 400 == 0:
        leap = True
    if n % 100 == 0:
        leap = False
    if n % 4 == 0:
        leap = True
    return leap
n = int ( input("Enter the year:"))
print (year(n))