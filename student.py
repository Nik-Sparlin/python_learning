# to create a class, we need to create another file => the file we are currently in
# then we do class (class name): [indent] attributes

class Student:
    # we use this initialize function to map out student attributes
    def __init__(self, name, major, gpa, is_on_probation):
        # now we assign some values
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# values on bottom are being passed through init function
# when we create a student, we are calling on init function
# self.name = name means that the objects name is equal to what we define
# we have to do this for each parameter in order to differentiate them from one another
# self refers to the actual objects that we create from this class!

# we can also create functions within classes

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
