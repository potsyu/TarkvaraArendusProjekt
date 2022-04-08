import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

#lisame teksti
font = pygame.font.Font(None, 30)
text = font.render("Hello PyGame", True, [0,0,0])
screen.blit(text, [200,200])

pygame.display.flip()