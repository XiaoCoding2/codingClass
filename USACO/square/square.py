
#square pasture
with open('square.in') as f:
    sq1:list[int]=list(map(int,f.readline().strip().split()))
    sq2:list[int]=list(map(int,f.readline().strip().split()))
xarea:int=(sq1[-1]-sq2[0])**2
yarea:int=(sq1[0]-sq2[-1])**2
with open('square.out','w') as outfile:
    outfile.write(str(max([xarea,yarea])))