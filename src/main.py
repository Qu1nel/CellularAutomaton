from typing import Literal

import pygame
from loguru import logger

from src.app import App
from src.config import COLOR_BG, FRAME_RATE, RESOLUTION_APP
from src.utils import setting_arguments_parser

ARGV = setting_arguments_parser()
HIDE_FPS: bool = ARGV.hide_fps
DEBUG: bool = ARGV.debug
MOORE: bool = ARGV.Moore
NEUMANN: bool = ARGV.Neumann

if DEBUG is True:
    from pathlib import Path

    from src.config import FILE_LOG_NAME

    # Adding a 'log' folder to the source directory
    path_to_log = Path(__file__).with_name('log') / FILE_LOG_NAME
    Path.mkdir(path_to_log.parent, exist_ok=True)

    logger.add(path_to_log, rotation="2.5 MB", compression='zip')
else:
    logger.stop()


def get_mode() -> Literal['Moore', 'Neumann']:
    if MOORE is True:
        return 'Moore'
    if NEUMANN is True:
        return 'Neumann'

    raise RuntimeError("never")


# TODO: сделать вывод сообщения на экран (3-5 сек) о том, какая расстановка клеток выбрана
# TODO: сделать вывод информации, о том, какое правило сейчас задействовано
# TODO: добавить новые правила
# TODO: добавить новые расстановки
# TODO: добавить добавление кастомных расположений на экран через файл с символами

@logger.catch
def main() -> None:
    """The main function of GameOfLive."""
    logger.debug("Start Game Of Live - __name__ == __main__")
    logger.debug("In main() function")
    pygame.init()

    # *RESOLUTION_APP -> width, height
    game = App(*RESOLUTION_APP, fps=FRAME_RATE, bg_color=COLOR_BG,
               hide_fps=HIDE_FPS, mode=get_mode())
    game.run()
