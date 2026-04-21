import pygame
import os
from settings import FONT
from settings import SLOTSIZE

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
class RenderText:
    def __init__(self, x, y, color, msg, size):
        self.font = pygame.font.SysFont(None, FONT * size)
        self.hint_surface = self.font.render(msg, False, color)
        self.rect = self.hint_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, screen):
        screen.blit(self.hint_surface, self.rect)
class Inventory:
    def __init__(self, slot_count, x, y, game):
        self.game = game
        self.slots = []
        if slot_count < 0:
            slot_count = 1
        for i in range(slot_count):
            self.slots.append(CreateSlot(i, x,y))

        self.background = pygame.Rect(x, y, SLOTSIZE[0] * slot_count, SLOTSIZE[1])
    def update(self, item):
        if item:
            for slot in self.slots:
                if slot.free == True:
                    slot.free = False
                    slot.set_item(item)
                    break
        
    def draw(self, screen):
        pygame.draw.rect(screen, (150,150,150, 0), self.background)
        for slot in self.slots:
            slot.draw(screen)

class CreateSlot:
    def __init__(self, slot_number, x, y):
        self.slot_number = slot_number
        self.free = True
        self.chosen = False
        self.slot = pygame.Rect(x + SLOTSIZE[1] * self.slot_number, y,SLOTSIZE[0], SLOTSIZE[1])
        self.image = None
        self.position = (self.slot.x, self.slot.y)
        self.chosen_color = (255,255,255, 1)
    def set_item(self, item):
        self.item = item
        base_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(base_dir)
        self.image = pygame.image.load(
            os.path.join(base_dir, "assets", item.product[0])
        ).convert_alpha()
        self.image = pygame.transform.scale(self.image,(SLOTSIZE[0], SLOTSIZE[1]))
        self.rect = self.image.get_rect(topleft=(self.position))
    def draw(self, screen):
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

