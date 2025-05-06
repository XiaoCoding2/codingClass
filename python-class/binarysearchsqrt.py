
def mySqrt(x: int) -> int|float:
    x=x*1_000_000
    if x==1:return 1
    low=0
    high=x
    while(low+1<high):
        mid=(low+high)//2
        mid_t=mid**2
        if mid_t>x:
            high=mid
        elif mid_t<x:
            low=mid
        else:
            return mid
    return low*0.001

print(mySqrt(50))