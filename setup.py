import sys
from setuptools import setup, find_packages

setup(name='motmot.utils',
      description='miscellaneous utilities for the motmot camera packages',
      version='20090612',
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      url='http://code.astraw.com/projects/motmot',
      license='BSD',
      packages=find_packages(),
      namespace_packages = ['motmot'],
      entry_points={'console_scripts':[
    'motmot_test=motmot.utils.utils:test_motmot',
    'motmot_check_new_namespace=motmot.utils.check_new_namespace:main',
    ]},
      )
