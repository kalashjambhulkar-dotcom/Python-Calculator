def calculator():
    print("\n=== Simple Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Choose (1-4): ")

    if choice not in "1234":
        print("Invalid option!")
        return

    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Please enter valid numbers!")
        return

    if choice == '1':
        print("Result:", a + b)
    elif choice == '2':
        print("Result:", a - b)
    elif choice == '3':
        print("Result:", a * b)
    elif choice == '4':
        if b == 0:
            print("Error: Division by zero.")
        else:
            print("Result:", a / b)

if __name__ == "__main__":
    while True:
        calculator()
        if input("Again? (y/n): ").lower() != 'y':
            print("Thanks for using the calculator!")
            break
