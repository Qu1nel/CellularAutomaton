"""
This file is a configuration file, i.e. it is solely responsible for configuring the operation of the main files.

It is better not to change some fields, because this may not lead to bad consequences.

Below are the fields (variables) that you can change, but taking into account the comments, if any.

    * WIDTH  // satisfactory values from 800 to <your monitor width resolution>
    * HEIGHT  // satisfactory values from 600 to <your monitor height resolution>

    * FPS  // satisfactory value from 30 to 30+

Version: 0.02
"""
from collections import namedtuple

WIDTH: int = 1920
HEIGHT: int = 1080
FPS: int = 144

# Below are the settings that it is not advisable to touch if you are not sure
# exactly what you are changing.
# -----------------------------------------------------------------------------

# Resolution window of app
WindowResolutionApp = namedtuple('WindowResolutionApp', ('Width', 'Height'))
Resolution = WindowResolutionApp(Width=WIDTH, Height=HEIGHT)

# Frame rate for app
FrameRate = FPS
