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
        
        #self.game.inventory.update(self.game.owned_items)
        if keys[pygame.K_e]:
            for object in self.objects:
                if object.is_colliding(self.game.player, self.camera):
                    self.game.current_state = Screen(self.game, screen) #MiniGame(self.game, screen, self.enemy_count)

        for slot in range(len(self.game.inventory.slots)):
            slot += 1
            key = getattr(pygame, f"K_{slot}")
            slot -= 1
            if keys[pygame.K_f] and self.game.inventory.slots[slot].free == False and self.game.inventory.slots[slot].chosen == True:
                self.game.inventory.slots[slot].free = True
                settings.MONEY_BOOST += self.game.inventory.slots[slot].item.product[5][0]
                
                self.game.player.curentItem = False
                self.game.inventory.slots[slot].image == False
                self.game.inventory.slots[slot].rect == False

            if keys[key]:
                
                for i in self.game.inventory.slots:
                    i.chosen = False
                self.game.inventory.slots[slot].chosen = True
                self.game.player.hold_item(self.game.inventory.slots[slot])
            
    def draw(self, screen):
        screen.fill(BLACK)
        self.background.draw(screen, self.camera)
        for object in self.objects:
            object.draw(screen, self.camera)
        self.game.player.draw(screen)
        self.game.progress_bar.draw(screen)
        self.game.inventory.draw(screen)
        RenderText(WIDTH - 200, HEIGHT - 100, GREEN, "$" + str(settings.MONEY), 1).draw(screen)
        for object in self.objects:
            if object.is_colliding(self.game.player, self.camera):
                self.hintText.draw(screen)