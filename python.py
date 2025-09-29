def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator():
    operators = ['+', '-', '*', '/']
    while True:
        op = input("Enter + for Add, - for Subtract, * for Multiply, / for Divide: ")
        if op in operators:
            return op
        print("Invalid operator. Try again.")

def perform_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b

def main():
    print("=== Welcome to Smart Calculator ===")
    while True:
        a = get_number("Enter 1st Number: ")
        b = get_number("Enter 2nd Number: ")
        op = get_operator()
        
        result = perform_operation(a, b, op)
        print("Result:", result)

        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Exiting Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
