"""An example exception

@file exceptions.py

A more elaborate description of exceptions.

@author [organization]
@author [name] (optional)

@par [unique category]
[designation]

@par Notifications
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
        super(ExampleError, self).__init__(msg)
        self.msg = msg
