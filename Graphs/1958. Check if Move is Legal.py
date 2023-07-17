class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:

        board = [['.']*10] + [                      #  <--  border the board with ['.'] cells
                 ['.']+row+['.'] for row in board]+ [ 
                 ['.']*10]

        other = 'B' if color == 'W' else 'W'

        dir = ((-1,-1), (-1,0), (-1, 1),            #   <--  The eight directions
               ( 0,-1),         ( 0, 1),
               ( 1,-1), ( 1,0), ( 1, 1))

        for dr, dc in dir:

            r, c = rMove + 1 + dr, cMove + 1 + dc   #   <--  First, check whether cell adj to 
            if board[r][c] != other: continue       #        move cell is the other color

            while board[r][c] == other:             #   <--  Second, iterate through any 
                r+= dr                              #        other-color cells
                c+= dc

            if board[r][c] == color: return True    #   <--  Third, if the cell after the string 
                                                    #        of other-color cells is a color cell
        return False
