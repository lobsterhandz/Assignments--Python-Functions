# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.
# Task 1: Create functions for each arithmetic operation.
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y
# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
input_operation = input("What operation do you want to perform? (add, subtract, multiply, divide): ")
input_num1 = float(input("Enter the first number: "))
input_num2 = float(input("Enter the second number: "))
# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
try:
    if input_operation == "add":
        result = add(input_num1, input_num2)
    elif input_operation == "subtract":
        result = subtract(input_num1, input_num2)
    elif input_operation == "multiply":
        result = multiply(input_num1, input_num2)
    elif input_operation == "divide":
        result = divide(input_num1, input_num2)
    else:
        print("Invalid operation.")
        result = None
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    result = None
    print("Result:", result)
    