# there are times when we want functions to give information back to us
# this is what the return keyword allows us to do
# note that you cannot put code after the return statement

def cube(num):
    return num*num*num

print(cube(3))

result = cube(4)
print(result)
