import pygame
import sys
import random
import math

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("some extra points, pls :D")

background = pygame.image.load("background_game.jpg").convert()

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
    "up": [pygame.image.load("character/character_up0.png").convert_alpha(),
           pygame.image.load("character/character_up1.png").convert_alpha(),
           pygame.image.load("character/character_up2.png").convert_alpha()],
    "down": [pygame.image.load("character/character_down0.png").convert_alpha(),
             pygame.image.load("character/character_down1.png").convert_alpha(),
             pygame.image.load("character/character_down2.png").convert_alpha()],
    "left": [pygame.image.load("character/character_left0.png").convert_alpha(),
             pygame.image.load("character/character_left1.png").convert_alpha(),
             pygame.image.load("character/character_left2.png").convert_alpha()],
    "right": [pygame.image.load("character/character_right0.png").convert_alpha(),
              pygame.image.load("character/character_right1.png").convert_alpha(),
              pygame.image.load("character/character_right2.png").convert_alpha()]
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
            moving = True
        if keys[pygame.K_d] and self.rect.right < walls[3].left:
            self.rect.x += self.speed
            self.last_direction = "right"
            moving = True
        if keys[pygame.K_w] and self.rect.top > walls[0].bottom:
            self.rect.y -= self.speed
            self.last_direction = "up"
            moving = True
        if keys[pygame.K_s] and self.rect.bottom < walls[1].top:
            self.rect.y += self.speed
            self.last_direction = "down"
            moving = True

        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed and moving:
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.last_direction])
            self.frame_counter = 0

    def attack(self, keys, enemies):
        if keys[pygame.K_p]:
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
                        enemies.remove(enemy)
                        break
            self.attacking = False

    def draw(self, screen, camera_x, camera_y):
        if self.attacking:
            screen.blit(self.animations[self.last_direction][2], (self.rect.x - camera_x, self.rect.y - camera_y))
        else:
            screen.blit(self.animations[self.last_direction][self.frame_index], (self.rect.x - camera_x, self.rect.y - camera_y))

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

enemy_image = pygame.image.load("enemy1.png").convert_alpha()

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(enemy_image, (80, 80))  
        self.rect = self.image.get_rect(center=(x, y))
        self.target = player.rect
        self.health = 50
        self.max_health = 50
        self.attack_cooldown = 0
        self.attack_interval = 120  

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
        player.take_damage(30)

    def can_attack(self):
        return self.attack_cooldown <= 0

    def update_attack_cooldown(self):
        self.attack_cooldown -= 1

enemies = []

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
    enemies.append(Enemy(x, y))

for _ in range(3):  
    spawn_enemy()

enemy_spawn_timer = 1
enemy_spawn_interval = 180

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()

        player.move(keys, walls)
        player.attack(keys, enemies)

        if enemy_spawn_timer <= 0:
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

        camera_x = player.rect.centerx - SCREEN_WIDTH // 2
        camera_y = player.rect.centery - SCREEN_HEIGHT // 2

        screen.blit(background, (0 - camera_x, 0 - camera_y))

        player.draw(screen, camera_x, camera_y)
        
        for enemy in enemies:
            enemy.draw_health_bar(camera_x, camera_y)
            screen.blit(enemy.image, (enemy.rect.x - camera_x, enemy.rect.y - camera_y))
        
        player.draw_health_bar(screen) 

        if player.health <= 0:
            game_over = True

    else:
        screen.fill((255, 0, 0))  
        font = pygame.font.Font(None, 64)
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, text_rect)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
