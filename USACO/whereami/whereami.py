
#tests
t1="ABC"
l1=3
''
t2="ABCAB"
l2=5
''
t3="ABABCABAB"
l3=9
''
t4="ABCDABC"
l4=7
''
t5="ABCABCDABCABC"
l5=13

t6="XYZABCABC"
l6=9

#code

def wai(Case:str,Len:int):
    for i,x in enumerate(Case):
        ss=Case[:i+1]
        print(ss)
        ns=""
        for y in range(i+1,Len):
            ns+=Case[y]
        if ss not in ns:
            print(i+1)
            break

wai(t6,len(t6))

#print((5-len(set("AAAAA"))+1))