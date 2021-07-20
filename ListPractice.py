# you can put strings, numbers, bools in lists
friends = ["Hope", "Tony", "Aspen", "Ambureen"]

print(friends)
# how can we access individual items within list? We refer to them by their index, beginning with 0.
# if we print 3 or -1, we get Ambureen
print(friends[3])
print(friends[-1])

# if I want to select last two friends
print(friends[2:])

# if I want to grab the two in the middle
print(friends[1:3])

# if I want to modify a value in the list
friends[1] = "Anthony"
print(friends)
