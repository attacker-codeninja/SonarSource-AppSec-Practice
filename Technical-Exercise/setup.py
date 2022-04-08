#!/usr/bin/env python
import sys
from setuptools import setup, find_packages

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)

install_requires = [
    'email_validator',
    'Flask',
    'Flask-Login',
    'Flask-SQLAlchemy',
    'pyOpenSSL',
    'Flask-WTF',
]

setup(name='appsec-exercise',
      version='1.0',
      install_requires=install_requires,
      packages=find_packages())
