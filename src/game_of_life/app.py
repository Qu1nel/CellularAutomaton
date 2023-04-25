from typing import NoReturn, Optional

import pygame as pg

from pygame import SurfaceType
from pygame.event import EventType
from pygame.time import Clock
from loguru import logger

from config import Resolution, FrameRate, COLOR_BG
from utils import exit_from_app, handle_event_for_key_event, handle_event_for_mouse_event


class App:
    __slots__ = ('width', 'height', 'screen', 'clock')

    width: int
    height: int
    screen: SurfaceType  # Display surface (application screen)
    clock: Clock  # Sets a delay for the desired amount of FPS

    def __init__(self) -> None:
        logger.debug("Start of class initialization {}", self.__class__.__name__)
        self.width = Resolution.Width
        self.height = Resolution.Height
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = Clock()
        logger.debug("Finish of class initialization {}", self.__class__.__name__)

    @staticmethod
    def _match_type(event: EventType) -> Optional[NoReturn]:
        """Compares events and, depending on its type, determines further actions.

        Args:
            event: The event can be from the keyboard or mouse.

        Returns:
            None or can exit the application.
        """
        match event.type:
            case pg.QUIT:
                logger.info("The user clicked on the cross")
                exit_from_app(0)
            case pg.KEYDOWN:
                logger.info("The user clicked on the key")
                handle_event_for_key_event(event)
            case pg.MOUSEBUTTONDOWN:
                logger.info("The user clicked on the mouse")
                handle_event_for_mouse_event(event)

    def handle_events(self) -> None:
        """Processes events entered by the user.

        Calls the auxiliary function _math_type() to determine the type of event.

        Returns:
            None
        """
        for event in pg.event.get():
            self._match_type(event)

    def draw(self) -> None:
        """Draws a picture on the display.

        Returns:
            None
        """
        self.screen.fill(COLOR_BG)
        pg.display.update()

    def loop(self) -> None:
        """Endless* game loop.

        Handles events.
        Update frame rate.

        Returns:
            None
        """
        while True:
            self.handle_events()
            self.draw()
            self.clock.tick(FrameRate)

    def run(self) -> Optional[NoReturn]:
        """Gameplay handler and exception maintenance.

        Always exits the application via exit_from_app(<code>)

        Returns:
            Nothing
        """
        try:
            self.loop()
        except KeyboardInterrupt:
            logger.info("A KeyboardInterrupt exception was caught")
            exit_from_app(-1)
