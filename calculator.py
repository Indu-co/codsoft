def calculator():
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number"))

    print("\n choose an operation:")
    print("1.addition(+)")
    print("2.subtraction(-)")
    print("3.multiplication(*)")
    print("4.division(/)")

    operation=input("enter your choice(1/2/3/4):")
    if operation=='1':
        result=num1+num2
        print(f"\the result of{num1}+{num2}is:{result}")
    elif operation=='2':
        result=num1-num2
        print(f"\the result of {num1}-{num2}is:{result}")
    elif operation=='3':
        result=num1*num2
        print(f"\n the result of {num1}*{num2} is:{result}")
    elif operation=='4':
        if num2!=0:
            result=num1/num2
            print(f"\n the result of {num1}/{num2}is :{result}")
        else:
            print("\n error:division by zero is not allowed")
    else:
        print("\n invalide operation choice")
calculator()

    