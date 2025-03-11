
lst=[1,2]
num=128
def alg(num,lst):
    for x in range(len(lst)):
        if lst[x]==num:
            print(x)
            return
        elif lst[x]>num:
            print("Not in list")
            return
    lst.append(lst[-1]*2)
    alg(num,lst)
#alg(num,lst)
