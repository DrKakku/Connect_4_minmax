from itertools import groupby, chain
import math
import random

NONE = '.'
RED = 'R'
YELLOW = 'Y'
global win 
win = False

def diagonalsPos (matrix, cols, rows):
	"""Get positive diagonals, going from bottom-left to top-right."""
	for di in ([(j, i - j) for j in range(cols)] for i in range(cols + rows -1)):
		yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]

def diagonalsNeg (matrix, cols, rows):
	"""Get negative diagonals, going from top-left to bottom-right."""
	for di in ([(j, i - cols + j + 1) for j in range(cols)] for i in range(cols + rows - 1)):
		yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < cols and j < rows]

class Player:
    def __init__ (self,token, board, requiredToWin = 4):
        """Create a new game."""
        self.token = token
        self.board = board
        self.win = requiredToWin

    def checkForWin (self):

        w = self.getWinner()
        if w:
            self.printBoard()
            print(w+" Has won")
         
    def insert (self, column):
        """Insert the color in the given column."""
        c = self.board[column]
        if c[0] != NONE:
            print('Column is full')
            
        i = -1
        while c[i] != NONE:
            i -= 1
        c[i] = self.token
        
        self.checkForWin()

    def getWinner (self):
        """Get the winner on the current board."""
        lines = (
			self.board, # columns
			zip(*self.board), # rows
			diagonalsPos(self.board, self.cols, self.rows), # positive diagonals
			diagonalsNeg(self.board, self.cols, self.rows) # negative diagonals
		)
        
        
        for line in chain(*lines):
            for color, group in groupby(line):
                if color != NONE and len(list(group)) >= self.win:
                    return color
    
    def randomPlay(self):
        return (random.uniform(0,len(self.board)-1))






class Game:

    def returnBoard(self):
        return self.board

    def checkForWin (self):

        w = self.getWinner()
        if w:
            self.isWin = True
            self.printBoard()
            print(w+" Has won")
     
    def __init__ (self, cols = 7, rows = 6, requiredToWin = 4):
        """Create a new game."""
        self.cols = cols
        self.rows = rows
        self.win = requiredToWin
        self.isWin = False
        self.board = [[NONE] * rows for _ in range(cols)]
        
    def getWin(self):
        return self.isWin
        
    def insert (self, column, color,win):
        """Insert the color in the given column."""
        c = self.board[column]
        if c[0] != NONE:
            print('Column is full')
            win = True
            
        i = -1
        while c[i] != NONE:
            i -= 1
        c[i] = color
        
        self.checkForWin()
        
        
        
    def getWinner (self):
        """Get the winner on the current board."""
        lines = (
			self.board, # columns
			zip(*self.board), # rows
			diagonalsPos(self.board, self.cols, self.rows), # positive diagonals
			diagonalsNeg(self.board, self.cols, self.rows) # negative diagonals
		)
        
        
        for line in chain(*lines):
            for color, group in groupby(line):
                if color != NONE and len(list(group)) >= self.win:
                    return color
            
            
    def printBoard (self):
        """Print the board."""
        print('  '.join(map(str, range(self.cols))))
        for y in range(self.rows):
            print('  '.join(str(self.board[x][y]) for x in range(self.cols)))
        print()
    

#figure out the heuristic first
# next move ho gaya by entering all pieces to every row
# Random ai is also working
#now generate the heurestic fir MinMax can be implemented

if __name__ == '__main__':
    g = Game()
    ai = Player(YELLOW,g.returnBoard())
    turn = RED
    while not g.getWin():
        g.printBoard()
        if turn == RED:
            row = input('{}\'s turn: '.format('Red' ))
        # if turn == RED else 'Yellow'
        g.insert(int(row), turn,win) if turn == RED else g.insert(int(ai.randomPlay()), turn,win)
        turn = YELLOW if turn == RED else RED