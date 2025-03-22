For this week, we will add our player and our inventory!


Step 1:
it turns out we were using the wrong version of pygame :D. The most updated version is in fact called pygame-ce (which is the community edition)
First, uninstall the current pygame by putting these commands in your vscode terminal:
pip uninstall pygame

Then, install pygame-ce:
pip install pygame-ce

And confirm that pygame-ce is being used: python -c "import pygame; print(pygame.__file__); print(pygame.version.ver)"

Next we will install pygame_gui, which will allow us to make a button and window for our inventory. Run this command in vscode terminal: pip install pygame pygame_gui

Perfect, we have installed everything needed for this week’s work! 

Step 2: Add a player to our game
In configuration.py, we create our tilemap using this code
tilemap = []
for i in range(int(MIN_HEIGHT / TILESIZE)):
    row = ''.join(random.choice(['B', 'G']) for _ in range(int(MIN_WIDTH / TILESIZE)))
    tilemap.append(row)

With ‘B’ representing the blocks (trees/flowers) and ‘G’ representing the ground. In this tilemap code add a singular ‘P’ to represent your player. This can be done in many ways; I did it by adding creating a row  with a ‘P’ outside of the for-loop and then appending it to the tilemap outside of the for-loop.

We also have 2 variables for layering, BLOCK_LAYER and TILE_LAYER. Add a third variable PLAYER_LAYER and set it to 3.

Next, we will go into sprites.py to create a player class. Let’s first consider what variables we have initialized in our block class— game, layer, groups, x, y, width, height, image, rect. We will have the same variables in our player class! Tbh you can copy paste the block class and put it in player class. However, instead of getting a random index for our image, we can use the coordinate of the standstill character image— I used (0,1).

        self.image = self.game.player_sheet.get_image(0,1)

In player class, we will now add three new variables in __init__.

        self.x_change = 0
        self.y_change = 0
	
        self.ITEMS = {
            "Coffee Beans": 0,
            "Strawberries": 0,
            "Vanilla": 0,
            "Tea leaves": 0    
        }

x_change and y_change will be used when we create our move function to allow the player to move. The ITEMS are used to keep track of what the player has in their inventory (you are free to change what these items are and how many items you want!). The ITEMS are held in a dictionary; a data structure with key-value pairs. Instead of a list, where to retrieve the amount of coffee beans you would use ITEMS[0], you can instead use ITEMS[“Coffee Beans”]. 

Now we will create the move and update player methods! Note that these are new methods and will not be contained inside of def __init__.

def move(self):
	#your code

def update(self):
	#your code 
In move, we will create one variable which will keep track of which keys the user has pressed.
	pressed = pygame.key.get_pressed()

Then, we can use a series of if-statements to check the value of pressed. Depending on what is pressed, we will set x_change and y_change accordingly. pygame.key.get_pressed() will return a value of 1 if a certain key is pressed. Below is an example for the player’s left movement (using w,a,s,d as the keys)

        if pressed[pygame.K_a] == 1:
            self.x_change = self.x_change - 3
            self.image = self.game.player_sheet.get_image(1,0)

The   self.image = self.game.player_sheet.get_image(1,0) is used to get the left-moving character image in the sprite sheet. Now, you will create three more if-statements to account for right, up and down!

Next, in main.py, add this to your game class __init__ function:  self.player_sheet = Spritesheet('characters.png')

This will allow your player to access the character images.
![Alt text](https://raw.githubusercontent.com/sofievargas/WiCS-Mentor-Group/characters.png)


Finally, in your createTileMap function, add a new ifstatement to check if tilemap[I][j] is ‘P’. If so, create a new player object with:
self.player = Player(self, i,j)


Next, run your game! Your player should be visible and moveable.
