

#largest distance of two dots out of many on a grid

f=open('distance.in')
#
amount=int(f.readline().strip())
#
dots_x=f.readline().strip().split()
#
dots_y=f.readline().strip().split()
#
dots_x_y=[
    [int(dots_x[num]),int(dots_y[num])]
    for num in range(amount)
    ]
#

#solution(dots_x,dots_y,amount)

def difference(lst:list,num:int,nxt:int,idx:int):
    return (lst[num][idx]-lst[nxt][idx])
#

def solution(dots_x_y,amount):
    #dots_x_y=[[321, 404], [-15, 373], [-525, 990]]
    import termcolor as tcr
    #
    xdif,ydif=0,0
    ans=0
    #
    for num in range(amount):
        for nxt in range(num+1,amount):
            if num<(amount-1):
                #
                xdif+=difference(dots_x_y,num,nxt,0)
                #
                ydif+=difference(dots_x_y,num,nxt,1)
                #
            distance=xdif**2+ydif**2
            if distance>ans:
                ans=0
                ans+=distance
            xdif,ydif=0,0
            #
    return ans
#

if __name__=='__main__':
    with open("distance.out","w") as outfile:
        outfile.write(str(solution(dots_x_y,amount)))

    print("done",flush=True)



#largest distance of two dots out of many on a grid
'''
f=open('distance.in')
#
amount=int(f.readline().strip())
#
dots_x=f.readline().strip().split()
#
dots_y=f.readline().strip().split()
#
f.close()
#
dots_x_y=[
    [int(dots_x[num]),int(dots_y[num])]
    for num in range(amount)
    ]
#

#solution(dots_x,dots_y,amount)

class largestDistance:
        
    def __init__(self,dots_x_y:list[list[int]],amount:int) -> None:
        self.dots_x_y=dots_x_y
        self.amount=amount
    #

    def difference2(self,lst:list[list[int]], num:int, nxt:int, idx:int) -> int:
        return (lst[num][idx]-lst[nxt][idx])
    #

    def in_range(self,num:int, length:int) -> bool:
        return num<(length-1)
    #

    def is_bigger(self,new:int,old:int) -> bool:
        return new>old
    #

    def solution2(self,dots_x_y:list[list[int]],amount:int) -> int:
        #
        ans=0
        #
        idx_lst:range=range(amount)
        #
        for num in idx_lst:
            for nxt in range(num+1,amount):
                if self.in_range(num,amount):
                    #
                    xdif=self.difference2(dots_x_y,num,nxt,0)
                    #
                    ydif=self.difference2(dots_x_y,num,nxt,1)
                    #
                distance=xdif**2+ydif**2
                if self.is_bigger(distance,ans):
                    ans=distance
                #
        return ans
    #

    def run_code(self) -> None:
        with open("distance.out","w") as outfile:
            outfile.write(str(self.solution2(self.dots_x_y,self.amount)))
        #
        print("done",flush=True)
    #

code=largestDistance(dots_x_y,amount)
if __name__=='__main__':
    code.run_code()
'''