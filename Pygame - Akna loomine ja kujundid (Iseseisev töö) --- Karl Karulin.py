# Pygame - Akna loomine ja kujundid (Iseseisev töö)

#Importitakse pygame
import pygame

#Alustatakse Pygame.
pygame.init()

#Ekraani seaded
screen = pygame.display.set_mode([640,480])

#Akna nimi
pygame.display.set_caption("My Screen")

#Erinevad värvid RGB formaadis.
punane = (255,0,0)
roheline = (0,255,0)
sinine = (0,0,255)
valge = (255,255,255)
must = (0,0,0)

#Täidab ekraani valitud RGB värviga.

screen.fill([204, 255, 255])

#Pygame'iga saab veel erinevaid objekte ekraanile lisada.

#List objektidest:
"""
joon (line)
ristkülik (rect)
ring (circle)
hulknurk (polygon)
ovaal (ellipse)
kaar (arc)
"""

#Erinevate objektide katsetused.

#Joon (line)


#Joonistab ekraanile joone kasutades värvi, mis on antud ning joone punktide x ning y koordinaate.
pygame.draw.line(screen, [255,0,0], [100,100], [200,200], 2)

#Joonistab ekraanile ristküliku.
pygame.draw.rect(screen, [0, 225, 0], [50, 80, 200, 300], 2)

#Joonistab ekraanile ringi.
pygame.draw.circle(screen, [0, 0, 255], [150,200], 100, 1)

#Joonistab ekraanile hulknurga.
pygame.draw.polygon(screen, [255, 0, 255], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2)

#Joonistab ekraanile ovaali.
pygame.draw.ellipse(screen, [0, 225, 0], [50, 80, 200, 300], 2)

#Joonistab ekraanile kaare.
pygame.draw.arc(screen,[0,0,0], [100,100,250,200], 0, 3.14*1.5, 1)

#Ekraani värskendus.
pygame.display.flip()

#My code :)
#Alumine osa ei lase Pygame ekraanil suvakalt kinni minna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()