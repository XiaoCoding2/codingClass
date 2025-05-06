
import pygame as pyg
from random import randint
pyg.init()
screen = pyg.display.set_mode((800,600))

clock = pyg.time.Clock()

#Store positions
bullets=[]
enemies=[]
last_shot_time = 0


running = True
while running:
    #Types of enemies
    norm ={"rect": pyg.Rect(780, 295, 15, 15), "health": 3, "type": "norm"}
    big  ={"rect": pyg.Rect(780, 295, 20, 20), "health": 6, "type": "big"}
    giant={"rect": pyg.Rect(780, 295, 25, 25), "health": 9, "type": "giant"}
    #Events
    for event in pyg.event.get():
        #Quit
        if event.type == pyg.QUIT:
            running = False
        #spawn enemy
        if event.type == pyg.KEYDOWN:
            if event.key==pyg.K_1:
                enemies.append(norm)
            if event.key==pyg.K_2:
                enemies.append(big)
            if event.key==pyg.K_3:
                enemies.append(giant)
    screen.fill((25,25,25))
    #--Draw parts of Game--                #X,Y,L,H
    #House
    house = pyg.draw.rect(screen,(255,0,0),(0,50,100,500))\
    #guns (bottom,mid,top)
    gun1 =pyg.draw.rect(screen, (0,0,195), (100,200,40,15))
    gun2 =pyg.draw.rect(screen, (0,0,225), (100,295,40,15))
    gun3 =pyg.draw.rect(screen, (0,0,255), (100,390,40,15))
    #--Moving Parts--
    #Spawn enemies
#    if len(enemies)==0:
#        for x in range(randint(1,3)):
#            pyg.Rect(780,295,15,15)
#            enemies.append(norm)
    #Move and draw Enemies
    for enemy in enemies:
        enemy["rect"].x-=1
        color = (0, 255, 0)
        if enemy["type"] == "big":
            color = (0, 205, 0)
        elif enemy["type"] == "giant":
            color = (0, 155, 0)
        pyg.draw.rect(screen, color, enemy["rect"])
    #check is enemy ahead
    line=pyg.Rect(140,295,660,1)
    DetectsEnemy= any(line.colliderect(enemy['rect']) for enemy in enemies)
    #Bullets
    curTime = pyg.time.get_ticks()
    if DetectsEnemy and curTime - last_shot_time > 500: #if Time between bullets>500
        bullets.append(pyg.Rect(140, 300, 5, 5)) #Put new bullet in list
        last_shot_time = curTime #reset ime before last shot
    for bullet in bullets: #Loop through list of bullets
        bullet.x += 3 #Move each one separetly
        pyg.draw.rect(screen, (255, 255, 255), bullet) #Draw the Bullet on screen
        if bullet.x > 800: #if bullet is out of screen
            bullets.remove(bullet) #remove bullet
        #--hitting--
        for enemy in enemies:
            #if hit
            if bullet.colliderect(enemy["rect"]):
                bullets.remove(bullet)
                enemy["health"] -= 1
                if enemy["health"] == 0:
                    enemies.remove(enemy)
                break
    #--Update screen--
    pyg.display.update()
    clock.tick(60)