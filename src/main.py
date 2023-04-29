from loguru import logger
import pygame

from app import App
from utils import setting_arguments_parser
from config import RESOLUTION_APP, FRAME_RATE, COLOR_BG

ARGV = setting_arguments_parser()
HIDE_FPS: bool = ARGV.hide_fps
DEBUG: bool = ARGV.debug

if DEBUG is True:
    from pathlib import Path
    from config import FILE_LOG_NAME

    # Adding a 'log' folder to the source directory
    path_to_log = Path(__file__).with_name('log') / FILE_LOG_NAME
    Path.mkdir(path_to_log.parent, exist_ok=True)

    logger.add(path_to_log, rotation="2.5 MB", compression='zip')
else:
    logger.stop()


@logger.catch
def main() -> None:
    """The main function of GameOfLive."""
    logger.debug("In main() function")
    pygame.init()
    # *RESOLUTION_APP -> width, height
    game = App(*RESOLUTION_APP, fps=FRAME_RATE, bg_color=COLOR_BG)
    game.run()


if __name__ == '__main__':
    logger.debug("Start Game Of Live - __name__ == __main__")
    main()
