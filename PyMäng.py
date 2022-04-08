import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne2")
screen.fill([204, 255, 204])



#Lisame pildid
bg = pygame.image.load("bg_shop.jpg")
screen.blit(bg,[0,0])

#lisame teksti
font = pygame.font.SysFont("Arial", 50)
text = font.render("Hello PyGame", True, [255,255,255])
screen.blit(text, [200,200])


pygame.display.flip()


#Alumine osa ei lase Pygame ekraanil ise kinni minna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()