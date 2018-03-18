# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='Pytest example',
    version='0.0.1',
    description="desc",
    url='https://brynjar-test.visualstudio.com/_git/Pytest%20example',
    license='MIT',
    author='Brynjar Smári Bjarnason',
    author_email='binni@binnisb.com',
    packages=['Demo'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'cli_add=Demo:__cli_add'
        ],
    }
)
