
'''
add 2 binarx numbers together without converting to int
'''

def addbin(b1,b2):
    #vars
    carry=0
    bsm=''
    #for loops
    for x in range(len(b1),0,-1):
        print(x,flush=True)
        # if1
        if [b1[x],b2[x],carry]==['0','1',0]:
            bsm+='1'
        #if2
        elif [b1[x],b2[x],carry]==['1','0',0]:
            bsm+='1'
        #if3
        elif [b1[x],b2[x],carry]==['1','1',0]:
            bsm+='0'
            carry=1
        #if4
        elif [b1[x],b2[x],carry]==['0','0',1]:
            bsm+='1'
        #if5
        elif [b1[x],b2[x],carry]==['0','1',1]:
            bsm+='0'
            carry=1
        #if6
        elif [b1[x],b2[x],carry]==['1','0',1]:
            bsm+='0'
            carry=1
        #if7
        elif [b1[x],b2[x],carry]==['1','1',1]:
            bsm+='1'
            carry=1
    #return
    return bsm+str(carry)
print(addbin("111","1111"))
