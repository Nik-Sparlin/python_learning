# as noted in readingfiles.py, we can write and append files as well

# we can add an employee to the end of the list with append
# be careful with appending because you can append each time the program is run
    # employee_file = open("Employees.txt", "a")
    # employee_file.write("\nKelly - Customer Service")

# you can overwrite files and create new files
# employee_file.write("\nKelly - Customer Service") will overwrite the entire file
# to create a new file and add to it:
employee_file = open("Employees1.txt", "w")
employee_file.write("\nKelly - Customer Service")

# remember to close the file at the end
employee_file.close()

# you can create many types of files like text and HTML!
