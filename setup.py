#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='tsincluder',
    version='0.1',
    packages=['tsincluder',],
    install_requires=[
        'future',
    ],
    include_package_data=True,
    entry_points = {
        'console_scripts': [
            'tsincluder = tsincluder.__main__:run',
        ],
    },
    license='Mozilla Public License, v. 2.0',
    long_description=open('README.md').read(),
)
