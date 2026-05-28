"""ui ten overlay vsechno so nenio vlastne svet"""


import pygame
import os
from settings import FONT
from settings import SLOTSIZE
from settings import LEVEL

class ProgressBar:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        """basic definice progress baru na stres"""
        self.border_rect = pygame.Rect(x, y, width, height)
        self.progress = 0
    def set(self, value: int) -> None:
        """nastaveni pokroku progres baru na stres"""
        self.progress = max(0, min(100, value))

    def draw(self, screen: pygame.Surface)-> None:
        """vykresleni samotneho progressbaru"""
        fill_width = int(self.border_rect.width * (self.progress / 100))
        fill_rect = self.border_rect.copy()
        fill_rect.width = fill_width

        pygame.draw.rect(screen, (255, 0, 0), fill_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.border_rect, 2)



class ExpBar:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        """basic definice progress baru na levely a exp"""
        self.border_rect = pygame.Rect(x, y, width, height)
        self.curent_level = LEVEL
        self.progress = 0
    def set(self, value: int) -> None:
        """nastaveni pokroku progres baru na exp"""
        self.progress += value
        #while self.progress >= 100 + 10 * self.curent_level:
        # print(100 + 10 * self.curent_level)
        # text = "added " + str(value) + "_curent level" + str(self.progress)
        # print(text)
        if self.progress >= 100 + 10 * self.curent_level:
            #print("add level")
            self.curent_level += 1
            self.progress = 0

    def draw(self, screen: pygame.Surface) -> None:
        """vykresleni samotneho progressbaru"""
        fill_width = int(self.border_rect.width * (self.progress / (100 + 10 * self.curent_level)))
        fill_rect = self.border_rect.copy()
        fill_rect.width = fill_width

        pygame.draw.rect(screen, (255, 255, 0), fill_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.border_rect, 2)




class RenderText:
    def __init__(self, x: int, y: int, color: tuple[int, int, int], msg: str, size: int) -> None:
        """funcke pro renderovani textu nastaveni zakladnu barva velikos co kde"""
        self.font = pygame.font.SysFont(None, FONT * size)
        self.hint_surface = self.font.render(msg, False, color)
        self.rect = self.hint_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, screen: pygame.Surface) -> None:
        """vykresleni textu"""
        screen.blit(self.hint_surface, self.rect)
class Inventory:
    def __init__(self, slot_count: int, x: int, y: int, game) -> None:
        """zakladni definice invetare a vytvareni slotu"""
        self.game = game
        self.slots = []
        if slot_count < 0:
            slot_count = 1
        for i in range(slot_count):
            self.slots.append(CreateSlot(i, x,y))

        self.background = pygame.Rect(x, y, SLOTSIZE[0] * slot_count, SLOTSIZE[1])
    def update(self, item) -> None:
        """pridavani itemu do prvniho volneho slotu"""
        if item:
            for slot in self.slots:
                if slot.free == True:
                    slot.free = False
                    slot.set_item(item)
                    break
        
    def draw(self, screen: pygame.Surface) -> None:
        """vykresleni inventare"""
        pygame.draw.rect(screen, (150,150,150, 0), self.background)
        for slot in self.slots:
            slot.draw(screen)

class CreateSlot:
    def __init__(self, slot_number: int, x: int, y: int) -> None:
        """Vytvoreni a definice zakladnich parametru jednotlivych slotu"""
        self.slot_number = slot_number
        self.free = True
        self.chosen = False
        self.slot = pygame.Rect(x + SLOTSIZE[1] * self.slot_number, y,SLOTSIZE[0], SLOTSIZE[1])
        self.image = None
        self.position = (self.slot.x, self.slot.y)
        self.chosen_color = (255,255,255, 1)
    def set_item(self, item) -> None:
        """Zapsani itemu do slotu"""
        self.item = item
        base_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(base_dir)
        self.image = pygame.image.load(
            os.path.join(base_dir, "assets", item.product[0])
        ).convert_alpha()
        self.image = pygame.transform.scale(self.image,(SLOTSIZE[0], SLOTSIZE[1]))
        self.rect = self.image.get_rect(topleft=(self.position))
    def draw(self, screen: pygame.Surface) -> None:
        """vykresleni"""
        if self.chosen == False:
            pygame.draw.rect(screen, (200,200,200, 1), self.slot)
        else:
            pygame.draw.rect(screen, self.chosen_color, self.slot)
        if self.free == False:
            screen.blit(
                self.image,
                (self.rect.x, self.rect.y)
            )

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}

    def load(self, name, path):
        self.sounds[name] = pygame.mixer.Sound(path)

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].play()

    def set_volume(self, name, volume):
        if name in self.sounds:
            self.sounds[name].set_volume(volume)

