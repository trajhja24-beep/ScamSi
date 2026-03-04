import pygame
from settings import PLAYER_SPEED

class Player:
    def __init__(self, image, start_pos, main_word):
        self.main_word = main_word
        self.image = image
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = PLAYER_SPEED

    def move_world(self, keys, camera, objects):
        dx = dy = 0
        if keys[pygame.K_a]:
            dx -= 0.5 * self.speed
        if keys[pygame.K_d]:
            dx += 0.5 * self.speed
        if keys[pygame.K_w]:
            dy -=  0.5 * self.speed
        if keys[pygame.K_s]:
            dy += 0.5 * self.speed

        new_camera = [
            camera[0] + dx,
            camera[1] + dy
        ]
        for object in objects:
            if not object.is_colliding(self.main_word.game.player, new_camera):
                if keys[pygame.K_a]:
                    camera[0] -= self.speed
                if keys[pygame.K_d]:
                    camera[0] += self.speed
                if keys[pygame.K_w]:
                    camera[1] -= self.speed
                if keys[pygame.K_s]:
                    camera[1] += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)