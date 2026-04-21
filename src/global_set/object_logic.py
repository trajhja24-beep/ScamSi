import pygame
from settings import PLAYER_SIZE

class Gun:
    def __init__(self):
        self.target = pygame.image.load("assets/target.png").convert_alpha()
        self.target = pygame.transform.scale(self.target, PLAYER_SIZE)
        self.target_rect = self.target.get_rect()
    def update(self, police=None):
        mouse_pos = pygame.mouse.get_pos()
        self.target_rect.center = mouse_pos
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            print("Gun updating")

        return police

    def draw(self, screen):
        screen.blit(self.target, self.target_rect)