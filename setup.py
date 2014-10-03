#!/usr/bin/env python
# coding: utf-8


from setuptools import setup, find_packages


VERSION = "0.1.3"


with open("README.rst") as readme:
    long_description = readme.read()

setup(
    name="mycsv",
    version=VERSION,
    description='Script to export query results into local CSV files',
    long_description=long_description,
    author='Osvaldo Santana Neto',
    url='https://github.com/osantana/mycsv',
    download_url='https://github.com/osantana/mycsv/tarball/{}'.format(VERSION),
    license="BSD",
    packages=find_packages(),
    install_requires=[
        "MySQL-python",
        "Click",
    ],
    entry_points='''
        [console_scripts]
        mycsv=mycsv.cli:main
    ''',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Database',
        'Topic :: Utilities',
    ],
)
