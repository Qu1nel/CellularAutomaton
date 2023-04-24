from typing import NoReturn, Union

from app import App


def main() -> Union[NoReturn, None]:
    game = App()
    game.run()

    return None


if __name__ == '__main__':
    main()
