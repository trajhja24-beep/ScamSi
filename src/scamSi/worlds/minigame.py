import pygame
import settings
import os
from settings import *
from entities.entities import Enemy
from settings import PLAYER_SPEED
import settings
from entities.player import Player
import random
from global_set.ui import RenderText


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
        #print("minigame Run")

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
                self.game.exp_bar.set(
                    40
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
        pygame.draw.rect(main_screen, (10, 10, 10), self.rect)
        pygame.draw.rect(main_screen, GREEN, self.finish)
        pygame.draw.rect(main_screen, RED, self.player)
        for enemy in self.enemys:
            enemy.draw(main_screen)





class MiniGameCrypto:
    def __init__(self, game, screen, difficulty):
        self.game = game
        self.screen = screen

        self.score = 100

        self.price = HEIGHT // 2
        self.points = []

        self.current_number = random.randint(1, 3)

        self.timer = 0

        self.difficulty = max(1, min(4, difficulty))

        self.time_limit = {
            1: 3.0,
            2: 2.0,
            3: 1.2,
            4: 0.8
        }[self.difficulty]

        self.speed = 120
        self.trend = 0

        self.finished = False
        self.win = False

        self.font = pygame.font.SysFont(None, 50)

        self.spacing = 8

    def reset_number(self):
        self.current_number = random.randint(1, 3)
        self.timer = 0
        self.trend = random.choice([-1, 1]) * random.uniform(20, 60)

    def check_answer(self, value):
        if self.finished:
            return

        if value == self.current_number:
            self.score += 10
            self.trend += 25
            self.price -= 10
        else:
            self.score -= 10
            self.trend -= 25
            self.price += 10

        self.reset_number()

    def update(self, dt, screen):
        if self.finished:
            return

        keys = pygame.key.get_pressed()

        self.timer += dt

        if self.timer >= self.time_limit:
            self.score -= 10
            self.price += 10
            self.reset_number()

        if keys[pygame.K_1]:
            self.check_answer(1)
        elif keys[pygame.K_2]:
            self.check_answer(2)
        elif keys[pygame.K_3]:
            self.check_answer(3)

        noise = random.uniform(-1, 1) * self.speed * dt
        self.price += self.trend * dt + noise

        self.price = max(100, min(HEIGHT - 100, self.price))

        self.points.append(self.price)

        max_points = WIDTH // self.spacing
        if len(self.points) > max_points:
            self.points = self.points[-max_points:]

        if self.score <= 0:
            self.finished = True
            self.win = False

        if self.score >= 200:
            self.finished = True
            self.win = True

    def draw(self, screen):

        mid_x = WIDTH // 2
        mid_y = HEIGHT // 2

        if len(self.points) > 1:
            for i in range(1, len(self.points)):
                x1 = mid_x + (i - len(self.points)) * self.spacing
                x2 = mid_x + (i - len(self.points) + 1) * self.spacing

                y1 = self.points[i - 1]
                y2 = self.points[i]

                pygame.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2), 2)

        pygame.draw.line(screen, (80, 80, 80), (0, mid_y), (WIDTH, mid_y), 1)

        text = self.font.render(str(self.current_number), True, (255, 255, 255))
        screen.blit(text, (50, 50))

        if self.finished:
            msg = "YOU WIN" if self.win else "YOU LOSE"
            end_text = self.font.render(msg, True, (255, 0, 0))
            screen.blit(end_text, (mid_x - 100, mid_y))
def minigame_screen(main_screen):
    rect = pygame.Rect(((WIDTH - WIDTH / 2) / 2 ,(HEIGHT - HEIGHT / 2) / 2), (WIDTH / 2, HEIGHT / 2))
    pygame.draw.rect(main_screen, (10, 10, 10), rect)

