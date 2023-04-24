import sys
from typing import NoReturn, Optional

import pygame as pg

from pygame import SurfaceType
from pygame.event import EventType
from pygame.time import Clock

from config import Resolution, FrameRate


def exit_from_app(code: int = 0) -> NoReturn:
    """Correctly exits the game.

    Args:
        code: Code that return app

    Returns:
        Nothing
    """
    pg.quit()
    sys.exit(code)


class App:
    __slots__ = ('width', 'height', 'screen', 'clock')

    width: int
    height: int
    screen: SurfaceType  # Display surface (application screen)
    clock: Clock  # Sets a delay for the desired amount of FPS

    def __init__(self) -> None:
        self.width = Resolution.Width
        self.height = Resolution.Height
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = Clock()

    @staticmethod
    def _handle_event_for_key_event(event: EventType) -> Optional[NoReturn]:
        """Catches events from the keyboard."""
        key: int = event.key
        match key:
            case pg.K_ESCAPE: exit_from_app()

    @staticmethod
    def _handle_event_for_mouse_event(event: EventType) -> None:
        """Catches events from the mouse."""
        button: int = event.button
        if button == 1:
            return None

    def _match_type(self, event: EventType) -> Optional[NoReturn]:
        """Compares events and, depending on its type, determines further actions.

        Args:
            event: The event can be from the keyboard or mouse.

        Returns:
            None or can exit the application.
        """
        match event.type:
            case pg.QUIT:
                exit_from_app()
            case pg.KEYDOWN:
                self._handle_event_for_key_event(event)
            case pg.MOUSEBUTTONDOWN:
                self._handle_event_for_mouse_event(event)

    def handle_events(self) -> None:
        """Processes events entered by the user.

        Calls the auxiliary function _math_type() to determine the type of event.

        Returns:
            None
        """
        for event in pg.event.get():
            self._match_type(event)

    def _game_loop(self) -> None:
        """Endless* game loop.

        Handles events.
        Update frame rate.

        Returns:
            None
        """
        while True:
            self.handle_events()
            self.clock.tick(FrameRate)

    def run(self) -> NoReturn:
        """Gameplay handler and exception maintenance.

        Always exits the application via exit_from_app(<code>)

        Returns:
            Nothing
        """
        try:
            self._game_loop()
        except KeyboardInterrupt:
            # TODO add logging
            exit_from_app(-1)
        finally:
            exit_from_app(0)
