#Foor ;)
#Made a few updates based on Ülesanne 1_lisaülesanded :)
#Modified by Karl Karulin

import pygame

#Ekraani seaded
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("Foor - #INSERT NAME HERE#")
screen.fill ([0, 0, 0])

#Valgusfoori tulekesed :)))

#Punane
pygame.draw.circle(screen, [255, 0, 0], [150, 32], 17, 0)
#Kollane
pygame.draw.circle(screen, [255, 255, 0], [150, 69], 17, 0)
#Roheline
pygame.draw.circle(screen, [0, 255, 0], [150, 107], 17, 0)

#Foori piir (ristküliku alumine on kõrgusest (0) -st 129 pikslit)
pygame.draw.rect(screen, [32, 32, 32], [120, 10, 58, 120], 2)

#Foori post
pygame.draw.polygon(screen, [64, 64, 64], [[155,129],[146, 129],[145, 260],[155, 260]], 0)

#Foori alus
pygame.draw.polygon(screen, [255, 255, 255], [[156, 260], [145, 260], [111, 300], [190, 300]], 0)

#Foori aluse vörvid (THIS TOOK SOOO MUCH TIMEEE)
#Sinine
pygame.draw.polygon(screen, [0, 0, 255], [[156, 260], [145, 260],[134, 273], [168, 274]], 0)
#Must
pygame.draw.polygon(screen, [0, 0, 0], [[134, 273], [168, 274],[181, 289],[121, 288]  ], 0)
#Valge riba
pygame.draw.polygon(screen, [64, 64, 64], [[156, 260], [145, 260], [111, 300], [190, 300]], 3)

#Ekraani värskendamine
pygame.display.flip()


#Alumine osa ei lase Pygame ekraanil ise kinni minna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()
