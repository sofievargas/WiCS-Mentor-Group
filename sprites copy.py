import pygame
from configuration import *
import sys
from sprites import *

"""The sprites class is responsible for creating new block (trees) and 
ground objects for display in your map.
"""
    

class Block(pygame.sprite.Sprite):
    """
    1. fill in the __init__ function:
        It should take three parameters: which game object it belongs to, an x value and a y value
    """
    def __init__(self, , , ):
        """1a. pass your game parameter in to set the self game variable"""
        self.game = 
        
        """1b. set the layer variable to BLOCK_LAYER"""
        self._layer = 

        """1c. set the groups variable by passing the block's game.all_sprites variable"""
        self.groups = 

        pygame.sprite.Sprite.__init__(self,self.groups)

        """1d. set the x and y variables by passing in the TILESIZE variable and multiplying it by x and y, respectively"""
        self.x = _ * _
        self.y = _ * _

        """1e. set the width and height variables to TILESIZE"""
        self.width = 
        self.height = 

        """Below are the coordinates for the different tree images (see basictiles.png)"""
        block_tiles = [(4,2),(6,3),(6,4)]

        """1f. We will now randomly generate which tree gets displayed
            - create an index using the random variable to select a coordinate from block_tiles
            - use the rand_index to pass in the chosen block_tiles coordinates as the x and y
            - set the rect x and rect y variables as the self.x and self.y variables from earlier
        """

        rand_index = random.randint
        self.image = self.game.terrain.get_image(block_tiles[][], block_tiles[][])
        self.rect = self.image.get_rect()
        self.rect.x = 
        self.rect.y = 
        
"""
2. complete the same steps for the ground tiles!
    instead of setting self.layer to BLOCK_LAYER, set it to GROUND_LAYER
"""
class Ground(pygame.sprite.Sprite):
    def __init__(self, , , ):
        self.game = 
        self._layer= 
        self.groups = 
        pygame.sprite.Sprite.__init__(self,self.groups)


        self.x = _*_
        self.y = _*_

        self.width = 
        self.height = 
        ground_tiles = [(3,1),(4,1),(0,8),(1,8)]
        rand_index = random.randint
        self.image = self.game.terrain.get_image(ground_tiles[][], ground_tiles[][])
        
        self.rect = self.image.get_rect()
        self.rect.x = 
        self.rect.y = 

"""
3. Run main.py to see if your map is generated!
"""


