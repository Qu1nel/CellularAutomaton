from typing import Sequence, Tuple

from . import base


class Cell(base.CellBase):
    __slots__ = ('__x', '__y', 'alive')
    alive: bool
    __x: int
    __y: int

    def __init__(self, coord: Sequence[int], alive: bool = False) -> None:
        assert len(coord) == 2
        self.alive = alive
        self.__x, self.__y = coord

    def __str__(self) -> str:
        return f'Cell(alive={self.alive} coord={self.coord})'

    @property
    def coord(self) -> Tuple[int, int]:
        """Property for taking __x and __y"""
        return self.__x, self.__y

    def is_alive(self) -> bool:
        """Returns the state of life of the cell.

        Returns:
            Status is the cell alive or not
        """
        return self.alive

    def copy(self) -> 'Cell':
        """Copies itself, creating a new cell

        Returns:
            Copy of the instance
        """
        return Cell(coord=self.coord, alive=self.alive)
