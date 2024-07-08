from games import Game


class TicTacToe(Game):
    def __init__(self, 
                 max_players : int = 2, 
                 title : str = "Tic Tac Toe"
                 ):
        super().__init__(max_players, title)

    