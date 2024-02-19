from enum import Enum
from typing import Literal, cast

from pydantic import BaseModel


class Mode(Enum):
    """Status of processing the playing field according to specified laws."""

    MOORE = "Moore"
    NEUMANN = "Neumann"

    def get_name(self) -> Literal["Moore", "Neumann"]:
        """Return a name of mode."""
        result = self.value
        return cast(Literal["Moore", "Neumann"], result)


class ARGV(BaseModel):
    """Argument values typing model for CLI."""

    logging: bool
    show_fps: bool
    mode: Mode


class Rules(str, Enum):
    """The rules by which cells on the playing field are calculated.

    The rule is built like this: first bN, where N is the number of cells that
    is necessary for the appearance of a new one (b - to be), then “/” and sM,
    where M is the number of cells that is necessary for the survival of the
    cell (s - survival).
    """

    b3_s23 = "b3/s23"
    b1_s012345678 = "b1/s012345678"
    b5678_s45678 = "b5678/s45678"


class StateInit(int, Enum):
    """Status of init a start playing area."""

    RANDOM = 0
    DOT = 1  # A dot in center area.
