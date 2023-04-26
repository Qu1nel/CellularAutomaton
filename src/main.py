from loguru import logger

from app import App
from utils import setting_arguments_parser
from config import Resolution, FrameRate, COLOR_BG

DEBUG: bool = setting_arguments_parser().debug

if DEBUG is False:
    logger.stop()
else:
    from pathlib import Path
    from config import FILE_LOG_NAME

    path_to_log = Path(__file__).with_name('log') / FILE_LOG_NAME
    Path.mkdir(path_to_log.parent, exist_ok=True)

    logger.add(path_to_log, rotation="2.5 MB", compression='zip')


@logger.catch
def main() -> None:
    """The main function of GameOfLive."""
    logger.debug("In main() function")
    game = App(*Resolution, fps=FrameRate, bg_color=COLOR_BG)
    game.run()


if __name__ == '__main__':
    logger.debug("Start Game Of Live - __name__ == __main__")
    main()
