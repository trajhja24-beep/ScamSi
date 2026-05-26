import pygame
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from settings import *
from entities.player import Player
from global_set.ui import ProgressBar, Inventory, ExpBar
from worlds.main_world import MainWorld


class Game:
    def __init__(self, screen: pygame.Surface, base_dir: str):
        self.progress_bar = ProgressBar(WIDTH - 250, HEIGHT - 40, 200, 20)
        self.exp_bar = ExpBar(WIDTH - 250, HEIGHT - 70, 200, 20)
        self.inventory = Inventory(SLOTCOUNT, 0, 0, self)

        self.main_world = MainWorld(self, base_dir)

        player_path = os.path.join(base_dir, "assets", "player.png")
        player_img = pygame.image.load(player_path).convert_alpha()
        player_img = pygame.transform.scale(player_img, PLAYER_SIZE)

        self.player = Player(player_img, PLAYER_STARTING_POSITION, self.main_world)
        self.current_state = self.main_world


def main() -> None:
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    game = Game(screen, BASE_DIR)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.current_state.update(dt, screen)
        game.current_state.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()