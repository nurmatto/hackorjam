import pygame
import sys

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

for direction, frames in animations.items():
    for i, frame in enumerate(frames):
        animations[direction][i] = pygame.transform.scale(frame, (100, 100))

character_rect = animations["up"][0].get_rect()
character_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
character_speed = 5

last_direction = "up"
frame_index = 0
animation_speed = 5
frame_counter = 0

moving = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    moving = False 
    if keys[pygame.K_LEFT]:
        character_rect.x -= character_speed
        last_direction = "left"
        moving = True
    if keys[pygame.K_RIGHT]:
        character_rect.x += character_speed
        last_direction = "right"
        moving = True
    if keys[pygame.K_UP]:
        character_rect.y -= character_speed
        last_direction = "up"
        moving = True
    if keys[pygame.K_DOWN]:
        character_rect.y += character_speed
        last_direction = "down"
        moving = True

    frame_counter += 1
    if frame_counter >= animation_speed and moving:
        frame_index = (frame_index + 1) % len(animations[last_direction])
        frame_counter = 0

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
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
