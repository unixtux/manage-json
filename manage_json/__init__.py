#!/usr/bin/env python3

__all__ = ('JsonManager',)

__version__ = '0.0.6'
VERSION = __version__

from apitele.logging import get_logger
logger = get_logger('json_management ' + VERSION)
del get_logger

from .manage_json import JsonManager
