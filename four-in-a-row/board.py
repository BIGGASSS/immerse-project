import utils

class Board:
    def __init__(self):
        pass

    grid = []

    def init_board(self):
        self.grid = [[0 for _ in range(7)] for _ in range(6)] # columns == 7, rows == 6
    def show_board(self):
        for i in range(len(self.grid)):
            print(self.grid[i])
    def deter_bottom(self, col): # Determines the bottom of the columns
        tmp = 0
        i = 0
        if self.grid[0][col] != 0:
            return -1
        while tmp == 0:
            if i < 6:
                tmp = self.grid[i][col]
                i += 1
            else:
                return 5
        return i-2
    def place(self, col, turn):
        if self.deter_bottom(col) == -1:
            return False
        if turn == "Player 1":
            self.grid[self.deter_bottom(col)][col] = 1
        else:
            self.grid[self.deter_bottom(col)][col] = 2
        return True
    def check_win(self, side):
        for row in range(6): # Horizontal
            for col in range(4):
                if (self.grid[row][col] == side and self.grid[row][col + 1] == side 
                    and self.grid[row][col + 2] == side and self.grid[row][col + 3] == side):
                    return True
        for row in range(3): # Vertical 
            for col in range(7):
                if (self.grid[row][col] == side and self.grid[row + 1][col] == side and 
                    self.grid[row + 2][col] == side and self.grid[row + 3][col] == side):
                    return True
        for row in range(3): # Top-left to bottom-right
            for col in range(4):
                if (self.grid[row][col] == side and self.grid[row + 1][col + 1] == side and 
                    self.grid[row + 2][col + 2] == side and self.grid[row + 3][col + 3] == side):
                    return True
        for row in range(3): # Top-right to bottom-left
            for col in range(3, 7):
                if (self.grid[row][col] == side and self.grid[row + 1][col - 1] == side and 
                    self.grid[row + 2][col - 2] == side and self.grid[row + 3][col - 3] == side):
                    return True
        return False
    def bot_place(self):
        for i in [3, 2, 4, 1, 5, 0, 6]: # Prioritize columns in the middle
            if self.deter_bottom(i) != -1:
                return i
        return utils.rand_int(0, 6) # Fallback to random integer