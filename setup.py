# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.rst', 'r') as f:
    longdesc = f.read().decode('utf-8')

setup(name='mac_alias',
      version='2.0.1',
      description='Generate/parse Mac OS Alias records from Python',
      long_description=longdesc,
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
