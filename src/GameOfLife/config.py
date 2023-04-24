"""
This file is a configuration file, i.e. it is solely responsible for configuring the operation of the main files.

It is better not to change some fields, because this may not lead to bad consequences.

Below are the fields (variables) that you can change, but taking into account the comments, if any.

    * WIDTH  // satisfactory values from 800 to <your monitor width resolution>
    * HEIGHT  // satisfactory values from 600 to <your monitor height resolution>

Version: 0.01
"""
from collections import namedtuple

WIDTH: int = 1920
HEIGHT: int = 1080

# Below are the settings that it is not advisable to touch if you are not sure
# exactly what you are changing.
# -----------------------------------------------------------------------------

_resolution = namedtuple('WindowResolutionApp', ('Width', 'Height'))
Resolution = _resolution(Width=WIDTH, Height=HEIGHT)
