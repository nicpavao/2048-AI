# import statements
import random

# game functions

def newgame(width,height):
    board = []
    randTwo = [random.randint(0,3),random.randint(0,3)]
    for i in range(width):
        board.append([])
        for j in range(height):
            if randTwo == [i,j]:
                board[i].append(1)
            else:
                board[j].append(0)
    return board

class NewGame_2048():

    def __init__(self):
        self.board = newgame()

    def left(self):
        pass
    def right(self):
        pass
    def up(self):
        pass
    def down(self):
        pass

# main script
if __name__ == "__main__":
    print()