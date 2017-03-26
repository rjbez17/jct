"""
    yact
    ~~~~~
    Yet Another Configuration Tool -
    A JSON based Python config tool loosely based on node.js config
    :copyright: (c) 2017 by Ryan Bezdicek.
    :license: MIT, see LICENSE for more details.
"""

__version__ = '0.1-dev'

from .yact import Yact, Config, create_config, load_env_vars
