from typing import Literal

import numpy as np
from numba import njit  # type: ignore

from src.misc.type_aliases import CheckCells


@njit(fastmath=True)  # type: ignore
def count_neighbors_Moore(field: np.ndarray, row: int, column: int, width_field: int, height_field: int) -> int:
    """Efficient* counts all 8 neighbors for a cell.

    The function does not go through all 8 possible values around the cell, but
    only through 4 of them, and it does it mirrored about the center, i.e.,
    about the cell for which the calculation is made. Thereby reducing
    the number of iterations from 9 maximum possible to 4.

    Args:
        field: The field on which the cells are located
        row: Cell x coordinate for which neighbors are calculated
        column: Cell y coordinate for which neighbors are calculated
        width_field: Field width - boundary for calculations
        height_field: Field height - boundary for calculations

    Returns:
        The number of living cells in a cell with x and y coordinates.
    """
    neighbors = 0

    for i, j in ((-1, 1), (0, 1), (1, 1), (1, 0)):
        x = row + i
        y = column + j
        if 0 <= y < width_field and 0 <= x < height_field:
            neighbors += field[x][y]

        x = row - i
        y = column - j
        if 0 <= y < width_field and 0 <= x < height_field:
            neighbors += field[x][y]

    return neighbors


@njit(fastmath=True)  # type: ignore
def count_neighbors_Neumann(field: np.ndarray, row: int, column: int, width_field: int, height_field: int) -> int:
    """Efficient* counts only 4 neighbors for a cell.

    Like the count_neighbors_Neumann function, it also counts the cell's
    neighbors. But it counts only those who are located on the same axis
    as the central cell, i.e. it counts only 4 of its neighbors. At what
    using only 2 iterations for this.

    Args:
        field: The field on which the cells are located
        row: Cell x coordinate for which neighbors are calculated
        column: Cell y coordinate for which neighbors are calculated
        width_field: Field width - boundary for calculations
        height_field: Field height - boundary for calculations

    Returns:
        The number of living cells in a cell with x and y coordinates.
    """
    neighbors = 0

    for i, j in ((1, 0), (0, 1)):
        x = row + i
        y = column + j
        if 0 <= y < width_field and 0 <= x < height_field:
            neighbors += field[x][y]

        x = row - i
        y = column - j
        if 0 <= y < width_field and 0 <= x < height_field:
            neighbors += field[x][y]

    return neighbors


@njit(fastmath=True)
def check_cells(
    current_field: np.ndarray,
    next_field: np.ndarray,
    width: int,
    height: int,
    rule: tuple[tuple[int, ...], tuple[int, ...]],
    mode: Literal["Moore", "Neumann"] = "Moore",
) -> CheckCells:
    """Counts for each cell how many living neighbors are nearby (3x3 cells).

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
        rule: A rule of the form [(2, ...), (3, 4, ...)] means that the cell
            appears with 2 neighbors, and survives if out of 3 or 4.

    Raises:
        ValueError: If `mode` argument was not passed.

    Returns:
        Calculated state for the next step, and an array of live cells that
        will be drawn.
    """
    result_for_drawing = []

    for x in range(width):
        for y in range(height):
            if mode == "Neumann":
                count_living = count_neighbors_Neumann(
                    field=current_field,
                    row=y,
                    column=x,
                    width_field=width,
                    height_field=height,
                )
            elif mode == "Moore":
                count_living = count_neighbors_Moore(
                    field=current_field,
                    row=y,
                    column=x,
                    width_field=width,
                    height_field=height,
                )
            else:
                msg = "mode is not set!"
                raise ValueError(msg)

            _be = rule[0]
            _survives = rule[1]

            # Apply rules for number of live cells nearby
            if current_field[y][x] == 1:
                if count_living in _survives:
                    next_field[y][x] = 1
                    result_for_drawing.append((x, y))
                else:
                    next_field[y][x] = 0
            elif count_living in _be:
                next_field[y][x] = 1
                result_for_drawing.append((x, y))
            else:
                next_field[y][x] = 0

    return next_field, result_for_drawing
