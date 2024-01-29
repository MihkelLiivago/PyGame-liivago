import pygame
pygame.init()

screen = pygame.display.set_mode([640, 480])  # defineerib akna dimensiooni
pygame.display.set_caption("2")  # akna nimi

#taust
bg = pygame.image.load("bg_shop.jpg")   #laeb taustapildi
screen.blit(bg,[0,0])   #määrab positsiooniks 0 kordinaadi

#poemüüja
seller = pygame.image.load("seller.png")    #laeb poemüüja pildi
seller = pygame.transform.scale(seller, [250, 300])     #muudab pildi mõõtmeid
screen.blit(seller,[105,160])   #määrab pildi positsiooni

#jutumull
chat = pygame.image.load("chat.png")    #laeb jutumulli pildi
chat = pygame.transform.scale(chat, [255, 205])     #muudab pildi mõõtmeid
screen.blit(chat, [245, 65])    #määrab pildi positsiooni

#tekst

font =pygame.font.Font(pygame.font.match_font('comic sans'), 19)    # Valib fondi ja fodi suuruse
text = font.render("Tere, olen Mihkel Liivago", True, [255,255,255])    #Kuvab teksti, valib värvi
screen.blit(text, [260,140])    #määrab positsiooni


pygame.display.flip()   #värskendab kuva

while True: #while loop mis annab programmile sulgemis käsu ristile vajutades
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
