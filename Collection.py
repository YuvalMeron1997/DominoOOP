from Exceptions import *
class Collection:
    """A class used to represent a Collection.
    :attribute values: a list of objects."""
    def __init__(self, array):
        """Constructor for Collection class.
        :param array: a list of objects"""
        self.array = array

    def get_collection(self):
        """The method will return the array field
        :return: The method will return the array field
        """
        return self.array

    def add(self, item, option):
        """The method does not will be implemented in this class"""
        raise NotImplementedError('The method will not be implemented in this class')

    def __getitem__(self, i):
        """The method will return the member in place i in the array field"""
        if i >= len(self.array):
            return None
        return self.array[i]

    def __eq__(self, other):
        """The method will return boolean value indicating if self and other are equal"""
        if not isinstance(other, Collection):
            return False
        else:
            return self.array == other.array

    def __ne__(self, other):
        """The method will return boolean value indicating if self and other are not equal"""
        if not self.__eq__(other):
            return True
        else:
            return False

    def __len__(self):
        """The method will return the number of objects in array"""
        return len(self.array)

    def __contains__(self, item):
        """The method will return boolean value indicating if the item is in the array or not"""
        for i in range(len(self.array)):
            if item == self.array[i]:
                answer = True
                break
            else:
                answer = False
        return answer

    def __str__(self):
        """The method will return a string that representing the current collection"""
        empty = ''
        for i in self.array:
            empty += str(i)
        return empty


    def __repr__(self):
        """The method will return boolean value indicating if self and other are equal"""
        return self.__str__()










