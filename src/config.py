"""
This file is a configuration file, i.e. it is solely responsible for configuring the operation of the main files.

It is better not to change some fields, because this may not lead to bad consequences.

Below are the fields (variables) that you can change, but taking into account the comments, if any.

    * WIDTH  // satisfactory values from 800 to <your monitor width resolution>
    * HEIGHT  // satisfactory values from 600 to <your monitor height resolution>

    * FPS  // satisfactory value from 30 to 30+

    * COLOR_BG  // The background color set by the RGB color model
    * COLOR_CELL  // The cell color set by the RGB color model

    * CELL_SIZE  // Size PxP pixels for one cell per field

    * FILE_LOG_NAME  // Name for the log file. Has a value when run with the --debug flag | -D

Version: 0.06
"""
from collections import namedtuple
from typing import Tuple

WIDTH: int = 1920
HEIGHT: int = 1080
FPS: int = 144
ColorCell: Tuple[int, int, int] = (241, 196, 15)  # Yellow almost
CellSize: int = 5

# Below are the settings that it is not advisable to touch if you are not sure
# exactly what you are changing.
# -----------------------------------------------------------------------------

# Resolution window of app
WindowResolutionApp = namedtuple('WindowResolutionApp', ('Width', 'Height'))
Resolution = WindowResolutionApp(Width=WIDTH, Height=HEIGHT)

# Frame rate for app
FrameRate = FPS

# RGB Color Model
Color = namedtuple("Color", ("R", "G", "B"))
COLOR_BG = Color(R=50, G=50, B=50)
COLOR_CELL: Color = Color(*ColorCell)

# Cell size
CELL_SIZE = CellSize

FILE_LOG_NAME: str = "debug.log"
