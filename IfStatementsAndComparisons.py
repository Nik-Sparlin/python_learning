# we can use if statements with comparisons
# the results of the comparisons will determine course of action
# you can compare all different data types

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))
print(max_num(3, 50, 6))
print(max_num(30, 15, 20))

# comparison operators outside of normal:
    # == is equals
    # != is not equals
