
grid = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

def board():
    for x in grid:
        print('|'.join(x))

def move_x():
    user = input("where do you want x?: ")
    locate = user.split(",")
    l1 = int(locate[0])
    l2 = int(locate[1])
    if grid[l1][l2] == '-':
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

for x in range(0, 4):
    board()
    move_x()
    board()
    move_o()