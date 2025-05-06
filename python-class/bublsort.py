
from random import sample
from time import time

def bubsort(lst,its):
    iters=0
    while True:
        swap=False
        for i in range(len(lst)-1):
            if lst[i]<=lst[i+1]:
                continue
            elif lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
                swap=True
                iters+=1
                print(lst)
            #if iters==its:
            #    break
        if swap==False:
            break
    print(iters)
    return lst

lst=[5,4,3,2,1]
print(lst,"\n")
start=time()
print(bubsort(lst,5))
end=time()
print(end-start)