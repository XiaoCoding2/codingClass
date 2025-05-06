grid = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

def are_all_items_same(items):
    for x in range(len(items)):
        if items[x] != items[0]:
            return False
    return True

def check(grid):
    list = []
    #diag1
    list = [grid[x][x] for x in range(0, len(grid))]
    if are_all_items_same(list) and list[0] != '-':
        return True
    list.clear()
    #diag2
    for x in range(0, len(grid)):                                  
        list.append(grid[x][-(x+1)])
    if are_all_items_same(list) and list[0] != '-':
        return True
    list.clear()
    #colums
    for y in range(0, len(grid)):
        for x in range(0, len(grid)):                                  
            list.append(grid[x][y])
        if are_all_items_same(list) and list[0] != '-':
            return True
    list.clear()
    #rows
    for y in range(0, len(grid)):
        for x in range(0, len(grid)):                                  
            list.append(grid[y][x])
        if are_all_items_same(list) and list[0] != '-':
            return True
    list.clear()

    return False

def check_draw(grid):
    draw = True
    for x in grid:
        for y in x:
            if y == '-':
                return draw
            return False

#play
def play():
    def board():
        for x in grid:
            print('|'.join(x))

    def move_x():
        user = input("where do you want x?: ")
        locate = user.split(",")
        l1 = int(locate[0])
        l2 = int(locate[1])
        if l1 or l2 > 2:
            print("Out of range")
            move_x()
        elif grid[l1][l2] == '-':
            grid[l1][l2] = 'x'
        else:
            print("choose anouther")
            move_x()

    def move_o():
        user = input("where do you want o?: ")
        locate = user.split(",")
        l1 = int(locate[0])
        l2 = int(locate[1])
        if grid[l1][l2] == '-':
            grid[l1][l2] = 'o'
        else:
            print("choose anouther")
            move_o()

    for x in range(0, 5):
        board()
        move_x()
        if check(grid) == True:
            print("yay")
            break
        if check_draw(grid):
            break
        board()
        move_o()
        if check(grid) == True:
            print("yay")
            break
        if check_draw(grid):
            break
play()
