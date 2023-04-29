from enum import Enum
from functools import partial
from typing import Tuple, TypeAlias, Union

import pygame as pg

from base import Buttons, InterfaceBase, RectBase
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

        self.radius = -1

    def set_radius(self, value: int) -> None:
        self.radius = value

    @property
    def coord(self) -> Tuple[Number, Number, Number, Number]:
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
        pass

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
        height = int(self.height * 0.08)

        width_point = int(self.width * 0.94)
        height_point = -int((height / 2))

        self._draw_bg_rect_on_display(
            rect=(width_point, height_point, 1000, height),
            border_radius=radius
        )

        self._draw_frame_rect_on_display(
            rect=(width_point, height_point, 1000, height),
            border_radius=radius,
            width=2
        )

        font = pg.font.SysFont("arial", int(height / 3))

        # Draw red fps if it's too low
        if frame_per_second <= 15:
            color = Colors.RED.value
        else:
            color = Colors.GREEN.value

        img = font.render(f'fps {frame_per_second}', True, color)

        self.screen.blit(img, (self.width * 0.952, self.height * 0.004))
