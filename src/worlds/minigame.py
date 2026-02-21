import pygame
from settings import *
from entities.entities import Enemy

class MiniGame:
    def __init__(self, game):
        self.game = game

        self.player = pygame.Rect((WIDTH - WIDTH / 2) / 2 + (WIDTH / 2) / 20, (HEIGHT - HEIGHT / 2) / 2 + HEIGHT / 2 - ((WIDTH / 2) / 20 + 10), (WIDTH / 2) / 20, (WIDTH / 2) / 20)
        self.finish = pygame.Rect((WIDTH - WIDTH / 2) / 2 + WIDTH / 2 - ((WIDTH / 2) / 20 + 10), (HEIGHT - HEIGHT / 2) / 2 + (WIDTH / 2) / 20, (WIDTH / 2) / 20, (WIDTH / 2) / 20)
        self.rect = pygame.Rect((WIDTH // 4),(HEIGHT // 4),(WIDTH // 2),(HEIGHT // 2)) 
        self.surface = pygame.Surface(self.rect.size)
        self.enemy = Enemy(pygame.Rect((WIDTH / 4), (HEIGHT / 4), (WIDTH / 2) / 20, (WIDTH / 2) / 20), self.surface)

    def update(self, dt):
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

    def draw(self, screen):
        self.surface.fill((20, 20, 20))
        pygame.draw.rect(self.surface, GREEN, self.finish.move(-self.rect.x, -self.rect.y))
        pygame.draw.rect(self.surface, RED, self.player.move(-self.rect.x, -self.rect.y))
        self.enemy.draw(self.surface)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        screen.blit(self.surface, self.rect.topleft)