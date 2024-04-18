import pygame
import sys
import random
import math

pygame.init()

SCREEN_WIDTH = 1720
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("some extra points :D")

background = pygame.image.load("background.png").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

animations = {
    "up": [pygame.image.load("character_up0.png").convert_alpha(),
           pygame.image.load("character_up1.png").convert_alpha(),
           pygame.image.load("character_up2.png").convert_alpha()],
    "down": [pygame.image.load("character_down0.png").convert_alpha(),
             pygame.image.load("character_down1.png").convert_alpha(),
             pygame.image.load("character_down2.png").convert_alpha()],
    "left": [pygame.image.load("character_left0.png").convert_alpha(),
             pygame.image.load("character_left1.png").convert_alpha(),
             pygame.image.load("character_left2.png").convert_alpha()],
    "right": [pygame.image.load("character_right0.png").convert_alpha(),
              pygame.image.load("character_right1.png").convert_alpha(),
              pygame.image.load("character_right2.png").convert_alpha()]
}

enemy_image = pygame.image.load("enemy.png").convert_alpha()

for direction, frames in animations.items():
    for i, frame in enumerate(frames):
        animations[direction][i] = pygame.transform.scale(frame, (100, 100))

character_rect = animations["up"][0].get_rect()
character_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
character_speed = 5

enemy_speed = 3
last_direction = "up"
frame_index = 0
animation_speed = 5
frame_counter = 0

class Enemy:
    def __init__(self, x, y):
        self.image = enemy_image
        self.rect = self.image.get_rect(center=(x, y))
        self.target = character_rect

    def update(self):
        dx = self.target.centerx - self.rect.centerx
        dy = self.target.centery - self.rect.centery
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist != 0:
            dx = dx / dist
            dy = dy / dist
        self.rect.x += dx * enemy_speed
        self.rect.y += dy * enemy_speed

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

for _ in range(10):  
    spawn_enemy()

enemy_spawn_timer = 0
enemy_spawn_interval = 60  

wall_thickness = 10
top_wall = pygame.Rect(0, 0, SCREEN_WIDTH, wall_thickness)
bottom_wall = pygame.Rect(0, SCREEN_HEIGHT - wall_thickness, SCREEN_WIDTH, wall_thickness)
left_wall = pygame.Rect(0, 0, wall_thickness, SCREEN_HEIGHT)
right_wall = pygame.Rect(SCREEN_WIDTH - wall_thickness, 0, wall_thickness, SCREEN_HEIGHT)

walls = [top_wall, bottom_wall, left_wall, right_wall]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    moving = False 
    if keys[pygame.K_LEFT] and character_rect.left > left_wall.right:
        character_rect.x -= character_speed
        last_direction = "left"
        moving = True
    if keys[pygame.K_RIGHT] and character_rect.right < right_wall.left:
        character_rect.x += character_speed
        last_direction = "right"
        moving = True
    if keys[pygame.K_UP] and character_rect.top > top_wall.bottom:
        character_rect.y -= character_speed
        last_direction = "up"
        moving = True
    if keys[pygame.K_DOWN] and character_rect.bottom < bottom_wall.top:
        character_rect.y += character_speed
        last_direction = "down"
        moving = True

    frame_counter += 1
    if frame_counter >= animation_speed and moving:
        frame_index = (frame_index + 1) % len(animations[last_direction])
        frame_counter = 0

    if enemy_spawn_timer <= 0:
        spawn_enemy()
        enemy_spawn_timer = enemy_spawn_interval
    else:
        enemy_spawn_timer -= 1

    for enemy in enemies:
        enemy.update()

    camera_x = character_rect.centerx - SCREEN_WIDTH // 2
    camera_y = character_rect.centery - SCREEN_HEIGHT // 2

    screen.blit(background, (0 - camera_x, 0 - camera_y))
    if moving:
        screen.blit(animations[last_direction][frame_index], (SCREEN_WIDTH // 2 - character_rect.width // 2, SCREEN_HEIGHT // 2 - character_rect.height // 2))
    else:
        if last_direction == "left":
            screen.blit(animations["left"][0], (SCREEN_WIDTH // 2 - character_rect.width // 2, SCREEN_HEIGHT // 2 - character_rect.height // 2))
        elif last_direction == "right":
            screen.blit(animations["right"][0], (SCREEN_WIDTH // 2 - character_rect.width // 2, SCREEN_HEIGHT // 2 - character_rect.height // 2))
        elif last_direction == "up":
            screen.blit(animations["up"][0], (SCREEN_WIDTH // 2 - character_rect.width // 2, SCREEN_HEIGHT // 2 - character_rect.height // 2))
        elif last_direction == "down":
            screen.blit(animations["down"][0], (SCREEN_WIDTH // 2 - character_rect.width // 2, SCREEN_HEIGHT // 2 - character_rect.height // 2))
    
    for enemy in enemies:
        screen.blit(enemy.image, (enemy.rect.x - camera_x, enemy.rect.y - camera_y))

    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.move(-camera_x, -camera_y))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
