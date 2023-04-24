from typing import NoReturn

from app import App


def main() -> NoReturn:
    game = App()
    game.run()


if __name__ == '__main__':
    main()
