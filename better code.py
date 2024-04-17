import pygame
import buttons
import sys
pygame.init()
pygame.mixer.init()


WIDTH = 1200
HEIGHT = 600
for_loop = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
current_size = screen.get_size()
pygame.display.set_caption('Savotz')
fps = pygame.time.Clock()
for_loop == True
# Load images
back_m = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/menu images/back.png').convert_alpha()
back_m = pygame.transform.scale(back_m, (1200, 600))
start_m = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/menu images/start.png').convert_alpha()
start_rect = start_m.get_rect(midbottom=(current_size[0] // 2, current_size[1] // 2))
quit_m = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/menu images/quit.png').convert_alpha()
quit_m = pygame.transform.scale(quit_m, (601, 164))
quit_rect = quit_m.get_rect(midtop=(current_size[0] // 2, start_rect.bottom + 20))

back_g = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/game images/background_game.webp').convert_alpha()
back_g = pygame.transform.scale(back_g, (WIDTH, HEIGHT))  # Scale the image to match the screen size
option_g = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/game images/option menu.png').convert_alpha()

x = 600
y = 300
click = False

def main_menu():
    pygame.mixer.music.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/music/back_mus.mp3')
    pygame.mixer.music.set_volume(0.09)
    pygame.mixer.music.play(-1)
    while True:
        screen.fill((0,0,0))
        
        mx, my = pygame.mouse.get_pos()

        if start_rect.collidepoint((mx, my)):
            if click:
                
                game()
                
        if quit_rect.collidepoint((mx, my)):
            if click:
                
                options()
        screen.blit(back_m, (0, 0))
        screen.blit(start_m, start_rect)
        screen.blit(quit_m, quit_rect)
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        fps.tick(60)
        
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(back_g, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        pygame.display.update()
        fps.tick(60)
        move()
        
def options():
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(option_g, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        pygame.display.update()
        fps.tick(60)
        
def move():
    global x,y
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
#           if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#               running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y-=30
        if keys[pygame.K_s]:
            y+=30
        if keys[pygame.K_a]:
            x-=30
        if keys[pygame.K_d]:
            x+=30
        screen.blit(back_g, (0, 0))
        pygame.draw.circle(screen, 'Blue', (x, y), 30)
        pygame.display.update()
        fps.tick(60)
        
main_menu()
