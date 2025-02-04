import importlib
import pkgutil
from games.game_interface import GameInterface

def load_games():
    games = {}
    for finder, name, ispkg in pkgutil.iter_modules(['games']):
        if not ispkg:
            module = importlib.import_module(f'games.{name}')
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, GameInterface) and attr is not GameInterface:
                    game_instance = attr()
                    games[str(len(games) + 1)] = (game_instance.get_name(), game_instance)
    return games

def main():
    games = load_games()

    while True:
        print("\nAvailable Games:")
        for key, (name, _) in games.items():
            print(f"{key}: {name}")
        print("Q: Quit")

        choice = input("Select a game to play or 'q' to quit: ").strip().upper()
        if choice == 'Q':
            break
        elif choice in games:
            game_instance = games[choice][1]
            game_instance.run()
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()
