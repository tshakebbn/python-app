"""Python installation and setup script

@file setup.py

A more elaborate description of setup script.

@author [organization]
@author [name] (optional)

@par [unique category]
[designation]

@par Notifications
[distribution designation]
[other designations]

@copyright Copyright [year] [organization]

"""

import os
import setuptools

def read(fname):
    """Utility function to read the README file

    Args:
        fname (str): name of file to read

    """

    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name="example_python_app",
    version="1.0.0.0",
    author="[organization]",
    description=("An example python application template"),
    license="MIT",
    packages=['python_app', 'python_app.utils', 'tests'],
    long_description=read('README.md'),
    test_suite="tests",
    include_package_data=True,
    scripts=['python_app/example_python_app'],
)
