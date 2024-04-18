import pygame
import sys

# Constants
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
    def __init__(self):
        self.animations = {
            'up': Animation('/Users/nurmatto/Desktop/nurmatto/HackOrJam/characters/move_up_', 4),
            'down': Animation('/Users/nurmatto/Desktop/nurmatto/HackOrJam/characters/move_down_', 4),
            'left': Animation('/Users/nurmatto/Desktop/nurmatto/HackOrJam/characters/move_left_', 4),
            'right': Animation('/Users/nurmatto/Desktop/nurmatto/HackOrJam/characters/move_right_', 4)
        }
        self.direction = 'down'
        self.x = 600
        self.y = 300
        self.speed = 5
        self.moving = False

    def move(self, keys):
        self.moving = False
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = 'up'
            self.moving = True
        elif keys[pygame.K_s]:
            self.y += self.speed
            self.direction = 'down'
            self.moving = True
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = 'left'
            self.moving = True
        elif keys[pygame.K_d]:
            self.x += self.speed
            self.direction = 'right'
            self.moving = True
        
        if self.moving:
            self.animations[self.direction].update()

    def draw(self, screen):
        current_frame = self.animations[self.direction].get_frame()
        screen.blit(current_frame, (self.x - current_frame.get_width() // 2, self.y - current_frame.get_height() // 2))

class GameScreen:
    def __init__(self, game):
        self.game = game
        self.player = Player()
        self.background = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/game images/background_game.webp').convert_alpha()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

    def display(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            self.game.screen.blit(self.background, (0, 0))
            self.player.draw(self.game.screen)

            pygame.display.update()
            self.game.clock.tick(FPS)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Savotz')
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu(self)
        self.game_screen = GameScreen(self)
        self.options_menu = OptionsMenu(self)

    def run(self):
        self.main_menu.display()

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.back_m = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/menu images/back.png').convert_alpha()
        self.back_m = pygame.transform.scale(self.back_m, (1200, 600))
        self.start_m = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/menu images/start.png').convert_alpha()
        self.start_rect = self.start_m.get_rect(midbottom=(WIDTH // 2, HEIGHT // 2))
        self.quit_m = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/menu images/quit.png').convert_alpha()
        self.quit_m = pygame.transform.scale(self.quit_m, (601, 164))
        self.quit_rect = self.quit_m.get_rect(midtop=(WIDTH // 2, self.start_rect.bottom + 20))

    def display(self):
        click = False
        pygame.mixer.music.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/music/back_mus.mp3')
        pygame.mixer.music.set_volume(0.09)
        pygame.mixer.music.play(-1)
        while True:
            self.game.screen.fill((0,0,0))
            mx, my = pygame.mouse.get_pos()

            if self.start_rect.collidepoint((mx, my)) and click:
                self.game.game_screen.display()

            if self.quit_rect.collidepoint((mx, my)) and click:
                self.game.options_menu.display()

            self.game.screen.blit(self.back_m, (0, 0))
            self.game.screen.blit(self.start_m, self.start_rect)
            self.game.screen.blit(self.quit_m, self.quit_rect)

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            self.game.clock.tick(60)

class OptionsMenu:
    def __init__(self, game):
        self.game = game
        self.option_g = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/game images/option menu.png').convert_alpha()

    def display(self):
        running = True
        while running:
            self.game.screen.fill((0,0,0))
            self.game.screen.blit(self.option_g, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
            self.game.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
    
