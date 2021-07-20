# functions are collections of code that perform specific tasks
# we can call on functions when we need them
# we can also create functions

# this new function will greet the user
# we use def to let Python know we are creating a new function
def say_hello(name):
    # this is where we define the function
    # note that you can include multiple parameters in function
    print("Hello " + name)

# we then call the function to perform what we want it to do
say_hello("Nik")

say_hello("Dill")

# note that Python executes functions from top to bottom
# we can make functions more powerful with parameters
# it is a good idea to break your code down into different functions
