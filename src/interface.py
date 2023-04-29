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


class Button(Rect):
    def collidepoint(self, x: int, y: int) -> bool:
        return self.left <= x <= self.left + self.width and self.top <= y <= self.top + self.height


class Interface(InterfaceBase):
    def __init__(self, screen: pg.SurfaceType, width: int, height: int):
        self.screen = screen

        self.width = width
        self.height = height

        self.hide_menu = False
        self.buttons_menu = Buttons()
        self._init_menu()

        self.buttons = Buttons()
        self._init_buttons()

        self._draw_bg_rect_on_display = partial(pg.draw.rect, surface=self.screen, color=COLOR_INTERFACE)
        self._draw_frame_rect_on_display = partial(pg.draw.rect, surface=self.screen, color=Colors.BLACK.value)

    def _init_menu(self) -> None:
        """Initializes the position and properties of the menu."""
        self._height_menu = int(self.height * 0.16 * (len(self.buttons_menu) + 1))
        self._width_menu = int(self.width * 0.08)
        self._radius = int(self._width_menu * 0.15)
        self._x_menu = self.width * 0.01
        self._y_menu = self.height / 2 - self._height_menu / 2
        self._rect_menu = pg.Rect(self._x_menu, self._y_menu, self._width_menu, self._height_menu)

    def _init_buttons(self) -> None:
        """Initializes buttons."""
        self.buttons.hide_menu = Button(
            left=self._x_menu + self._width_menu - self._radius,
            top=self._y_menu + self._height_menu - self._height_menu * 0.01,
            width=self._radius * 2,
            height=self._radius * 2
        )
        self.buttons.open_menu = Button(
            left=-self.width * 0.02,
            top=self.height / 2 - self.height * 0.2 / 2,
            width=self.width * 0.04,
            height=self.height * 0.2
        )

    def draw_menu(self) -> None:
        """Draws a menu containing buttons on the left

        The menu can be hidden by clicking on the arrow in the lower right
        corner of the menu.

        The menu is drawn relative to the size of the window. It all depends
        on the length and width of the window.

        Returns:
            None
        """
        if not self.hide_menu:
            self._draw_bg_rect_on_display(
                rect=self._rect_menu,
                border_radius=self._radius
            )

            pg.draw.circle(
                surface=self.screen,
                color=COLOR_INTERFACE,
                center=(self._x_menu + self._width_menu,
                        self._y_menu + (self._height_menu / 2) * 2 + self.width * 0.01),
                radius=self._radius
            )
        else:
            width_open_menu = self.width * 0.04
            self._draw_bg_rect_on_display(
                rect=(-width_open_menu / 2, self.height / 2 - self.height * 0.2 / 2,
                      width_open_menu, self.height * 0.2),
                border_radius=self._radius
            )

        pg.draw.rect(surface=self.screen, color=Colors.RED.value, rect=self.buttons.hide_menu.coord, width=2)
        pg.draw.rect(surface=self.screen, color=Colors.RED.value, rect=self.buttons.open_menu.coord, width=2)

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
