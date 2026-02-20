import pygame
import random
from settings import MINIGAME_ENEMY_SPEED

class Enemy:
    def __init__(self, enemy, screen):
        self.enemy = enemy
        self.screen = screen
        self.speed = MINIGAME_ENEMY_SPEED

    def move_toward(self, target):
        if random.choice([True, False]):
            if self.enemy.x < target.x:
                if self.enemy.right + self.speed <= self.screen.width:
                    self.enemy.x += self.speed
            else:
                self.enemy.x -= self.speed
        else:
            if self.enemy.y < target.y:
                self.enemy.y += self.speed
            else:
                self.enemy.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.enemy)