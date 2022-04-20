#Pygame - Tekstide ja piltide kasutamine.

#Pygame'i import ning käivitamine.
import pygame
pygame.init()

#ekraani seaded (resolutsioon, ekraani nimi ning terve ekraani värvus.
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

"""
# lisame teksti, mis kasutab tavalist fonti ning kirjutab ekraanile "Hello PyGame"
# See omakorda paigutatakse ekraani keskele
font = pygame.font.SysFont("Comic Sans MS", 30)  #Fonti saab muuda selleks nagu soovid. Valisin fondiks ise Comic Sans MS ;)
#Saab veel lisada erinevaid vormindamisviise
font.set_underline(False) #Saab ka panna false, aga see ei muuda midagi.
font.set_bold(True)
font.set_italic(True)

text = font.render("Hello PyGame", True, [0,0,0])



#Saab ka muuta tekstikasti suurust :))
text_width = text.get_rect().width
text_height = text.get_rect().height
screen.blit(text, [320-text_width/2,240-text_height/2])
"""

#Piltide lisamine.
#Saab lisada ka erinevaid pilte nendes pildiformaatides:

# JPG
# PNG
# GIF (mitteanimeeritud)
# BMP
# PCXTGA
# TIF
# LBM (PBM)
# PBM (PGM, PPM)
# XPM

#Pildi lisamine
bg = pygame.image.load("suvaline_pilt.jfif") #Nunnu kiisu :)
screen.blit(bg, [0,0])

#Ekraani uuendatakse.
pygame.display.flip()

#Alumine osa ei lase Pygame ekraanil ise kinni minna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()