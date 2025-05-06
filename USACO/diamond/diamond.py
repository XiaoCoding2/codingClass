
def Code():
    #input
    with open('diamond.in') as infile:
        lineone:list[str] = infile.readline().strip().split()
        diamonds:list[int] = list(map(int,infile.readlines()))
        #works
    #code
    for x in diamonds:
        if max(diamonds)-min(diamonds)>int(lineone[1]):
            diamonds.remove(max(diamonds))
        else:
            break
    #output
    with open('diamond.out','w') as outfile:
        outfile.write(str(len(diamonds)))
Code()
#O(2n)