
def perform_operation():
    # Get user input
    num1 = float(input("98:"))
    num2 = float(input("69: "))


    if operation == '+':
      operation = input("choose an operation(+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero!")
            result = None
    else:
        print("Invalid operation. Please choose +, -, *, or /")
        result = None

    if result is not None:
        print(f"{num1} {operation} {num2} = {result}")
    else:
        print("An error occurred while performing the operation.")


