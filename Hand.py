from Collection import *
from Domino import *
from Exceptions import *

class Hand(Collection):
    """A class used to represent a Hand of a domino player.
            :attribute value: dominoes.
            the class is inherit from Collection class"""
    def __init__(self, dominoes):
        """Constructor for Hand class.
            :param dominoes: a list"""
        super().__init__(dominoes)
        self.array = dominoes

    def add(self, domino, index = None):
        """
The method will add a domino to the array at the index place
        :param domino:Domino stone that you want to add to the hand
        :param index: If the index is None, the domino will be added to the end of the array.
otherwise, the domino will be added to the index position and the dominoes after the index position will be moved one place
right
        :return: the method return the array
        """
        if index == None:
            return self.array.append(domino)
        if index != None:
            return self.array.insert(index, domino)

    def remove_domino(self, domino):
        """
The method will remove a domino from the array and return the index in the array where the domino was.
If the domino is not on the board, it will be thrown away
NoSuchDominoException exception
        :param domino: Domino stone that you want to remove from the hand
        :return: the method will return the index the stone in an array or exception if the stone cannot be removed
        """
        if domino not in self.array:
            raise NoSuchDominoException('No such domino in the list')
        else:
            for index in range(len(self.array)):
                i = index
                if self.array[i] == domino:
                    self.array.pop(i)
                    return i



