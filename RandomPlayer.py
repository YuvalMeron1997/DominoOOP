import copy
import random
from Player import Player
from Hand import *
from Board import *

class RandomPlayer(Player):
    """The RandomPlayer class inherits from the Player class and is therefore defined by
the three fields (age, name and hand). A random player before each move randomly arranges
his hand and places the first stone corresponding to the stones on the board."""
    def __init__(self, name, age, hand):
        """
Constructor for RandomPlayer class.
        :param name: string
        :param age: int
        :param hand: Hand object
        """
        Player.__init__(self, name, age, hand)

    def play(self, board):
        """
A method that performs a single move for the RandomPlayer player.
The hand randomly and then move the hand starting from the domino stone in the 0 position. The player put
on the board the first stone he can put on the board. First the player tries to add the stone to the right side of
the board then to the left. If the player was able to add a domino to the board the board is updated accordingly and the stone
removed from the player's hand
        :param board: Domino game board
        :return: True if the player succeed to put a domino on the board and False otherwise
        """
        # Don't change this line and don't move it!
        random.seed(12)  # You can read about seed here: https://en.wikipedia.org/wiki/Random_seed
        # TODO: write your code after this line
        old_hand = copy.deepcopy(self.hand.array)
        random.shuffle(old_hand)
        if len(board) == 0:
            board.add(old_hand[0])
            self.hand.remove_domino(old_hand[0])
            return True
        for index_part in range(len(old_hand)):
            if board.add_right(old_hand[index_part]):
                self.hand.remove_domino(old_hand[index_part])
                return True
            if board.add_left(old_hand[index_part]):
                self.hand.remove_domino(old_hand[index_part])
                return True
        return False


