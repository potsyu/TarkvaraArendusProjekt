import pygame #Sellel real imporditakse Pygame
pygame.init() #See rida sisestab kõik pygame moodulid programmi.

screen = pygame.display.set_mode([300,300]) #See rida teeb uue akna, kuhu ilmuvad programmis kirjutatud kujutised 300 * 300.
pygame.display.set_caption("Lumemees - #INSERT NAME HERE#") #See rida paneb aknale pealkirja
screen.fill([0, 0, 0])