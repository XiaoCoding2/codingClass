
#christmas tree
'''
infile:
num test case
{
num branch, base, height
heights of branches

}*num test case
'''
from termcolor import colored as cr

#input
print(cr("input",'yellow'))
with open('xmas.in') as infile:
    numcases:int=int(infile.readline())
    def info() -> list[int]:
        return list(map(int,infile.readline().strip().split()))
    def heights() -> list[int]:
        return list(map(int,infile.readline().strip().split()))
    print("No problems")
    #code
    areas=[]
    def code():
        global areas
        print(cr("code",'yellow'))
        info_list:list[int]=info()
        heights_list:list[int]=heights()
        num_b:int=info_list[0]
        base:int=info_list[1]
        h:int=info_list[2]
        area1:float=(base*h)/2
        print(area1,"area1")
        print(info_list,"info list")
        print(heights_list,"heights list")
        h_idx:range=range(len(heights_list))
        total_a:float=0
        #
        for i in h_idx:
            if i < len(heights_list)-1:
                h_dif:int=(heights_list[i+1]-heights_list[i])
                print(h_dif)
                if h_dif<h:
                    base2=(((h-h_dif)*(base/2))/h)*2
                    print(base2,"Base2")
                    area2:float=((base+base2)/2)*(h_dif)
                    print(h-h_dif)
                    print(area2,"+area2")
                    total_a+=area2
                else: #if h_dif>=h
                    print(area1,"+area1")
                    total_a+=area1
            else:
                print(area1,"+area1")
                total_a+=area1
        if int(total_a)==total_a:
            print(int(total_a),"total area")
            areas.append(int(total_a))
        else:
            print(total_a)
            areas.append(total_a)
    for x in range(numcases):
        code()
    print(areas,"Final ans")
