# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='mac_alias',
      version='1.1.0',
      description='Generate/parse Mac OS Alias records from Python',
      long_description=u"""
``mac_alias`` lets you generate or read binary Alias records from Python code.
While it is written in pure Python, some OS X specific code is required to
generate a proper Alias record for a given file, so this module currently
is not portable to other platforms.

Credit is due to Wim Lewis <wiml@hhhh.org>, whose work on reverse engineering
the alias format was extremely useful in writing this code.""",
      author='Alastair Houghton',
      author_email='alastair@alastairs-place.net',
      url='http://alastairs-place.net/projects/mac_alias',
      license='MIT License',
      platforms='darwin',
      packages=['mac_alias'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Topic :: Desktop Environment',
          'Topic :: Software Development :: Libraries :: Python Modules'],
      provides=['mac_alias'])

