# catching errors in Python:
# we often encounter different errors or exceptions that stop our program for running
# we can watch out for certain errors and handle them so the program can continue running
# this is where try/except blocks come in

# try:
#    number = int(input("Enter a number: "))
#    print(number)
# except is highlighted here because it has too broad of a scope
# a good practice is to catch specific errors
# except:
#    print("Invalid input. Enter an integer.")

# we can except specific types of errors
try:
    number = int(input("Enter a number: "))
    print(number)
# you can print out error that was thrown
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input. Enter an integer.")
    