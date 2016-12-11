#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs

from setuptools import setup
from pip.req import parse_requirements

here = os.path.abspath(os.path.dirname(__file__))

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements(os.path.join(here, 'requirements.txt'), session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

# Get the long description from the relevant file
try:
    f = codecs.open('README.rst', encoding='utf-8')
    long_description = f.read()
    f.close()
except:
    long_description = ''


setup(
    install_requires=reqs,
    name='speedtest-cli-datadog',
    version='0.1.1',
    description=('Command line interface for testing internet bandwidth using '
                 'speedtest.net, using datadog statsd.'),
    long_description=long_description,
    keywords='speedtest speedtest.net datadog',
    author='Jordi Riera',
    author_email='kender.jr@gmail.com',
    url='https://github.com/sivel/speedtest-cli',
    license='Apache License, Version 2.0',
    py_modules=['speedtest_cli_datadog'],
    entry_points={
        'console_scripts': [
            'speedtest=speedtest_cli_datadog:main',
            'speedtest-cli=speedtest_cli_datadog:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
