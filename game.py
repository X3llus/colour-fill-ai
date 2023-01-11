import os
from rich.console import Console
import numpy as np

# Game object for colour fill
class Game:
    console = Console()
    # clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    # initalize 14 by 14 game board with random values 1 to 6
    board = np.random.randint(0, 6, (14, 14))
    # initalize score to 0
    score = 0
    visited = []
    total_captured = 0

    # reset game board and score
    def reset(self):
        self.board = np.random.randint(0, 6, (14, 14))
        self.score = 0

    # get the board
    def getBoard(self):
        return self.board

    # Print the board using numbers
    def print_board(self, board):
        for row in board:
            print(" ".join([str(cell) for cell in row]))

    # Print the board using colours
    def print_board_emoji(self, board):
        emoji_map = {
            0: "🟥",  # red
            1: "🟩",  # green
            2: "🟦",  # blue
            3: "🟪",  # purple
            4: "🟫",  # brown
            5: "🟨",  # yellow
        }
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        for row in board:
            self.console.print("".join([emoji_map[cell] for cell in row]))

    # Flood fill function
    def flood_fill(self, board, x, y, old_color, new_color):
        # Check if the coordinates are out of bounds
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return
        # Check if the cell is not the old color or has already been visited
        if board[x][y] != old_color or board[x][y] == new_color:
            return
        # Change the color of the cell
        board[x][y] = new_color
        # Recursively fill the surrounding cells
        self.flood_fill(board, x+1, y, old_color, new_color)
        self.flood_fill(board, x-1, y, old_color, new_color)
        self.flood_fill(board, x, y+1, old_color, new_color)
        self.flood_fill(board, x, y-1, old_color, new_color)

    def count_captured(self, board, x, y, color) -> int:
        self.visited = []
        captured = self.flood_count(board, x, y, color)
        captured -= self.total_captured
        self.total_captured += captured
        return captured

    def flood_count(self, board, x, y, color) -> int:
        captured: int = 0
        # Check if the coordinates are out of bounds
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return 0
        # Check if the cell is not the old color or has already been visited
        if board[x][y] != color or self.visited.count([x, y]) > 0:
            return 0

        captured += 1
        self.visited.append([x, y])
        # Recursively count the surrounding cells
        captured += self.flood_count(board, x+1, y, color)
        captured += self.flood_count(board, x-1, y, color)
        captured += self.flood_count(board, x, y+1, color)
        captured += self.flood_count(board, x, y-1, color)

        return captured
    
    # Calculate new score
    def calculate_score_gain(self, captured):
        # calculate the new score
        return 100*pow(captured,2) + (900*captured)
