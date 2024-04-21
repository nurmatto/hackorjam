import pygame
import sys
import random
import math
from right_button import *
from main import *

pygame.init()

icon = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/Game/icon.png')
pygame.display.set_icon(icon)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
button_next = Button_m('Next Level', 400, 77, (400, 250), 7)
class MainMenu:
    def __init__(self, game):
        self.game = game
        self.back_m = pygame.image.load('/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/mainmenu(zombie ver).png').convert_alpha()
        self.back_m = pygame.transform.scale(self.back_m, (1000, 600))
        
    def display(self):
        
        button = Button('START', 200, 50, (400, 300), 3)
        button_2 = Button('QUIT GAME', 200, 50, (400, 376), 3)
        while True:
            
            self.game.screen.blit(self.back_m, (0, 0))
            if button.draw():
                level_one()
            if button_2.draw():
                pygame.quit()
                sys.exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.game.clock.tick(60)
            


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Savotz')
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu(self)
        
    def run(self):
        self.main_menu.display()

def level_one():
    pygame.mixer.set_num_channels(2)
    background_channel = pygame.mixer.Channel(0)
    back = pygame.mixer.Sound('/Users/nurmatto/Desktop/nurmatto/Game/level_1/music/zombie sound.mp3')
    background_channel.set_volume(0.09)
    background_channel.play(back, loops=7)
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("some extra points, pls :D")
        
    background = pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/BACKGROUN_REAL (1).png").convert()

    background_center = (background.get_width() // 2, background.get_height() // 2)

    wall_x = background_center[0] - 600
    wall_y = background_center[1] - 300

    invisible_color = (255, 255, 255, 0)
    top_wall = pygame.Rect(wall_x, wall_y, 1200, 10)
    bottom_wall = pygame.Rect(wall_x, wall_y + 590, 1200, 10)
    left_wall = pygame.Rect(wall_x, wall_y, 10, 600)
    right_wall = pygame.Rect(wall_x + 1190, wall_y, 10, 600)

    walls = [top_wall, bottom_wall, left_wall, right_wall]

    for wall in walls:
        pygame.draw.rect(screen, invisible_color, wall)

    animations = {
        "up": [pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/character/character_up0.png").convert_alpha(),
            pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/character/character_up1.png").convert_alpha(),
            pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/character/character_up2.png").convert_alpha()],
        "down": [pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/character/character_down0.png").convert_alpha(),
                pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/character/character_down1.png").convert_alpha(),
                pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/character/character_down2.png").convert_alpha()],
        "left": [pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/character/character_left0.png").convert_alpha(),
                pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/character/character_left1.png").convert_alpha(),
                pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/character/character_left2.png").convert_alpha()],
        "right": [pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/character/character_right0.png").convert_alpha(),
                pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/character/character_right1.png").convert_alpha(),
                pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/character/character_right2.png").convert_alpha()]
    }

    for direction, frames in animations.items():
        for i, frame in enumerate(frames):
            animations[direction][i] = pygame.transform.scale(frame, (100, 100))


    class Player:
        def __init__(self, x, y, animations):
            self.animations = animations
            self.rect = self.animations["up"][0].get_rect()
            self.rect.center = (x, y)
            self.speed = 9
            self.last_direction = "up"
            self.frame_index = 0
            self.animation_speed = 5
            self.frame_counter = 0
            self.attacking = False
            self.attack_cooldown = 0
            self.health = 100
            self.max_health = 100

        def move(self, keys, walls):
            moving = False
            if keys[pygame.K_a] and self.rect.left > walls[2].right:
                self.rect.x -= self.speed
                self.last_direction = "left"
            
                pygame.mixer.music.load('/Users/nurmatto/Desktop/nurmatto/Game/level_1/music/steps.mp3')
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(loops=1)
                moving = True
            if keys[pygame.K_d] and self.rect.right < walls[3].left:
                self.rect.x += self.speed
                self.last_direction = "right"
                moving = True
                pygame.mixer.music.load('/Users/nurmatto/Desktop/nurmatto/Game/level_1/music/steps.mp3')
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play()
            if keys[pygame.K_w] and self.rect.top > walls[0].bottom:
                self.rect.y -= self.speed
                self.last_direction = "up"
                moving = True
                pygame.mixer.music.load('/Users/nurmatto/Desktop/nurmatto/Game/level_1/music/steps.mp3')
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play()
            if keys[pygame.K_s] and self.rect.bottom < walls[1].top:
                self.rect.y += self.speed
                self.last_direction = "down"
                moving = True
                pygame.mixer.music.load('/Users/nurmatto/Desktop/nurmatto/Game/level_1/music/steps.mp3')
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play()

            self.frame_counter += 1
            if self.frame_counter >= self.animation_speed and moving:
                self.frame_index = (self.frame_index + 1) % len(self.animations[self.last_direction])
                self.frame_counter = 0

        def attack(self, keys, enemies):
            if keys[pygame.K_SPACE]:
                if not self.attacking and self.attack_cooldown == 0:
                    self.attacking = True
                    self.attack_cooldown = 10

            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1

            if self.attacking:
                for enemy in enemies:
                    if self.rect.colliderect(enemy.rect):
                        enemy.health -= 25
                        if enemy.health <= 0:
                            spawn_potion(enemy.rect.x, enemy.rect.y)
                            spawn_blood_effect(enemy.rect.centerx, enemy.rect.bottom)  # Create blood effect
                            enemies.remove(enemy)
                            break
                self.attacking = False

        def draw(self, screen, camera_x, camera_y):
            if self.attacking:
                screen.blit(self.animations[self.last_direction][2], (self.rect.x - camera_x, self.rect.y - camera_y))
            else:
                screen.blit(self.animations[self.last_direction][self.frame_index],
                            (self.rect.x - camera_x, self.rect.y - camera_y))

        def take_damage(self, amount):
            self.health -= amount
            if self.health < 0:
                self.health = 0

        def draw_health_bar(self, screen):
            health_bar_width = 100
            health_bar_height = 10
            health_bar_x = SCREEN_WIDTH // 2 - health_bar_width // 2
            health_bar_y = SCREEN_HEIGHT - 30

            pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))

            health_width = (self.health / self.max_health) * health_bar_width
            pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, health_width, health_bar_height))


    player = Player(wall_x + 600, wall_y + 300, animations)

    enemy_images = {
        1: pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/ZOMBIE.png").convert_alpha(),
        2: pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/enemy1.png").convert_alpha(),
        3: pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/ZOMBIE.png").convert_alpha()
    }

    earthquake_duration = 0
    earthquake_intensity = 0


    class Enemy:
        def __init__(self, x, y, level):
            self.level = level
            self.set_image(level)  # Set the image based on the level
            self.rect = self.image.get_rect(center=(x, y))
            self.target = player.rect
            self.health = 50
            self.max_health = 50
            self.attack_cooldown = 0
            self.attack_interval = 120

        def set_image(self, level):
            if level == 1:
                self.image = pygame.transform.scale(enemy_images[1], (80, 80))
            elif level == 2:
                self.image = pygame.transform.scale(enemy_images[2], (80, 80))
            elif level == 3:
                self.image = pygame.transform.scale(enemy_images[3], (80, 80))

        def update(self):
            dx = self.target.centerx - self.rect.centerx
            dy = self.target.centery - self.rect.centery
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dist != 0:
                dx = dx / dist
                dy = dy / dist
            self.rect.x += dx * 3
            self.rect.y += dy * 3

        def draw_health_bar(self, camera_x, camera_y):
            health_bar_width = self.rect.width
            health_bar_height = 5
            health_bar_x = self.rect.x - camera_x
            health_bar_y = self.rect.y - camera_y - 10

            pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
            health_width = (self.health / self.max_health) * health_bar_width
            pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, health_width, health_bar_height))

        def attack(self, player):
            player.take_damage(5)

        def can_attack(self):
            return self.attack_cooldown <= 0

        def update_attack_cooldown(self):
            self.attack_cooldown -= 1


    enemies = []

    class Potion:
        def __init__(self, x, y):
            self.image = pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/potion.png").convert_alpha()
            self.rect = self.image.get_rect(center=(x, y))

    potions = []

    class Blood:
        def __init__(self, x, y):
            self.image = pygame.image.load("/Users/nurmatto/Desktop/nurmatto/Game/level_1/image/ded2.png").convert_alpha()
            self.rect = self.image.get_rect(center=(x, y))
            self.duration = 180  # 3 seconds at 60 FPS

        def update(self):
            self.duration -= 1

        def should_disappear(self):
            return self.duration <= 0

        def draw(self, screen, camera_x, camera_y):
            screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))


    blood_effects = []

    def spawn_potion(x, y):
        if random.random() < 0.25:
            potion = Potion(x, y)
            potions.append(potion)

    def spawn_enemy():
        side = random.choice(["left", "right", "top", "bottom"])
        if side == "left":
            x = 0
            y = random.randint(0, SCREEN_HEIGHT)
        elif side == "right":
            x = SCREEN_WIDTH
            y = random.randint(0, SCREEN_HEIGHT)
        elif side == "top":
            x = random.randint(0, SCREEN_WIDTH)
            y = 0
        elif side == "bottom":
            x = random.randint(0, SCREEN_WIDTH)
            y = SCREEN_HEIGHT
        enemy = Enemy(x, y, level)
        enemies.append(enemy)

    def spawn_blood_effect(x, y):
        blood_effect = Blood(x, y)
        blood_effects.append(blood_effect)

    level = 1
    start_ticks = pygame.time.get_ticks()
    
    enemy_spawn_timer = 1
    enemy_spawn_interval = 180

    running = True
    game_over = False
    screen_shake = [0, 0]
    fade = False
    while running:
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Convert milliseconds to seconds
        if seconds > 59:  
            screen.fill((0, 0, 0))
            
            if button_next.draw():
                fade = True
                scnd_lev()
    
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                exit()

        if not game_over and fade == False:
            keys = pygame.key.get_pressed()

            player.move(keys, walls)
            player.attack(keys, enemies)

            if level == 1:
                enemy_spawn_interval = 180
                max_enemies = 5
            elif level == 2:
                enemy_spawn_interval = 150
                max_enemies = 10
                if len(enemies) == 2:
                    # Earthquake effect at level 2
                    earthquake_duration = 3 * 60  # 3 seconds at 60 FPS
                    earthquake_intensity = 5
            elif level == 3:
                enemy_spawn_interval = 120
                max_enemies = 15

            if enemy_spawn_timer <= 0 and len(enemies) < max_enemies:
                spawn_enemy()
                enemy_spawn_timer = enemy_spawn_interval
            else:
                enemy_spawn_timer -= 1

            for enemy in enemies:
                enemy.update()

            for enemy in enemies:
                if enemy.can_attack() and player.rect.colliderect(enemy.rect):
                    enemy.attack(player)
                    enemy.attack_cooldown = enemy.attack_interval

            camera_x = player.rect.centerx - SCREEN_WIDTH // 2 + screen_shake[0]
            camera_y = player.rect.centery - SCREEN_HEIGHT // 2 + screen_shake[1]

            screen.blit(background, (0 - camera_x, 0 - camera_y))

            player.draw(screen, camera_x, camera_y)
            current_time = int(pygame.time.get_ticks()/1000)
            score_surf = text_font.render(f'Time:{current_time}', False, (255, 255 , 255))
            score_rect = score_surf.get_rect(topleft = (5, 5))
            
            screen.blit(score_surf, (0, 0))
            

            for enemy in enemies:
                enemy.draw_health_bar(camera_x, camera_y)
                screen.blit(enemy.image, (enemy.rect.x - camera_x, enemy.rect.y - camera_y))

            player.draw_health_bar(screen)
            for potion in potions[:]:
                if player.rect.colliderect(potion.rect):
                    player.health = min(player.health + 25, player.max_health)
                    potions.remove(potion)

            for potion in potions:
                screen.blit(potion.image, (potion.rect.x - camera_x, potion.rect.y - camera_y))

            if player.health <= 0:
                game_over = True

            if earthquake_duration > 0:
                screen_shake = [random.randint(-earthquake_intensity, earthquake_intensity),
                                random.randint(-earthquake_intensity, earthquake_intensity)]
                earthquake_duration -= 1

            if len(enemies) == 0 and level < 3:
                level += 1

                player.health = player.max_health

                enemy_spawn_timer = 1

                for _ in range(3 + (level - 1) * 5):
                    spawn_enemy()

            for blood_effect in blood_effects[:]:
                blood_effect.update()
                blood_effect.draw(screen, camera_x, camera_y)
                if blood_effect.should_disappear():
                    blood_effects.remove(blood_effect)
            
        else:
            screen.fill((255, 0, 0))
            font = pygame.font.Font(None, 64)
            game_over_text = font.render("Game Over", True, (255, 255, 255))
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(game_over_text, text_rect)


        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    game = Game()
    game.run()
    



    
