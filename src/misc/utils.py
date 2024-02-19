import sys
from abc import ABCMeta
from typing import Any, ClassVar, NoReturn

import numpy as np
import pygame as pg
from pydantic import NonNegativeInt


class SingletonABC(ABCMeta):
    """Class template singleton."""

    _instances: ClassVar[dict] = {}

    def __call__(cls: Any, *args: Any, **kwargs: Any):  # type: ignore  # noqa: ANN204, D102
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


def exit_from_app_with_code(code: int = 0) -> NoReturn:
    """Correctly exits the game.

    Args:
        code: Code that return app

    Returns:
        Nothing

    """
    pg.quit()
    sys.exit(code)


def get_empty_area(width: NonNegativeInt, height: NonNegativeInt) -> np.ndarray:
    """Generates an empty playing field.

    Args:
        width: A width a playing field.
        height: A height a playing field.

    Returns:
        The Matrix as a playing field.
    """
    return np.array([[0 for _ in range(width)] for _ in range(height)])
