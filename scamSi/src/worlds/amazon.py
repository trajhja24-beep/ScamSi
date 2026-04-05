import pygame
import os
<<<<<<< HEAD
import settings
=======
>>>>>>> 1a999ba5162325de6f5d226f3b8f25df3a277889
from global_set.ui import RenderText
from global_set.products_info import PRODUCTS
from settings import *

class Shop:
    def __init__(self, game, type):
        self.type = type
        self.game = game
        self.minigame_screen = pygame.Rect(((WIDTH - WIDTH / 2) / 2 ,(HEIGHT - HEIGHT / 2) / 2), (WIDTH / 2, HEIGHT / 2))
        self.productsArr = filter_product(PRODUCTS, self.type)
        self.product = []
        for product in self.productsArr:
            self.product.append(productCreate(product))
        self.offset = 15
        self.product = re_pos_prod(self.product, self.offset)
        

    def update(self, dt, screen):
<<<<<<< HEAD
         if pygame.mouse.get_pressed()[0] == True:
            mouse_position = pygame.mouse.get_pos()
            for product in self.product:
                if mouse_position[0] >= product.buy_button.x and mouse_position[0] <= product.buy_button.x + PRODUCTBUYSIZE[0] and mouse_position[1] >= product.buy_button.y and mouse_position[1] <= product.buy_button.y + PRODUCTBUYSIZE[1]:
                    if settings.MONEY >= product.product[2]:
                        settings.MONEY -= product.product[2]
                        print("mas penize")
                        self.game.inventory.update(product)
                        self.game.current_state = self.game.main_world
                    else:
                        print("no money")
=======
        print("test")
>>>>>>> 1a999ba5162325de6f5d226f3b8f25df3a277889
    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), self.minigame_screen)
        for prod in self.product:
            prod.draw(screen)

class productCreate:
    def __init__(self, product):
        self.position = (0,0)
        self.product = product
        base_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(base_dir)
        self.buy_button = pygame.Rect((0,0), PRODUCTBUYSIZE)
        self.buy_text = RenderText(0,0,(225,225,225),"BUY", 1)
        self.bc = pygame.Rect((0,0), PRODUCTBCSIZE)
        self.name_text = RenderText(0,0,(225,225,225),product[1], 1)
<<<<<<< HEAD
        self.price_text = RenderText(0,0, (200,225,200), "$" + str(product[2]), 1)
=======
        self.price_text = RenderText(0,0, (200,225,200), "$" + product[2], 1)
>>>>>>> 1a999ba5162325de6f5d226f3b8f25df3a277889
        self.imgsize = PRODUCTIMGSIZE

        self.image = pygame.image.load(
            os.path.join(base_dir, "assets", product[0])
        ).convert_alpha()

        self.image = pygame.transform.scale(self.image, self.imgsize)
        self.rect = self.image.get_rect(topleft=self.position)
    def draw(self, screen):
        pygame.draw.rect(screen, (75,75,75), self.bc)
        pygame.draw.rect(screen, (0,255,0), self.buy_button)
        self.buy_text.draw(screen)
        self.name_text.draw(screen)
        self.price_text.draw(screen)
        screen.blit(
            self.image,
            (self.rect.x, self.rect.y)
        )

def filter_product(productsAll, type):
    arrFin = []
    for product in productsAll:
        if type in product[4]:
            arrFin.append(product)
    return arrFin
def re_pos_prod(products, offset):
    mini_offset = offset / 3
    y_possition = 0
    updated_arr = []
    base_x = (WIDTH - WIDTH / 2) / 2
    base_y = (HEIGHT - HEIGHT / 2) / 2
    for i in products:
        i.bc.x = base_x + offset
        i.bc.y = base_y + y_possition * PRODUCTBCSIZE[1] + offset * (y_possition + 1)

        i.rect.x = i.bc.x + offset
        i.rect.y = i.bc.y + ((PRODUCTBCSIZE[1] - PRODUCTIMGSIZE[1]) / 2)

        i.name_text.rect.x = i.rect.x + offset * 2 + PRODUCTIMGSIZE[0]
        i.name_text.rect.y = i.bc.y + ((PRODUCTBCSIZE[1] - i.name_text.rect.height) / 2)

        i.price_text.rect.x = i.name_text.rect.x + i.name_text.rect.width + offset
        i.price_text.rect.y = i.bc.y + ((PRODUCTBCSIZE[1] - i.price_text.rect.height) / 2)

        i.buy_button.x = i.bc.width + i.bc.x - (mini_offset + PRODUCTBUYSIZE[0])
        i.buy_button.y = i.bc.y + ((PRODUCTBCSIZE[1] - PRODUCTBUYSIZE[1]) / 2)

        i.buy_text.rect.x = i.buy_button.x + ((PRODUCTBUYSIZE[0] - i.buy_text.rect.width) / 2)
        i.buy_text.rect.y = i.bc.y + ((PRODUCTBCSIZE[1] - PRODUCTBUYSIZE[1]) / 2) + ((PRODUCTBUYSIZE[1] - i.buy_text.rect.height) / 2)

        updated_arr.append(i)

        y_possition += 1

    return updated_arr

        