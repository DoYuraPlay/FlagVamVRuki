import pygame
from pygame.locals import *
from sys import exit
from random import randint
import time

pygame.init()
pygame.display.set_caption('Zmeika')
screen = pygame.display.set_mode( (600,600) )
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

pygame.mixer.init()

game_sound = pygame.mixer.Sound('gamesound.mp3')
game_sound.set_volume(1)
point_sound = pygame.mixer.Sound('appli.mp3')
point_sound.set_volume(0.9)
kitai_sound = pygame.mixer.Sound('hi.mp3')
kitai_sound.set_volume(1)
skrim_sound = pygame.mixer.Sound('krik.mp3')
skrim_sound.set_volume(0.9)

#head = Rect(400, 300, 40, 40)

SPEED = 10
DIRECTION = [SPEED, 0]
COLOR = (255, 255, 255)
GAME_POINTS = 0
GOLDI = 0


def load_image(scr, x, y):
    image = pygame.image.load(scr).convert()
    image = pygame.transform.scale(image, (50, 50))
    rect = image.get_rect(center=(x, y))
    
    transparent = image.get_at((0,0))
    image.set_colorkey(transparent)
    
    return image, rect

def load_pol(scr, x, y):
    image = pygame.image.load(scr).convert()
    image = pygame.transform.scale(image, (600, 600))
    rect = image.get_rect(center=(x, y))
    
    transparent = image.get_at((0,0))
    image.set_colorkey(transparent)
    
    return image, rect


def move(head, snake):
    global DIRECTION, KEYS, GAME_POINTS
    
    if KEYS[K_UP] and DIRECTION[1] == 0:
        DIRECTION = [0, -SPEED]
    elif KEYS[K_DOWN] and DIRECTION[1] == 0:
        DIRECTION = [0, SPEED]
    elif KEYS[K_RIGHT] and DIRECTION[0] == 0:
        DIRECTION = [SPEED, 0]
    elif KEYS[K_LEFT] and DIRECTION[0] == 0:
        DIRECTION = [-SPEED, 0]

    
    if head.bottom < 0:
        GAME_POINTS -= 10
        print(f'GAME_POINTS:{GAME_POINTS}')
        head.top = 600
        
    elif head.top > 600:
        GAME_POINTS -= 10
        print(f'GAME_POINTS:{GAME_POINTS}')
        head.bottom = 0
        
    elif head.left < 0 :
        GAME_POINTS -= 10
        print(f'GAME_POINTS:{GAME_POINTS}')
        head.right = 600
        
    elif head.right > 600:
        GAME_POINTS -= 10
        print(f'GAME_POINTS:{GAME_POINTS}')
        head.left = 0
        
    for index in range(len(snake)-1, 0, -1):
        snake[index].x = snake[index-1].x
        snake[index].y = snake[index-1].y
        
    head.move_ip(DIRECTION)
    
def pickup(head):
    global apple_rect, head_rect, GAME_POINTS, snake, skrim_rect, ejik_rect

#     GOLDI = randint(0,1)
#     print(GOLDI)
    if head_rect.colliderect(apple_rect):
        apple_rect.x = randint(50, 550)
        apple_rect.y = randint(50, 550)
        GAME_POINTS += 10
        print(f'GAME_POINTS:{GAME_POINTS}')
        snake.append(snake[-1].copy())
        point_sound.play()
        kitai_rect.x = randint(50,550)
        kitai_rect.y = randint(50,550)
        kitai_sound.play()
        ejik_rect.x = randint(50,550)
        ejik_rect.y = randint(50,550)
        
    if head_rect.colliderect(kitai_rect):
        skrim_sound.play()
        kitai_rect.x = randint(50,550)
        kitai_rect.y = randint(50,550)
        GAME_POINTS -= 10
        print(f'GAME_POINTS:{GAME_POINTS}')
    
    if head_rect.colliderect(ejik_rect):
        head.right -= 25
        head.left -= 25
        head.bottom -= 25
        head.top -= 25
        GAME_POINTS -= 20
        print(f'GAME_POINTS:{GAME_POINTS}')

        
        
#     if GOLDI == 1:
#         
#         goappl_rect.x = 30
#         goappl_rect.y = 150
#         if head_rect.colliderect(goappl_rect):
#             GAME_POINTS += 100
#             print(f'GAME_POINTS:{GAME_POINTS}')
#             goappl_rect.x = randint(50, 550)
#             goappl_rect.y = randint(50, 550)
#     else:
#         goappl_rect.x = 700
#         goappl_rect.y = 700
        
            
        
def score():
    global GAME_POINTS, SPEED
    text = font.render(f'SCORE:{GAME_POINTS}', True,(255,255,255))
    text_rect = text.get_rect(center=(300,550))
    screen.blit(text, text_rect)
    if GAME_POINTS < 0:
        text2 = font.render('GAME OVER RETRY SPACE', True,(255,0,90))
        text_rect2 = text2.get_rect(center=(300,300))
        screen.blit(text2, text_rect2)
        SPEED = 0
        

def retry():
    global KEYS, GAME_POINTS, SPEED
    if KEYS[K_SPACE]:
        SPEED = 10
        GAME_POINTS = 0
        head_rect.x = 400
        head_rect.y = 300
        apple_rect.x = 200
        apple_rect.y = 300
        kitai_rect.x = 500
        kitai_rect.y = 500
        ejik_rect.x = 400
        ejik_rect.y = 400

pole_image, pole_rect = load_pol('pole.jpeg',300,300)
head_image, head_rect = load_image('golovzmeika.png',400,300)
apple_image, apple_rect = load_image('apple.jpg',200,300)
body_image, body_rect = load_image('baget.png',450,300)
kitai_image, kitai_rect = load_image('kitai.png',500,500)
ejik_image, ejik_rect = load_image('egik.png',400,400)
#goappl_image, goappl_rect = load_image('goldapple.png',300,300)

snake = [head_rect, body_rect]

game_sound.play(-1)    
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    screen.fill((0, 0, 0,))
            
    KEYS = pygame.key.get_pressed()
        
    screen.blit(pole_image, pole_rect)
    screen.blit(head_image, head_rect)
    screen.blit(apple_image, apple_rect)
    screen.blit(kitai_image, kitai_rect)
    screen.blit(ejik_image, ejik_rect)
#     screen.blit(goappl_image, goappl_rect)
    
    for segment in snake[1:]:
        screen.blit(body_image, segment)
    
    move(head_rect, snake)
    pickup(head_rect)
    score()
    retry()
    
#     if gameover():
#         text3 = font.render('GAME OVER', True,(255,0,90))
#         text_rect3 = text3.get_rect(center=(300,300))
#         screen.blit(text3, text_rect3)

    
    pygame.display.update()
    clock.tick(30)
    
    