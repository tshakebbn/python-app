"""Unit test fixture for example utility

@file test_example.py

A more elaborate description of unit test fixture.

@author [organization]
@author [name] (optional)

@par [unique category]
[designation]

@par Notifications
[distribution designation]
[other designations]

@copyright Copyright [year] [organization]

"""

import unittest
import sys

import python_app.utils.example as example

class TestExample(unittest.TestCase):
    """Unittest TestCase for Example class

	"""

    def test_methods(self):
        """Method to test example class methods

        """
        with example.Example(param1=1, param2=2) as test_example:
            self.assertEquals(test_example.attr1, 1)
            self.assertEquals(test_example.attr2, 2)
            self.assertEquals(example.Example.example_static_method(
                param1=1, param2=2), False)
            self.assertEquals(example.Example.example_static_method(
                param1=2, param2=1), True)
            self.assertEquals(example.Example.example_static_method(
                param1=2, param2=2), False)
            self.assertEquals(test_example.example_method(), 1)
            test_example.attr4 = 4
            self.assertEquals(test_example.attr4, 4)

def main():
    """Main function if ran standalone

    """

    test_classes = [TestExample]
    suites_list = []
    for test_class in test_classes:
        suites_list.append(unittest.TestLoader().loadTestsFromTestCase(test_class))

    return_value = not unittest.TextTestRunner(verbosity=2).run(
        unittest.TestSuite(suites_list)).wasSuccessful()
    sys.exit(return_value)

if __name__ == '__main__':
    main()
