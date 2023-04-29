from typing import Union, Tuple

import pygame as pg

from pygame.event import EventType
from pygame.time import Clock
from pygame import SurfaceType
from loguru import logger

from utils import exit_from_app_with_code, handle_event_for_key_event, handle_event_for_mouse_event
from base import AppBase, GameEngineBase, InterfaceBase
from interface import Interface
from engine import GameEngine
from config import Color


class App(AppBase):
    slots = ('width', 'height', 'screen', 'clock', 'GameEngine', 'fps', 'bg_color', 'pause')

    width: int
    height: int
    fps_chill: int
    fps: int
    pause: bool
    bg_color: Union[Color, Tuple[int, int, int]]
    screen: SurfaceType  # Display surface (application screen)
    GameEngine: GameEngineBase
    interface: InterfaceBase
    clock: Clock  # Sets a delay for the desired amount of FPS

    def __init__(self, width: int, height: int, fps: int, bg_color: Union[Color, Tuple[int, int, int]]) -> None:
        logger.debug("Start of class initialization {}", self.__class__.__name__)
        self.width = width
        self.height = height

        self.fps_chill = 3
        self.fps = fps
        self.pause = False

        self.bg_color = bg_color

        self.screen = pg.display.set_mode((self.width, self.height))

        self.GameEngine = GameEngine(app=self, screen=self.screen)
        self.interface = Interface(screen=self.screen, width=width, height=height)

        self.clock = Clock()
        logger.debug("Finish of class initialization {}", self.__class__.__name__)

    def _match_type(self, event: EventType) -> None:
        """Compares events and, depending on its type, determines further actions.

        Args:
            event: The event can be from the keyboard or mouse.

        Returns:
            None
        """
        match event.type:
            case pg.QUIT:
                logger.info("The user clicked on the cross")
                exit_from_app_with_code(0)
            case pg.KEYDOWN:
                logger.info("The user clicked on the key")
                handle_event_for_key_event(event, self)
            case pg.MOUSEBUTTONDOWN:
                logger.info("The user interacts with the mouse")
                handle_event_for_mouse_event(event, self)

    def handle_events(self) -> None:
        """Processes events entered by the user.

        Calls the auxiliary function _math_type() to determine the type of event.

        Returns:
            None
        """
        for event in pg.event.get():
            self._match_type(event)

    def draw(self) -> None:
        """Draws a picture on the display."""
        self.screen.fill(self.bg_color)
        self.GameEngine.draw_area()
        self.interface.draw_menu()
        self.interface.draw_fps(
            frame_per_second=int(self.clock.get_fps())
        )
        pg.display.update()

    def process(self) -> None:
        """Calculates necessary before trapping events"""
        if not self.pause:
            self.GameEngine.process()

    def loop(self) -> None:
        """Endless* game loop.

        Catches events from the user.
        Calculates the required steps for the game.
        Draws an image on the screen.
        Updates the frame rate.

        Returns:
            None
        """
        logger.debug("In App.loop()")
        while True:
            self.handle_events()
            self.process()
            self.draw()
            self.clock.tick(self.fps if not self.pause else self.fps_chill)

    def run(self) -> None:
        """Gameplay handler and exception maintenance."""
        try:
            self.loop()
        except KeyboardInterrupt:
            logger.info("A KeyboardInterrupt exception was caught")
            exit_from_app_with_code(-1)
