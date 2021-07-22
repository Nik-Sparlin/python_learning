# help make your programs more organized and powerful
# we work with a lot of different kinds of data and data structures
# but not all data can be represented with strings, numbers, or booleans (like a person, phone, or computer)
# with classes and objects, we can create our own data types with classes (overview/template of the data type)!

# to create a class, we need to create another file
# then we do class (class name): [indent] attributes
#class Student:
    # we use this initialize function to map out student attributes
#    def __init__(self, name, major, gpa, is_on_probation):
        # now we assign some values
#        self.name = name
#        self.major = major
#        self.gpa = gpa
#        self.is_on_probation = is_on_probation

# now we can call on the student.py class we created to make a student (object)
# we first need to import the Student class from the other file

from student import Student

student1 = Student("Jim", "Business Administration", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.name)
print(student2.gpa)
