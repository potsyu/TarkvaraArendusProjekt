#Ülesanne 3: Tsüklid ja funksioonid.

#Initialize the screen
import pygame
pygame.init()

#Värvid
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
red = [255, 0, 0]

#Set the screen mode :)
screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine - Ülesanne 3: Tsüklid ja funksioonid. (Karl_Karulin)")
screen.fill(lGreen)

#Properties
joone_vrv = [255, 0, 0]
ruudud_hor = 0
ridade_arv = 50
ruudud_ver = 0
veergude_arv = 50

#The content :)
screen.fill(lGreen)

for i in range (ridade_arv):
  pygame.draw.line(screen, joone_vrv, [ruudud_hor, 0], [ruudud_hor, 480], 2)

  #Increase this to make the rect BIGGER
  ruudud_hor += 20

for i in range (veergude_arv):
  pygame.draw.line(screen, joone_vrv, [0, ruudud_ver], [640, ruudud_ver], 2)

  # Increase this to make the rect BIGGER
  ruudud_ver += 20

pygame.display.flip()
#Alumine osa ei lase Pygame ekraanil ise kinni minna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()
