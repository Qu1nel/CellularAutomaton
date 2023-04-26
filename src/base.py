from abc import ABC, abstractmethod
from typing import Tuple


class AppBase(ABC):
    width: int
    height: int

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


class CellBase(ABC):
    alive: bool
    coord: Tuple[int, int]

    @abstractmethod
    def copy(self) -> 'CellBase':
        pass


class GameEngineBase(ABC):
    @abstractmethod
    def draw_area(self) -> None:
        pass

    @abstractmethod
    def next_cycle(self) -> None:
        pass
