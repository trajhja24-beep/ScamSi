import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


pygame.init()

def updatePosition(player, sx, sy):
    player.x += sx
    player.y += sy

sx, sy = 1280, 720
screen = pygame.display.set_mode((sx, sy))

pygame.display.set_caption('ScamSImulator')

running = True
fps = 15
clock = pygame.time.Clock()

px = 45
final_sx = (sx - px) / 2
final_sy = (sy - px) / 2

background_path = os.path.join(BASE_DIR, "bc.jpg")
background =  pygame.image.load(background_path).convert_alpha()
background_image = pygame.transform.scale(background, (2000, 2000))

player_path = os.path.join(BASE_DIR, "player.png")
player =  pygame.image.load(player_path).convert_alpha()
player_image = pygame.transform.scale(player, (50, 50))

player_rect = player_image.get_rect()
player_rect.topleft = (final_sx, final_sy)

camera_x = 0
camera_y = 0
speed = 10

move_interval = 0.5
time_since_last_move = 0

while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time_since_last_move += dt
    keys = pygame.key.get_pressed()
    if time_since_last_move >= move_interval:
        if keys[pygame.K_a]:
            camera_x -= speed
        if keys[pygame.K_d]:
            camera_x += speed
        if keys[pygame.K_w]:
            camera_y -= speed
        if keys[pygame.K_s]:
            camera_y += speed
        time_since_last_move = 0
    screen.fill((0, 0, 0))
    screen.blit(background_image, (-camera_x, -camera_y))
    screen.blit(player_image, player_rect)
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()