from typing import Tuple
from random import randint

import pygame as pg

from loguru import logger

import config as c

from utils import quick_copy, RowCell, MatrixCell
from cell import Cell

from . import base


class GameEngine(base.GameEngineBase):
    __slots__ = ('app', 'screen', 'color_cell', 'previous_area', 'area')
    app: base.AppBase
    screen: pg.Surface
    color_cell: c.Color
    previous_area: MatrixCell  # previous state of area
    area: MatrixCell  # current state of area

    def __init__(self, app: base.AppBase, screen: pg.Surface) -> None:
        logger.debug("Start of class initialization {}", self.__class__.__name__)
        self.app = app
        self.screen = screen
        self.color_cell = c.COLOR_CELL
        self.previous_area = [[]]

        number_width_x, number_height_y = self.app.width // c.CELL_SIZE, self.app.height // c.CELL_SIZE

        logger.info("Number of cells in width - {}", number_width_x)
        logger.info("Number of cells in height - {}", number_height_y)

        logger.debug("Start of filling area initialization")

        self.area = []
        for y in range(number_height_y):
            row: RowCell = []

            for x in range(number_width_x):
                row.append(Cell(coord=(x, y), alive=bool(randint(0, 1))))

            self.area.append(row)

        logger.info("area size is - {}", len(self.area))
        logger.info("Total cells in area - {}", number_width_x * number_height_y)
        logger.debug("Finish of filling area initialization")
        logger.debug("Finish of class initialization {}", self.__class__.__name__)

    def draw_area(self) -> None:
        """Draws the cells in self.area on the monitor."""

        def _normalized(coord: Tuple[int, int]) -> tuple[int, ...]:
            return tuple(i * c.CELL_SIZE for i in coord)

        logger.debug("Starting drawing game area in GameEngine.draw_area")
        for row in self.area:
            for cell in row:
                if cell.is_alive():
                    pg.draw.rect(
                        surface=self.screen,
                        color=self.color_cell,
                        rect=pg.Rect(_normalized(cell.coord), (c.CELL_SIZE - 1, c.CELL_SIZE - 1))
                    )

    def next_cycle(self) -> None:
        """Calculates the next state of self.area from the current state."""
        logger.debug("Start process next cycle for game area")

        self.previous_area = quick_copy(self.area)

        for line in self.previous_area[1:-1]:
            for cell in line[1:-1]:
                number_living = 0
                X, Y = cell.coord

                for dx, dy in ((-1, 1), (0, 1), (1, 1), (1, 0)):
                    column = Y + dy if Y + dy > 0 else 0
                    row = X + dx if X + dx > 0 else 0

                    number_living += self.previous_area[column][row].is_alive()

                    column = Y - dy if Y - dy > 0 else 0
                    row = X - dx if X - dx > 0 else 0

                    number_living += self.previous_area[column][row].is_alive()

                if cell.is_alive() and number_living not in (2, 3):
                    x, y = cell.coord
                    self.area[y][x].alive = False
                elif not cell.is_alive() and number_living == 3:
                    x, y = cell.coord
                    self.area[y][x].alive = True

        logger.debug("Finish process next cycle for game area")
