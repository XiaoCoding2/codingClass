import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

x = [3.50, 3.69, 3.44, 3.43, 4.34, 4.42, 2.37]
y = [18.0, 15.0, 18.0, 16.0, 15.0, 14.0, 24.0]

def draw_line(plt,x,y,w,b):
    xline=np.linspace(min(x),max(x),100)
    yline=w*xline+b

    plt.figure()
    plt.scatter(x,y,label="data")
    plt.plot(xline, yline, label= 'line, y=mx+b')
    plt.xlabel('miles')
    plt.ylabel("price")
    plt.title("data2")
    plt.legend()
    plt.show()

#x = [1,2,3,4]
#y = [1,2,3,4]

#print(xline)

w=(-10/2.05)
b=35.57

def error(w,x,b,y):
    cur_e=0
    for val in range(0,len(x)):
        cur_e+=(w*x[val]+b-y[val])**2
    return cur_e

print(error(w,x,b,y))


prev_e=error(w,x,b,y)+1
prev_e2=error(w,x,b,y)+1
direction=True #True=up,False=down
direction2=True
for z in range(10_000):
    #bias
    #find total error
    cur_e=error(w,x,b,y)
    print(cur_e,"b")
    #change based on error accordingly
    biggerError=cur_e>prev_e
    smallerError=cur_e<prev_e
    go_up=direction is True
    go_down=direction is False
    #changing
    if biggerError and go_up:
        b-=0.01
        direction=False
    elif biggerError and go_down:
        b+=0.01
        direction=True
    elif smallerError and go_up:
        b+=0.01
    elif smallerError and go_down:
        b-=0.01
    else:
        pass
    #weight
    cur_e2=error(w,x,b,y)
    print(cur_e2,"w")
    biggerError2=cur_e2>prev_e2
    smallerError2=cur_e2<prev_e2
    go_up2=direction2 is True
    go_down2=direction2 is False
    #
    if biggerError2 and go_up2:
        w-=0.01
        direction2=False
    elif biggerError2 and go_down2:
        w+=0.01
        direction2=True
    elif smallerError2 and go_up2:
        w+=0.01
    elif smallerError2 and go_down2:
        w-=0.01
    else:
        pass
    #make previous error
    prev_e=cur_e
    prev_e2=cur_e2

print(sqrt(error(w,x,b,y)))
print(error(w,x,b,y))


draw_line(plt,x,y,w,b)