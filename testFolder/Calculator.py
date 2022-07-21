
def add(a, b):
    return a + b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

print('Select the operation:')
print('1. Addition.')
print('2. Substraction.')
print('3. Multiplication.')
print('4. Division.')
while True:
    choice=input("Enter the choice(1,2,3,4):")
    if choice in ('1','2','3','4'):
        x = float(input("Enter the first number:"))
        y = float(input("Enter the second number:"))
        if choice == '1':
            print(x, "+", y, "=", add(x, y))
        elif choice == '2':
            print(x, "-",y, "=", subtract(x, y))
        elif choice == '3':
            print(x, "*", y, "=", multiply(x, y))
        elif choice == '4':
            print(x, "/", y, "=", divide(x, y))
        next_calculation = input("Do you wanted to do next calculation?(yes/no):")
        if next_calculation == 'no':
            break
    else:
        print('Invalid choice.')