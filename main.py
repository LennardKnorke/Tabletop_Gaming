#Main Application will run here
import os

from games.src.tictactoe import TicTacToe


if __name__ == '__main__':
    g = "TicTacToe"

    choice = input("Choose:\nc - Client\ns - Server\n")
    while choice.lower() not in ['c', 's']:
        choice = input("Choose:\nc - Client\ns - Server\n")

    if choice.lower() == 'c':
        game = TicTacToe(hosting=False)
    else:
        game = TicTacToe(hosting=True)
    # Command Line Arguments (OPTIONAL. TO DO)

    # Run Main Application.