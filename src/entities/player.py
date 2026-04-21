import pygame
import os
from settings import PLAYER_SPEED
from settings import PLAYER_SIZE

class Player:
    def __init__(self, image, start_pos, main_word):
        self.main_word = main_word
        self.image = image
        self.start_pose = start_pos
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = PLAYER_SPEED
        self.itemimage = ""
        self.curentItem = False

    def move_world(self, keys, camera, objects):
        self.camera = camera
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
    def hold_item(self, item):
        if item.free == False:
            self.curentItem = item
            base_dir = os.path.dirname(os.path.abspath(__file__))
            base_dir = os.path.dirname(base_dir)
            self.itemimage = pygame.image.load(
                os.path.join(base_dir, "assets", item.item.product[0])
            ).convert_alpha()
            self.itemimage = pygame.transform.scale(self.itemimage,(PLAYER_SIZE[0] / 2,PLAYER_SIZE[1] / 2))
            self.itemRect = self.itemimage.get_rect(topleft=(self.start_pose[0], self.start_pose[1]))
        else:
            self.curentItem = False
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if not self.curentItem == False:
            screen.blit(self.itemimage, self.itemRect)

    def get_world_position(self):
        if not hasattr(self, "camera"):
            return self.rect.center
        world_x = self.rect.x + self.camera[0]
        world_y = self.rect.y + self.camera[1]
        return [world_x, world_y]