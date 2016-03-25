#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

version = '0.2.0'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()


def read(filename):
    with open(filename) as f:
        return f.read()

readme = read('README.rst')
history = read('HISTORY.rst').replace('.. :changelog:', '')
requirements = [
    'django>=1.8',
    'wheel==0.24.0',
]
test_requirements = [
    'nose',
    'django_nose',
]

setup(
    name='django-dedal',
    version=version,
    description="""Fast CRUD builder.""",
    long_description=readme + '\n\n' + history,
    author='Arkadiusz Adamski',
    author_email='arkadiusz.adamski@gmail.com',
    url='https://github.com/ar4s/django-dedal',
    packages=[
        'dedal',
    ],
    include_package_data=True,
    install_requires=requirements,
    tests_require=requirements + test_requirements,
    license="BSD",
    zip_safe=False,
    keywords='django-dedal',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)