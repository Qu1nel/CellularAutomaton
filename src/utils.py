import argparse
import sys

from typing import List, NoReturn, Optional, Tuple, TypeAlias
from collections import namedtuple

import pygame as pg
import numpy as np

from pygame.event import EventType
from loguru import logger

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


def handle_event_for_mouse_event(event: EventType) -> None:
    """Catches events from the mouse."""
    logger.debug("Event received from the mouse - {}", event)
    button: int = event.button
    if button == 1:
        logger.info("The LMB was pressed")


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
