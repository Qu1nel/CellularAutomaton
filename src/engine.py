import copy

from random import randint
from typing import List

import pygame as pg
import numpy as np

from loguru import logger
from numba import njit

import config as c

from base import AppBase, GameEngineBase
from utils import Size, CheckCells
from config import Color


@njit(fastmath=True)
def count_neighbors(field: np.ndarray, row: int, column: int, width_field: int, height_field: int) -> int:
    neighbors = 0

    for i, j in ((-1, 1), (0, 1), (1, 1), (1, 0)):
        X = row + i
        Y = column + j
        if 0 <= Y < width_field and 0 <= X < height_field:
            neighbors += field[X][Y]

        X = row - i
        Y = column - j
        if 0 <= Y < width_field and 0 <= X < height_field:
            neighbors += field[X][Y]

    return neighbors


@njit(fastmath=True)
def check_cells(current_field: np.ndarray, next_field: np.ndarray, width: int, height: int) -> CheckCells:
    """Counts for each cell how many living neighbors are nearby (3×3 cells).

    Accepts the current state of the field and the next. Based on the current
    one, the next state for next_field is calculated. Iterates over each cell
    and for each cell checks all its 8 neighbors. If there are fewer neighbors
    by the condition, then the cell dies and will not appear in next_filed.
    Also, if a cell survives it seems, it is entered into
    result_for_drawing array, which is sent to the draw_area() method and all
    the cells in it will be drawn.

    Args:
        current_field: The current state of the playing field, according to
                    which the next state will be calculated

        next_field: The field that will be filled with the new state of the
                    cells

        width: Number indicating the width of the playing field
        height: Number indicating the height of the playing field

    Returns:
        Calculated state for the next step, and an array of live cells that
        will be drawn.
    """
    result_for_drawing = []

    for x in range(width):
        for y in range(height):
            count_living = count_neighbors(
                field=current_field,
                row=y,
                column=x,
                width_field=width,
                height_field=height
            )

            if current_field[y][x] == 1:
                if count_living in (2, 3):
                    next_field[y][x] = 1
                    result_for_drawing.append((x, y))
                else:
                    next_field[y][x] = 0
            else:
                if count_living == 3:
                    next_field[y][x] = 1
                    result_for_drawing.append((x, y))
                else:
                    next_field[y][x] = 0

    return next_field, result_for_drawing


class GameEngine(GameEngineBase):
    __slots__ = ('app', 'screen', 'color_cell', 'current_area', 'next_area', 'width_area', 'size_area', 'draw_rects')

    app: AppBase
    screen: pg.SurfaceType
    color_cell: Color
    current_area: np.ndarray
    next_area: np.ndarray
    draw_rects: List
    size_area: Size

    def __init__(self, app: AppBase, screen: pg.SurfaceType) -> None:
        logger.debug("Start of class initialization {}", self.__class__.__name__)
        self.app = app
        self.screen = screen
        self.color_cell = c.COLOR_CELL

        width_area = self.app.width // c.CELL_SIZE
        height_area = self.app.height // c.CELL_SIZE

        logger.info("Number of cells in width - {}", width_area)
        logger.info("Number of cells in height - {}", height_area)

        self.size_area = Size(width=width_area, height=height_area)

        self.current_area = np.array([[randint(0, 1) for _ in range(width_area)] for _ in range(height_area)])
        self.next_area = np.array([[0 for _ in range(width_area)] for _ in range(height_area)])
        self.draw_rects = []

        logger.debug("Finish of class initialization {}", self.__class__.__name__)

    def draw_area(self) -> None:
        """Draws the cells in self.area on the monitor."""
        for x, y in self.draw_rects:
            pg.draw.rect(
                surface=self.screen,
                color=self.color_cell,
                rect=(x * c.CELL_SIZE, y * c.CELL_SIZE, c.CELL_SIZE - 1, c.CELL_SIZE - 1)
            )

    def process(self) -> None:
        """Calculates the next state of self.area from the current state."""
        self.next_area, self.draw_rects = check_cells(
            current_field=self.current_area,
            next_field=self.next_area,
            width=self.size_area.width,
            height=self.size_area.height
        )

        self.current_area = copy.deepcopy(self.next_area)
