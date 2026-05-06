import pygame
import os
import random

class WorldObject:
    def __init__(self, image_path, position, size, logic=None):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(base_dir)

        self.image = pygame.image.load(
            os.path.join(base_dir, "assets", image_path)
        ).convert_alpha()

        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=position)
        self.logic = logic
    def draw(self, screen, camera):
        screen.blit(
            self.image,
            (self.rect.x - camera[0], self.rect.y - camera[1])
        )
    def is_colliding(self, player, camera):
        return self.rect.colliderect(player.rect.move(camera))