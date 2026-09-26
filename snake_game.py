### This is the main program for the snake game.
###
### Christopher Phillips

# Import modules
import config
import snake_class

import threading
import os
from sshkeyboard import listen_keyboard, stop_listening
import matplotlib.pyplot as pp
import numpy as np
import time

# Functions to track keyboard inputs for humans
# Function to track snake direction command
if (config.player == 'human'):
    key = ''
    def snake_dir(press):
        global key
        key = press
        return

    def start_listener():
        listen_keyboard(on_press=snake_dir, sequential=True)

    # Create the keyboard listener on its own thread
    key_thread = threading.Thread(target=start_listener, daemon=True)
    key_thread.start()

# Build the initial game board and add the snake
snake = snake_class.snake()
board = snake.location

# Add the first apple
# Make sure it's not on the snake
apple_loc = [np.random.randint(0, high=config.board_y), 
             np.random.randint(0, high=config.board_x)]
while board[*apple_loc] > 0:
    apple_loc[0] = np.random.randint(0, high=config.board_y)
    apple_loc[1] = np.random.randint(0, high=config.board_x)
board[*apple_loc] = snake.length+1

fig, ax = pp.subplots()
img = ax.imshow(board, origin='lower', vmin=0, vmax=snake.length, cmap=config.board_color)
ax.axis('off')
pp.draw()
pp.show(block=False)
pp.pause(config.frame_delay)

# Delay until user is ready to play (for humans only)
if (config.player == 'human'):
    print("Press 'w' when ready to start.")
    while key != 'w':
        fig.canvas.flush_events()
        time.sleep(0.1)

# Go into the game loop
while True:

    # Get the new snake location
    # Let AI choose a command every frame
    if (config.player == 'ai'):
        pass
    loss_flag = snake.direction(board, key)

    # Check for losing
    if (loss_flag):
        print('You Lose!')
        board[1::2,1::2] = 255 # Checkerboard pattern on board
        board[::2,::2] = 0
        img.set_data(board)
        img.set_clim(0, snake.length)
        pp.draw()
        pp.pause(config.frame_delay+1)
        stop_listening()
        os.system('stty sane')
        break

    board = snake.location

    # Check if an apple was eaten
    if (snake.head == apple_loc):
        while board[*apple_loc] > 0:
            apple_loc[0] = np.random.randint(0, high=config.board_y)
            apple_loc[1] = np.random.randint(0, high=config.board_x)
        board[*apple_loc] = snake.length+1
    else:
        board[*apple_loc] = snake.length+1 # Reset apple after tail was cleared.

    # Draw the new snake
    board = snake.location
    img.set_data(board)
    img.set_clim(0, snake.length)
    pp.draw()
    pp.pause(config.frame_delay)
    fig.canvas.flush_events()