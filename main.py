#Main Application will run here


import os


if __name__ == '__main__':
    run : bool = True
    # Find available games
    files : list = os.listdir("./games")
    games : list = [f for f in files if f.endswith(".exe")]
    games : list = [os.path.basename(f) for f in games]

    if len(games) == 0:
        print("No games found")
        run = False

    # Main loop
    while run:
        print("Choose a game by picking a valid number: ")
        print("0: Exit")
        for i, game in enumerate(games):
            print(f"{i+1}: {game}")
        choice = input("Enter your choice: ")

        # Validate choice
        if not choice.isdigit():
            continue
        choice = int(choice)
        if choice == 0:
            break
        if choice < 1 or choice > len(games):
            continue

        # Run a given game
        os.system(f"start games/{games[choice-1]}")
        print(f"Running {games[choice-1]}")


