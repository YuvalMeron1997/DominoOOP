from Domino import *
from Hand import *
from abc import ABC, abstractmethod

class Player(ABC):
    """A class used to represent a Player.
        :attribute values: name(string), age(int), hand(Hand obgect) ."""
    def __init__(self, name, age, hand):
        """
Constructor for Player class.
        :param name: string
        :param age: int
        :param hand: Hand object
        """
        self.name = name
        self.age = age
        self.hand = hand

    def score(self):
        """
A method that defines the number of points of the player - the sum the dominoes in the hand of the player
        :return: The number of points of the player(int)
        """
        if self.hand == []:
            return 0
        player_new_sum = 0
        for part in self.hand.array:
            player_sum = part.get_left() + part.get_right()
            player_new_sum += player_sum
        return player_new_sum

    def has_dominoes(self):
        """
A method that returns bool if the player has more dominoes in hand
        :return: True if there are dominoes in the player's hand and False otherwise
        """
        if self.hand.array == []:
            return False
        else:
            return True

    @abstractmethod
    def play(self, board):
        """abstract method"""
        pass

    def __str__(self):
        """
 The function returns a string representing the player:
 Name: name, Age: age, Hand: hand, Score: self.score()
        :return: The method will return a string representing the player
        """
        return f'Name: {self.name}, Age: {self.age}, Hand: {self.hand}, Score: {self.score()}'

    def __repr__(self):
        """
The method will return a string representing the player as defined in the str
        :return: The method will return a string representing the player as defined in the str
        """
        return self. __str__()
