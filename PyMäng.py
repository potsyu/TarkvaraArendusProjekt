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
Mehikene = pygame.transform.scale(Mehikene, [298, 352])
screen.blit(Mehikene,[50,100])

#Lisame chatti
chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, [270, 210])
screen.blit(chat,[220,40])

#lisame teksti
font = pygame.font.SysFont("Arial", 32)
text = font.render("Tere, olen sinu ori", True, [255,255,255])
screen.blit(text, [250,110])


pygame.display.flip()


#Alumine osa ei lase Pygame ekraanil ise kinni minna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()