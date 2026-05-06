from worlds.object_create import WorldObject
from worlds.minigame import MiniGame
from worlds.desktop import Screen
from settings import *
from global_set.ui import RenderText
from global_set.object_logic import Gun
from entities.entities import Police

import pygame
import settings
import math

ITEM_CLASSES = {
    "gun": Gun
}

OBJECT_CLASSES = {
    "pc": Screen,
    "" : Shop
}

class MainWorld:
    def __init__(self, game, BASE_DIR):
        self.BASE_DIR = BASE_DIR
        self.police = []
        self.enemy_count = 2
        self.game = game
        self.camera = [0, 0]
        self.hintText = RenderText(100, HEIGHT - 100, GREEN, "Press E", 1)
        self.objects = [
             WorldObject(
                "object.png",
                (700, 400),
                (100, 50),
                "pc"
            ),
            WorldObject(
                "object.png",
                (1000, 400),
                (100, 50)
            )
        ]
        self.background = WorldObject(
            "bc.jpg",
            (0, 0),
            (2000, 2000)
        )
        self.police_spawn_timer = 0
        self.police_spawn_delay = 5
    def update(self, dt, screen):
        self.police_spawn_timer += dt
        if self.game.progress_bar.progress >= 100 and len(self.police) < 3 and self.police_spawn_timer >= self.police_spawn_delay:
            self.police.append(Police(self.BASE_DIR, screen))
            self.police_spawn_timer = 0.0

        player_pos = self.game.player.get_world_position()
        self.police = [p for p in self.police if p.healt > 0]
        for police in self.police:
            police.update(player_pos)
        keys = pygame.key.get_pressed()
        self.game.player.move_world(keys, self.camera, self.objects)
        
        #self.game.inventory.update(self.game.owned_items)
        if keys[pygame.K_e]:
            for object in self.objects:
                if object.is_colliding(self.game.player, self.camera):
                    
                    
                    if not object.logic == None:

                        if object.logic in OBJECT_CLASSES:
                            
                            object.logic = OBJECT_CLASSES[object.logic](self.game, screen)
                        self.game.current_state = object.logic                     #Screen(self.game, screen) #MiniGame(self.game, screen, self.enemy_count)
                    
        for slot_index in range(len(self.game.inventory.slots)):
            key = getattr(pygame, f"K_{slot_index + 1}")
            slot = self.game.inventory.slots[slot_index]

            if keys[key]:
                for i in self.game.inventory.slots:
                    i.chosen = False

                slot.chosen = True
                self.game.player.hold_item(slot)

                if not slot.free:
                    item = slot.item

                    if not hasattr(item, "logic"):
                        try:
                            item_type = slot.item.product[6]

                            if item_type in ITEM_CLASSES:
                                
                                item.logic = ITEM_CLASSES[item_type]()
                            else:
                                
                                item.logic = None

                        except IndexError:
                            item.logic = None

            if not slot.free and slot.chosen:
                if keys[pygame.K_f]:
                    item = slot.item

                    if hasattr(item, "logic"):
                        del item.logic

                    slot.free = True
                    settings.MONEY_BOOST += item.product[5][0]

                    self.game.player.curentItem = False
                    slot.image = False
                    slot.rect = False

            if not slot.free and slot.chosen:
                logic = getattr(slot.item, "logic", None)
                if logic:
                    logic.update(dt ,self.camera,slot ,self.police)
        # for slot in range(len(self.game.inventory.slots)):
        #     slot += 1
        #     key = getattr(pygame, f"K_{slot}")
        #     slot -= 1
        #     if keys[key]:
                
        #         for i in self.game.inventory.slots:
        #             i.chosen = False
        #         self.game.inventory.slots[slot].chosen = True
        #         self.game.player.hold_item(self.game.inventory.slots[slot])

        #         if not self.game.inventory.slots[slot].free:
        #             item = self.game.inventory.slots[slot].item

        #             if not hasattr(item, "logic"):
        #                 try:
        #                     item_type = item.product[6]

        #                     if item_type in ITEM_CLASSES:
        #                         item.logic = ITEM_CLASSES[item_type](self)
        #                     else:
        #                         item.logic = None

        #                 except IndexError:
        #                     item.logic = None
        #     if self.game.inventory.slots[slot].free == False and self.game.inventory.slots[slot].chosen == True:
                
        #         if keys[pygame.K_f]:
                    
        #             self.game.inventory.slots[slot].free = True
        #             settings.MONEY_BOOST += self.game.inventory.slots[slot].item.product[5][0]
                    
        #             self.game.player.curentItem = False
        #             self.game.inventory.slots[slot].image = False
        #             self.game.inventory.slots[slot].rect = False
        #     if not self.game.inventory.slots[slot].free and self.game.inventory.slots[slot].chosen:
        #         logic = getattr(self.game.inventory.slots[slot].item, "logic", None)
        #         if logic:
        #             logic.update()
            
    def draw(self, screen):
        screen.fill(BLACK)
        self.background.draw(screen, self.camera)
        for object in self.objects:
            object.draw(screen, self.camera)
        self.game.player.draw(screen)
        if self.police:
            for p in self.police:
                p.draw(screen, self.camera)


        
        self.game.progress_bar.draw(screen)
        self.game.inventory.draw(screen)
        RenderText(WIDTH - 200, HEIGHT - 100, GREEN, "$" + str(settings.MONEY), 1).draw(screen)
        for object in self.objects:
            if object.is_colliding(self.game.player, self.camera):
                self.hintText.draw(screen)

        for slot in self.game.inventory.slots:
            if not slot.free and slot.chosen:
                logic = getattr(slot.item, "logic", None)

                if logic:
                    logic.draw(screen)
                