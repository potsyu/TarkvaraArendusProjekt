import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne2")
screen.fill([204, 255, 204])



#Lisame BAKKROUND
bg = pygame.image.load("bg_shop.jpg")
screen.blit(bg,[0,0])

#Lisame mehikene
Mehikene = pygame.image.load("seller.png")
Mehikene = pygame.transform.scale(Mehikene, [252, 300])
screen.blit(Mehikene,[105,165])

#Lisame chatti
chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, [262, 210])
screen.blit(chat,[245,65])

#lisame teksti
font = pygame.font.SysFont("arial", 24)
text = font.render("Tere, olen PEETER :)", True, [255,255,255])
screen.blit(text, [280,140])


pygame.display.flip()


#Alumine osa ei lase Pygame ekraanil ise kinni minna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()
