from abc import ABC, abstractmethod


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
    pass


class GameEngineBase(ABC):
    pass
