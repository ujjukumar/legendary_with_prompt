import legendary
import subprocess
import time

class Game:
    def __init__(self, game_string_raw) -> None:
        self.name = game_string_raw.split('(')[0].strip()
        self.disksize = game_string_raw.split('|')[-1].strip().split(')')[0]

    def __str__(self):
        return f"{self.name} ({self.disksize})"

def on_launch():
    print(f"Welcome to legendary laucher for Epic Games!\nCurrent version is:- {legendary.__version__}")

    # Get current list of installed games and check for update
    code = 'legendary list-installed --check-update'
    current_games = subprocess.run(code,
                                    shell=False,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)

    print(f"\n{current_games.stdout}")
    return current_games.stdout.split('*')[1:]

def promt_user_and_doit(installed_games_list):
    print("-----------------------------------------------------------------")
    print(f"Which game you want to launch?")
    game_object_list = [Game(game) for game in installed_games_list]
    
    for i, game in enumerate(game_object_list):
        print(f"{i + 1}: {game}")

    promt = int(input("\n\nEnter number for the game you want to launch:- ")) - 1
    code = f"legendary launch {game_object_list[promt].name}"
    print(f"Launching {game_object_list[promt]}\n")
    proc = subprocess.Popen(code, shell=False)

    while proc.poll() is None:
        time.sleep(1)
    print(f"Game:- {game_object_list[promt]} launched successfully with code {proc.poll()}")

    print("\nClosing this window in 5 second.")
    time.sleep(5)
    return

if __name__ == '__main__':
    installed_games_list = on_launch()

    # Promt user to choose b/w differnent operations
    promt_user_and_doit(installed_games_list)