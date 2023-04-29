from typing import Tuple, Union, TypeAlias
from functools import partial
from enum import Enum

import pygame as pg

from base import InterfaceBase, RectBase, Buttons
from config import COLOR_INTERFACE

Number: TypeAlias = Union[int, float]


class Colors(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)


class Rect(RectBase):
    def __init__(self, left: Number, top: Number, width: Number, height: Number):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def set_radius(self, value: int) -> None:
        self.radius = value

    @property
    def coord(self) -> Tuple[int, int, int, int]:
        return self.left, self.top, self.width, self.height


class Interface(InterfaceBase):
    def __init__(self, screen: pg.SurfaceType, width: int, height: int):
        self.screen = screen

        self.width = width
        self.height = height

        self.buttons = Buttons()

        self._draw_bg_rect_on_display = partial(pg.draw.rect, surface=self.screen, color=COLOR_INTERFACE)
        self._draw_frame_rect_on_display = partial(pg.draw.rect, surface=self.screen, color=Colors.BLACK.value)

    def draw_menu(self) -> None:
        height_menu = int(self.height * 0.16 * (len(self.buttons) + 1))  # Depends on the number of buttons in the menu
        width_menu = int(self.width * 0.08)

        radius = int(width_menu * 0.15)

        x_menu = self.width * 0.01
        y_menu = self.height / 2 - height_menu / 2

        self._draw_bg_rect_on_display(
            rect=(x_menu, y_menu, width_menu, height_menu),
            border_radius=radius
        )

        pg.draw.circle(
            surface=self.screen,
            color=COLOR_INTERFACE,
            center=(x_menu + width_menu, y_menu + (height_menu / 2) * 2 + self.width * 0.01),
            radius=radius
        )

    def draw_buttons(self) -> None:
        pass

    def draw_fps(self, frame_per_second: int) -> None:
        """Draws FPS on the screen in the upper right corner of the game.

        Args:
            frame_per_second: Just a number that will be displayed as fps
                on the screen.

        Returns:
            None
        """
        radius = int(self.width * 0.04)
        height = self.height * 0.08

        width_point = self.width * 0.94
        height_point = -(height / 2)

        pg.draw.rect(
            surface=self.screen,
            color=COLOR_INTERFACE,
            rect=(width_point, height_point, 1000, height),
            border_radius=radius
        )

        pg.draw.rect(
            surface=self.screen,
            color=Colors.BLACK.value,
            rect=(width_point, height_point, 1000, height),
            border_radius=radius,
            width=2
        )

        font = pg.font.SysFont("arial", int(height / 3))
        img = font.render(f'fps {frame_per_second}', True, Colors.GREEN.value)

        self.screen.blit(img, (self.width * 0.952, self.height * 0.004))
