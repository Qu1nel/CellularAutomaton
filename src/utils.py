import argparse
import sys
from collections import namedtuple
from typing import List, NoReturn, Optional, Tuple, TypeAlias

import numpy as np
import pygame as pg
from loguru import logger
from pygame.event import EventType

from base import AppBase

# Types for function check_cells() in src/engine.py
ResultToDrawing: TypeAlias = List[Tuple[int, int]]
CheckCells: TypeAlias = Tuple[np.ndarray, ResultToDrawing]

# Type for __init__ GameEngine in src/engine.py
Size = namedtuple("Size", ("width", "height"))


def setting_arguments_parser() -> argparse.Namespace:
    """Adds and configures the argument parser to enable the debug (logging) flag."""
    parser = argparse.ArgumentParser(
        prog="The entry point to the game of Live",
        description="Logging mode is available, to enable it, make sure that all \
        the dependencies specified in README.md, then set the --debug flag"
    )
    parser.add_argument('-D', '--debug', action='store_true', help="Enables game logging")
    parser.add_argument('-H', '--hide-fps', action='store_true', help="Disable showing fps in game")
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument('-N', '--Neumann', action='store_true', help="Set Neumann count neighbors mode")
    mode_group.add_argument('-M', '--Moore', action='store_true', help="Set Moore count neighbors mode")
    args = parser.parse_args()
    return args


def handle_event_for_key_event(event: EventType, app: AppBase) -> Optional[NoReturn]:
    """Catches events from the keyboard."""
    logger.debug("Event received from the keyboard - {}", event)
    key: int = event.key
    match key:
        case pg.K_ESCAPE:
            logger.info("ESC was pressed")
            exit_from_app_with_code(0)
        case pg.K_SPACE:
            logger.info("SPACE was pressed")
            app.pause = not app.pause
        case pg.K_0:
            if pg.key.get_mods() & pg.KMOD_SHIFT:
                logger.info("SHIFT+0 was pressed")
            else:
                logger.info("Button 0 was pressed")
        case pg.K_1:
            if pg.key.get_mods() & pg.KMOD_SHIFT:
                logger.info("SHIFT+1 was pressed")
            else:
                logger.info("Button 1 was pressed")
        case pg.K_2:
            if pg.key.get_mods() & pg.KMOD_SHIFT:
                logger.info("SHIFT+2 was pressed")
            else:
                logger.info("Button 2 was pressed")


def handle_event_for_mouse_event(event: EventType, app: AppBase) -> None:
    """Catches events from the mouse."""
    logger.debug("Event received from the mouse - {}", event)
    button: int = event.button
    position: Tuple[int, int] = event.pos
    if button == 1:
        logger.info("The LMB was pressed")
        if app.interface.buttons.hide_menu.collidepoint(*position) and app.interface.hide_menu is False:
            logger.info("Click on \"Hide menu\"")
            app.interface.hide_menu = True
        elif app.interface.buttons.open_menu.collidepoint(*position) and app.interface.hide_menu is True:
            logger.info("Click on \"Open menu\"")
            app.interface.hide_menu = False

        if not app.interface.hide_menu:
            if app.interface.buttons.Neumann.collidepoint(*position):
                logger.info("Click on von Neumann neighborhood")
                app.GameEngine.mode = 'Neumann'
            elif app.interface.buttons.Moore.collidepoint(*position):
                app.GameEngine.mode = 'Moore'
                logger.info("Click on Moore neighborhood")


def exit_from_app_with_code(code: int = 0) -> NoReturn:
    """Correctly exits the game.

    Args:
        code: Code that return app

    Returns:
        Nothing
    """
    logger.info("Exiting from app with code <{}>", code)
    pg.quit()
    sys.exit(code)
