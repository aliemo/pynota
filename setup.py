from setuptools import setup

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='pynota',  
    version='0.1',
    author="Ali Mohammadpour",
    author_email="aliemohammadpour@gmail.com",
    description="A Python Library for Notations, Characters and Symbols",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alimpk/pynota",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
 