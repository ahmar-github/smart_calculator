print("=== Welcome to Smart Calculator ===")

while True:
    # Input first number
    a_input = input("Enter 1st Number: ")
    if a_input.replace('.', '', 1).isdigit():
        a = float(a_input)
    else:
        print("Invalid input. Please enter a number.")
        continue

    # Input second number
    b_input = input("Enter 2nd Number: ")
    if b_input.replace('.', '', 1).isdigit():
        b = float(b_input)
    else:
        print("Invalid input. Please enter a number.")
        continue

    # Input operator
    op = input("Enter + for Add, - for Subtract, * for Multiply, / for Divide: ")

    # Perform operation
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operator.")

    # Ask to continue or exit
    again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Exiting Calculator. Goodbye!")
        break
