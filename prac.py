
#initialize a grid of 4x4 that contains numbers 1 - 16
grid = [[1, 2, 3, 4    ],
        [5, 6, 7, 8    ],
        [9, 10, 11, 12 ],
        [13, 14, 15, 16]]
# Accessing elements
print(grid[3][3])
# Modifying elements
grid[3][3] = 5
print(grid[3][3])
#change grid[1][1] to 
grid[1][1] = 3
print(grid[1][1])
# Iterating over rows
for x in grid:
    print(x)
# Iterating over all elements in a grid
for x in grid:
    for y in x:
        print(y, end = ' ')
    print()
#compare elements 
# compare [1][3] and [2][3] and print equal if equal and false false
if grid[1][3] == grid[2][3]:
    print("egeal")
else:
    print("false")