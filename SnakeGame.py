
from tkinter import *
from random import randint
from time import sleep

root=Tk()

canvas=Canvas(root,width=800,height=600,bg="white")
canvas.pack()

#goal starting coords
g_a=360
g_b=360
player=canvas.create_rectangle(0,0,20,20,fill="blue")
goal=canvas.create_rectangle(g_a,g_b,g_a+20,g_b+20,fill="red")

right=0
down=0
while True:
    key = canvas.get_last_key_press()
    if key == 'ArrowLeft':
        right=-20
        down=0
    if key == 'ArrowRight':
        right=20
        down=0
    if key == 'ArrowUp':
        down=-20
        right=0
    if key == 'ArrowDown':
        down=20
        right=0
    canvas.move(player,right,down)
    #end game if out of bounds
    player_left=canvas.get_left_x(player)
    player_right=canvas.get_left_x(player)+20
    player_top=canvas.get_top_y(player)
    player_bottom=canvas.get_top_y(player)+20

    if player_top<0:
        print(0)
        break
    if player_left<0:
        print(0)
        break
    if player_bottom>600:
        print(0)
        break
    if player_right>800:
        print(0)
        break
    #get goal=win

    def rand_mult_20():
        while True:
            num=randint(0, 380)
            if num%20==0:
                return num
    if len(canvas.find_overlapping(g_a,g_b,g_a+20,g_b+20))>1:
        print(1)
        canvas.delete(goal)
        g_a=rand_mult_20()
        g_b=rand_mult_20()
        goal=canvas.create_rectangle(g_a,g_b,
                                g_a+20,g_b+20,fill="red")

    sleep(0.2)
        
root.mainloop()