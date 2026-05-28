import pygame
from settings import PLAYER_SIZE
import os

class Gun:
    def __init__(self, BASE_DIR) -> None:
        """nacteni vsech potrebnych assetu pro spravne vykreslovani a funkcnost zbrane"""
        target_path = os.path.join(BASE_DIR, "assets", "target.png")
        self.target = pygame.image.load(target_path).convert_alpha()
        self.target = pygame.transform.scale(self.target, PLAYER_SIZE)
        self.target_rect = self.target.get_rect()
        self.last_fire = 0
        self.delay = 1
    def update(self, dt: float, camera: list[int], slot=None, police=[]) -> None:
        """Logika zbrane aby to strilelo a ubiralo zivoty"""
        self.last_fire += dt
        mouse_pos = pygame.mouse.get_pos()
        self.target_rect.center = mouse_pos
        mouse_buttons = pygame.mouse.get_pressed()
        og_color = slot.chosen_color
        if not self.last_fire >= self.delay:
            slot.chosen_color = (255, 0,0,1)
        else:
            slot.chosen_color = (255,255,255, 1)
        if mouse_buttons[0] and self.last_fire >= self.delay:
            self.last_fire = 0.0
            print("fire")
            world_center = self.target_rect.copy()
            world_center.centerx += camera[0]
            world_center.centery += camera[1]
            for p in police:
                if p.rect.colliderect(world_center):
                    p.healt -= 20
                    break

        

    def draw(self, screen: pygame.Surface) -> None:
        """vykresleni zbrane"""
        screen.blit(self.target, self.target_rect)