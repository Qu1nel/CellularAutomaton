from typing import NoReturn, Optional

from app import App
from utils import setting_arguments_parser

from loguru import logger

DEBUG: bool = setting_arguments_parser().debug

if DEBUG is False:
    logger.stop()
else:
    logger.add("debug.log", rotation="100 KB", compression='zip')


@logger.catch
def main() -> Optional[NoReturn]:
    """The main function of GameOfLive."""
    game = App()
    game.run()


if __name__ == '__main__':
    main()
