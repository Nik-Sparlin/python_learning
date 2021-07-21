# we will build an exponent function to take a number and raise it to a certain power
# we can do this with print function
print(2**3)

# we can also do this with a for loop inside of our function
def raise_to_power(base_num, power_num):
    result = 1
    # loops through power_num of times (but not including power_num)
    for i in range(power_num):
        # each time we multiply by base_num
        result = result * base_num
    return result

print(raise_to_power(3, 4))