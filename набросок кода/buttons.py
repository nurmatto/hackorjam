import pygame
pygame.init()
pygame.mixer.init()
# Загрузка музыкального файла
pygame.mixer.music.load('/Users/nurmatto/Desktop/nurmatto/HackOrJam/music/button_sound.mp3')
class Knopka():
    def __init__(self, image, rect):
        self.image = image
        self.rect = rect

    def draw(self, surface):
        # Получаем текущее положение мыши
        pos = pygame.mouse.get_pos()

        # Проверяем, находится ли курсор мыши над кнопкой
        hover = self.rect.collidepoint(pos)

        # Проверяем условия наведения мыши и нажатия кнопки
        action = False
        if hover and pygame.mouse.get_pressed()[0]:
            action = True
            pygame.mixer.music.play()  # Проигрываем музыку

        # Отображаем кнопку на экране
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
    