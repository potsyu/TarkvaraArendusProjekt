import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([1280,720])
pygame.display.set_caption("Ülesanne 2 - Lisaylesanded")
screen.fill([204, 255, 204])

#Background
bg = pygame.image.load("Pilt\VIKK.jpg")
screen.blit(bg,[0,0])


pygame.display.flip()








#Alumine osa ei lase Pygame ekraanil ise kinni minna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()