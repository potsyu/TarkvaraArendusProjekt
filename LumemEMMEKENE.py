## OG CODE FROM TAURI REINIKE
## MODIFIED BY THE LEGEND KARL KARULIN :)

import pygame #Sellel real imporditakse Pygame
pygame.init() #See rida sisestab kõik pygame moodulid programmi.

screen = pygame.display.set_mode([300,300]) #See rida teeb uue akna, kuhu ilmuvad programmis kirjutatud kujutised 300 * 300.
pygame.display.set_caption("Lumemees - Karl Karulin :)") #See rida paneb aknale pealkirja
screen.fill([0, 0, 0])

#Joonistamine
#lumememme ringid
pygame.draw.circle(screen, [255,255,255], [150,220], 50, 100) #See rida joonistab lumememme alumise ringi, mis on valget värvi.
pygame.draw.circle(screen, [255,255,255], [150,135], 40, 100) #See rida joonistab lumememme teise ringi, mis on valget värvi.
pygame.draw.circle(screen, [255,255,255], [150,70], 30, 100) #See rida joonistab lumememme kolmanda ringi, mis on valget värvi.

#lumememme nina
pygame.draw.polygon(screen, [255,0,0], [[145,80], [155,80], [150,92]],0) #See rida joonistab lumememme nina, mis on oranzi värvi.

#Silmad
pygame.draw.circle(screen, [0,0,0], [140,66], 5, 100) #See rida lisab lumememmele vasakpoolse silma.
pygame.draw.circle(screen, [0,0,0], [160,66], 5, 100) #See rida lisab lumememmele parempoolse silma.


#New attitions

# 3 nööbikest
pygame.draw.circle(screen, [0,0,0], [150,115], 5, 100)
pygame.draw.circle(screen, [0,0,0], [150,135], 5, 100)
pygame.draw.circle(screen, [0,0,0], [150,155], 5, 100)

#Pole just kõige ilusamad aga nojah haha
# Vasak käsi
pygame.draw.line(screen, [139, 69, 19], [110, 130], [40, 70], 4)
#Näpukesed :)
pygame.draw.line(screen, [139, 69, 19], [60, 90], [50, 60], 4)
pygame.draw.line(screen, [139, 69, 19], [63, 90], [37, 85], 4)

# Parem käsi
pygame.draw.line(screen, [139, 69, 19], [190, 130], [260, 70], 4)
#Näpukesed :)
pygame.draw.line(screen, [139, 69, 19], [240, 90], [250, 60], 4)
pygame.draw.line(screen, [139, 69, 19], [237, 90], [263, 85], 4)


#Mütsike lmfao
pygame.draw.polygon(screen, [32, 32, 32], [[110, 40], [190, 40], [190, 30], [170, 30], [170, 7], [130, 7], [130, 30], [110, 30]], 0)

#Teeme ilusa punase riba kaabule ka :)))
pygame.draw.polygon(screen, [255, 0, 0], [[190, 30], [170, 30], [170, 25], [130, 25], [130, 30]], 0)

#Ekraani värskendus :)
pygame.display.flip() #See rida uuendab pygame ekraani.


#Alumine osa ei lase Pygame ekraanil ise kinni minna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()



