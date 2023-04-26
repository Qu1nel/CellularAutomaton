from typing import Union, Tuple

import pygame as pg

from pygame.event import EventType
from pygame.time import Clock
from pygame import SurfaceType
from loguru import logger

from utils import exit_from_app_with_code, handle_event_for_key_event, handle_event_for_mouse_event
from config import Color
from engine import GameEngine
from base import AppBase


class App(AppBase):
    slots = ('width', 'height', 'screen', 'clock', 'GameEngine', 'fps', 'bg_color')

    width: int
    height: int
    screen: SurfaceType  # Display surface (application screen)
    clock: Clock  # Sets a delay for the desired amount of FPS

    def __init__(self, width: int, height: int, fps: int, bg_color: Union[Color, Tuple[int, int, int]]) -> None:
        logger.debug("Start of class initialization {}", self.__class__.__name__)
        self.width = width
        self.height = height
        self.fps = fps
        self.bg_color = bg_color
        self.screen = pg.display.set_mode((self.width, self.height))
        self.GameEngine = GameEngine(app=self, screen=self.screen)
        self.clock = Clock()
        logger.debug("Finish of class initialization {}", self.__class__.__name__)

    @staticmethod
    def _match_type(event: EventType) -> None:
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
        """Draws a picture on the display."""
        self.screen.fill(self.bg_color)
        self.GameEngine.draw_area()
        pg.display.update()

    def process(self) -> None:
        """Calculates necessary before trapping events"""
        self.GameEngine.process()

    def loop(self) -> None:
        """Endless* game loop.

        Draws an image on the screen.

        Calculates the required steps for the game.

        Catches events from the user.

        Updates the frame rate.

        Returns:
            None
        """
        logger.debug("In App.loop()")
        while True:
            self.draw()
            self.process()
            self.handle_events()
            self.clock.tick(self.fps)

    def run(self) -> None:
        """Gameplay handler and exception maintenance."""
        try:
            self.loop()
        except KeyboardInterrupt:
            logger.info("A KeyboardInterrupt exception was caught")
            exit_from_app_with_code(-1)
