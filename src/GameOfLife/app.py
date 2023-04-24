import sys
from typing import NoReturn, Optional

import pygame as pg

from pygame import SurfaceType
from pygame.event import EventType
from pygame.time import Clock

from config import Resolution, FrameRate


def exit_from_app() -> NoReturn:
    pg.quit()
    sys.exit(0)


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
        key: int = event.key
        match key:
            case pg.K_ESCAPE: exit_from_app()

    @staticmethod
    def _handle_event_for_mouse_event(event: EventType) -> None:
        button: int = event.button
        if button == 1:
            return None

    def _match_type(self, event: EventType) -> Optional[NoReturn]:
        match event.type:
            case pg.QUIT:
                exit_from_app()
            case pg.KEYDOWN:
                self._handle_event_for_key_event(event)
            case pg.MOUSEBUTTONDOWN:
                self._handle_event_for_mouse_event(event)

    def handle_events(self) -> None:
        for event in pg.event.get():
            self._match_type(event)

    def _game_loop(self) -> None:
        while True:
            self.handle_events()
            self.clock.tick(FrameRate)

    def run(self) -> NoReturn:
        try:
            self._game_loop()
        except KeyboardInterrupt:
            # TODO add logging
            pass
        finally:
            exit_from_app()
