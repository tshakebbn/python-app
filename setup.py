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

# Utility function to read the README file
def read(fname):
    """Utility function to read the README file

    Args:
        fname (str): name of file to read

    """

    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name="Example python app",
    version="0.0.0.1",
    author="[organization]",
    description=("An example python application template"),
    license="MIT",
    packages=['python_app', 'python_app.utils', 'tests'],
    long_description=read('README'),
)
