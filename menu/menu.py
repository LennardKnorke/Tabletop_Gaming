import os
import sys
import tkinter as tk
from tkinter import ttk

games = ["TicTacToe"]

# represents the Main Menu of the TableTop Library - you'll start every added game from here
class MainMenu():
    title = "TableTopGaming"

    def __init__(self, width: int, height: int) -> None:
        # creates the inital window
        self.root = tk.Tk()
        self.root.title(MainMenu.title)
        self.width: int = str(width)
        self.height: int = str(height)
        self.resoulution = self.root.geometry(self.width + "x" + self.height)

        self.library_label = ttk.Label(self.root,
                                    text=self.title,
                                    anchor="center", 
                                    font=("Arial", 30), 
                                    padding=20, relief="solid")
        
        self.library_label.pack(side="top", fill="x")

        self.game_grid_frame = ttk.Frame(self.root, relief="solid")
        self.game_grid_frame.pack(side="left")

        self.game_desc_frame = ttk.Labelframe(self.root)
        self.game_desc_frame.pack(side="right")       

class Game():
    # creates an game-object 
    def __init__(self, frame, name) -> None:
        self.name = name
        root_frame = frame
        self.image = ""

        self.game_frame = ttk.Frame(root_frame, padding=20)
        
        self.game_label = ttk.Label(self.game_frame, text=name)
        self.game_button = ttk.Button(self.game_frame, text="Click me!", command=self.start_game)
        self.game_label.pack(side="top")
        self.game_button.pack(side="bottom", padx = 25, pady = 25)
        self.game_frame.grid()
        pass

    # method for starting the game when clicking the corresponding button
    def start_game(self):
        print(self.game_label.cget("text"))
        # Big To-Do
        pass
    

    # method for creating the game-description (right part of the main menu) when selecting a game
    def create_game_description(self):
        if self.game_frame.state() == tk.ACTIVE:
            print("Hi.")
            pass
        pass     



    # for-loop to create all games
    @staticmethod
    def create_games(game_grid_frame):
        game_count = []
        for i, game in enumerate(games):
            game_object = Game(game_grid_frame ,games[i])
            game_count.append(game_object)
        return game_count


menu = MainMenu(800,600)
game_count = Game.create_games(menu.game_grid_frame)
menu.root.mainloop()
