from Player import *
from Hand import *
from Board import *

class NaivePlayer(Player):
    """The NaivePlayer class inherits from the Player class and is therefore defined by those three
The fields (age, name and hand.) A naive player is a player who lays the first stone corresponding to the stones
Which are on the board. """
    def __init__(self, name, age, hand):
        """
Constructor for NaivePlayer class.
        :param name: string
        :param age: int
        :param hand: Hand object
        """
        Player.__init__(self, name, age, hand)

    def play(self, board):
        """
A method that performs a single move for the NaivePlayer player. A naive player moves over the hand starting from
the domino in the first position. A player places the first stone he can put on the board. First the player
try to add the stone to the right side of the board and then to the left side. If the player managed to add a domino
for the board, the board is updated accordingly and the stone is removed from the player's hand
        :param board: Domino game board
        :return: True if the player succeed to put a domino on the board and False otherwise
        """
        if len(board) == 0:
            board.add(self.hand[0])
            self.hand.remove_domino(self.hand[0])
            return True
        for part in self.hand.array:
            if board.add_right(part):
                self.hand.remove_domino(part)
                return True
            if board.add_left(part):
                self.hand.remove_domino(part)
                return True
        return False




