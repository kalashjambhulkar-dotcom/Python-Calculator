def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("===== CLI Calculator =====")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1-4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            return

        if choice == '1':
            print("Result:", addition(num1, num2))
        elif choice == '2':
            print("Result:", subtraction(num1, num2))
        elif choice == '3':
            print("Result:", multiplication(num1, num2))
        elif choice == '4':
            print("Result:", division(num1, num2))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    while True:
        calculator()
        again = input("Do you want to continue? (y/n): ")
        if again.lower() != 'y':
            print("Exiting... Thanks for using CLI Calculator!")
            break
