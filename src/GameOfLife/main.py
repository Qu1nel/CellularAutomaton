from typing import NoReturn, Optional

from app import App


def main() -> Optional[NoReturn]:
    """The main function of GameOfLive."""
    game = App()
    game.run()


if __name__ == '__main__':
    main()
