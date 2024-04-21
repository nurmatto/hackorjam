import pygame
import sys
from right_button import *# Constants
WIDTH = 1200
HEIGHT = 600
FPS = 60

# Initialize Pygame
pygame.init()
pygame.mixer.init()

class Animation:
    def __init__(self, base_path, frame_count):
        self.frames = [
            pygame.transform.scale(
                pygame.image.load(f"{base_path}{i}.png").convert_alpha(), 
                (int(pygame.image.load(f"{base_path}{i}.png").get_width() / 3),
                 int(pygame.image.load(f"{base_path}{i}.png").get_height() / 3))
            ) for i in range(frame_count)
        ]        
        self.frame_index = 0
        self.animation_speed = 5
        self.tick_count = 0

    def update(self):
        self.tick_count += 1
        if self.tick_count >= self.animation_speed:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.tick_count = 0

    def get_frame(self):
        return self.frames[self.frame_index]

class Player:
    def __init__(self, x, y):
        self.animations = {
            'up': Animation('/Users/nurmatto/Desktop/nurmatto/HackOrJam/characters/move_up_', 4),
            'down': Animation('/Users/nurmatto/Desktop/nurmatto/HackOrJam/characters/move_down_', 4),
            'left': Animation('/Users/nurmatto/Desktop/nurmatto/HackOrJam/characters/move_left_', 4),
            'right': Animation('/Users/nurmatto/Desktop/nurmatto/HackOrJam/characters/move_right_', 4)
        }
        self.direction = 'down'
        self.speed = 5
        self.moving = False
        self.x = x
        self.y = y
        current_frame = self.animations[self.direction].get_frame()
        self.rect = current_frame.get_rect(center=(self.x, self.y))

    def move(self):
        self.moving = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y > 167:
            self.y -= self.speed
            self.direction = 'up'
            self.moving = True
        elif keys[pygame.K_s] and self.y < 690:
            self.y += self.speed
            self.direction = 'down'
            self.moving = True
            
        if keys[pygame.K_a] and self.x > 138:
            self.x -= self.speed
            self.direction = 'left'
            self.moving = True
        elif keys[pygame.K_d] and self.x < 1285:
            self.x += self.speed
            self.direction = 'right'
            self.moving = True
        if self.moving:
            self.animations[self.direction].update()
            current_frame = self.animations[self.direction].get_frame()
            self.rect = current_frame.get_rect(center=(self.x, self.y))
        else:
            self.animations[self.direction].frame_index = 0

            
    def draw(self, screen):
        current_frame = self.animations[self.direction].get_frame()
        screen.blit(current_frame, (self.x - current_frame.get_width() // 2, self.y - current_frame.get_height() // 2))

class GameScreen:
    def __init__(self, game):
        self.game = game
        self.player = Player(400, 400)
        self.background = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/game images/background_game.webp').convert_alpha()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        self.enemy = Enemy(500, 500, enemy_image)

    def display(self):
        running = True
        while running:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.game.screen.blit(self.background, (0, 0))
            self.player.move()
            self.player.draw(self.game.screen)
            self.enemy.draw(self.game.screen)

            pygame.display.update()
            self.game.clock.tick(FPS)

class Enemy:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.health = 100  # Assuming enemy also has health

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Load Enemy Image
enemy_image = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/characters/move_up_0.png')
enemy_image = pygame.transform.scale(enemy_image, (275, 333))

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Savotz')
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu(self)
        self.game_screen = GameScreen(self)

    def run(self):
        self.main_menu.display()

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.back_m = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/menu images/back.png').convert_alpha()
        self.back_m = pygame.transform.scale(self.back_m, (1200, 600))

    def display(self):
        pygame.mixer.set_num_channels(2)
        background_channel = pygame.mixer.Channel(0)
        back = pygame.mixer.Sound('/Users/nurmatto/Desktop/nurmatto/HackOrJam/music/back_mus.mp3')
        background_channel.set_volume(0.09)
        background_channel.play(back, loops=-1)
        button = Button('START', 200, 50, (500, 300), 3)
        button_2 = Button('QUIT GAME', 200, 50, (500, 376), 3)
        while True:

            self.game.screen.blit(self.back_m, (0, 0))
            if button.draw():
                self.game.game_screen.display()
    
            if button_2.draw():
                pygame.quit()
                sys.exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.game.clock.tick(60)
            

#class OptionsMenu:
#   def __init__(self, game):
#       self.game = game
#       self.option_g = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/game images/option.webp').convert_alpha()
#       self.option_g = pygame.transform.scale(self.option_g, (1200, 600))
#       
#   def display(self):
#       running = True
#       button_speed = Button('Speed', 200, 50, (100, 300), 3)
#       button_number_of_zombie = Button('Number of Zombie', 200, 50, (100, 370), 3)
#       weapon = Button('Choose a weapon', 200, 50,(100, 440), 3)
#       
#       while running:
#           self.game.screen.blit(self.option_g, (0, 0))
#           button_speed.draw()
#           button_number_of_zombie.draw()
#           weapon.draw()
#           for event in pygame.event.get():
#               if event.type == pygame.QUIT:
#                   pygame.quit()
#                   sys.exit()
#               if event.type == pygame.KEYDOWN:
#                   if event.key == pygame.K_ESCAPE:
#                       running = False
#
#           pygame.display.update()
#           self.game.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
    