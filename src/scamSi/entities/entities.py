import pygame
import random
from settings import *
import os
from pathlib import Path

class Enemy:
    def __init__(self, enemy: pygame.Rect, screen: pygame.Surface) -> None:
        """zakladni definice nepritele v minihre tam jak jdes y bodu a do b"""
        self.enemy = enemy
        self.screen = screen
        self.speed = MINIGAME_ENEMY_SPEED + random.randint(-2, 1)
        self.enemy.x += random.randint(-100, 100)
        self.enemy.y += random.randint(-100, 100)
        self.enemy.height += random.randint(-25, 25)
        self.enemy.width += random.randint(-25, 25)

    def move_toward(self, target) -> None:
        """bohyp nepritele k danemu cili"""
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

    def draw(self, screen: pygame.Surface) -> None:
        """vykresleni nepritele"""
        pygame.draw.rect(screen, (0, 0, 255), self.enemy)

class Police:
    def __init__(self, BASE_DIR: Path, screen: pygame.Surface) -> None:
        """zakladni definice policistu kteri se zobrazuji v hlavnim svete"""
        self.screen = screen
        self.healt = 100
        image_path = os.path.join(BASE_DIR, "assets", "player.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.start_pos = (WIDTH // 3, HEIGHT // 3)
        self.rect = self.image.get_rect(center=self.start_pos)
        self.speed = PLAYER_SPEED - 1
    def update(self, target) -> None:
        """pohyb policisty ke hraci pokud zijou"""
        if self.healt > 0:
            if random.choice([True, False]):
                if self.rect.x < target[0]:
                    if self.rect.right + self.speed <= self.screen.width:
                        self.rect.x += self.speed + random.randint(-2, 2)
                else:
                    self.rect.x -= self.speed + random.randint(-2, 2)
            else:
                if self.rect.y < target[1]:
                    self.rect.y += self.speed + random.randint(-2, 2)
                else:
                    self.rect.y -= self.speed + random.randint(-2, 2)
    def draw(self, screen: pygame.Surface, camera: tuple[int, int]) -> None:
        """vykresleni policistu pokud zijou"""
        if self.healt > 0:
            screen.blit(
                self.image,
                (self.rect.x - camera[0], self.rect.y - camera[1])
            )
        
        