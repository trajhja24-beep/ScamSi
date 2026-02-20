import pygame
import os
from settings import *
from worlds.minigame import MiniGame

class MainWorld:
    def __init__(self, game):
        self.game = game
        self.camera = [0, 0]

        base_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(base_dir)

        self.background = pygame.image.load(
            os.path.join(base_dir, "assets", "bc.jpg")
        ).convert()

        self.background = pygame.transform.scale(self.background, (2000, 2000))

        self.object_image = pygame.image.load(
            os.path.join(base_dir, "assets", "object.png")
        ).convert_alpha()
        self.object_image = pygame.transform.scale(self.object_image, (100, 50))
        self.object_rect = self.object_image.get_rect(topleft=(700, 400))

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.game.player.move_world(keys, self.camera)

        if keys[pygame.K_e]:
            self.game.current_state = MiniGame(self.game)

    def draw(self, screen):
        screen.fill(BLACK)
        screen.blit(self.background, (-self.camera[0], -self.camera[1]))
        screen.blit(
            self.object_image,
            (self.object_rect.x - self.camera[0],
             self.object_rect.y - self.camera[1])
        )
        self.game.player.draw(screen)
        self.game.progress_bar.draw(screen)