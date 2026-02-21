import pygame
from settings import PLAYER_SPEED

class Player:
    def __init__(self, image, start_pos):
        self.image = image
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = PLAYER_SPEED

    def move_world(self, keys, camera):
        if keys[pygame.K_a]:
            camera[0] -= self.speed
        if keys[pygame.K_d]:
            camera[0] += self.speed
        if keys[pygame.K_w]:
            camera[1] -= self.speed
        if keys[pygame.K_s]:
            camera[1] += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)