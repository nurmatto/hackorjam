import pygame
from fighter import Fighter
from pygame import mixer

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('HackOrJam')
fps = pygame.time.Clock()
bg = pygame.image.load('/Users/nurmatto/Desktop/shooter game/background.webp')
black = pygame.image.load('/Users/nurmatto/Desktop/shooter game/Black/black.png')
blue = pygame.image.load('/Users/nurmatto/Desktop/shooter game/Blue/blue.png')
mixer.music.load('/Users/nurmatto/Desktop/shooter game/music/back.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)
black_animation_steps = [8, 8, 2, 6, 6, 4, 6]
blue_animation_steps = [4, 8, 3, 4, 4, 3, 7]
def draw_bg():
    scaled = pygame.transform.scale(bg, (1000, 600))
    screen.blit(scaled, (0, 0))
def draw_health(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, 'White', (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, 'Red', (x, y, 400, 30))
    pygame.draw.rect(screen, 'Yellow', (x, y, 400* ratio, 30))
nurma = True
black_size = 200
black_scale = 4
black_right_size = [90, 77]
blue_right_size = [88, 83]

black_data = [200, black_scale, black_right_size]
blue_scale = 4
blue_data = [200, blue_scale, blue_right_size]
blue_size = [200]
fighter_1 = Fighter(1 ,200, 310, False,black_data, black, black_animation_steps)
fighter_2 = Fighter(2 ,700,310, True,blue_data, blue, blue_animation_steps)


while nurma:
    draw_bg()
    draw_health(fighter_1.health, 20, 20)
    draw_health(fighter_2.health, 580, 20)
    fighter_1.update()
    fighter_2.update()
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    fighter_1.move(screen, fighter_2)
    fighter_2.move(screen, fighter_1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            nurma = False

    pygame.display.update()
    fps.tick(60)
    