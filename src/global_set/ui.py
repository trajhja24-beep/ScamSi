import pygame

class ProgressBar:
    def __init__(self, x, y, width, height):
        self.border_rect = pygame.Rect(x, y, width, height)
        self.progress = 0

    def set(self, value):
        self.progress = max(0, min(100, value))

    def draw(self, screen):
        fill_width = int(self.border_rect.width * (self.progress / 100))
        fill_rect = self.border_rect.copy()
        fill_rect.width = fill_width

        pygame.draw.rect(screen, (255, 0, 0), fill_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.border_rect, 2)