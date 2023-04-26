from typing import Tuple

from base import CellBase


class Cell(CellBase):
    __slots__ = ('coord', 'alive')
    alive: bool
    coord: Tuple[int, int]

    def __init__(self, coord: Tuple[int, int], alive: bool = False) -> None:
        self.alive = alive
        self.coord = coord

    def __str__(self) -> str:
        return f'Cell(alive={self.alive} coord={self.coord})'

    def copy(self) -> 'Cell':
        """Copies itself, creating a new cell

        Returns:
            Copy of the instance
        """
        return Cell(coord=self.coord, alive=self.alive)