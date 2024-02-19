from typing import TypeAlias

import numpy as np
from pydantic import BaseModel, NonNegativeInt


class Color(BaseModel):
    """Color as RGB model."""

    R: NonNegativeInt
    G: NonNegativeInt
    B: NonNegativeInt

    def get_rgb(self) -> tuple[NonNegativeInt, NonNegativeInt, NonNegativeInt]:
        """Pseudo property for get color as tuple with int (RGB)."""
        return self.R, self.G, self.B


class Size(BaseModel):
    """Size model with `width` and `height` attr."""

    width: NonNegativeInt
    height: NonNegativeInt


class Resolution(BaseModel):
    """Resolution model for window of game."""

    width: NonNegativeInt
    height: NonNegativeInt

    def values(self) -> tuple[NonNegativeInt, NonNegativeInt]:
        """Pseudo property for get a resolution as tuple with int (width, height)."""
        return self.width, self.height


ResultToDrawing: TypeAlias = list[tuple[int, int]]
CheckCells: TypeAlias = tuple[np.ndarray, ResultToDrawing]

NumberType: TypeAlias = int | float
ColorType: TypeAlias = Color | tuple[int, int, int]
DeclareOptionType: TypeAlias = tuple[str, str]
DeclareOptionModeType: TypeAlias = tuple[str, str, str]
