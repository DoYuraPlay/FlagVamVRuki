# coding: utf8
import pygame

size = (600,600)
window = pygame.display.set_mode(size)

pygame.display.set_caption("Hello world")

screen = pygame.Surface(size)

square = pygame.Surface([300 , 300])
gag = pygame.Surface([100 , 100])
gsg = pygame.Surface([100 , 100])

square.fill([255,40,0])
gag.fill([255,255,255])
gsg.fill([255,255,255])

right_free = True
x = 0
y = 0
r = 1
t = 1
rgb_free = True
x2 = 500
y2 = 500
g = 1.5

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        
    screen.fill([0,0,0])
    
    if right_free == True:
        x += r
        y += t
        if x > 300:
            right_free = False
            r += 0.1
        if y > 300:
            right_free = False
            t += 0.1
    else:
        x -= r
        y -= t
        if x < 0:
            right_free = True
            r += 0.1
        if y < 0:
            right_free = True
            t += 0.1
    if rgb_free == True:
        x2 += g
        y2 += g
        if x2 > 500:
            rgb_free = False
            g += 0.001
    else:
        x2 -= g
        y2 -= g
        if x2 < 0:
            rgb_free = True
            g += 0.001
            
#     if keyPressed:
#         key:'w':
#             r = 1
    screen.blit(square, [x, y])
    screen.blit(gag, [x2,0])
    screen.blit(gsg, [y2,500])
    
    window.blit(screen, [0, 0])
    pygame.display.flip()
    pygame.time.delay(5)
    
pygame.quit()