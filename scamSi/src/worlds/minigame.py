import pygame
import settings
import os
from settings import *
from main import BASE_DIR
from entities.entities import Enemy
from settings import PLAYER_SPEED
from entities.player import Player

class MiniGame:
    def __init__(self, game, screen, enemy_count):
        self.minigame_start = False
        self.game = game
        self.main_screen = screen
        self.player = pygame.Rect((settings.WIDTH - WIDTH / 2) / 2 + (WIDTH / 2) / 20, (HEIGHT - HEIGHT / 2) / 2 + HEIGHT / 2 - ((WIDTH / 2) / 20 + 10), (WIDTH / 2) / 20, (WIDTH / 2) / 20)
        
        self.finish = pygame.Rect((WIDTH - WIDTH / 2) / 2 + WIDTH / 2 - ((WIDTH / 2) / 20 + 10), (HEIGHT - HEIGHT / 2) / 2 + (WIDTH / 2) / 20, (WIDTH / 2) / 20, (WIDTH / 2) / 20)
        self.rect = pygame.Rect(((WIDTH - WIDTH / 2) / 2 ,(HEIGHT - HEIGHT / 2) / 2), (WIDTH / 2, HEIGHT / 2)) 
        self.enemys = []
        for x in range(enemy_count):
            self.enemys.append(Enemy(pygame.Rect((WIDTH / 2), (HEIGHT / 2), (WIDTH / 2) / 20, (WIDTH / 2) / 20), self.main_screen))

    def update(self, dt, screen):
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
                settings.MONEY += 10
                self.game.current_state = self.game.main_world
            for enemy in self.enemys:
                if self.player.colliderect(enemy.enemy):
                    self.game.progress_bar.set(
                        self.game.progress_bar.progress + 10
                    )

                    settings.MONEY -= 5

                    self.game.current_state = self.game.main_world

    def draw(self, main_screen):
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

        self.rect = pygame.Rect(((WIDTH - WIDTH / 2) / 2 ,(HEIGHT - HEIGHT / 2) / 2), (WIDTH / 2, HEIGHT / 2))
        player_path = os.path.join(BASE_DIR, "assets", "player.png")
        player_img = pygame.image.load(player_path).convert_alpha()
        player_img = pygame.transform.scale(player_img, (50, 50))
        self.player = Player(player_img, (WIDTH // 2, HEIGHT // 2), self.game.main_world)
        self.player2 = pygame.Rect((settings.WIDTH - WIDTH / 2) / 2 + (WIDTH / 2) / 20, (HEIGHT - HEIGHT / 2) / 2 + HEIGHT / 2 - ((WIDTH / 2) / 20 + 10), (WIDTH / 2) / 20, (WIDTH / 2) / 20)
    def update(self, dt, screen):
        keys = pygame.key.get_pressed()
        self.player.move_world(keys, self.camera, [])
    def draw(self, main_screen):
        pygame.draw.rect(self.main_screen, (10, 10, 10), self.rect)
        self.player.draw(self.rect)
        pygame.draw.rect(self.main_screen, RED, self.player2)

