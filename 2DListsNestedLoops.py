# 2D lists: lists inside of lists, or a grid

num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# we can access specific numbers based on position in grid [row index][column index]
# remember to use zero-indexing
print(num_grid[0][0])
print(num_grid[2][1])

# we can also nest for loops within for loops
# we will use it to print out our entire grid
for row in num_grid:
    for column in row:
        print(column)
        