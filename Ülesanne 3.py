import pygame

pygame.init()

# värvid
lGreen = [153, 255, 153]  # tausta värv

# ekraani seaded
screen = pygame.display.set_mode([640, 480])  # defineerib akna dimensiooni
pygame.display.set_caption("Ülesanne3- Mihkel Liivago")  # akna nimi
screen.fill(lGreen)  # täidab tausta värviga


# funktsioon, kus parameetrite abiga saab muuta ruudu suurust, ridade ja veergude arvu, jooni värvi
def joonista(ruut, rida, veerg, värv):
    for i in range(rida):   #Ridade kordamis loop
        for j in range(veerg):  #Veergude kordamis loop
            pygame.draw.rect(screen, värv, pygame.Rect(j * ruut, i * ruut, ruut, ruut), 1)  #Joonistab ekraanile valitud värviga ruudud


while True:  # while loop mis annab programmile sulgemis käsu ristile vajutades
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()

    joonista(10, 100, 100, [255, 0, 0])
