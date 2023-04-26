from random import randint

import pygame as pg

from loguru import logger

import config as c

from utils import quick_copy, MatrixCell
from base import AppBase, GameEngineBase


class GameEngine(GameEngineBase):
    __slots__ = ('app', 'screen', 'color_cell', 'area')
    app: AppBase
    screen: pg.Surface
    color_cell: c.Color
    area: MatrixCell  # current state of area

    def __init__(self, app: AppBase, screen: pg.Surface) -> None:
        logger.debug("Start of class initialization {}", self.__class__.__name__)
        self.app = app
        self.screen = screen
        self.color_cell = c.COLOR_CELL

        number_width_x, number_height_y = self.app.width // c.CELL_SIZE, self.app.height // c.CELL_SIZE

        self.M = number_width_x
        self.N = number_height_y

        logger.info("Number of cells in width - {}", number_width_x)
        logger.info("Number of cells in height - {}", number_height_y)
        logger.info("Total cells in area - {}", number_width_x * number_height_y)

        self.area = [[randint(0, 1) for _ in range(number_width_x)] for _ in range(number_height_y)]

        logger.debug("Finish of class initialization {}", self.__class__.__name__)

    def draw_area(self) -> None:
        """Draws the cells in self.area on the monitor."""
        logger.debug("Starting drawing game area in GameEngine.draw_area")
        for i in range(self.N):
            for j in range(self.M):
                if self.area[i][j] == 1:
                    pg.draw.rect(
                        surface=self.screen,
                        color=self.color_cell,
                        rect=pg.Rect((j * c.CELL_SIZE, i * c.CELL_SIZE), (c.CELL_SIZE - 1, c.CELL_SIZE - 1))
                    )

    def next_cycle(self) -> None:
        """Calculates the next state of self.area from the current state."""
        logger.debug("Start process next cycle for game area")

        a = quick_copy(self.area)

        for i in range(self.N):
            for j in range(self.M):
                cell = self.area[i][j]

                if i == j == 0:
                    number_living = (a[i + 1][j], a[i][j + 1], a[i + 1][j + 1]).count(1)
                elif i == 0 and j < self.M - 1:
                    number_living = (a[i][j - 1], a[i + 1][j - 1], a[i + 1][j], a[i + 1][j + 1], a[i][j + 1]).count(1)
                elif i == 0 and j == self.M - 1:
                    number_living = (a[i][j - 1], a[i + 1][j - 1], a[i + 1][j]).count(1)
                elif i < self.N - 1 and j == 0:
                    number_living = (a[i - 1][j], a[i - 1][j + 1], a[i][j + 1], a[i + 1][j + 1], a[i + 1][j]).count(1)
                elif i < self.N - 1 and j == self.M - 1:
                    number_living = (a[i - 1][j], a[i - 1][j - 1], a[i][j - 1], a[i + 1][j - 1], a[i + 1][j]).count(1)
                elif i == self.N - 1 and j == 0:
                    number_living = (a[i - 1][j], a[i - 1][j + 1], a[i][j + 1]).count(1)
                elif i == self.N - 1 and j < self.M - 1:
                    number_living = (a[i][j - 1], a[i - 1][j - 1], a[i - 1][j], a[i - 1][j + 1], a[i][j + 1]).count(1)
                elif i == self.N - 1 and j == self.M - 1:
                    number_living = (a[i - 1][j], a[i - 1][j - 1], a[i][j - 1]).count(1)
                else:
                    number_living = (a[i - 1][j - 1], a[i - 1][j], a[i - 1][j + 1], a[i][j - 1],
                                     a[i][j + 1], a[i + 1][j - 1], a[i + 1][j], a[i + 1][j + 1]).count(1)

                if cell == 1 and number_living not in (2, 3):
                    self.area[i][j] = 0
                elif cell == 0 and number_living == 3:
                    self.area[i][j] = 1

        logger.debug("Finish process next cycle for game area")
