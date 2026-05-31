"""Menu hry hlavni menu"""

from global_set.ui import RenderText
from settings import *
import pygame

class menu:
    def __init__(self, game, base_dir, origin=None) -> None:

        """zadefinovani nayvu tlacitek a kam se to ma smerovat"""
        if origin == None:
            self.origin = game.main_world
        else:
            self.origin = origin

        self.game = game
        self.base_dir = base_dir

        self.minigame_screen = pygame.Rect((0,0), (WIDTH, HEIGHT))

        self.title_text = RenderText(10,10,(225,225,225),"ScamSi", 1) 

        self.play_text = RenderText(10,100,(225,225,225),"plaz", 1)
    def update(self, dt: float, screen: pygame.Surface)  -> None:
        """funkcnost tlacitek a presmerovani"""
        mouse_position = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == True:
            if mouse_position[0] >= self.play_text.rect.x and mouse_position[0] <= self.play_text.rect.x + PRODUCTBUYSIZE[0] and mouse_position[1] >= self.play_text.rect.y and mouse_position[1] <= self.play_text.rect.y + PRODUCTBUYSIZE[1]:

                self.game.current_state = self.origin
            
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, (10, 10, 10), self.minigame_screen)
        self.title_text.draw(screen)
       
        self.play_text.draw(screen)