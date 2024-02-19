import copy
from random import randint
from typing import Union, assert_never, cast

import numpy as np
from loguru import logger

from src import config
from src.bases import AppBase, GameEngineBase
from src.engines.core import check_cells
from src.misc.states import Mode, Rules, StateInit
from src.misc.type_aliases import ResultToDrawing, Size
from src.misc.utils import get_empty_area


class GameEngine(GameEngineBase):
    """A game engine that performs all the calculations for the game.

    Attributes:
        _mode: The mod you need to render the game with.
        app: An instance of the game.
        current_area: Current playing field.
        next_area: The following is the state of the playing field.
        size_area: Size of playing filed.

    """

    app: AppBase
    current_area: np.ndarray
    next_area: np.ndarray
    size_area: Size

    def __init__(self, app: AppBase) -> None:
        self.app = app
        self._preset: str = Rules.b3_s23.value

        width_area = self.app.resolution.width // config.GameSettings.Sizes.cell
        height_area = self.app.resolution.height // config.GameSettings.Sizes.cell
        self.size_area = Size(width=width_area, height=height_area)

        self.current_area = self.init_area(state=StateInit.RANDOM)
        self.next_area = get_empty_area(width=width_area, height=height_area)

    def init_area(self, state: StateInit) -> np.ndarray:
        """Initialization of the initial playing field.

        Args:
            state: Reconfiguring initialization for the playing field.

        Returns:
            The matrix as a playing field.
        """
        width = self.app.resolution.width // config.GameSettings.Sizes.cell
        height = self.app.resolution.height // config.GameSettings.Sizes.cell

        match state:
            case StateInit.RANDOM:
                current_area = np.array([[randint(0, 1) for _ in range(width)] for _ in range(height)])
            case StateInit.DOT:
                current_area = np.array([[0 for _ in range(width)] for _ in range(height)])
                current_area[height // 2][width // 2] = 1
            case _ as unreachable:
                assert_never(unreachable)

        return current_area

    @property
    def mode(self) -> Mode:
        """Property for `_mode` attribute."""
        return self._mode

    @mode.setter
    def mode(self, value: Mode) -> None:
        self._mode = value

    @property
    def preset(self) -> Union[Rules, str]:
        """Property for `_preset` attribute."""
        return self._preset

    @preset.setter
    def preset(self, value: Union[Rules, str]) -> None:
        logger.info(f"SET RULE: '{value}'")
        if isinstance(value, str):
            self._preset = value
        if isinstance(value, Rules):
            self._preset = value.value
        else:
            msg = "no way"
            raise TypeError(msg)

    def process(self) -> ResultToDrawing:
        """Calculates the next state of self.area from the current state."""
        b, s = self._preset.split("/")
        preset = (tuple(int(i) for i in b[1:]), tuple(int(i) for i in s[1:]))

        self.next_area, draw_rects = check_cells(
            current_field=self.current_area,
            next_field=self.next_area,
            width=self.size_area.width,
            height=self.size_area.height,
            mode=self.mode.get_name(),
            rule=preset,
        )

        self.current_area = copy.deepcopy(self.next_area)

        return cast(ResultToDrawing, draw_rects)
