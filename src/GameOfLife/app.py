from typing import NoReturn

import pygame as pg

from pygame import SurfaceType
from pygame.time import Clock

from config import Resolution, FrameRate


class App:
    __slots__ = ('width', 'height', 'screen', 'clock')

    width: int
    height: int
    screen: SurfaceType  # Display surface (application screen)
    clock: Clock  # Sets a delay for the desired amount of FPS

    def __init__(self):
        self.width = Resolution.Width
        self.height = Resolution.Height
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = Clock()

    def handle_events(self):
        pass

    def run(self) -> NoReturn:
        while True:
            self.handle_events()
            self.clock.tick(FrameRate)
