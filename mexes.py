
N=int(input())
Arr=list(map(int,input().split()))

Arr.sort()

def Mex(lst,n)->int:
    #Find mex
    s=min(lst)
    if s>0:
        return 0
    else:
        for i in range(n+1):
            if i not in lst:
                return i
    return lst[-1]+1

M=Mex(Arr,N)
Narr=Arr.copy()
ops=0
#
for x in range(N+1):
    if x==M:
        print(0)
    else:
        ...