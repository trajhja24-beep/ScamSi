import pygame
import os
from settings import *
from worlds.minigame import MiniGame
from worlds.minigame import MiniGameCrypto
from worlds.amazon import Shop
import math

class Screen:
    def __init__(self, game: "Game", screen: pygame.Surface) -> None:
        """zadefinovani rozmeru obrayovky a aplikaci na ni"""
        self.game = game
        self.minigame_screen = pygame.Rect(((WIDTH - WIDTH / 2) / 2 ,(HEIGHT - HEIGHT / 2) / 2), (WIDTH / 2, HEIGHT / 2))
        self.apps = [
            AppCreate("close.png", (0,0), self.game.main_world),
            AppCreate("play.png", (0,0), MiniGame(self.game, screen, enemy_count(self.game))),
	        AppCreate("play.png", (0,0), MiniGameCrypto(self.game, screen, enemy_count(self.game))),
            AppCreate("amazon.jpg", (0,0), Shop(self.game, "a")),
            AppCreate("amazon.jpg", (0,0), Shop(self.game, "g"))
        ]
        self.offset = 15
        self.grid_size = 4
        self.updated_app = setAppsPosition(self.apps, self.offset, self.grid_size)
    def update(self, dt: float, screen: pygame.Surface) -> None:
        """kontrola kliknuti od uzivatele"""
        if pygame.mouse.get_pressed()[0] == True:
            mouse_position = pygame.mouse.get_pos()
            for app in self.updated_app:
                for y in range(DESKTOPAPPSIZE):
                    for x in range(DESKTOPAPPSIZE):
                        if mouse_position[0] == x + app.rect.x and mouse_position[1] == y + app.rect.y:
                            self.game.current_state = app.act
    def draw(self, screen: pygame.Surface) -> None:
        """vykresleni"""
        pygame.draw.rect(screen, (10, 10, 10), self.minigame_screen)
        for app in self.updated_app:
            app.draw(screen)


class AppCreate:
    def __init__(self, image_path: str, position: list[int], act) -> None:
        """zadefinovani ikonky aplikace"""
        self.act = act
        base_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(base_dir)
        self.size = (DESKTOPAPPSIZE, DESKTOPAPPSIZE)

        self.image = pygame.image.load(
            os.path.join(base_dir, "assets", image_path)
        ).convert_alpha()

        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=position)
    def draw(self, screen: pygame.Surface) -> None:
        """vykresleni"""
        screen.blit(
            self.image,
            (self.rect.x, self.rect.y)
        )

def setAppsPosition(apps: list, offset: int, grid_size: int) -> list:
    """offsetnuti aplikaci tak aby byli v gridu"""
    updated_app = []
    app_position_x = 0
    app_position_y = 0
    base_x = (WIDTH - WIDTH / 2) / 2
    base_y = (HEIGHT - HEIGHT / 2) / 2
    for i in apps:
        if app_position_x > grid_size:
            app_position_x = 0
            app_position_y += 1
        i.rect.x = base_x + app_position_x * DESKTOPAPPSIZE + offset
        i.rect.y = base_y + app_position_y * DESKTOPAPPSIZE + offset
        updated_app.append(i)
        app_position_x += 1

    return updated_app
def enemy_count(game) -> int:
    """urcuje uroven slozitosti miniher"""
    enemy_count = math.floor(game.progress_bar.progress * 0.05)
    if enemy_count == 0:
        enemy_count = 1
    return enemy_count

