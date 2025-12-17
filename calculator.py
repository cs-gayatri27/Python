print("CALCULATOR.........")
print("....................")

while True:
    print("..........................")
    print("\n choose your operation: \n")
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")
    print("5. Remainder(%)")
    print("6. power(**)")
    print("7. quotient(//)")
    print("8. Even/odd check")
    print("9. Exit")

    choice = int(input("Enter your choice(1-9): "))

    if choice == 9:
        print("calculator closed")
        break

    if choice < 1 or choice > 9:
        print("please try again. Your choice is invalid")
        break #terminate the loop and exit the calculator

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == 1:
        result = num1 + num2
        print(f"Addition result is {result}")
            
    elif choice == 2:
        sub = num1 - num2
        print(f"Subtraction result is {sub}")

    elif choice == 3:
        mul = num1 * num2
        print(f"multiplication result is {mul}")

    elif choice == 4:
        div = num1 / num2
        print(f"Division result is {div}")

    elif choice == 5:
        rem = num1 % num2
        print(f"remainder is {rem}")

    elif choice == 6:
        pow = num1 ** num2
        print(f"power is {pow}")

    elif choice == 7:
        quo = num1 // num2
        print(f"quotient is {quo}")

    elif choice == 8:
        if num1 % 2 == 0:
            print(f"{num1} is an even number")
        else:
            print(f"{num1} is an odd number")

        if num2 % 2 == 0:
            print(f"{num2} is an even number")
        else:
            print(f"{num2} is an odd number")

    




