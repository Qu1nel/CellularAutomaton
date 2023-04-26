from abc import ABC, abstractmethod
from typing import Tuple, Union


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
    alive: Union[bool, int]
    coord: Tuple[int, int]

    @abstractmethod
    def copy(self) -> 'CellBase':
        pass


class GameEngineBase(ABC):
    @abstractmethod
    def process(self) -> None:
        pass

    @abstractmethod
    def draw_area(self) -> None:
        pass
