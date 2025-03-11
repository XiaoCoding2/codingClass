
grid = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

def are_all_items_same(items):
    for x in range(0, len(items)):
        if items[x] != items[0]:
            return(False)
    return(True)
print(are_all_items_same(grid))

#diag1
def compare():
    list = []
    for x in range(0, len(grid)):                                  
        list.append(grid[x][x])
    print(are_all_items_same(list))
compare()

#diag2
def compare2():
    list = []
    for x in range(0, len(grid)):                                  
        list.append(grid[x][-(x+1)])
    print(are_all_items_same(list))
compare2()

#colums
def compare3():
    list = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid)):                                  
            list.append(grid[x][y])
        print(are_all_items_same(list), end = ' ')
        list.clear()
    print()
compare3()

#rows
def compare4():
    list = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid)):                                  
            list.append(grid[y][x])
        print(are_all_items_same(list), end = ' ')
        list.clear()
    print()
compare4()