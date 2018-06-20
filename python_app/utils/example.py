"""An example utility

@file example.py

A more elaborate description of example utility.

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
import os
import pkg_resources

import python_app.utils.exceptions as exceptions

class Example(object):
    """An example class.

    Attributes:
        attr1 (int):  First attribute
        attr2 (int):  Second attribute
        attr3 (int):  Third attribute

    """

    def __init__(self, param1, param2):
        """A brief description of __init__ method.

        Args:
            param1 (int):  First input parameter
            param2 (int):  Second input parameter

        Raises:
            IOError: Error accessing the config file or log file
            OSError: Error creating utility directory

        """

        # setup logger, config, and utility directory
        if not os.path.exists(
                os.path.join(os.path.expanduser("~"), '.python_app')):
            os.makedirs(os.path.join(os.path.expanduser("~"), '.python_app'))
        self._config_file = pkg_resources.resource_filename(
            pkg_resources.Requirement.parse("ExamplePythonApp"), "config/python_app.conf")
        logging.config.fileConfig(self._config_file, disable_existing_loggers=False)
        self._logger = logging.getLogger("python")

        self.attr1 = param1
        self.attr2 = param2

        self.attr3 = None

        self._attr4 = None

    @staticmethod
    def example_static_method(param1, param2):
        """Example method description.

        Args:
            param1 (int): First input parameter
            param2 (int): Second input parameter

        Returns:
            True if param1 is greater than param2, False otherwise

        """

        return bool(param1 > param2)

    def example_method(self):
        """Example method description.

        Returns:
            self.attr1

        """

        self._logger.debug("A debug severity message")
        self._logger.info("An informational severity message")
        self._logger.warning("A warning severity message")
        self._logger.error("An error severity message")
        self._logger.critical("A critical severity message")

        try:
            raise exceptions.ExampleError("An example error occured")
        except exceptions.ExampleError:
            pass

        return self.attr1

    @property
    def attr4(self):
        """Getter method for _attr4 attribute

        Returns:
            self._attr4

        """

        return self._attr4

    @attr4.setter
    def attr4(self, value):
        """Setter method for _attr4 attribute

        Args:
            value (int): value to set _attr4

        """
        self._attr4 = value

    def _private(self):
        pass
