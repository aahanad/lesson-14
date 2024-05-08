import pygame
import time
pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
bg=pygame.image.load("mothers day\scroll.png")
flower=pygame.image.load("mothers day\Flower.png")
sign=pygame.image.load("mothers day\sign.png")
bg=pygame.transform.scale(bg,(550,550))
flower=pygame.transform.scale(flower,(150,150))
sign=pygame.transform.scale(sign,(590,100))
font=pygame.font.SysFont("brannboll script",25)
while(True):
    screen.fill("light blue")
    screen.blit(bg,(0,0))
    pygame.display.update()
    time.sleep(5)
    text1=font.render("You are the best mom",True,"black")
    text2=font.render("I could ever wish for!",True,"black")
    screen.blit(text1,(200,250))
    screen.blit(text2,(200,270))
    pygame.display.update()
    time.sleep(1)
    print("happy mother's day!")
    print("time over")
    screen.blit(flower,(50,70))
    pygame.display.update()
    time.sleep(2)
    print("timer finished")
    screen.blit(sign,(5,400))
    pygame.display.update()
    time.sleep(3)
    print("dinner is ready")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        