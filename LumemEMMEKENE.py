## OG CODE FROM TAURI REINIKE
## MODIFIED BY THE LEGEND KARL KARULIN :)

import pygame #Sellel real imporditakse Pygame
pygame.init() #See rida sisestab kõik pygame moodulid programmi.

screen = pygame.display.set_mode([300,300]) #See rida teeb uue akna, kuhu ilmuvad programmis kirjutatud kujutised 300 * 300.
pygame.display.set_caption("Lumemees - Karl Karulin") #See rida paneb aknale pealkirja
screen.fill([0, 191, 255])

#Joonistamine
#Teeme lume kah
pygame.draw.polygon(screen, [220, 220, 220], [[0, 250], [300, 250], [300, 300], [0, 300]], 0)

#Ilus päike :)
pygame.draw.circle(screen, [255, 255, 0], [250, 30], 20, 100)

#Päikesekiired
pygame.draw.line(screen, [255,255,0], [250, 7], [250, 0], 1)
pygame.draw.line(screen, [255,255,0], [270, 15], [285, 5], 1)
pygame.draw.line(screen, [255,255,0], [275, 30], [290, 30], 1)
pygame.draw.line(screen, [255,255,0], [265, 45], [280, 55], 1)
pygame.draw.line(screen, [255,255,0], [230, 15], [210, 5], 1)
pygame.draw.line(screen, [255,255,0], [220, 30], [200, 30], 1)
pygame.draw.line(screen, [255,255,0], [230, 45], [210, 55], 1)
pygame.draw.line(screen, [255,255,0], [240, 53], [236, 70], 1)
pygame.draw.line(screen, [255,255,0], [254, 53], [260, 70], 1)

#Kuusepuu
#Alus
pygame.draw.polygon(screen, [139, 63, 13], [[220, 250],[250, 250], [250, 200], [220, 200] ], 0)

#Kuusk :)
pygame.draw.polygon(screen, [0, 128, 0], [[190, 200], [280, 200],[255, 170], [215, 170]])

pygame.draw.polygon(screen, [0, 128, 0], [[200, 170], [225, 140],[250, 140], [270, 170]])

pygame.draw.polygon(screen, [0, 128, 0], [[210, 140], [265, 140],[237, 110]])

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


#No ss tuleb hari kah
pygame.draw.line(screen, [160, 82, 45], [50, 40], [50, 200], 5)
#Harja otsad ffs
pygame.draw.line(screen, [139, 69, 19], [50, 40], [35, 15], 5)
pygame.draw.line(screen, [139, 69, 19], [50, 40], [42, 10], 5)
pygame.draw.line(screen, [139, 69, 19], [50, 40], [49, 5], 5)
pygame.draw.line(screen, [139, 69, 19], [50, 40], [60, 5], 5)
pygame.draw.line(screen, [139, 69, 19], [50, 40], [71, 10], 5)

#Mütsike lmfao
pygame.draw.polygon(screen, [32, 32, 32], [[110, 40], [190, 40], [190, 30], [170, 30], [170, 7], [130, 7], [130, 30], [110, 30]], 0)

#Teeme ilusa punase riba kaabule ka :)))
pygame.draw.polygon(screen, [255, 255, 255], [[190, 30], [170, 30], [170, 25], [130, 25], [130, 30]], 0)

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
