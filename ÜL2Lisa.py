import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([1280,720])
pygame.display.set_caption("Ülesanne2Lisa")
screen.fill([204, 255, 204])

#taustakas
bg = pygame.image.load("Pilt/VIKK.jpg")
screen.blit(bg,[0,0])

#Lisame logo
logo = pygame.image.load("Pilt/VIKK logo.png")
screen.blit(logo,[50,20])

#lisame mõõga
mõõk = pygame.image.load("Pilt/Mõõk.png")
mõõk = pygame.transform.scale(mõõk, [641, 761])
screen.blit(mõõk,[500,50])

#lisame koogi
cake = pygame.image.load("Pilt/cake.png")
cake = pygame.transform.scale(cake, [385, 388])
screen.blit(cake,[100,200])

#lisame teksti
font = pygame.font.SysFont("comic sans", 50)
text = font.render("Palju õnne Torren!", True, [0,0,0])
screen.blit(text, [100,570])


pygame.display.flip()
#Alumine osa ei lase Pygame ekraanil ise kinni minna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()