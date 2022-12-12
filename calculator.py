a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
while True:
    print("\nMenu\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n")
    c = int(input("\nEnter the choice:"))
    if c==1:
        print("\nAddition: ",a+b)
    elif c==2:
        print("\nSubstraction: ", a-b)
    elif c==3:
        print("\nMultiplication: ", a*b)
    elif c==4:
        print("\nDivision: ", a/b)
    else:
        print("\nInvalid Choice.")
    user_input = input('Do you want to continue? yes/no: ')
    if user_input.lower() == 'yes':
        print("\nMenu\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Exit")
        c = int(input("\nEnter the choice:"))
        if c==5:
            print("\nExit satisfied.")
        if c==1:
            print("\nAddition: ",a+b)
        elif c==2:
            print("\nSubstraction: ", a-b)
        elif c==3:
            print("\nMultiplication: ", a*b)
        elif c==4:
            print("\nDivision: ", a/b)
        else:
            print("\nInvalid Choice.")
            continue
        
    elif user_input.lower() == 'no':
        print('Exit Satisfied.')
        break
    else:
        print('Type yes/no')
