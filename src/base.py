from enum import Enum
from abc import ABC, abstractmethod
from typing import Optional, Tuple, Union, Literal

import pygame as pg


class Buttons(dict):
    """Dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__  # type: ignore
    __delattr__ = dict.__delitem__  # type: ignore


class RectBase:
    left: Union[int, float]
    top: Union[int, float]
    width: Union[int, float]
    height: Union[int, float]

    radius: Optional[int] = None

    @property
    @abstractmethod
    def coord(self) -> Tuple[Union[int, float], Union[int, float], Union[int, float], Union[int, float]]:
        pass

    @abstractmethod
    def set_radius(self, param: int) -> None:
        pass


class Rules(str, Enum):
    b3_s23 = 'b3/s23'
    b1_s012345678 = 'b1/s012345678'
    b5678_s45678 = 'b5678/s45678'


class StateInit(int, Enum):
    RANDOM = 0
    DOT = 1


class InterfaceBase(ABC):
    screen: pg.SurfaceType

    width: int
    height: int

    buttons: Buttons

    @abstractmethod
    def draw_menu(self, mode: Literal['Moore', 'Neumann']) -> None:
        pass

    @abstractmethod
    def draw_buttons(self) -> None:
        pass

    @abstractmethod
    def draw_fps(self, frame_per_second: int) -> None:
        pass


class GameEngineBase(ABC):
    _mode: Literal['Moore', 'Neumann']

    @abstractmethod
    def init_area(self, state: StateInit) -> None:
        pass

    @property
    @abstractmethod
    def mode(self) -> Literal['Moore', 'Neumann']:
        pass

    @mode.setter
    @abstractmethod
    def mode(self, value: Literal['Moore', 'Neumann']) -> None:
        pass

    @property
    @abstractmethod
    def preset(self) -> Union[Rules, str]:
        pass

    @preset.setter
    @abstractmethod
    def preset(self, value: Union[Rules, str]) -> None:
        pass

    @abstractmethod
    def process(self) -> None:
        pass

    @abstractmethod
    def draw_area(self) -> None:
        pass


class AppBase(ABC):
    width: int
    height: int

    pause: bool
    fps: int

    screen: pg.SurfaceType

    GameEngine: GameEngineBase
    interface: InterfaceBase

    @abstractmethod
    def handle_events(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def process(self) -> None:
        pass

    @abstractmethod
    def loop(self) -> None:
        pass

    @abstractmethod
    def run(self) -> None:
        pass
