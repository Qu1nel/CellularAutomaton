"""
This file is a configuration file, i.e. it is solely responsible for configuring the operation of the main files.

It is better not to change some fields, because this may not lead to bad consequences.

Below are the fields (variables) that you can change, but taking into account the comments, if any.

    * WIDTH  // satisfactory values from 800 to <your monitor width resolution>
    * HEIGHT  // satisfactory values from 600 to <your monitor height resolution>

    * FPS  // satisfactory value from 30 to 30+

    * COLOR_BG  // The background color set by the RGB color model
    * COLOR_CELL  // The cell color set by the RGB color model

    * CELL_SIZE  // Size P×P pixels for one cell per field (minimum is 2px)

    * FILE_LOG_NAME  // Name for the log file. Has a value when run with the --debug flag | -D

Version: 0.11
"""
from collections import namedtuple
from typing import Tuple

# For correct operation of interface rendering, please use wide format resolutions. 4:3, 1:1 not supported
WIDTH_APP: int = 1600
HEIGHT_APP: int = 900
FPS: int = 30
cell_color: Tuple[int, int, int] = (241, 196, 15)  # Yellow almost
bg_color: Tuple[int, int, int] = (50, 50, 50)  # Dark Gray
cell_size_px: int = 5  # Minimum value is 2

# Below are the settings that it is not advisable to touch if you are not sure
# exactly what you are changing.
# -----------------------------------------------------------------------------

# Resolution window of app
WindowResolutionApp = namedtuple('WindowResolutionApp', ('Width', 'Height'))
RESOLUTION_APP = WindowResolutionApp(Width=WIDTH_APP, Height=HEIGHT_APP)

# Frame rate for app
FRAME_RATE = FPS

# RGB Color Model
Color = namedtuple("Color", ("R", "G", "B"))
COLOR_BG = Color(R=50, G=50, B=50)
COLOR_CELL = Color(*cell_color)
COLOR_INTERFACE = Color(R=30, G=39, B=46)

# Cell size
CELL_SIZE = cell_size_px

FILE_LOG_NAME: str = "debug.log"
