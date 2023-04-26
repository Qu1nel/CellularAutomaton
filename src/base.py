from abc import ABC, abstractmethod


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


class GameEngineBase(ABC):
    @abstractmethod
    def process(self) -> None:
        pass

    @abstractmethod
    def draw_area(self) -> None:
        pass
