from typing import List, TypeAlias, Tuple

import pygame as pg

import config as c

from app import App
from cell import Cell
from utils import quick_copy

RowCell: TypeAlias = List[Cell]
MatrixCell: TypeAlias = List[RowCell]


class GameEngine:
    __slots__ = ('app', 'screen', 'color_cell', 'previous_area', 'area')
    app: App
    screen: pg.Surface
    color_cell: c.Color
    previous_area: MatrixCell  # previous state of area
    area: MatrixCell  # current state of area

    def __init__(self, app: App, screen: pg.Surface) -> None:
        self.app = app
        self.screen = screen
        self.color_cell = c.COLOR_CELL
        self.previous_area = [[]]

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

        def _normalized(coord: Tuple[int, int]) -> tuple[int, ...]:
            return tuple(i * c.CELL_SIZE for i in coord)

        for row in self.area:
            for cell in row:
                if cell.is_alive():
                    pg.draw.rect(
                        surface=self.screen,
                        color=self.color_cell,
                        rect=pg.Rect(_normalized(cell.coord), (c.CELL_SIZE - 2, c.CELL_SIZE - 2))
                    )

    def next_cycle(self) -> None:
        """Calculates the next state of self.area from the current state.

        Returns:
            None
        """
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

                if cell.is_alive():
                    if number_living not in (2, 3):
                        x, y = cell.coord
                        self.area[x][y].alive = False
                else:
                    if number_living == 3:
                        x, y = cell.coord
                        self.area[x][y].alive = True
