import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne2")
screen.fill([204, 255, 204])

#lisame teksti
font = pygame.font.SysFont("Comic Sans MS", 50)
font.set_bold(True)
font.set_underline(True)
font.set_italic(True)
text = font.render("Hello PyGame", True, [0,0,0])


#tekstikasti suurus
text_width = text.get_rect().width
text_height = text.get_rect().height
screen.blit(text, [150,150])

#Ilus pilt :)
#Lisame pildid
bg = pygame.image.load("bg_shop.jpg")
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