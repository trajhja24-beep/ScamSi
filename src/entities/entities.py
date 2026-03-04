import pygame
import random
from settings import *

class Enemy:
    def __init__(self, enemy, screen):
        self.enemy = enemy
        self.screen = screen
        self.speed = MINIGAME_ENEMY_SPEED + random.randint(-2, 1)
        self.enemy.x += random.randint(-100, 100)
        self.enemy.y += random.randint(-100, 100)
        self.enemy.height += random.randint(-25, 25)
        self.enemy.width += random.randint(-25, 25)

    def move_toward(self, target):
        if random.choice([True, False]):
            if self.enemy.x < target.x:
                if self.enemy.right + self.speed <= self.screen.width:
                    self.enemy.x += self.speed + random.randint(-2, 2)
            else:
                self.enemy.x -= self.speed + random.randint(-2, 2)
        else:
            if self.enemy.y < target.y:
                self.enemy.y += self.speed + random.randint(-2, 2)
            else:
                self.enemy.y -= self.speed + random.randint(-2, 2)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.enemy)