from abc import ABC, abstractmethod
from typing import Tuple


class AppBase(ABC):
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
    @property
    @abstractmethod
    def coord(self) -> Tuple[int, int]:
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        pass

    @abstractmethod
    def copy(self) -> 'CellBase':
        pass


class GameEngineBase(ABC):
    pass
