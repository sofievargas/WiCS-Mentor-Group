"""
CONFIGURATION.PY
This file is for the fixed variables of the game:
- Dimensions
- Frames per Second

"""
import random

#dimensions of the game
MIN_WIDTH = 800
MIN_HEIGHT = 800
TILESIZE = 16
FPS = 60

PLAYER_LAYER = 3
BLOCK_LAYER = 2
TILE_LAYER = 1

BLACK = (123,168,66)

#our tile map will be 14x20 block, or a '2D' list (list of 14 x 20-character strings)

tilemap = [
]
row_1 = ''.join(random.choice(['B','G']) for _ in range(int(MIN_WIDTH/TILESIZE/2)))
row_1 = row_1 + 'P'
row_1 = row_1 + ''.join(random.choice(['B','G']) for _ in range(int(MIN_WIDTH/TILESIZE/2) -1))
tilemap.append(row_1)
for i in range(int(MIN_HEIGHT/TILESIZE)-1):
        row = ''.join(random.choice(['B', 'G']) for _ in range(int(MIN_WIDTH/TILESIZE)))
        tilemap.append(row)
