"""Includes useful logging functions.

@file log.py

A more elaborate description of logging.

@author [organization]
@author [name] (optional)

@par [unique category]
[designation]

@par Notifications
[distribution designation]
[other designations]

@copyright Copyright [year] [organization]

"""

import logging
import logging.config
import ConfigParser
import os
import sys
import traceback

try:
    CONFIG_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))), 'config/python.conf')
    logging.config.fileConfig(CONFIG_FILE, disable_existing_loggers=False)
    LOGGER = logging.getLogger("python")
    CONFIG = ConfigParser.RawConfigParser()
    CONFIG.read(CONFIG_FILE)
except IOError:
    traceback.print_exc()
    sys.exit("Aborting. Unable to find python config file")
else:
    pass
