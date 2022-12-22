

import sys
import pygame

from pygame.locals import*
from sys import exit
from random import randint
pygame.init()
pygame.display.set_caption('snake')
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
# noinspection PyTypeChecker
font = pygame.font.SysFont(None, 32)
pygame.mixer.init()

SPEED = 30
DIRECTION = [SPEED, 0]
COLOR = (255, 255, 255)
GAME_POINTS = 0
def load_image(src, x, y):
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, (30, 30))
    rect = image.get_rect(center = (x, y))
    transparent = image.get_at((0, 0))
    image.set_colorkey(transparent)
    return image, rect
def random_color():
    r = randint(0 , 255)
    g = randint(0 , 255)
    b = randint(0 , 255)
    return (r, g, b)
def move(head, snake):
    global DIRECTION, COLOR, KEYS
    if KEYS[K_UP] and DIRECTION[1] == 0:
        DIRECTION = [0, -SPEED]
    elif KEYS[K_DOWN] and DIRECTION[1] == 0:
        DIRECTION = [0, SPEED]
    elif KEYS[K_LEFT] and DIRECTION[0] == 0:
        DIRECTION = [-SPEED, 0]
    elif KEYS[K_RIGHT] and DIRECTION[0] == 0:
        DIRECTION = [SPEED, 0]
    if head.bottom > 600:
        head.top = 0
    elif head.top < 0:
        head.bottom = 600
    elif head.left < 0:
        head.right = 800
    elif head.right > 800:
        head.left = 0
    for index in range(len(snake)-1, 0, -1):
        snake[index].x = snake[index-1].x
        snake[index].y = snake[index-1].y
    head.move_ip(DIRECTION)
def pickup():
    global appel_rect, head_react, GAME_POINTS, snake
    if head_rect.colliderect(appel_rect):
        appel_rect.x = randint(40, 760)
        appel_rect.y = randint(40, 560)
        GAME_POINTS += 10
        print(f'GAME_POINTS: {GAME_POINTS}')
        snake.append(snake[-1].copy())
def score():
    global GAME_POINTS
    text = font.render(f'Score: {GAME_POINTS}', True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 500))
    screen.blit(text, text_rect)
head_image, head_rect = load_image('head.png', 400, 300)
appel_image, appel_rect = load_image('appel.png', 400, 300)
body_image, body_rect = load_image('body.png', 370, 300)
snake = [head_rect, body_rect]

def gameover():
    global snake, head_rect
    for segment in snake[1:]:
        if head_rect.colliderect(segment):
            return True
    return False
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    screen.fill((0, 0, 0))
    KEYS = pygame.key.get_pressed()
    screen.blit(head_image, head_rect)
    screen.blit(appel_image, appel_rect)
    for segment in snake[1:]:
        screen.blit(body_image, segment)
    move(head_rect, snake)
    pickup()
    score()
    if gameover():
        pygame.quit()
        exit()
    pygame.display.update()
    clock.tick(60)