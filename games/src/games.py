from abc import abstractmethod
from enum import Enum
import socket



# Enum for the different types of games that can be played.
class GamesID(Enum):
    TIC_TAC_TOE = 0
    CHESS = 1

class game_errors(Enum):
    NO_ERROR = 0
    CONNECTION_ERROR = 1

# Base Class for all games. Provides overall variables and functions that are common to all games.
class Game:
    # Default variables to be set by all games
    title : str
    max_players : int
    game_id : GamesID

    # Variable with default values on start up
    running : bool = True
    error_code : game_errors = game_errors.NO_ERROR
    
    # Default variables to be set upon loading a game
    n_players : int
    host : bool
    
    def __init__(self, n_players : int, hosting : bool, hostIp : str = None, hostPort : int = None):
        self.n_players = n_players
        self.host = hosting
        if not hosting:
            assert hostIp is not None and hostPort is not None, "If not hosting, hostIp and hostPort must be set."
            self.hostIp = hostIp
            self.hostPort = hostPort
        else:
            self.hostIp = 'localhost'
            port_aval, number = self.get_free_port()
            if port_aval:
                self.hostPort = number
            else:
                print("No port available")
                self.running = False

    def get_free_port()->tuple[bool, int]:
        """Get a free port to bind to.
        Returns:
            tuple[bool, int]: true if a port was found, false if not, and the port number.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 50_000
        while port < 60_000:
            try:
                s.bind(("localhost", port))
                s.close()
                break
            except OSError:
                port += 1
        success = False if port == 60_000 else True
        return success, port
    
    @abstractmethod
    def startup(self):
        pass