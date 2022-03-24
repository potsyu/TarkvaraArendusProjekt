import pygame #Sellel real imporditakse Pygame

pygame.init() #See rida sisestab kõik pygame moodulid programmi.


screen = pygame.display.set_mode([300,300]) #See rida teeb uue akna, kuhu ilmuvad programmis kirjutatud kujutised 300 * 300.

pygame.display.set_caption("Lumemees - Tauri Reinike") #See rida paneb aknale pealkirja


#Joonistamine
#lumememme ringid
pygame.draw.circle(screen, [255,255,255], [150,220], 50, 100) #See rida joonistab lumememme alumise ringi, mis on valget värvi.
pygame.draw.circle(screen, [255,255,255], [150,135], 40, 100) #See rida joonistab lumememme teise ringi, mis on valget värvi.
pygame.draw.circle(screen, [255,255,255], [150,75], 30, 100) #See rida joonistab lumememme kolmanda ringi, mis on valget värvi.

#lumememme nina

pygame.draw.polygon(screen, [255,0,0], [[145,80], [155,80], [150,97]],0) #See rida joonistab lumememme nina, mis on oranzi värvi.

#Silmad
pygame.draw.circle(screen, [0,0,0], [140,71], 5, 100) #See rida lisab lumememmele vasakpoolse silma.
pygame.draw.circle(screen, [0,0,0], [160, 71], 5, 100) #See rida lisab lumememmele parempoolse silma.

pygame.display.flip() #See rida uuendab pygame ekraani.


#Alumine osa ei lase Pygame ekraanil ise kinni minna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()



