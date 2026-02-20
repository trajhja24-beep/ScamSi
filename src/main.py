import pygame
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from settings import *
from entities.player import Player
from global_set.ui import ProgressBar
from worlds.main_world import MainWorld



pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

player_path = os.path.join(BASE_DIR, "assets", "player.png")
player_img = pygame.image.load(player_path).convert_alpha()
player_img = pygame.transform.scale(player_img, (50, 50))

player = Player(player_img, (WIDTH // 2, HEIGHT // 2))

progress_bar = ProgressBar(WIDTH - 250, HEIGHT - 40, 200, 20)

class Game:
    def __init__(self):
        self.player = player
        self.progress_bar = progress_bar
        self.main_world = MainWorld(self)
        self.current_state = self.main_world

game = Game()

running = True
while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.current_state.update(dt)
    game.current_state.draw(screen)

    pygame.display.flip()

pygame.quit()