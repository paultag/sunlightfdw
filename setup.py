#!/usr/bin/env python

from setuptools import setup
from sunlightfdw import __version__

long_description = "Sunlight FDW"

setup(
    name="sunlightfdw",
    version=__version__,
    packages=['sunlightfdw',],
    author="Paul Tagliamonte",
    author_email="paultag@debian.org",
    long_description=long_description,
    description='does some stuff with things & stuff',
    license="Expat",
    url="",
    platforms=['any']
)
