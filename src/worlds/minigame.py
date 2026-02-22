import pygame
from settings import *
from entities.entities import Enemy

class MiniGame:
    def __init__(self, game, screen):
        self.game = game
        self.main_screen = screen
        self.player = pygame.Rect((WIDTH - WIDTH / 2) / 2 + (WIDTH / 2) / 20, (HEIGHT - HEIGHT / 2) / 2 + HEIGHT / 2 - ((WIDTH / 2) / 20 + 10), (WIDTH / 2) / 20, (WIDTH / 2) / 20)
        self.finish = pygame.Rect((WIDTH - WIDTH / 2) / 2 + WIDTH / 2 - ((WIDTH / 2) / 20 + 10), (HEIGHT - HEIGHT / 2) / 2 + (WIDTH / 2) / 20, (WIDTH / 2) / 20, (WIDTH / 2) / 20)
        self.rect = pygame.Rect(((WIDTH - WIDTH / 2) / 2 ,(HEIGHT - HEIGHT / 2) / 2), (WIDTH / 2, HEIGHT / 2)) 
        
        self.enemy = Enemy(pygame.Rect((WIDTH / 4), (HEIGHT / 4), (WIDTH / 2) / 20, (WIDTH / 2) / 20), self.main_screen)

    def update(self, dt, screen):
        keys = pygame.key.get_pressed()

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

        self.enemy.move_toward(self.player)

        if self.player.colliderect(self.finish):
            self.game.progress_bar.set(
                self.game.progress_bar.progress - 10
            )
            self.game.current_state = self.game.main_world

        # if self.player.colliderect(self.enemy.rect):
        #     self.game.progress_bar.set(
        #         self.game.progress_bar.progress + 10
        #     )
        #     self.game.current_state = self.game.main_world

    def draw(self, main_screen):
        pygame.draw.rect(self.main_screen, (10, 10, 10), self.rect)
        pygame.draw.rect(self.main_screen, GREEN, self.finish)
        pygame.draw.rect(self.main_screen, RED, self.player)
        self.enemy.draw(self.main_screen)