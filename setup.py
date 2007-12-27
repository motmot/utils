import sys
from setuptools import setup, find_packages

setup(name='motmot.utils',
      description='miscellaneous utilities for the motmot camera packages',
      version='20071227.00',
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      url='http://code.astraw.com/projects/motmot',
      license='BSD',
      packages=find_packages(),
      namespace_packages = ['motmot'],
      )
