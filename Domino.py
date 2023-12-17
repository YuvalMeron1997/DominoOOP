from Exceptions import *


class Domino:
    """A class used to represent a Domino.
        :attribute values: left and right- integer positive numbers."""
    def __init__(self, left, right):
        """Constructor for Domino class.
                :param left and right: integer numbers"""
        if left > 6 or left < 0:
            raise InvalidNumberException('The number is not valid')
        if right > 6 or right < 0:
            raise InvalidNumberException('The number is not valid')
        self.__left = left
        self.__right = right

    def get_left(self):
        """The method will return the number of the left side of the domino (int)"""
        return self.__left

    def get_right(self):
        """The method will return the number of the right side of the domino (int)"""
        return self.__right

    def __str__(self):
        """The method will return the domino as a string"""
        return f'[{self.__left}|{self.__right}]'

    def __repr__(self):
        """The method will return the domino as a string"""
        return self.__str__()

    def __eq__(self, other):
        """The method return True if 2 dominos are equel or False otherwise"""
        if self.__left == other.__left and self.__right == other.__right:
            return True
        if self.__left == other.__right and self.__right == other.__left:
            return True
        else:
            return False

    def __ne__(self, other):
        """The method return True if 2 dominos are not equel or False otherwise"""
        if self.__eq__(other):
            return False
        else:
            return True

    def __gt__(self, other):
        """The method checks if the value of the domino is bigger than the other domino's value and return True if it does, otherwise return False"""
        if self.__left + self.__right > other.__right + other.__left:
            return True
        else:
            return False

    def __contains__(self, key):
        """The method will return True if the key is equal to the right side or the left side of the domino and False if not"""
        if key == self.__right or key == self.__left:
            return True
        else:
            return False

    def flip(self):
        """The method will flip the dimono. the right side will be the left side and the opposite"""
        new_domino = Domino(self.__right, self.__left)
        return new_domino


