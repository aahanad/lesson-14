import pygame
import time
pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
on=pygame.image.load("C:\Aahana\Game Dev 2\lesson 4\lightbulb\on.PNG")
off=pygame.image.load("C:\Aahana\Game Dev 2\lesson 4\lightbulb\off.PNG")
while(True):
    screen.fill("white")
    screen.blit
    pygame.display.update()
    screen.blit(off,(50,70))
    pygame.display.update()
    time.sleep(3)
    screen.blit(on,(50,70))
    pygame.display.update()
    time.sleep(3)
   