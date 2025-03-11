
with open('moo.in') as file:
    info=file.readline().strip().split()
    txt=file.readline()
    freq=int(info[1])


def ismoo(i,txt)->bool:
    return (txt[i]!=txt[i+1]) and (txt[i+1]==txt[i+2])

def inrange(l,i,txt,d)->bool:
    if d=='s':
        return (i+1)-l>=0
    elif d=='b':
        return (i+1)-l<=len(txt)
    return False

def isSimilar(nxt,moo)->bool:
    pairs=[]
    for i,x in enumerate(moo):
        pairs.append([moo[i],nxt[i]])
    print(pairs,"pairs")
    difs=[]
    for x in pairs:
        if x[0]!=x[1]:
            difs.append(False)
        else:
            difs.append(True)
    return difs.count(False)==1

print(txt)
moos=[]
for i,l in enumerate(txt):
    if inrange(3,i,txt,'s'): #in range lower
        print(i,"i")
        if ismoo(i,txt):
            moo=f"{txt[i]}{txt[i+1]}{txt[i+2]}"
            print(moo,"moo")
            if moo==ismoo(i-(3*freq-1),txt):
                moos.append(moo)
                print(moos,"moos")
            elif isSimilar(f"{txt[i+3]}{txt[i+4]}{txt[i+5]}",moo):
                moos.append(moo)
                print(moos,"moos")
    elif inrange((3*freq-1),i,txt,'b'): #in range upper
        print(i)
        if ismoo(i,txt):
            moo=f"{txt[i]}{txt[i+1]}{txt[i+2]}"
            print(moo,"moo")
            if ismoo(i,txt)==ismoo(i+(3*freq-1),txt):
                moos.append(moo)
                print(moos,"moos")
            elif isSimilar(f"{txt[i+3]}{txt[i+4]}{txt[i+5]}",moo):
                moos.append(moo)
                print(moos,"moos")
print(len(moos))
for x in moos:
    print(x,"answer")