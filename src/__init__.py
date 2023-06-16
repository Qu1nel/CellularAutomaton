from pathlib import Path

from src.app import *
from src.base import *
from src.config import *
from src.engine import *
from src.interface import *
from src.main import main
from src.utils import *

__author__ = "Qu1nel"
__version__ = 1.0
__package__ = 'GameOfLife'
__license__ = Path(__file__).parent.with_name("LICENSE").read_text(encoding='UTF-8')
__doc__ = Path(__file__).parent.with_name("README.md").read_text(encoding='UTF-8')

del Path
