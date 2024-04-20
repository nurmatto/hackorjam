import pygame
from button import Button
from pygame import mixer

class Fighter():
    def __init__(self, player,x, y, flip, data,sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.flip = flip
        self.player = player
        self.right_size = data[2]
        # 0idle, 1run, 2jump, 3attack, 4attack, 5get_hit, 6death
        self.action = 0
        self.frame_index = 0
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect(x, y, 80, 180)
        self.jump = False  
        self.velocity_y = 0  
        self.running = False
        self.attack_type = 0 
        self.attacking = False
        self.attack_cooldown = 0
        self.health = 100
        self.hit = False
        self.alive = True  
        
    def load_images(self, sprite_sheet, animation_steps):
        animation_list = []
        for y,animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y*self.size, self.size, self.size)
                temp_img = pygame.transform.scale(temp_img, (self.image_scale*self.size, self.image_scale*self.size))
                temp_img_list.append(temp_img)
            animation_list.append(temp_img_list)
        return animation_list
    def move(self, surface, target):
        SPEED = 10
        GRAVITY = 1  
        self.running = False
        self.attack_type = 0
        keys = pygame.key.get_pressed()
        
        if self.attacking == False:
            if self.player == 1:
                if keys[pygame.K_a] and self.rect.x > 0:
                    self.rect.x -= SPEED
                    self.running = True
                if keys[pygame.K_d] and self.rect.x < 920:
                    self.rect.x += SPEED
                    self.running = True
                    
                if keys[pygame.K_r] or keys[pygame.K_f]:
                    self.attack(surface, target)
                    nurma = mixer.Sound('/Users/nurmatto/Desktop/shooter game/music/sword1.mp3')
                    nurma.play()
                    if keys[pygame.K_r]:
                        self.attack_type = 1
                    if keys[pygame.K_f]:
                        self.attack_type = 2
                        
                        
                if not self.jump:  
                    if keys[pygame.K_w]:
                        woof = mixer.Sound('/Users/nurmatto/Desktop/shooter game/music/jump.mp3')
                        woof.play()
                        self.jump = True
                        self.velocity_y = -15       
                if self.jump:
                    self.velocity_y += GRAVITY  
                    self.rect.y += self.velocity_y 
        
                    if self.rect.bottom > 490:  
                        self.rect.bottom = 490  
                        self.jump = False  
                        self.velocity_y = 0  
            if self.player == 2:
                if keys[pygame.K_LEFT] and self.rect.x > 0:
                    self.rect.x -= SPEED
                    self.running = True
                if keys[pygame.K_RIGHT] and self.rect.x < 920:
                    self.rect.x += SPEED
                    self.running = True
                    
                if keys[pygame.K_SPACE] or keys[pygame.K_m]:
                    self.attack(surface, target)
                    nurma_top = mixer.Sound('/Users/nurmatto/Desktop/shooter game/music/sword2.mp3')
                    nurma_top.play()
                    if keys[pygame.K_SPACE]:
                        self.attack_type = 1
                    if keys[pygame.K_m]:
                        self.attack_type = 2
                        
                        
                if not self.jump:  
                    if keys[pygame.K_UP]:
                        hero = mixer.Sound('/Users/nurmatto/Desktop/shooter game/music/jump.mp3')
                        hero.play()
                        self.jump = True
                        self.velocity_y = -15       
                if self.jump:
                    self.velocity_y += GRAVITY  
                    self.rect.y += self.velocity_y 
                    
                    if self.rect.bottom > 490:  
                        self.rect.bottom = 490  
                        self.jump = False  
                        self.velocity_y = 0  
                        
        if self.attack_cooldown > 0:
            self.attack_cooldown-=1
        
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True
    def update(self):
        anim_cooldown = 50
        self.image = self.animation_list[self.action][self.frame_index]
        
        if self.health <=0:
            self.health = 0
            self.alive = False
            self.update_action(6)
            
        elif self.hit == True:
            self.update_action(5)
        elif self.attacking == True:
            if self.attack_type == 1:
                self.update_action(3)
            elif self.attack_type == 2:
                self.update_action(4)
        elif self.running == True:
            self.update_action(1)
        elif self.jump == True:
            self.update_action(2)
        else:
            self.update_action(0)
        if pygame.time.get_ticks() - self.update_time > anim_cooldown:
            self.frame_index+=1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action])-1
                
                
            else:
                if self.action == 3 or self.action == 4:
#                   pygame.
                    self.attacking = False
                    self.attack_cooldown = 10
                if self.action == 5:
                    self.hit = False
                self.frame_index = 0
            
    def attack(self, surface, target):
        if self.attack_cooldown == 0:
            
            self.attacking = True
            attacking_rect = pygame.Rect(self.rect.centerx - (4*self.rect.width*self.flip), self.rect.y, self.rect.width*4, self.rect.height)
            if attacking_rect.colliderect(target.rect):
                target.health -= 10
                target.hit = True
            
            
#       pygame.draw.rect(surface, (128, 128, 128), attacking_rect)  
    
    
    def update_action(self, new_action):
        if new_action!=self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    
    def draw(self, surface):
        image_flip = pygame.transform.flip(self.image, self.flip, False)
#       pygame.draw.rect(surface, (61, 183, 228), self.rect)
        surface.blit(image_flip, (self.rect.x - (self.right_size[0]*self.image_scale), self.rect.y - (self.right_size[1]*self.image_scale)))


class Game_Over:
    def __init__(self, screen):
        self.game = game
        self.game_over = pygame.image.load('/Users/nurmatto/Desktop/shooter game/game_over_back.webp').convert_alpha()
        self.game_over = pygame.transform.scale(self.game_over, (1200, 600))
        
    def display(self):
        running = True
        button_new_game = Button('QUIT GAME', 200, 50, (100, 300), 3)
        button_game_over = Button('GAME QUIT', 200, 50, (100, 370), 3)
        
        while running:
            self.game.screen.blit(self.game_over, (0, 0))
            button_new_game.draw()
            button_game_over.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                
            pygame.display.update()
            self.game.clock.tick(60)
#class Game:
#   def __init__(self):
#       self.screen = pygame.display.set_mode((1000, 600))
#       self.game_over = GameOver(self)
#
#if __name__ == "__main__":
#   game = Game_Over()
#   game.run()
#   