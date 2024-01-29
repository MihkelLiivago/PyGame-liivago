import pygame

pygame.init()

screen = pygame.display.set_mode([300, 300])  # defineerib akna dimensiooni
pygame.display.set_caption("Lumemees- Mihkel Liivago")  # akna nimi
screen.fill([0, 0, 0])  #Tausta värv
pygame.draw.circle(screen, [255, 255, 255], [150,70], 30, 100)  #Ülemine pall
pygame.draw.circle(screen, [255, 255, 255], [150,135], 40, 100) #Keskmine pall
pygame.draw.circle(screen, [255, 255, 255], [150,220], 50, 100) #Alumine pall

pygame.draw.polygon(screen, [255, 0, 0], [[145, 75], [155, 75], [150,90]], 0)   #Nina

pygame.draw.circle(screen, [0, 0, 0], [140, 65], 5, 0)  #vasak silm
pygame.draw.circle(screen, [0, 0, 0], [160, 65], 5, 0)  #parem silm
pygame.display.flip()   #värskendab kuva

while True: #while loop mis annab programmile sulgemis käsu ristile vajutades
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
