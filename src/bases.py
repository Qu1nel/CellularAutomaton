from abc import ABC, abstractmethod

import numpy as np
import pygame as pg
from pydantic import NonNegativeFloat, NonNegativeInt

from src.misc.states import Mode, Rules, StateInit
from src.misc.type_aliases import Resolution, ResultToDrawing
from src.misc.utils import SingletonABC


class RectBase(ABC):
    left: NonNegativeInt
    top: NonNegativeInt
    width: NonNegativeInt
    height: NonNegativeInt

    radius: int | None = None

    @property
    @abstractmethod
    def coord(self) -> tuple[NonNegativeInt, NonNegativeInt, NonNegativeInt, NonNegativeInt]:
        pass

    @abstractmethod
    def set_radius(self, value: int) -> None:
        pass


class ButtonBase(ABC):
    name: str | None = None
    draw: bool

    left: NonNegativeFloat
    top: NonNegativeFloat
    width: NonNegativeFloat
    height: NonNegativeFloat

    radius: int | None = None

    @property
    @abstractmethod
    def coord(self) -> tuple[NonNegativeFloat, NonNegativeFloat, NonNegativeFloat, NonNegativeFloat]:
        pass

    @abstractmethod
    def set_radius(self, value: NonNegativeInt) -> None:
        pass

    @abstractmethod
    def set_drawing(self, value: bool) -> None:
        pass

    @abstractmethod
    def drawing_name(self, value: str) -> None:
        pass

    @abstractmethod
    def collidepoint(self, x: NonNegativeInt, y: NonNegativeInt) -> bool:
        pass


class GUIBase(metaclass=SingletonABC):
    screen: pg.SurfaceType
    resolution: Resolution
    buttons: dict[str, ButtonBase]

    hide_menu: bool

    @property
    @abstractmethod
    def drawing_cells(self) -> ResultToDrawing:
        pass

    @drawing_cells.setter
    @abstractmethod
    def drawing_cells(self, value: ResultToDrawing) -> None:
        pass

    @abstractmethod
    def draw_cells(self) -> None:
        pass

    @abstractmethod
    def draw_menu(self, mode: Mode) -> None:
        pass

    @abstractmethod
    def draw_buttons(self) -> None:
        pass

    @abstractmethod
    def draw_fps(self, frame_per_second: NonNegativeInt) -> None:
        pass

    @abstractmethod
    def fill_bg(self) -> None:
        pass

    @abstractmethod
    def update_display(self) -> None:
        pass


class GameEngineBase(metaclass=SingletonABC):
    _mode: Mode

    @abstractmethod
    def init_area(self, state: StateInit) -> np.ndarray:
        pass

    @property
    @abstractmethod
    def mode(self) -> Mode:
        pass

    @mode.setter
    @abstractmethod
    def mode(self, value: Mode) -> None:
        pass

    @property
    @abstractmethod
    def preset(self) -> Rules | str:
        pass

    @preset.setter
    @abstractmethod
    def preset(self, value: Rules | str) -> None:
        pass

    @abstractmethod
    def process(self) -> ResultToDrawing:
        pass


class AppBase(metaclass=SingletonABC):
    resolution: Resolution

    pause: bool

    screen: pg.SurfaceType
    clock: pg.time.Clock

    engine: GameEngineBase
    gui: GUIBase

    def __init__(self, res: Resolution, pause: bool) -> None:
        self.resolution = res
        self.pause = pause

        self.screen = pg.display.set_mode(self.resolution.values())
        self.clock = pg.time.Clock()

    @abstractmethod
    def _handle_events(self) -> None:
        pass

    @abstractmethod
    def _draw(self) -> None:
        pass

    @abstractmethod
    def _process(self) -> None:
        pass

    @abstractmethod
    def _loop(self) -> None:
        pass

    @abstractmethod
    def _run(self) -> None:
        pass
