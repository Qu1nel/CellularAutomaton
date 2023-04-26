import copy
from random import randint
from typing import Tuple, List, TypeAlias

import numpy as np
import pygame as pg

from numba import njit
from loguru import logger
from pygame import SurfaceType

import config as c

from base import AppBase, GameEngineBase
from config import Color

ResultToDrawing: TypeAlias = List[Tuple[int, int]]
CheckCells: TypeAlias = Tuple[np.ndarray, ResultToDrawing]


@njit(fastmath=True)
def check_cells(current_field: np.ndarray, next_field: np.ndarray, width: int, height: int) -> CheckCells:
    result_for_drawing = []

    for x in range(width - 1):
        for y in range(height - 1):
            count_living = 0
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if current_field[j][i] == 1:
                        count_living += 1

            if current_field[y][x] == 1:
                count_living -= 1
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
    __slots__ = ('app', 'screen', 'color_cell', 'current_area', 'next_area', 'width_area', 'height_area', 'draw_rects')
    app: AppBase
    screen: SurfaceType
    color_cell: Color
    current_area: np.ndarray[np.ndarray[int]]
    next_area: np.ndarray[np.ndarray[int]]
    draw_rects: List
    width_area: int
    height_area: int

    def __init__(self, app: AppBase, screen: pg.Surface) -> None:
        logger.debug("Start of class initialization {}", self.__class__.__name__)
        self.app = app
        self.screen = screen
        self.color_cell = c.COLOR_CELL

        self.width_area = self.app.width // c.CELL_SIZE
        self.height_area = self.app.height // c.CELL_SIZE

        logger.info("Number of cells in width - {}", self.width_area)
        logger.info("Number of cells in height - {}", self.height_area)

        self.current_area = np.array([[randint(0, 1) for _ in range(self.width_area)] for _ in range(self.height_area)])
        self.next_area = np.array([[0 for _ in range(self.width_area)] for _ in range(self.height_area)])
        self.draw_rects = []

        logger.debug("Finish of class initialization {}", self.__class__.__name__)

    def process(self) -> None:
        self.next_area, self.draw_rects = check_cells(
            current_field=self.current_area,
            next_field=self.next_area,
            width=self.width_area,
            height=self.height_area
        )

        self.current_area = copy.deepcopy(self.next_area)

    def draw_area(self) -> None:
        for x, y in self.draw_rects:
            pg.draw.rect(
                surface=self.screen,
                color=self.color_cell,
                rect=(x * c.CELL_SIZE, y * c.CELL_SIZE, c.CELL_SIZE - 1, c.CELL_SIZE - 1)
            )
