# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='TestProject',
    version='0.0.1',
    description="desc",
    url='https://brynjar-test.visualstudio.com/_git/TestProject',
    license='MIT',
    author='Brynjar Smári Bjarnason',
    author_email='binni@binnisb.com',
    packages=['Calc'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'cli_add=Calc:__cli_add',
            'stock_fetch=Calc:__stock_fetch'
        ],
    }
)
