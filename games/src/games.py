from abc import abstractmethod
import pygame



# Base Class for all games. Provides overall variables and functions that are common to all games.
class Game:
    def __init__(self, max_players : int, title : str):
        self.max_players : int = max_players
        self.title : str = title

    @abstractmethod
    def startup(self):
        pass