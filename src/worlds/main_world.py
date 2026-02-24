from worlds.object_create import WorldObject
from worlds.minigame import MiniGame
from settings import *
from global_set.ui import RenderText
import pygame

class MainWorld:
    def __init__(self, game):
        self.game = game
        self.camera = [0, 0]
        self.hintText = RenderText(100, HEIGHT - 100, GREEN, "Press E")
        self.objects = [
             WorldObject(
                "object.png",
                (700, 400),
                (100, 50)
            )
        ]
        self.background = WorldObject(
            "bc.jpg",
            (0, 0),
            (2000, 2000)
        )
    def update(self, dt, screen):
        keys = pygame.key.get_pressed()
        self.game.player.move_world(keys, self.camera, self.objects)
        if keys[pygame.K_e]:
            for object in self.objects:
                if object.is_colliding(self.game.player, self.camera):
                    self.game.current_state = MiniGame(self.game, screen)
    def draw(self, screen):
        screen.fill(BLACK)
        self.background.draw(screen, self.camera)
        for object in self.objects:
            object.draw(screen, self.camera)
        self.game.player.draw(screen)
        self.game.progress_bar.draw(screen)
        for object in self.objects:
            if object.is_colliding(self.game.player, self.camera):
                self.hintText.draw(screen)