from Player import *
from Domino import *
from Board import *
from Hand import *
import copy


class MaxScorePlayer(Player):
    """The MaxScorePlayer class is inherited from the Player class and is therefore defined by
the same three fields (age, name and hand.) A Max Score Player tries to get rid of dominoes first
have the highest score"""
    def __init__(self, name, age, hand):
        """
Constructor for MaxScorePlayer class.
        :param name: string
        :param age: int
        :param hand: Hand object
        """
        Player.__init__(self, name, age, hand)

    def play(self, board):
        """
A method that performs a single move for the MaxScorePlayer player. The player wants to reduce the
score during the current move and therefore will put on the board the domino stone with the maximum value.
If there are two dominoes having the same value it is possible to decide on an arrangement between them at random
        :param board: Domino game board
        :return: True if the player succeed to put a domino on the board and False otherwise
        """
        copy_hand = copy.deepcopy(self.hand)
        def find_max():
            temp = 0
            temp_index = 0
            if len(board) == 0:
                board.add(self.hand[0])
                self.hand.remove_domino(self.hand[0])
                return True
            for domino_index in range(len(copy_hand.array)):
                sum_one_domino = copy_hand.array[domino_index].get_right() + copy_hand.array[domino_index].get_left()
                if sum_one_domino > temp:
                    temp = sum_one_domino
                    temp_index = domino_index
            return try_put_in_board(temp_index)


        def try_put_in_board(temp_index):
            if board.add_right(copy_hand.array[temp_index]):
                self.hand.remove_domino(self.hand.array[temp_index])
                return True
            if board.add_left(copy_hand.array[temp_index]):
                self.hand.remove_domino(self.hand.array[temp_index])
                return True
            if len(copy_hand.array) == 1:
                return False
            copy_hand.remove_domino(copy_hand.array[temp_index])
            return find_max()
        return find_max()

    def __str__(self):
        """
String representing the player according to the following format:
Name: name, Age: age, Hand: hand, Score: self.score(), I can win the
game!
        :return: The method will return a string representing the player
        """
        return f'Name: {self.name}, Age: {self.age}, Hand: {self.hand}, Score: {self.score()}, I can win the game!'






