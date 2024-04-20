import pygame, sys
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(2)
class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes 
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # Top rectangle 
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = (0, 176, 176)

        # Bottom rectangle 
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = (178, 178, 178)

        # Text
        self.text_surf = gui_font.render(text, True, (75, 37, 109))
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # Elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        return self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (178, 178, 178)
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
                
                pygame.mixer.music.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/music/button.mp3')
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play()
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    self.pressed = False
                    return True  # Return True on button release after a press
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = (0, 176, 176)
        return False
screen = pygame.display.set_mode((500,500))
gui_font = pygame.font.Font(None,30)
