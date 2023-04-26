import argparse
import sys

from typing import Optional, NoReturn, TypeAlias, List

import pygame as pg

from pygame.event import EventType
from loguru import logger
from base import CellBase

RowCell: TypeAlias = List[CellBase]
MatrixCell: TypeAlias = List[RowCell]


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


def handle_event_for_key_event(event: EventType) -> Optional[NoReturn]:
    """Catches events from the keyboard."""
    logger.debug("Event received from the keyboard - {}", event)
    key: int = event.key
    match key:
        case pg.K_ESCAPE:
            logger.info("ESC was pressed")
            exit_from_app_with_code(0)


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


def quick_copy(area_cell: MatrixCell) -> MatrixCell:
    """Copies the playing field, creates a new instance playing field.

    Args:
        area_cell: Matrix of Cell (game area)

    Returns:
        Same game area - copy
    """
    logger.debug("In quick_copy()")
    try:
        logger.debug("Start copy game area")
        result = [[cell.copy() for cell in row] for row in area_cell]
    except Exception as exc:
        logger.error("Error in quick_copy(). Details: {}", exc)
        raise exc from None
    else:
        return result
    finally:
        logger.debug("Exiting from quick_copy()")
