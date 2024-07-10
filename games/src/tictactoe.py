import threading

from games.src.games import Game, GamesID


class TicTacToe(Game):
    def __init__(self,
                hosting : bool,
                hostIp : str = None, 
                hostPort : int = None,
                ):
        super().__init__(2, hosting, hostIp, hostPort)

        self.title = "TicTacToe"
        self.game_id = GamesID.TIC_TAC_TOE
        self.max_players = 2
