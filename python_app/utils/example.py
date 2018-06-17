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

        """
        self.attr1 = param1
        self.attr2 = param2

        self.attr3 = None

        self._attr4 = None

    @staticmethod
    def example_static_method(param1, param2):
        """Example method description.

        @param param1 The first parameter.
        @param param2 The second parameter.
        @return True if successful, False otherwise.

        """
        return bool(param1 > param2)

    def example_methond(self):
        """Example method description.

        @return attr1

        """
        LOGGER.debug("A debug severity message")
        LOGGER.info("An informational severity message")
        LOGGER.warning("A warning severity message")
        LOGGER.error("An error severity message")
        LOGGER.critical("A critical severity message")

        return self.attr1

    @property
    def attr4(self):
        """Getter method for _attr4 attribute
        @return _attr4 attribute

        """

        return self._attr4

    @attr4.setter
    def attr4(self, value):
        """Setter method for _attr4 attribute
        @param value value for attr4 attribute

        """
        self._attr4 = value

    def _private(self):
        """By default private members are not included."""
        pass
