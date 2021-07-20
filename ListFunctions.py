
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Dwight", "Pam", "Jim", "Oscar", "Toby"]

# list functions
# print returns list values
print(friends)

# extend lets you take a list and append another list to the end
# friends.extend(lucky_numbers)

# append allows you to add an element to the end of a list
friends.append("Michael")
print(friends)

# insert allows you to specify where you want to add an item
friends.insert(1, "Angela")
print(friends)

# remove allows you to remove an element
friends.remove("Angela")
print(friends)

# you can clear out the list with clear
# friends.clear()

# pop removes the last value from the list
#friends.pop()

# you can check if an element is within a list with index
# it will return the index where Pam is located
print(friends.index("Pam"))
# it will also tell you if a name is not within the list with an error

# you can count the number of similar elements within a list with count
print(friends.count("Jim"))

# sort allows you to sort a list in ascending order
friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

# reverse will reverse the list values
friends.reverse()
print(friends)

lucky_numbers.reverse()
print(lucky_numbers)

# copy function does as it  says on the box  with the same attributes as copied list
friends2 = friends.copy()
print(friends2)