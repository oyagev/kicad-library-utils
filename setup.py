#!/usr/bin/env python

from distutils.core import setup

setup(name='KicadLibUtils',
      version='1.0',
      description='Python library to read and edit Kicad files',
      url='https://github.com/oyagev/kicad-library-utils',
      packages=['sch', 'pcb', 'schlib']
      )
