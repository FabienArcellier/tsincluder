#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='tsincluder',
    version='0.1',
    packages=['tsincluder',],
    install_requires=[
        'future',
    ],
    license='Mozilla Public License, v. 2.0',
    long_description=open('README.md').read(),
)
