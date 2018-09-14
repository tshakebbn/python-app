"""Unit test fixture for example utility

A more elaborate description of unit test fixture. (optional)

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
    """Unittest TestCase for Example class"""

    def setUp(self):
        """Set up method run before all test methods"""

        self.test_example_class = example.Example(param1=1, param2=2)

    def tearDown(self):
        """Tear down method for all test methods"""

        del self.test_example_class

    def test_methods(self):
        """Method to test example class methods"""

        self.assertEquals(self.test_example_class.attr1, 1)
        self.assertEquals(self.test_example_class.attr2, 2)
        self.assertEquals(example.Example.example_static_method(
            param1=1, param2=2), False)
        self.assertEquals(example.Example.example_static_method(
            param1=2, param2=1), True)
        self.assertEquals(example.Example.example_static_method(
            param1=2, param2=2), False)
        self.assertEquals(self.test_example_class.example_method(), 1)
        self.test_example_class.attr4 = 4
        self.assertEquals(self.test_example_class.attr4, 4)

def main():
    """Main function if ran standalone"""

    test_classes = [TestExample]
    suites_list = []
    for test_class in test_classes:
        suites_list.append(unittest.TestLoader().loadTestsFromTestCase(test_class))

    return_value = not unittest.TextTestRunner(verbosity=2).run(
        unittest.TestSuite(suites_list)).wasSuccessful()
    sys.exit(return_value)

if __name__ == '__main__':
    main()
