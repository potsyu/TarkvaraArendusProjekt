# Ülesanne 1: Akna loomine ja kujundid
# Valisin Foor -i.

import pygame
pygame.init()

#Ekraani seaded
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("Foor - Björn Johansonm")
screen.fill ([0, 0, 0])

#Joonistamine (foori piir)
pygame.draw.rect(screen, [255, 255, 255], [100, 20, 100, 260], 2)

#Joonistamine (Punane ring)
pygame.draw.circle(screen, [255, 0, 0], [150, 70], 37 , 0)

#Joonistamine (Kollane ring)
pygame.draw.circle(screen, [255, 255, 0], [150, 150], 37 , 0)


#Joonistamine (Roheline ring)
pygame.draw.circle(screen, [0, 255, 0], [150, 230], 37 , 0)


#Ekraani värskendamine
pygame.display.flip()

#Kood, et ekraan automaatselt ei läheks kinni.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()