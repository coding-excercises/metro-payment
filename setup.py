# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='metro-payment',
    version='0.0.1',
    description='metro payment engine',
    long_description=readme,
    author='Rajan Manickavasagam',
    author_email='rajan.manickavasagam@gmail.com',
    url='https://github.com/coding-excercises/metro-payment',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
