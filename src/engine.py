import copy
from random import randint
from typing import List, Literal, Union, Tuple, Sequence

import numpy as np
import pygame as pg
from loguru import logger
from numba import njit

import config as c
from base import AppBase, GameEngineBase, Rules
from config import Color
from utils import CheckCells, Size


@njit(fastmath=True)
def count_neighbors_Moore(field: np.ndarray, row: int, column: int, width_field: int, height_field: int) -> int:
    """Efficient* counts all 8 neighbors for a cell

    The function does not go through all 8 possible values around the cell, but
    only through 4 of them, and it does it mirrored about the center, i.e.,
    about the cell for which the calculation is made. Thereby reducing
    the number of iterations from 9 maximum possible to 4.

    Args:
        field: The field on which the cells are located
        row: Cell x coordinate for which neighbors are calculated
        column: Cell y coordinate for which neighbors are calculated
        width_field: Field width – boundary for calculations
        height_field: Field height – boundary for calculations

    Returns:
        The number of living cells in a cell with x and y coordinates.
    """
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
def count_neighbors_Neumann(field: np.ndarray, row: int, column: int, width_field: int, height_field: int) -> int:
    """Efficient* counts only 4 neighbors for a cell
    
    Like the count_neighbors_Neumann function, it also counts the cell's
    neighbors. But it counts only those who are located on the same axis
    as the central cell, i.e. it counts only 4 of its neighbors. At what
    using only 2 iterations for this.

    Args:
        field: The field on which the cells are located
        row: Cell x coordinate for which neighbors are calculated
        column: Cell y coordinate for which neighbors are calculated
        width_field: Field width – boundary for calculations
        height_field: Field height – boundary for calculations

    Returns:
        The number of living cells in a cell with x and y coordinates.
    """
    neighbors = 0

    for i, j in ((1, 0), (0, 1)):
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
def check_cells(current_field: np.ndarray, next_field: np.ndarray, width: int, height: int,
                rule: Sequence[Tuple[int]], mode: Literal['Moore', 'Neumann'] = 'Moore') -> CheckCells:
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
        mode: Mod defining the principle of counting cell neighbors
        rule: A rule of the form [(2, ...), (3, 4, ...)] means that the cell appears with 2
            neighbors, and survives if out of 3 or 4.

    Raises:
        ValueError: If `mode` argument was not passed.

    Returns:
        Calculated state for the next step, and an array of live cells that
        will be drawn.
    """
    result_for_drawing = []

    for x in range(width):
        for y in range(height):
            if mode == 'Neumann':
                count_living = count_neighbors_Neumann(
                    field=current_field,
                    row=y,
                    column=x,
                    width_field=width,
                    height_field=height
                )
            elif mode == 'Moore':
                count_living = count_neighbors_Moore(
                    field=current_field,
                    row=y,
                    column=x,
                    width_field=width,
                    height_field=height
                )
            else:
                raise ValueError("mode is not set!")

            _be = rule[0]
            _survives = rule[1]

            # Apply rules for number of live cells nearby
            if current_field[y][x] == 1:
                if count_living in _survives:
                    next_field[y][x] = 1
                    result_for_drawing.append((x, y))
                else:
                    next_field[y][x] = 0
            else:
                if count_living in _be:
                    next_field[y][x] = 1
                    result_for_drawing.append((x, y))
                else:
                    next_field[y][x] = 0

    return next_field, result_for_drawing


class GameEngine(GameEngineBase):
    __slots__ = ('app', 'screen', 'color_cell', 'current_area',
                 'next_area', 'width_area', 'size_area', 'draw_rects', '_mode')

    app: AppBase
    screen: pg.SurfaceType
    color_cell: Color
    current_area: np.ndarray
    next_area: np.ndarray
    draw_rects: List
    size_area: Size
    _mode: Literal['Moore', 'Neumann']

    def __init__(self, app: AppBase, screen: pg.SurfaceType, mode: Literal['Moore', 'Neumann']) -> None:
        logger.debug("Start of class initialization {}", self.__class__.__name__)
        self.app = app
        self.screen = screen
        self.color_cell = c.COLOR_CELL
        self._mode: Literal['Moore', 'Neumann'] = mode
        self._preset: str = Rules.b3_s23.value

        logger.info(f"SET RULE: {self._preset}")
        logger.info(f"MODE IS '{self._mode}'")

        width_area = self.app.width // c.CELL_SIZE
        height_area = self.app.height // c.CELL_SIZE

        logger.info("Number of cells in width - {}", width_area)
        logger.info("Number of cells in height - {}", height_area)

        self.size_area = Size(width=width_area, height=height_area)

        self.current_area = np.array([[randint(0, 1) for _ in range(width_area)] for _ in range(height_area)])
        self.next_area = np.array([[0 for _ in range(width_area)] for _ in range(height_area)])
        self.draw_rects = []

        logger.debug("Finish of class initialization {}", self.__class__.__name__)

    @property
    def mode(self) -> Literal['Moore', 'Neumann']:
        return self._mode

    @mode.setter
    def mode(self, value: Literal['Moore', 'Neumann']) -> None:
        logger.info(f"SET MODE: '{value}'")
        self._mode = value

    @property
    def preset(self) -> Union[Rules, str]:
        return self._preset

    @preset.setter
    def preset(self, value: Union[Rules, str]) -> None:
        logger.info(f"SET RULE: '{value}'")
        self._preset = value if isinstance(value, str) else value.value

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
        b, s = self._preset.split('/')
        preset = (tuple(int(i) for i in b[1:]), tuple(int(i) for i in s[1:]))

        self.next_area, self.draw_rects = check_cells(
            current_field=self.current_area,
            next_field=self.next_area,
            width=self.size_area.width,
            height=self.size_area.height,
            mode=self.mode,
            rule=preset
        )

        self.current_area = copy.deepcopy(self.next_area)
