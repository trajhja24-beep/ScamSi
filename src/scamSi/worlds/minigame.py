import pygame
import settings
import os
from settings import *
from entities.entities import Enemy
from settings import PLAYER_SPEED
import settings
from entities.player import Player


class MiniGame:
    def __init__(self, game, screen: pygame.Surface, enemy_count: int) -> None:
        """zadefinovani minihry samotne"""
        self.minigame_start = False
        self.game = game
        self.main_screen = screen
        self.player = pygame.Rect((settings.WIDTH - WIDTH / 2) / 2 + (WIDTH / 2) / 20, (HEIGHT - HEIGHT / 2) / 2 + HEIGHT / 2 - ((WIDTH / 2) / 20 + 10), (WIDTH / 2) / 20, (WIDTH / 2) / 20)
        
        self.finish = pygame.Rect((WIDTH - WIDTH / 2) / 2 + WIDTH / 2 - ((WIDTH / 2) / 20 + 10), (HEIGHT - HEIGHT / 2) / 2 + (WIDTH / 2) / 20, (WIDTH / 2) / 20, (WIDTH / 2) / 20)
        self.rect = pygame.Rect(((WIDTH - WIDTH / 2) / 2 ,(HEIGHT - HEIGHT / 2) / 2), (WIDTH / 2, HEIGHT / 2)) 
        self.enemys = []
        for x in range(enemy_count):
            self.enemys.append(Enemy(pygame.Rect((WIDTH / 2), (HEIGHT / 2), (WIDTH / 2) / 20, (WIDTH / 2) / 20), self.main_screen))
        print("minigame Run")

    def update(self, dt: float, screen: pygame.Surface) -> None:
        """
            kontra a reseni pohybu

            reseni vysledku minihry win/loss
        """

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_s] or keys[pygame.K_w]:
            self.minigame_start = True


        if self.minigame_start:

            if keys[pygame.K_a]:
                if self.player.left - MINIGAME_PLAYER_SPEED >= self.rect.left:
                    self.player.x -= MINIGAME_PLAYER_SPEED

            if keys[pygame.K_d]:
                if self.player.right + MINIGAME_PLAYER_SPEED <= self.rect.right:
                    self.player.x += MINIGAME_PLAYER_SPEED

            if keys[pygame.K_w]:
                if self.player.top - MINIGAME_PLAYER_SPEED >= self.rect.top:
                    self.player.y -= MINIGAME_PLAYER_SPEED

            if keys[pygame.K_s]:
                if self.player.bottom + MINIGAME_PLAYER_SPEED <= self.rect.bottom:
                    self.player.y += MINIGAME_PLAYER_SPEED
            for enemy in self.enemys:
                enemy.move_toward(self.player)

            if self.player.colliderect(self.finish):
                self.game.progress_bar.set(
                    self.game.progress_bar.progress - 5
                )
                settings.MONEY += 10 * settings.MONEY_BOOST
                self.game.current_state = self.game.main_world
            for enemy in self.enemys:
                if self.player.colliderect(enemy.enemy):
                    self.game.progress_bar.set(
                        self.game.progress_bar.progress + 10
                    )

                    settings.MONEY -= 5 

                    self.game.current_state = self.game.main_world

    def draw(self, main_screen: pygame.Surface) -> None:
        """vykresleni"""
        pygame.draw.rect(self.main_screen, (10, 10, 10), self.rect)
        pygame.draw.rect(self.main_screen, GREEN, self.finish)
        pygame.draw.rect(self.main_screen, RED, self.player)
        for enemy in self.enemys:
            enemy.draw(self.main_screen)





class MiniGameCrypto:
    def __init__(self, game, screen, difficulty):

        
        self.speed = PLAYER_SPEED
        self.camera = [0, 0]
        self.minigame_start = False
        self.game = game
        self.main_screen = screen
        self.line = []
        self.player = pygame.Rect(((WIDTH / 2, HEIGHT / 2)), ((WIDTH / 2) / 20, (WIDTH / 2) / 20))
        self.line.append(self.player)
    def update(self, dt, screen):
        keys = pygame.key.get_pressed()
        self.player.x += 1
        if dt % 2 == 0: 
            self.player.y += 1
    def draw(self, main_screen):
        minigame_screen(main_screen)
        for player in self.line:
            pygame.draw.rect(main_screen, GREEN, player)
        
def minigame_screen(main_screen):
    rect = pygame.Rect(((WIDTH - WIDTH / 2) / 2 ,(HEIGHT - HEIGHT / 2) / 2), (WIDTH / 2, HEIGHT / 2))
    pygame.draw.rect(main_screen, (10, 10, 10), rect)

