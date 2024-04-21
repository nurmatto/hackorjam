import pygame
from pygame import mixer
#from button_1 import *
from fighter import *
from button_for_menu import *
from level_one import*
def scnd_lev():
    
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('HackOrJam')
    fps = pygame.time.Clock()
    
    bg = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/Game/level _ 2/images/bglvl2.png')
    black = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/Game/level _ 2/images/charac/Arnur/arnur.png')
    blue = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/Game/level _ 2/images/charac/Arnur/arnur.png')
    #mixer.music.load('/Users/nurmatto/Desktop/shooter game/music/back.mp3')
    #mixer.music.set_volume(0.1)
    #mixer.music.play(-1)
    
    black_animation_steps = [4, 4, 2, 4, 4, 3, 8]
    blue_animation_steps = [4, 4, 2, 4, 4, 3, 8]
    
    def draw_bg():
        scaled = pygame.transform.scale(bg, (1000, 600))
        screen.blit(scaled, (0, 0))
        
    def draw_health(health, x, y):
        ratio = health / 100
        pygame.draw.rect(screen, (128, 128, 0), (x - 2, y - 2, 404, 34), border_radius=5)
        pygame.draw.rect(screen, (102, 0, 0), (x, y, 400*ratio, 30), border_radius=5)
        
    nurma = True
    black_size = 2
    black_scale = 4
    black_right_size = [90, 77]
    blue_right_size = [90, 77]
    
    black_data = [200, black_scale, black_right_size]
    blue_scale = 4
    blue_data = [200, blue_scale, blue_right_size]
    blue_size = [200]
    fighter_1 = Fighter(1 ,200, 310, False,black_data, black, black_animation_steps)
    fighter_2 = Fighter(2 ,700,310, True, blue_data, blue, blue_animation_steps)
    
    paused = False
    
    button_resume = Button_m('Resume', 276, 55, (375, 220), 10)
    button_quit = Button_m('Quit Game', 370, 55, (335, 305), 10)
    while nurma:
        if not paused:
            draw_bg()
            draw_health(fighter_1.health, 20, 20)
            draw_health(fighter_2.health, 580, 20)
            fighter_1.update()
            fighter_2.update()
            fighter_1.draw(screen)
            fighter_2.draw(screen)
            fighter_1.move(screen, fighter_2)
            fighter_2.move(screen, fighter_1)
            display_score(screen)
        else:
            screen.fill((0, 0, 0))
            if button_resume.draw():
                paused = False
            if button_quit.draw():
                pygame.exit()
                exit()
                nurma = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nurma = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
        pygame.display.update()
        fps.tick(60)
    
#scnd_lev()

    
    