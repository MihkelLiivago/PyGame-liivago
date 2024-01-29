import pygame, sys

pygame.init()
#ekraan
screenX= 640
screenY= 480
screen = pygame.display.set_mode([screenX, screenY])  # defineerib akna dimensiooni
pygame.display.set_caption("Ülesanne4- Mihkel Liivago")  # akna nimi
bg = pygame.image.load("bg_rally.jpg")   #laeb taustapildi
screen.blit(bg,[0,0])   #määrab positsiooniks 0 kordinaadi
clock = pygame.time.Clock()
#auto1
auto1 = pygame.image.load("f1_blue.png")
auto1_posX, auto1_posY = 360, 390
auto1_speedY= -2
auto1_speedX= 0

#auto2
auto2 = pygame.image.load("f1_red.png")
auto2_posX, auto2_posY = 200, 240
auto2_speedY= -1.5
auto2_speedX= 0


#uto3 = pygame.image.load("f1_red.png")
#screen.blit(auto3, [300, 400])



while True: #while loop mis annab programmile sulgemis käsu ristile vajutades
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #auto1 animatsioon
    screen.blit(auto1, [auto1_posX, auto1_posY])
    auto1_posX += auto1_speedX
    auto1_posY += auto1_speedY
    auto1_skoor = 0
    if  auto1_posY < -120:
        auto1_posY = 600
        auto1_skoor += 1
        #auto1 = pygame.transform.rotate(auto1, 180)



    #auto2 animatsioon
    screen.blit(auto2, [auto2_posX, auto2_posY])
    auto2_posY += auto2_speedY
    if  auto2_posY < -120:
        auto2_posY = 600
        #auto2 = pygame.transform.rotate(auto2, 180)

    pygame.display.flip()  # värskendab kuva
    screen.blit(bg, [0, 0])
   # auto3 = pygame.image.load("f1_red.png")
   # screen.blit(auto3, [300, 400])