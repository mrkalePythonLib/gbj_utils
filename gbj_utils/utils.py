# -*- coding: utf-8 -*-
"""Module for auxilliary constants, utilities, and functions."""
__version__ = '0.4.0'
__status__ = 'Beta'
__author__ = 'Libor Gabaj'
__copyright__ = 'Copyright 2019-2020, ' + __author__
__credits__ = []
__license__ = 'MIT'
__maintainer__ = __author__
__email__ = 'libor.gabaj@gmail.com'


import platform
import os
import psutil


###############################################################################
# Functions
###############################################################################
def check_service(script: str) -> bool:
    """Detect running script as a service.

    Arguments
    ---------
    script : str
        Name of a script process to be checked or script file name without
        path and extension.

    Returns
    -------
    bool
        Flag about running script as a service.

    """
    lst = []
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] == script:
            lst.append(process)
    return len(lst) > 0


def linux() -> bool:
    """Return flag about running on Linux platform."""
    return platform.system() == 'Linux'


def windows() -> bool:
    """Return flag about running on Windows platform."""
    return platform.system() == 'Windows'


def root() -> bool:
    """Return flag about running on Linux as root."""
    if hasattr(os, 'getegid'):
        return os.getegid() == 0  # pylint: disable=no-member
    return True


def envdir(env_var: str) -> str:
    """Return folder from environment variable or current one."""
    result = None
    if os.environ.get(env_var):
        result = os.path.expandvars('$' + env_var)
        if not os.path.isdir(result):
            result = None
    return result or os.getcwd()
