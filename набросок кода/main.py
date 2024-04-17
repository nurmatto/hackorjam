import pygame
import buttons

pygame.mixer.init()
pygame.init()

WIDTH = 600
HEIGHT = 800
for_loop = True

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
current_size = screen.get_size()
virtual_surface = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption('Savotz ')

# Load images
back_m = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/menu images/back.png').convert_alpha()
back_m = pygame.transform.scale(back_m, (600, 800))
start_m = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/menu images/start.png').convert_alpha()
start_rect = start_m.get_rect(midbottom=(current_size[0] // 2, current_size[1] // 2))
quit_m = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/menu images/quit.png').convert_alpha()
quit_m = pygame.transform.scale(quit_m, (601, 164))
quit_rect = quit_m.get_rect(midtop=(current_size[0] // 2, start_rect.bottom + 20))  

back_g = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/menu images/back.png').convert_alpha()
back_g = pygame.transform.scale(back_g, (600, 800))  # Scale the image to match the screen size

# Create button instances
start_button = buttons.Knopka(start_m, start_rect)  
quit_button = buttons.Knopka(quit_m, quit_rect)  

# Set up game loop
fps = pygame.time.Clock()
while for_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            for_loop = False
            
        elif event.type == pygame.VIDEORESIZE:
            current_size = event.size
            screen = pygame.display.set_mode(current_size, pygame.RESIZABLE)
            start_rect = start_m.get_rect(midbottom=(current_size[0] // 2, current_size[1] // 2))
            quit_rect = quit_m.get_rect(midtop=(current_size[0] // 2, start_rect.bottom + 20))
            start_button.rect = start_rect
            quit_button.rect = quit_rect
            
            pygame.mixer.music.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/music/back_mus.mp3')
            pygame.mixer.music.set_volume(0.09)
            pygame.mixer.music.play(-1)
            
    action_start = start_button.draw(virtual_surface)  
    action_quit = quit_button.draw(virtual_surface)  
    
    if action_start:  
        pygame.mixer.music.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/music/button_sound.mp3')
        pygame.mixer.music.play()
        music_played = True  
        screen.blit(back_g, (0, 0))  # Blit the new background image
    if action_quit:  
        pygame.mixer.music.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/music/button_sound.mp3')
        pygame.mixer.music.play()
        for_loop = False
        music_played = True  
    
    # Update screen
    if action_start == False:
        virtual_surface.fill((0, 0, 0))
        virtual_surface.blit(back_g, (0, 0))
        scaled_surface = pygame.transform.scale(virtual_surface, current_size)
        screen.blit(scaled_surface, (0, 0))
        screen.blit(start_m, start_rect)
        screen.blit(quit_m, quit_rect)  
    pygame.display.flip()
    fps.tick(60)
