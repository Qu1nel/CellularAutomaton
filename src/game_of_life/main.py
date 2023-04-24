from typing import NoReturn, Optional

from loguru import logger

from app import App
from utils import setting_arguments_parser

DEBUG: bool = setting_arguments_parser().debug

if DEBUG is False:
    logger.stop()
else:
    logger.add("../log/debug.log", rotation="100 MB", compression='zip')


@logger.catch
def main() -> Optional[NoReturn]:
    """The main function of GameOfLive."""
    logger.debug("In main() function")
    game = App()
    game.run()


if __name__ == '__main__':
    logger.debug("Start Game Of Live - __name__ == __main__")
    main()
