import pygame
import time
pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
bg=pygame.image.load("balloons.jpg")
box=pygame.image.load("real box.png")
cake=pygame.image.load("yummy cake.png")
cake=pygame.transform.scale(cake,(200,400))
while(True):
    screen.fill("pink")
    screen.blit(bg,(0,0))
    pygame.display.update()
    time.sleep(5)
    print("time over")
    screen.blit(box,(50,70))
    pygame.display.update()
    time.sleep(2)
    print("timer finished")
    screen.blit(cake,(5,270))
    pygame.display.update()
    time.sleep(3)
    print("dinner is ready")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            #make mothers day animation