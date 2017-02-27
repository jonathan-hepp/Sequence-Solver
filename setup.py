#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='sequence_solver',
    version='0.1.0',
    description="Sequence Solver uses several strategies to try to guess the next element of a given sequence.",
    long_description=readme + '\n\n' + history,
    author="Jonathan Hepp",
    author_email='jonathan.hepp@gmail.com',
    url='https://github.com/jonathan-hepp/Sequence-Solver',
    packages=[
        'sequence_solver',
    ],
    package_dir={'sequence_solver':
                 'sequence_solver'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='sequence_solver',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
