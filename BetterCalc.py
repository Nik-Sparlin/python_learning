# Add, subtract, multiply, and divide
# allow user to choose which function to perform

# get input from the user
num1 = float(input("Enter first number: "))
op = input("Enter operation: ")
num2 = float(input("Enter second number: "))

# figure out op
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operation")
