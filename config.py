### This file contains game options for snake
import matplotlib

# Game seconds between frames
frame_delay = 0.25

# Board properties
board_x = 20 # Board shape, size
board_y = 20
board_color = matplotlib.colormaps['summer'].copy()
board_color.set_over('red')

# Snake properties
snake_length = 3

# Human control or ai control ('human' or 'ai')
player = 'human'