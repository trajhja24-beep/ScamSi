import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()

def show_hint():
        hint_surface = font.render('Press E', False, (0, 255, 0))
        screen.blit(hint_surface, (sx / 20, sy - font_size_medium * 2))

sx, sy = 1280, 720
screen = pygame.display.set_mode((sx, sy))
pygame.display.set_caption("ScamSimulator")
camera_x = 0
camera_y = 0
speed = 10

running = True
fps = 30
clock = pygame.time.Clock()
font_size_medium = 30
font = pygame.font.SysFont('Comic Sans MS', font_size_medium)

player_path = os.path.join(BASE_DIR, "player.png")
player_img = pygame.image.load(player_path).convert_alpha()
player_image = pygame.transform.scale(player_img, (50, 50))

player_screen_rect = player_image.get_rect(center=(sx // 2, sy // 2))
player_world_rect = player_image.get_rect()

background_path = os.path.join(BASE_DIR, "bc.jpg")
background = pygame.image.load(background_path).convert_alpha()
background_image = pygame.transform.scale(background, (2000, 2000))

object_path = os.path.join(BASE_DIR, "object.png")
object_img = pygame.image.load(object_path).convert_alpha()
object_image = pygame.transform.scale(object_img, (100, 50))

object_rect = object_image.get_rect(topleft=(700, 400))
collision_object_rect = object_rect.inflate(speed * 2, speed * 2)


move_interval = 0.01
time_since_last_move = 0

while running:
    dt = clock.tick(fps) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                print("action")

    time_since_last_move += dt
    keys = pygame.key.get_pressed()
    lastKey = ""

    if time_since_last_move >= move_interval:
        if keys[pygame.K_a]:
            lastKey = "a"
            camera_x -= speed
        if keys[pygame.K_d]:
            lastKey = "d"
            camera_x += speed
        if keys[pygame.K_w]:
            lastKey = "w"
            camera_y -= speed
        if keys[pygame.K_s]:
            lastKey = "s"
            camera_y += speed
        time_since_last_move = 0

    player_world_rect.center = (
        camera_x + sx // 2,
        camera_y + sy // 2
    )

    if player_world_rect.colliderect(object_rect):
        if keys[pygame.K_a]:
            camera_x += speed
        if keys[pygame.K_d]:
            camera_x -= speed
        if keys[pygame.K_w]:
            camera_y += speed
        if keys[pygame.K_s]:
            camera_y -= speed
        
    
    screen.fill((0, 0, 0))

    screen.blit(background_image, (-camera_x, -camera_y))

    screen.blit(
        object_image,
        (object_rect.x - camera_x, object_rect.y - camera_y)
    )

    screen.blit(player_image, player_screen_rect)

    colliding_with_objeect = player_world_rect.colliderect(collision_object_rect)

    if colliding_with_objeect:
        show_hint()

        if keys[pygame.K_e] and not e_pressed_last_frame:
            print("action")

    e_pressed_last_frame = keys[pygame.K_e]

    pygame.display.flip()

pygame.quit()
