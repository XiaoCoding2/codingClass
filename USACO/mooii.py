
from sys import stdout as t

N=int(input())
nums=list(map(int, input().split()))

#N=6
#nums=[1,2,2,3,2,2]

freq={}
count=0
for i in range(N):
    if i+1>=N:
        freq[nums[i]]=count
        break
    count+=1
    if nums[i]!=nums[i+1]:
        freq[nums[i]]=count
        count=0
    else:
        count+=1

lfreq=len(freq)
freq2=list(freq.values())
moos=0
for x in freq:
    if x>=2:
        moos+=lfreq-1

t.write(str(moos))
