import pygame
import random
from configuration import *
import sys
from sprites import *



class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)


        self.x = x*TILESIZE
        self.y = y*TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE
        block_tiles = [(4,2),(6,3),(6,4)]
        rand_index = random.randint(0,len(block_tiles)-1)
        self.image = self.game.terrain.get_image(block_tiles[rand_index][1], block_tiles[rand_index][0])
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer=TILE_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)


        self.x = x*TILESIZE
        self.y = y*TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE
        ground_tiles = [(3,1),(4,1),(0,8),(1,8)]
        rand_index = random.randint(0,len(ground_tiles)-1)
        self.image = self.game.terrain.get_image(ground_tiles[rand_index][1], ground_tiles[rand_index][0])
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Player(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)


        self.x = x*TILESIZE
        self.y = y*TILESIZE

        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.image = self.game.player_sheet.get_image(0,1)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.direction = "right"

        self.ITEMS = {
            "Coffee Beans": 0,
            "Strawberries": 0,
            "Vanilla": 0,
            "Tea leaves": 0    
        }
        
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a] == 1:
            self.x_change = self.x_change - 3
            self.direction = "left"
            self.image = self.game.player_sheet.get_image(1,0)
        elif pressed[pygame.K_d] == 1:
            self.x_change = self.x_change + 3
            self.direction = "right"
            self.image = self.game.player_sheet.get_image(2,2)
        elif pressed[pygame.K_w] == 1:
            self.y_change = self.y_change - 3
            self.direction = "up"
            self.image = self.game.player_sheet.get_image(3,0)
        elif pressed[pygame.K_s] == 1:
            self.y_change = self.y_change + 3
            self.direction = "down"    
            self.image = self.game.player_sheet.get_image(0,0)
        else:
            if pressed[pygame.K_f] == 1:
                rand = random.choice(list(self.ITEMS.keys()))
                self.ITEMS[rand] = self.ITEMS[rand] + 1

            self.image = self.game.player_sheet.get_image(0,1)

    def update(self):
        self.move() 
        self.rect.x = self.rect.x + self.x_change
        self.rect.y = self.rect.y + self.y_change
            
        self.x_change = 0
        self.y_change = 0