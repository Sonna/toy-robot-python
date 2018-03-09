# -*- coding: utf-8 -*-

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
https://docs.python.org/2/distutils/setupscript.html
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='toy_robot_python',
    version='0.1.0',
    description='A Pyton version of the Toy Robot test',
    long_description=long_description,
    author='Alex Sonneveld',
    author_email='alex.sonneveld@live.com.au',
    url='https://github.com/sonna/toy-robot-python',
    packages=find_packages(exclude=('docs', 'tests')),
    entry_points={
        'console_scripts': [
            'toy_robot=toy_robot:main',
        ],
    },
)
