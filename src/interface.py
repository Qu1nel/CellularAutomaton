from typing import Tuple, Union, TypeAlias

import pygame as pg

from base import InterfaceBase, RectBase, Buttons

Number: TypeAlias = Union[int, float]


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

    def draw_menu(self) -> None:
        pass

    def draw_buttons(self) -> None:
        pass

    def draw_fps(self, frame_per_second: int) -> None:
        pass
