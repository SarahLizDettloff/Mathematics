import os
import sys
import operator

global index
index = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}

global board
board = [[0] * 8 for x in xrange(8)]
global piece_location


class rook(object):

    def __init__(self, piece_location):
        self.rook_moves(piece_location)

    def rook_moves(self, piece_location):
        """
        Calculates and prints the possible moves for the rook.
        """
        PossibleMoves = []
        x, y = index[piece_location[:1]], int(piece_location[1]) + 1
        print "Possible moves for the rook in location {} are: ".format(piece_location)
        for y in xrange(9):
            if y != 0 and y != int(piece_location[1]):
                move_y = str(piece_location[:1]) +  str(y)
                PossibleMoves.append(move_y)
        for x in xrange(9):
            if x != 0 and x != index[piece_location[:1]]:
                try:
                    move_x = index.keys()[x] + str(piece_location[1])
                    PossibleMoves.append(move_x)
                except:
                    pass
        print sorted(PossibleMoves[:])

class knight(object):
    def __init__(self, piece_location):
        self.knight_moves(piece_location)

    def knight_moves(self, piece_location):
        """
        Calculates and prints the possible moves for the knight piece.
        """
        PossibleMoves = []
        x, y = index[piece_location[:1]], piece_location[1]
        moves = [ index.keys()[(x - 1)] + str(int(y) - 1),
                  index.keys()[(x - 1)] + str(int(y) + 1),
                  index.keys()[(x - 2)] + str(int(y) - 2),
                  index.keys()[(x - 2)] + str(int(y) + 2),
                  index.keys()[(x)] + str(int(y) - 2),
                  index.keys()[(x)] + str(int(y) + 2),
                  index.keys()[(x + 3)] +  str(int(y) - 1),
                  index.keys()[(x + 3)] + str(int(y) + 1),
                 ]
        print "Possible moves for the knight in location {} are: ".format(piece_location)
        for each_possible_moves in moves:
            try:
                PossibleMoves.append(each_possible_moves)
            except:
                pass
        print PossibleMoves
        

class pawn(object):

    def __init__(self, piece_location):
        self.pawn_moves(piece_location)

    def pawn_moves(self, piece_location):
        """
        Calculates and prints the possible moves for the pawn.
        """
        PossibleMoves = []
        x, y = index[piece_location[:1]], piece_location[1]
        first_moves = [index.keys()[x] + str(int(y) + 1),
                 index.keys()[x] + str(int(y) + 2)
                 ]
        moves_after_1st = [index.keys()[x] + str(int(y) + 1)
                           ]
        answer = raw_input("First move? (y/n)\n")
        answer = answer.upper()
        if answer == "Y" or answer == "YES":
            moves = first_moves
        elif answer == "N" or answer == "NO":
            moves = moves_after_1st
        else:
            print("Enter one of the following:\nYes\nNo\y\nn")
            pawn_moves()
        for each_possible_moves in moves:
            PossibleMoves.append(each_possible_moves)
        print PossibleMoves

class king(object):

    def __init__(self, piece_location):
        self.king_moves(piece_location)

    def king_moves(self, piece_location):
        """
        Calculates and prints the possible moves for the king piece.
        """
        PossibleMoves = []
        x, y = index[piece_location[:1]], piece_location[1]
        moves = [ index.keys()[(x - 1) + 1] + str(int(y) - 1),
                  index.keys()[(x)] + y,
                  index.keys()[(x - 1) + 1] + str(int(y) + 1),
                  index.keys()[(x - 1)] + str(int(y) - 1),
                  index.keys()[(x - 1)] + str(int(y) + 1),
                  index.keys()[x + 2] + str(int(y) - 1),
                  index.keys()[x + 2] + y,
                  index.keys()[x + 2] + str(int(y) + 1)
                 ]
        print "Possible moves for the king in location {} are: ".format(piece_location)
        for each_possible_moves in moves:
            PossibleMoves.append(each_possible_moves)
        print PossibleMoves

global piece_type
piece_type = {
    "rook": rook,
    "knight": knight,
 #   "queen": queen,
 #   "bishop": bishop,
    "pawn": pawn,
    "king": king
}

class Main(object):

    def __init__(self):
        self.run()

    def newgame(self):
        clear = lambda: os.system('cls')
        clear()

    def run(self):

        board = [[0] * 8 for x in xrange(8)]
        piece = raw_input("Enter the type of the piece: \n")
        piece = piece.lower()

        if piece not in piece_type:
            print("Please enter rook, knight, king, or pawn. Queen and bishop will be added in the future.")
            Main()
        try:
            piece_location = raw_input("Enter the location of that piece: \n")
            if 1 <= int(piece_location[1]) <= 8:
                pass
            else:
                raise exception
        except:
            print("That is an invalid location. The first letter must be a through h, the second must be a digit 0-7.\n")
            piece_location = None
            piece = None
            Main()
        try:
            piece_type[piece](piece_location)
        except Exception as KeyError:
            pass

    def another_piece():
        another = raw_input("Do you want to move another piece?\nEnter 1 for Yes or 2 for No.\n")
        if another == "1":
            Main()
        else:
            exit()


if __name__=="__main__":
    Main()
