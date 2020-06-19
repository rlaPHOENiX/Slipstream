#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Slipstream - The most informative Home-media backup solution.
Copyright (C) 2020 PHOENiX

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

~~~

Metadata used throughout the application.
By calculating all the metadata in __version__.py, it allows us
to easily expose the information to the user via import as well as
throughout the code by importing only what we want.
"""

# std
import os
import datetime
import platform
import pkg_resources
# pip packages
from cefpython3 import cefpython as cef
from appdirs import user_data_dir


# general
__title__ = "Slipstream"
__title_pkg__ = "pslipstream"
__description__ = "The most informative Home-media backup solution."
__url__ = "https://github.com/rlaPHOENiX/Slipstream"
__version__ = "0.1.0"
__author__ = "PHOENiX"
__author_email__ = "rlaphoenix@pm.me"
__min_size__ = "1200x440"  # todo ; move this to config file
__package_obj__ = None
try:
  __package_obj__ = pkg_resources.Requirement.parse(f"{__title_pkg__}=={__version__}")
except pkg_resources.DistributionNotFound:
  pass

# environment
__cef_version__ = cef.GetVersion()
__py_version__ = platform.python_version()
__architecture__ = platform.architecture()[0]
__platform__ = platform.system()
__windows__ = __platform__ == "Windows"
__linux__ = __platform__ == "Linux"
__darwin__ = __platform__ == "Darwin"

# licensing and copyright
__license__ = "GPLv3"
__copyright__ = f"Copyright (C) {datetime.datetime.now().year} {__author__}"
__copyright_paragraph__ = "\n".join([
  f"{__title__}  {__copyright__}",
  "This program comes with ABSOLUTELY NO WARRANTY.",
  "This is free software, and you are welcome to redistribute it",
  f"under certain conditions; type '{__title_pkg__} --license' for details."
])

# directories
__root_dir__ = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
__user_dir__ = user_data_dir(__title_pkg__, __author__)
__static_dir__ = os.path.join(__root_dir__, "static")
if __package_obj__:
  try:
    __static_dir__ = pkg_resources.resource_filename(__package_obj__, f"{__title_pkg__}/static")
  except pkg_resources.DistributionNotFound:
    pass
  except pkg_resources.VersionConflict:
    pass

# file paths
__config_file__ = os.path.join(__user_dir__, "config.yml")
__icon_file__ = os.path.join(__static_dir__, "icon.png")
__ui_index__ = None  # prefix with `file://` for local file