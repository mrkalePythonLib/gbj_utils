#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup function for the package."""

from setuptools import setup, find_namespace_packages

setup(
  name='gbj_utils',
  version='1.0.1',
  description='Python package for module utils.',
  long_description='Module for general actions related to interaction with operating system.',
  classifiers=[
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    'Topic :: System :: Monitoring',
  ],
  keywords='utils',
  url='http://github.com/mrkalePythonLib/gbj_utils',
  author='Libor Gabaj',
  author_email='libor.gabaj@gmail.com',
  license='MIT',
  packages=find_namespace_packages(),
  install_requires=['psutil'],
  include_package_data=True,
  zip_safe=False
)
