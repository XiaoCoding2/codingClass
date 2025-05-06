#Top

# USACO Problem
# https://usaco.org/index.php?page=viewproblem2&cpid=568

#NOTE------------------- Adding 'speed.in' to a list --------------------NOTE
f = open("speed.in")
numbers1 = f.readlines()
f.close()
M, N = int(numbers1[0].strip().split()[0]), int(numbers1[0].strip().split()[1])
#
proper_speeds, Cow_speeds = [], []
with open('speed.in', 'r') as infile:
    infile.readline()
    #
    for x in range(0, N+M):
#---------- Adding each line as a list of integers
        line = [int(x) for x in infile.readline().strip().split()]
#---------- Adding proper road length and speed to one list and Cow length and speed to other list
        if x < M: proper_speeds.append(line)
        else: Cow_speeds.append(line)
#print(f"{proper_speeds}- -{Cow_speeds}\n{M}, {N}")

#NOTE-------------------- Main Code --------------------NOTE
def speeding_ticket():
    diffs = []
    for x in range(0,M):
        if(proper_speeds[x][0] == Cow_speeds[x][0]):
            diffs.append(-(proper_speeds[x][1]-Cow_speeds[x][1]))
        elif(proper_speeds[x][0] > Cow_speeds[x][0]):
            diffs.append(-(proper_speeds[x][1]-Cow_speeds[x][1]))
            diffs.append(-(proper_speeds[x][1]-Cow_speeds[x+1][1]))
        else:
            diffs.append(-(proper_speeds[x][1]-Cow_speeds[x][1]))
    with open('speed.out','w') as outfile:
        outfile.write(str(max(diffs)))
speeding_ticket()