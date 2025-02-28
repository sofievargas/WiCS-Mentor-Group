import pygame
from configuration import *
import sys
from sprites import *

"""
MAIN.PY
This file manages:
- Game initialization
- The main game loop
- Rendering and event handling
Follow each step to complete the class!
"""

class Spritesheet:
    """
    Loads and slices a spritesheet into individual tiles.
    No changes needed here.
    """
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path).convert()
        self.sheet_width = 128
        self.sheet_height = 240
        self.sprites = []

        for i in range(self.sheet_height // TILESIZE):
            row_sprites = []
            for j in range(self.sheet_width // TILESIZE):
                sprite = pygame.Rect(j * TILESIZE, i * TILESIZE, TILESIZE, TILESIZE)
                row_sprites.append(self.spritesheet.subsurface(sprite))
            self.sprites.append(row_sprites)

    def get_image(self, x, y):
        """
        Retrieves an individual sprite from the spritesheet.
        :param x: Column index
        :param y: Row index
        :return: The selected sprite image
        """
        return self.sprites[y][x]  # Ensure correct row-column order


class Game:
    """
    The main game class handles:
    - Initialization
    - The game loop
    - Rendering and updating objects
    """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((MIN_WIDTH, MIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.terrain = Spritesheet('basictiles.png')
        self.running = True

    def create_tilemap(self):
        """
        Step 1:
        - Use a nested loop to iterate through the tilemap (from configuration.py)
        - If the tile is 'B', create a Block object
        - If the tile is 'G', create a Ground object
        """
        # Your code here:
        pass

    def create(self):
        """
        Step 2:
        - Initialize a sprite group (LayeredUpdates for rendering order)
        - Call create_tilemap() to generate the world
        """
        self.all_sprites = pygame.sprite.LayeredUpdates()
        #your code here
        pass

    def update(self):
        """
        Updates all game objects each frame.
        """
        self.all_sprites.update()

    def events(self):
        """
        Step 3:
        - Loop through pygame events
        - If the event type is pygame.QUIT, set self.running to False
        """
        # Your code here:
        pass

    def draw(self):
        """
        Step 4:
        - Fill the screen with BG_COLOR
        - Draw all sprites
        - Update the display
        """
        # Your code here:
        pass

    def main(self):
        """
        Step 5:
        - Run the game loop while self.running is True
        - Call events(), update(), and draw() each frame
        """
        while self.running:
            # Call the necessary functions
            pass

"""
Step 6:
- Initialize a new Game object
- Call the create() method
"""
game = None  # Replace None with your code
game.


#Run the game loop
while game.running:
    game.main()

#Cleanly exit Pygame when the game is closed
pygame.quit()
sys.exit()

"""
Next Step -> sprites.py
"""
