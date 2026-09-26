### This file contains the class for a snake object

# Imports
import config
import numpy as np

# Snake class
class snake:

    # Initialization function
    def __init__(self):

        self.length = config.snake_length
        self.head = [config.board_y//2, config.board_x//2]
        self.location = np.zeros((config.board_y, config.board_x), dtype=int)
        for i in range(self.length):
            self.location[self.head[0]-i, self.head[1]] = self.length-i
        
        self.old_location = self.location

        return

    # Get the new location of the snake
    def direction(self, board, key):
        board = np.array(board, dtype=int)

        # Find the new head
        if (key == 's'):
            self.head[0] = self.head[0]-1
        elif (key == 'w'):
            self.head[0] = self.head[0]+1
        elif (key == 'a'):
            self.head[1] = self.head[1]-1
        elif (key== 'd'):
            self.head[1] = self.head[1]+1

        # Test for leaving the board
        if (self.head[1] >= config.board_x) or (self.head[1] < 0) or (self.head[0] >= config.board_y) or (self.head[0] < 0):
            return True

        # Test if an apple was eaten
        apple_flag = False
        if (board[*self.head] == self.length+1):
            self.length += 1
            self.location += 1 # This will prevent the tail from being cleared
            apple_flag = True

        # Remove the tail
        board[self.location>0] -= 1
        self.location[self.location>0] -= 1

        # Test for the snake colliding with itself
        if (board[*self.head] > 0) and (board[*self.head] < self.length) and (not apple_flag):
            return True

        # Update the head
        self.location[*self.head] = self.length

        return False