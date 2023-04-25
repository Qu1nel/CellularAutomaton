from typing import List, TypeAlias

import pygame as pg

import config as c

from app import App
from cell import Cell

RowCell: TypeAlias = List[Cell]
MatrixCell: TypeAlias = List[RowCell]


class GameEngine:
    __slots__ = ('app', 'screen', 'color_cell', 'previous_area', 'area')
    app: App
    screen: pg.Surface
    color_cell: c.Color
    previous_area: MatrixCell | None  # previous state of area
    area: MatrixCell  # current state of area

    def __init__(self, app: App, screen: pg.Surface) -> None:
        self.app = app
        self.screen = screen
        self.color_cell = c.COLOR_CELL
        self.previous_area = None

        width_x, height_y = self.app.width // c.CELL_SIZE, self.app.height // c.CELL_SIZE

        self.area = []
        for y in range(height_y):
            row: RowCell = []

            for x in range(width_x):
                row.append(Cell(coord=(x, y), alive=True))

            self.area.append(row)

    def draw_area(self) -> None:
        """Draws the cells in self.area on the monitor.

        Returns:
            None
        """
