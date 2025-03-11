
with open("shell.in", 'r') as numbers:
    #---------------------------------------creates list
    amount = numbers.readline()
    M = int(amount)
    #-
    numbers_list = []
    for x in range(M):
        line = numbers.readline().strip()
        numbers_list.append(line)
    #----------------------------------------Changes list
    new_list = [line.split() for line in numbers_list]
shells = [0, 0, 0]
swaps_g = new_list
#--------------------Simulate the swaps
scores = []
def ShellGame(stone):
    shells = [0, 0, 0]
    shells[stone] = 1
    score = 0
#----------change indexes
    swaps2 = [
        (int(x)-1, int(y)-1, int(z)-1)
        for (x, y, z) in swaps_g
        ]
#----------Perform the swap
    for (s1, s2, g) in swaps2:
        shells[s1], shells[s2] = shells[s2], shells[s1]
        if shells[g] == 1:
            score += 1
#----------Adding Score
        scores.append(score)
ShellGame(0)
ShellGame(1)
ShellGame(2)
print(max(scores))

with open("shell.out", "w") as outfile:
    outfile.write(str(max(scores)))
    ...