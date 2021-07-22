# class functions are functions that can be used by objects within the class or to modify class objects

from student import Student

student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyllis", "Business Administration", 3.8, False)

print(student1.on_honor_roll())
print(student2.on_honor_roll())
