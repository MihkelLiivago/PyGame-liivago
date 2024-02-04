import pygame, sys

pygame.init()
#ekraan
screenX= 640
screenY= 480
screen = pygame.display.set_mode([screenX, screenY])  # defineerib akna dimensiooni
pygame.display.set_caption("Ülesanne4- Mihkel Liivago")  # akna nimi
bg = pygame.image.load("bg_rally.jpg")   #laeb taustapildi
screen.blit(bg,[0,0])   #määrab positsiooniks 0 kordinaadi
clock = pygame.time.Clock()     #fps
font =pygame.font.Font(pygame.font.match_font('comic sans'), 18)    # Valib skoori fondi ja fondi suuruse
#auto1
auto1 = pygame.image.load("f1_blue.png")    #Laeb sinise auto pildi
auto1_posX, auto1_posY = 360, 390           #Defineerib alguse positsiooni
auto1_speedY= -2.5                          #Defineerib auto liikumis kiiruse Y teljel
auto1_speedX= 0                             #Defineerib auto liikumis kiiruse X teljel
auto1_skoor = 0                             #Skoor

#auto2
auto2 = pygame.image.load("f1_red.png")     #Laeb punase auto pildi
auto2_posX, auto2_posY = 200, 240           #Defineerib alguse positsiooni
auto2_speedY= -2                            #Defineerib auto liikumis kiiruse Y teljel
auto2_speedX= 0                             #Defineerib auto liikumis kiiruse X teljel


#auto3 = pygame.image.load("f1_red.png")
#screen.blit(auto3, [300, 400])

while True: #while loop mis annab programmile sulgemis käsu ristile vajutades
    clock.tick(60) #fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #auto1 animatsioon (On loopis sees kuna nii värskendatakse animatsiooni vastavalt)
    screen.blit(auto1, [auto1_posX, auto1_posY])    #Paneb sinise auto ekraanile
    auto1_posX += auto1_speedX      #Auto positsiooni animeeritakse vastavalt eelpool väljatoodud kiiruse muutuja järgi
    auto1_posY += auto1_speedY
    if  auto1_posY < -120:          #Kui auto jõuab kaadrist välja siis liigutatakse ta tagasi kaadri alla ja lisatakse skoorile +1
        auto1_posY = 600
        auto1_skoor += 1
        #auto1 = pygame.transform.rotate(auto1, 180)

    text = font.render(f"Score: {auto1_skoor}", True, [255, 255, 255])  # Tekst sinise auto skooriga
    screen.blit(text, [520, 30])    #Paneb skoori ekraanile

    #auto2 animatsioon
    screen.blit(auto2, [auto2_posX, auto2_posY])    #Paneb punase auto ekraanile
    auto2_posY += auto2_speedY      #Auto positsiooni animeeritakse vastavalt eelpool väljatoodud kiiruse muutuja järgi
    if  auto2_posY < -120:          #Kui auto väljub kaadrist siis liigutatakse ta tagasi kaadri alla
        auto2_posY = 600


    pygame.display.flip()  # värskendab kuva
    screen.blit(bg, [0, 0]) #Kuvab tausta
   # auto3 = pygame.image.load("f1_red.png")
   # screen.blit(auto3, [300, 400])