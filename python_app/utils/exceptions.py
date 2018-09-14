"""@package exceptions
An example exception

A more elaborate description of exceptions. (optional)

@author [organization]
@author [name] (optional)

@par [unique category]
[designation]

@par Notifications:
[distribution designation]
[other designations]

@copyright Copyright [year] [organization]

"""

class Error(Exception):
    """Base class for exceptions"""
    pass

class ExampleError(Error):
    """An example exception.

    Args:
        msg (str):  Error message

    Attributes:
        msg (str):  Error message

    """

    def __init__(self, msg):
        """A brief description of __init__ method."""

        super(ExampleError, self).__init__(msg)
        self.msg = msg

class ConfigError(Error):
    """An config file or configuration exception.

    Args:
        msg (str):  Error message

    Attributes:
        msg (str):  Error message

    """

    def __init__(self, msg):
        """Constructor with error message argument."""

        super(ConfigError, self).__init__(msg)
        self.msg = msg
