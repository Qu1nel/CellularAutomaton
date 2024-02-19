import pygame as pg
from loguru import logger
from pygame.event import EventType

from src.bases import AppBase
from src.misc.states import Mode, Rules, StateInit
from src.misc.utils import exit_from_app_with_code


def handle_event_for_key_event(event: EventType, app: AppBase) -> None:
    """Catches events from the keyboard.

    Args:
        event: Event object.
        app: The game in which the event occurred.

    Returns:
        None
    """
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
                app.engine.init_area(state=StateInit.RANDOM)
            else:
                logger.info("Button 0 was pressed")
                app.engine.preset = Rules.b3_s23
        case pg.K_1:
            if pg.key.get_mods() & pg.KMOD_SHIFT:
                logger.info("SHIFT+1 was pressed")
                app.engine.init_area(state=StateInit.DOT)
            else:
                logger.info("Button 1 was pressed")
                app.engine.preset = Rules.b1_s012345678
        case pg.K_2:
            if pg.key.get_mods() & pg.KMOD_SHIFT:
                logger.info("SHIFT+2 was pressed")
            else:
                logger.info("Button 2 was pressed")
                app.engine.preset = Rules.b5678_s45678


def handle_event_for_mouse_event(event: EventType, app: AppBase) -> None:
    """Catches events from the mouse.

    Args:
        event: Event object.
        app: The game in which the event occurred.

    Returns:
        None
    """
    logger.debug("Event received from the mouse - {}", event)

    button: int = event.button
    position: tuple[int, int] = event.pos

    if button == 1:
        logger.info("The LMB was pressed")
        if app.gui.buttons["hide_menu"].collidepoint(*position) and app.gui.hide_menu is False:
            logger.info('Click on "Hide menu"')
            app.gui.hide_menu = True
            app.gui.buttons["hide_menu"].set_drawing(False)
            app.gui.buttons["open_menu"].set_drawing(True)
        elif app.gui.buttons["open_menu"].collidepoint(*position) and app.gui.hide_menu is True:
            logger.info('Click on "Open menu"')
            app.gui.hide_menu = False
            app.gui.buttons["open_menu"].set_drawing(False)
            app.gui.buttons["hide_menu"].set_drawing(True)

        if not app.gui.hide_menu:
            if app.gui.buttons["Neumann"].collidepoint(*position):
                logger.info("Click on von Neumann neighborhood")
                app.engine.mode = Mode.NEUMANN
            elif app.gui.buttons["Moore"].collidepoint(*position):
                app.engine.mode = Mode.MOORE
                logger.info("Click on Moore neighborhood")
