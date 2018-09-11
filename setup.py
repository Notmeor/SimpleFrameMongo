#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='framemongo',
    version='0.1.0',
    packages=find_packages(include=["framemongo"]),
    author='notmeor',
    author_email='kevin.inova@gmail.com',
    description='', install_requires=['pandas>=0.20.0', 'pymongo']
)
