# build a basic addition calculator from user input
# step one is to create your variables
num1 = input("Enter a number: ")
num2 = input("Enter a second number: ")

# result = num1 + num2 will give you a combination of the inputs
# this is because python defaults to strings for user input
# this means we need to convert

# we could use the int() function...
# result = int(num1) + int(num2) only allows you to use ints, not floats

# using float allows you to use ints and floats
result = float(num1) + float(num2)
print(result)
