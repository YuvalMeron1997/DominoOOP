from Domino import *
from Exceptions import *
from Collection import *


class Board(Collection):
    """A class used to represent a Domino Board.
        :attribute value: max capacity.
        the class is inherit from Collection class"""
    def __init__(self, max_capacity):
        """Constructor for Board class.
                :param max_capacity: a int"""
        Collection.__init__(self, array=[])
        if max_capacity < 1 or max_capacity > 28:
            raise InvalidNumberException('The number is not valid')
        self.max_capacity = max_capacity

    def in_left(self):
        """The method that returns the leftmost value in the board"""
        if len(self.array) == 0:
            raise EmptyBoardException('The board is empty')
        left = self[0]
        return left.get_left()

    def in_right(self):
        """The method that returns the rightmost value in the board"""
        if len(self.array) == 0:
            raise EmptyBoardException('The board is empty')
        right = self[-1]
        return right.get_right()

    def add(self, domino, add_to_right=True):
        """The method will add a domino to the board (first to the right and if it's not legal with flip and then to the left in the same way)
        if the move is legal. if the board is full the user will get an exception"""
        if len(self.array) >= self.max_capacity:
            raise FullBoardException('The board is full')
        elif len(self.array) == 0:
            self.array.append(domino)
            return True
        else:
            if add_to_right:
                return self.add_right(domino)
            if not add_to_right:
                return self.add_left(domino)

    def add_left(self, domino):
        """try to add a domino to the board on the left side"""
        if self.in_left() == domino.get_right():
            self.array = [domino] + self.array
            return True
        if self.in_left() == domino.get_left():
            new = domino.flip()
            self.array = [new] + self.array
            return True
        else:
            return False

    def add_right(self, domino):
        """try to add a domino to the board on the right side"""
        if self.in_right() == domino.get_left():
            self.array = self.array + [domino]
            return True
        if self.in_right() == domino.get_right():
            new = domino.flip()
            self.array = self.array + [new]
            return True
        else:
            return False

    def __getitem__(self, i):
        """The method will return the domino in the i index. if there is no domino in the i index it will return none"""
        if len(self.array) - 1 >= i:
            return self.array[i]
        if len(self.array) - 1 < i:
            return None


    def __eq__(self, other):
        """The method will return a Boolean value indicating whether the current object and the other object are equal. True if equal"""
        if self.max_capacity == other.max_capacity:
            return Collection.__eq__(self, other)
        return False

    def __ne__(self, other):
        """The method will return a Boolean value indicating whether the current object and the other object are equal. False if equal"""
        if self.max_capacity == other.max_capacity:
            return Collection.__ne__(self, other)
        return True




