from Player import *
from RandomPlayer import *
from MaxScorePlayer import *
from NaivePlayer import *
from Board import *


class Team:
    """The Team class defines a group of players in the domino game"""
    def __init__(self, name, players):
        """
Constructor for Team class.
        :param name: string
        :param players: list
        """
        self.name = name
        self.__players = players

    def get_team(self):
        """
The method will return the list of players.
        :return: The method will return the list of players.
        """
        return self.__players

    def score_team(self):
        """
A method that calculates the number of points of the group. The number of points is a scheme of the score values ​​of each
The actors.
        :return: score of the team - int
        """
        sum_team = 0
        for one_player in self.__players:
            player_sum = one_player.score()
            sum_team += player_sum
        return sum_team

    def has_dominoes_team(self):
        """
A method that returns bool if the team players have more dominoes
        :return: -True if there is at least one player who has dominoes (one or more) and False otherwise
        """
        for one_player in self.__players:
            if one_player.has_dominoes():
                return True
        return False

    def play(self, board):
        """
A method that performs a single move for the team. The team will go through a list
of the players starting with the player in the first position. First the player in the 0th position will try to play
followed by the player in the 1st position and so on (if a player managed to add a domino to the board is updated
accordingly, the stone is removed from the player's hand and the team's round ends
        :param board: Domino game board
        :return: True if the group was able to make a move and False otherwise
        """
        result = False
        for one_player in self.__players:
            if one_player.play(board):
                result = True
                break
        return result

    def __str__(self):
        """
A string representing the group in the following format:
Name: name, Score team: self.score_team(), Players: players
        :return: The method will return a string representing the group
        """
        empty = ''
        for one_player in self.__players:
            empty += str(one_player) + ' '
        string_team = f'Name {self.name}, Score team: {self.score_team()}, Players: {empty}'
        return string_team[:-1]

    def __repr__(self):
        """
The method will return a string representing the group as defined in the str.
        :return: The method will return a string representing the group as defined in the str.
        """
        return self.__str__()


