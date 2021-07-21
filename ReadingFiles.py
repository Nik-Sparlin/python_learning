# we often want to read from files outside of our Python file
# we can use the Python read command to do this and parse through files

# first we need to open file within Python
# variable = open("filename.ext", "mode")
# modes:
# "r" = read => allows you to view contents of a file
# "w" = write => allows you to modify the contents of a file
# "a" = append => allows you to add new information to the end of a file
# "r+" = read/write => allows you to read and edit file

employee_file = open("Employees.txt", "r")
# you can also use for loops
for employee in employee_file.readlines():
    print(employee)

# we can check to make sure a file is readable ; it will return a boolean
print(employee_file.readable())

# functions we can perform on files:
    # print(employee_file.read()) to read the full file
    # print(employee_file.readline()) to read singular lines in file (if you repeat this, it will give you another line)
    # print(employee_file.readlines()) puts lines into a list
        # print(employee_file.readlines()[1]) will return line in that index


# we always want to close the file when we are finished
employee_file.close()
