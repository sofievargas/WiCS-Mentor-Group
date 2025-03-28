import pygame
import pygame_gui as gui
from configuration import *
import sys
import json
from sprites import *

class Spritesheet:
    """
    Handles loading and slicing a spritesheet into individual tiles.
    """
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path).convert()
        self.sheet_width = self.spritesheet.get_width()
        self.sheet_height = self.spritesheet.get_height()
        self.sprites = []
        for i in range(int(self.sheet_height/16)):
            row_sprites = []
            for j in range(int(self.sheet_width/16)):
                sprite = pygame.Rect(j*TILESIZE, i*TILESIZE, TILESIZE, TILESIZE)
                row_sprites.append(self.spritesheet.subsurface(sprite))
            self.sprites.append(row_sprites)

    def get_image(self, x,y):
        sprite = self.sprites[x][y]
        return sprite



class Inventory:
    """
    The Main inventory class handles the player's tools and items.
    """
    def __init__(self,manager, player):
        self.manager = manager
        self.player = player
        self.inventory_button = gui.elements.UIButton(
            relative_rect=pygame.Rect((40,40),(32,32)),
            text="",
            manager=self.manager)

        self.inventory_window = gui.elements.UIWindow(
            rect= pygame.Rect((40,64),(200,300)),
            window_display_title="Inventory",
            manager=self.manager,
            visible=False
        )

        self.inventory_text = gui.elements.UITextBox(
            html_text= "TEST TEXT" , #"json.dumps(player.ITEMS, indent=4),
            relative_rect=pygame.Rect((10,40),(150,150)),
            manager=self.manager,
            container=self.inventory_window,
            visible=True
        )

    def update_inventory(self, player):
        item_lines = [f"{key} : {value}" for key, value in player.ITEMS.items()]
        new_text = "\n".join(item_lines)
        self.inventory_text.set_text(new_text)

    def toggle_inventory(self):
        self.inventory_window.visible = not self.inventory_window.visible
        self.inventory_text.visible = not self.inventory_text.visible


class Game:
    """
    The Main game class handles initialization, looping the game, + rendering.

    __init__ is similar to a java constructor; 
    when you create a new Game object the following variables will be initialized
    """
    def __init__(self):
        self.screen = pygame.display.set_mode((MIN_WIDTH, MIN_HEIGHT))
        self.clock = pygame.time.Clock()
        print(pygame.font.get_default_font())
        pygame.font.init()
        self.manager = gui.UIManager((MIN_WIDTH, MIN_HEIGHT), theme_path="inventory.json")
        self.player_sheet = Spritesheet('characters.png')
        self.terrain = Spritesheet('basictiles.png')
        self.running = True
    """
    You will create the TileMap Here!
    """
    def createTileMap(self):
        for i in range (len(tilemap)):
            for j in range (len(tilemap[i])):
                if tilemap[i][j] == 'B':
                    Block(self,i,j)
                if tilemap[i][j] == 'G':
                    Ground(self,i,j)
                if tilemap[i][j] == 'P':
                    self.player = Player(self, i,j)
                    self.inventory = Inventory(self.manager, self.player)

    def create(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.createTileMap()

    def update(self, time_delta):
        self.all_sprites.update()
        self.inventory.update_inventory(self.player)
        self.manager.update(time_delta)
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.inventory.inventory_button:
                    print('hello! Your inventory: \n')
                    print(self.player.ITEMS)
                    self.inventory.toggle_inventory()
            self.manager.process_events(event)

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        self.manager.draw_ui(self.screen)
        pygame.display.update()

    def main(self):
        while game.running:
            time_delta = self.clock.tick(FPS)/1000.0
            self.events()
            self.update(time_delta)
            self.draw()
        






game = Game()
game.create()

game.main()

pygame.quit()
sys.exit()