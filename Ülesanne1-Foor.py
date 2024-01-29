import pygame

pygame.init()

screen = pygame.display.set_mode([300, 300])  # defineerib akna dimensiooni
pygame.display.set_caption("Foor- Mihkel Liivago")  # akna nimi
screen.fill([0, 0, 0])  #Tausta värv
pygame.draw.circle(screen, [255, 0, 0], [150,60], 40, 100)      #Punane ring
pygame.draw.circle(screen, [255, 255, 0], [150,145], 40, 100)   #Kollane ring
pygame.draw.circle(screen, [0, 255, 0], [150,230], 40, 100)     #Roheline ring

pygame.draw.rect(screen, [100, 100, 100], [100, 10, 100, 270], 2)       #Hall ruut ringide ümber


pygame.display.flip()   #Värskendab kuva

while True:     #while loop millega saab programm sulgemis käsu ristile vajutades
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()