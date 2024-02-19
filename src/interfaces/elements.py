from dataclasses import dataclass, field
from enum import Enum

import pygame as pg
from pydantic import NonNegativeFloat, NonNegativeInt

from src.bases import ButtonBase, RectBase
from src.config import GameSettings
from src.misc.type_aliases import Color, Resolution


class Rect(RectBase):
    """Rectangle object."""

    def __init__(
        self, left: NonNegativeInt, top: NonNegativeInt, width: NonNegativeInt, height: NonNegativeInt
    ) -> None:
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        self.radius = -1

    def set_radius(self, value: int) -> None:
        """Set radius for rectangle (pseudo setter)."""
        self.radius = value

    @property
    def coord(self) -> tuple[NonNegativeInt, NonNegativeInt, NonNegativeInt, NonNegativeInt]:
        """Property for coordinates of rectangle."""
        return self.left, self.top, self.width, self.height


class Button(ButtonBase):
    """Button object.

    Attributes:
        draw: Flag a whether to render the button or not.
        name: String for drawing as text on button.

    """

    def __init__(
        self,
        left: NonNegativeFloat,
        top: NonNegativeFloat,
        width: NonNegativeFloat,
        height: NonNegativeFloat,
        draw: bool,
    ) -> None:
        self.draw = draw

        self.left = left
        self.top = top
        self.width = width
        self.height = height

        self.radius = -1

    def set_radius(self, value: int) -> None:
        """Set radius (pseudo setter)."""
        self.radius = value

    def set_drawing(self, value: bool) -> None:
        """Set draw flag (pseudo setter)."""
        self.draw = value

    def drawing_name(self, value: str) -> None:
        """Set draw flag (pseudo setter)."""
        self.name = value

    @property
    def coord(self) -> tuple[NonNegativeFloat, NonNegativeFloat, NonNegativeFloat, NonNegativeFloat]:
        """Property for coordinates of button."""
        return self.left, self.top, self.width, self.height

    def collidepoint(self, x: NonNegativeInt, y: NonNegativeInt) -> bool:
        """Check intersection with another object (which have x and y)."""
        return self.left <= x <= self.left + self.width and self.top <= y <= self.top + self.height


@dataclass
class Menu:
    """Menu object."""

    parent_resolution: Resolution

    width: NonNegativeInt
    height: NonNegativeInt

    x: NonNegativeFloat = field(init=False)
    y: NonNegativeFloat = field(init=False)
    radius: NonNegativeInt = field(init=False)
    rect: pg.Rect = field(init=False)

    def __post_init__(self) -> None:
        self.radius = int(self.width * 0.15)
        self.x = self.parent_resolution.width * 0.01
        self.y = self.parent_resolution.height / 2 - self.height / 2
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)


class GUIColors(Enum):
    """GUI COLORS for game."""

    BLACK = Color(R=0, G=0, B=0)
    WHITE = Color(R=255, G=255, B=255)
    GREEN = Color(R=0, G=255, B=0)
    RED = Color(R=255, G=0, B=0)
    BLUE = Color(R=0, G=0, B=255)

    BG = GameSettings.GUIColors.back_ground
    INTERFACE = GameSettings.GUIColors.interface
    CELL = GameSettings.GUIColors.cell

    def rgb(self) -> tuple[NonNegativeInt, NonNegativeInt, NonNegativeInt]:
        """Return color as RGB model (as tuple[int, int, int])."""
        return self.value.get_rgb()

    def hex(self, lower: bool = False, prefix: bool = True) -> str:
        """Return color as HEX model."""
        r, g, b = self.rgb()
        _prefix = "0x" if prefix is True else ""
        result = _prefix + f"{r:x}".rjust(2, "0") + f"{g:x}".rjust(2, "0") + f"{b:x}".rjust(2, "0")
        return result.upper() if lower else result.lower()

    @classmethod
    def default_color(cls) -> "GUIColors":
        """Return a default color (RED)."""
        return cls.RED

    def __str__(self) -> str:
        return self.name.lower()
