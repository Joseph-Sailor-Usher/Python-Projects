### This is an abstract base class, which will allow my main.py to display information from all the games I might eventually make.
from abc import ABC, abstractmethod

class GameInterface(ABC):
    @abstractmethod
    def run(self):
        """Start the game."""
        pass

    @abstractmethod
    def get_name(self):
        """Return the name of the game."""
        pass

    @abstractmethod
    def get_help(self):
        """Return help information about the game."""
        pass
