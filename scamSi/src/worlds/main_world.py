from worlds.object_create import WorldObject
from worlds.minigame import MiniGame
from worlds.desktop import Screen
from settings import *
from global_set.ui import RenderText

import pygame
import settings
import math

class MainWorld:
    def __init__(self, game):
        self.enemy_count = 2
        self.game = game
        self.camera = [0, 0]
        self.hintText = RenderText(100, HEIGHT - 100, GREEN, "Press E", 1)
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
<<<<<<< HEAD
        
        if keys[pygame.K_e]:
            for object in self.objects:
                if object.is_colliding(self.game.player, self.camera):
=======
        if keys[pygame.K_e]:
            for object in self.objects:
                if object.is_colliding(self.game.player, self.camera):
                    
>>>>>>> 1a999ba5162325de6f5d226f3b8f25df3a277889
                    self.game.current_state = Screen(self.game, screen) #MiniGame(self.game, screen, self.enemy_count)
    def draw(self, screen):
        screen.fill(BLACK)
        self.background.draw(screen, self.camera)
        for object in self.objects:
            object.draw(screen, self.camera)
        self.game.player.draw(screen)
        self.game.progress_bar.draw(screen)
<<<<<<< HEAD
        self.game.inventory.draw(screen)
=======
>>>>>>> 1a999ba5162325de6f5d226f3b8f25df3a277889
        RenderText(WIDTH - 200, HEIGHT - 100, GREEN, "$" + str(settings.MONEY), 1).draw(screen)
        for object in self.objects:
            if object.is_colliding(self.game.player, self.camera):
                self.hintText.draw(screen)