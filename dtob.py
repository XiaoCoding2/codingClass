
def dtob_(Num):
    bn=''
    zs='0'
    if Num%2==0:
        zs*=int(Num**0.5)
        bn+='1'
        bn+=zs
    return bn
#print(dtob_(2))
'''
0 0
1 1
2 10
3 11
4 100
5 101
6 110
7 111
8 1000
9 1001
10 1010
11 1011
12 1100
13 1101
14 1110
15 1111
'''

import time
def dtob(Num):
    if Num==0: return 0
    #
    neg=False
    if Num<0:
        neg+=True
        Num=abs(Num)
    #
    binary=''
    while(Num>0):
        binary=str(Num%2)+binary
        print(binary,flush=True,end=' ')
        time.sleep(1)
        Num=int(Num/2)
        print(Num,flush=True)
        time.sleep(1)
    if neg==True: binary='-'+binary
    return binary
print(dtob(9988214))
