"""
CONFIGURATION.PY
This file defines the fixed variables of the game:
- Screen dimensions
- Frames per second (FPS)
- Tile size and layers
- Background color
- Tilemap generation (custom or random)
"""

import random

# Step 1: Set the dimensions of the game screen (replace None with integer values)
MIN_WIDTH = None  # Example: 320
MIN_HEIGHT = None  # Example: 240

# Step 2: Define the tile size (fixed at 16 pixels)
TILESIZE = 16

# Step 3: Set layer values (higher values render on top of lower values)
BLOCK_LAYER = 2
GROUND_LAYER = 1

# Step 4: Set frames per second (FPS) and background color (RGB format)
FPS = 
BG_COLOR = (None, None, None)  # Example: (123,168,66) for green

# Step 5: Create a custom tilemap, or randomly generate one
# 'B' = Block (tree), 'G' = Ground (grass)
tilemap = []
for i in range(int(MIN_HEIGHT / TILESIZE)):
    row = ''.join(random.choice(['B', 'G']) for _ in range(int(MIN_WIDTH / TILESIZE)))
    tilemap.append(row)

"""
Next Step -> main.py
"""
