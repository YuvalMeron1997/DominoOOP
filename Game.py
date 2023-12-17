from Team import *
from Player import *
from RandomPlayer import *
from MaxScorePlayer import *
from NaivePlayer import *
from Board import *

class Game:
    """The Game class defines the domino game."""
    def __init__(self, board, team1, team2):
        """
The contracture of the Game class
        :param board: Domino game board
        :param team1: first team (Team objects)
        :param team2: second team (Team objects)
        """
        self.board = board
        self.team1 = team1
        self.team2 = team2

    def play(self):
        """
call the functions
        :return: the result of the game(string)
        """
        def first_second_team():
                """
A method that manages the game. The first team to play will be team1 followed by team2.
A team will try to add a domino to the board every queue. The game ends when one of the teams runs out
the stones or no group can place a domino on the board. The board is updated during the game and so on
also the hand of the players
                :return:
                """
                if len(self.board) == self.board.max_capacity:
                    return check()
                if self.team1.has_dominoes_team() == False or self.team2.has_dominoes_team() == False:
                    return check()
                if self.team1.play(self.board):
                    if not self.team1.has_dominoes_team():
                        return check()
                    if len(self.board) == self.board.max_capacity:
                        return check()
                    if self.team2.play(self.board):
                        return first_second_team()
                    return first_second_team()
                if self.team2.play(self.board):
                    if not self.team2.has_dominoes_team():
                        return check()
                    if len(self.board) == self.board.max_capacity:
                        return check()
                    return first_second_team()
                return check()

        def check():
            """
the function checks which team won
            :return: string with the result of the game- which team won
            """
            if self.team1.score_team() > self.team2.score_team():
                return f'Team {self.team2.name} wins Team {self.team1.name}'

            if self.team2.score_team() > self.team1.score_team():
                return f'Team {self.team1.name} wins Team {self.team2.name}'

            if self.team2.score_team() == self.team1.score_team():
                return 'Draw !'
        return first_second_team()













