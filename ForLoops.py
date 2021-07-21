# for loops will repeat code a specific number of times/iterations
# define variable to change for each iteration of loop (ex: letter)
for letter in "lol":
    print(letter)

# you can loop through lists
friends = ["Aspen", "Hope", "Tony"]
for friend in friends:
    print(friend)

# we can get the length of the list
print(len(friends))

# this will give us an index for each friend in list
for index in range(len(friends)):
    print(index)

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first iteration")

# prints out numbers not including four
#for index in range(4):
#    print(index)

# prints out a range of numbers not including 7
# for index in range(4, 7):
#    print(index)
