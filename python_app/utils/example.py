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
import ConfigParser
import pkg_resources
import appdirs

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
            ConfigError: Error with logger level in config file

        """

        # setup logger, config, and utility directory
        self._configure()

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

    def _configure(self):

        # configure directories and files
        self._config_directory = appdirs.user_config_dir('example_python_app')
        self._log_directory = appdirs.user_log_dir('example_python_app')
        self._config_file = os.path.join(self._config_directory, 'python_app.conf')
        if not os.path.isfile(self._config_file):
            self._create_user_config()
        self._log_file = os.path.join(self._log_directory, 'python_app.log')
        if not os.path.isdir(self._log_directory):
            os.makedirs(self._log_directory)

        # configure logger
        #logging.config.fileConfig(self._config_file, disable_existing_loggers=False)
        self._logger = logging.getLogger("python_app")
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s <%(levelname)s> [%(filename)s: %(lineno)d]: %(message)s')
        console.setFormatter(formatter)
        self._logger.addHandler(console)
        file_handle = logging.FileHandler(self._log_file)
        file_handle.setLevel(logging.DEBUG)
        file_handle.setFormatter(formatter)
        self._logger.addHandler(file_handle)

        # get log level from config file
        self._config = ConfigParser.RawConfigParser()
        self._config.read(self._config_file)

        if self._config.get('logger', 'level') == 'DEBUG':
            self._logger.setLevel(logging.DEBUG)
        elif self._config.get('logger', 'level') == 'INFO':
            self._logger.setLevel(logging.INFO)
        elif self._config.get('logger', 'level') == 'WARNING':
            self._logger.setLevel(logging.WARNING)
        elif self._config.get('logger', 'level') == 'ERROR':
            self._logger.setLevel(logging.ERROR)
        elif self._config.get('logger', 'level') == 'CRITICAL':
            self._logger.setLevel(logging.CRITICAL)
        else:
            raise exceptions.ConfigError("Invalid logger level in config file")

    def _create_user_config(self):

        source = pkg_resources.resource_stream(__name__, '../../config/python_app.conf')
        if not os.path.isdir(self._config_directory):
            os.makedirs(self._config_directory)
        with open(self._config_file, 'w') as destination:
            destination.writelines(source)
