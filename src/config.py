from pathlib import Path

from pydantic import BaseModel, NonNegativeInt

from src.misc.type_aliases import Color, DeclareOptionModeType, DeclareOptionType, Resolution


class _MetaInfo(BaseModel):
    author: str = "Ivan Kovach"
    copyright: str = "Copyright 2024 (c) Ivan Kovach aka Qu1nel"
    license: str = Path(__file__).parent.with_name("LICENSE").read_text(encoding="UTF-8")
    version: str = "1.0.1"

    maintainer: str = "Ivan Kovach"
    email: str = "covach.qn@gmail.com"
    status: str = "Development"


class _GameSettings(BaseModel):
    fps: NonNegativeInt = 100
    low_fps: NonNegativeInt = 14
    chill_fps: NonNegativeInt = 18

    class GUIColors:
        cell: Color = Color(R=241, G=196, B=15)  # Yellow almost
        back_ground: Color = Color(R=50, G=50, B=50)  # Dark gray
        interface: Color = Color(R=30, G=39, B=46)

    class Sizes:
        cell: NonNegativeInt = 8


class _WindowConfig(BaseModel):
    caption: str = "Cellular Automaton"
    resolution: Resolution = Resolution(width=1600, height=900)

    class PathToFile:
        log_name: Path = Path("debug.log")
        icon: Path = Path("icons/icon.png")


class _RotationSettings(BaseModel):
    size: str = "2.5 MB"
    type: str = "zip"
    folder: str = "log"


class _CLI(BaseModel):
    class Docs:
        logging: str = "Enables game logging."
        hide_fps: str = "Disable showing fps in game."

        class Mode:
            moore: str = "Set Moore count neighbors mode (default)"
            neumann: str = "Set Neumann count neighbors mode"

    class Param:
        logging: DeclareOptionType = ("-L", "--logging/--no-logging")
        hide_fps: DeclareOptionType = ("-S", "--show-fps/--no-show-fps")
        moore: DeclareOptionModeType = ("-M", "--Moore", "mode")
        neumann: DeclareOptionModeType = ("-N", "--Neumann", "mode")


MetaInfo = _MetaInfo()
GameSettings = _GameSettings()
WindowConfig = _WindowConfig()
RotationSettings = _RotationSettings()
CLI = _CLI()
