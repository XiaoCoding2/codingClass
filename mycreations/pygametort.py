#
import pygame as pyg
#
pyg.init()
#
screen=pyg.display.set_mode((800,600))
#
pyg.display.set_caption("Space Invaders")
icon=pyg.image.load('ufo.png')
pyg.display.set_icon(icon)
#
running=True
while running:
    for event in pyg.event.get():
        if event.type==pyg.QUIT:
            running=False
    #
    screen.fill((25,25,25))
    pyg.display.update()