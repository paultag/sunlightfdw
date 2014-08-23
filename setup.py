#!/usr/bin/env python

from setuptools import setup
from sunlightfdi import __version__

long_description = "Sunlight FDI Wrapper"

setup(
    name="sunlightfdi",
    version=__version__,
    packages=['sunlightfdi',],
    author="Paul Tagliamonte",
    author_email="paultag@debian.org",
    long_description=long_description,
    description='does some stuff with things & stuff',
    license="Expat",
    url="",
    platforms=['any']
)
