"""The Game of Life is a cellular automaton."""

import sys
from pathlib import Path

import click
import pygame as pg
from loguru import logger

import src.misc.logs as lg
from src import cli, config
from src.main import _init
from src.misc.utils import exit_from_app_with_code

__author__ = config.MetaInfo.author
__copyright__ = config.MetaInfo.copyright
__license__ = config.MetaInfo.license
__version__ = config.MetaInfo.version

__maintainer__ = config.MetaInfo.maintainer
__email__ = config.MetaInfo.email
__status__ = config.MetaInfo.status


def resource_path(relative_path: Path) -> Path:
    """Function for working paths inside an exe for python."""
    base_path = Path(getattr(sys, "_MEIPASS", ".")).absolute()
    return base_path.joinpath(relative_path)


# the try/except block for the case of testing the cli part of the program
try:
    argv = cli.run(standalone_mode=False)
except (click.exceptions.NoSuchOption, click.exceptions.UsageError) as exc:
    logger.error(exc)
    argv = cli.default_argv

if isinstance(argv, int):
    exit_from_app_with_code(argv)

pg.init()
lg.init(log=argv.logging)

logger.debug(argv)

icon_path = config.WindowConfig.PathToFile.icon
pg.display.set_caption(config.WindowConfig.caption)

try:
    icon = pg.image.load(resource_path(icon_path))
except FileNotFoundError:
    logger.error(f"{resource_path(icon_path)} is not found.")
else:
    pg.display.set_icon(icon)

GameCellularAutomaton = _init(argv)
