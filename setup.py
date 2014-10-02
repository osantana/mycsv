#!/usr/bin/env python
# coding: utf-8


from setuptools import setup, find_packages


setup(
    name="mycsv",
    version="0.1",
    description='Script to export query results into local CSV files',
    author='Osvaldo Santana Neto',
    url='https://github.com/osantana/mycsv',
    packages=find_packages(),
    install_requires=[
        "MySQL-python",
        "Click",
    ],
    entry_points='''
        [console_scripts]
        mycsv=mycsv.cli:main
    ''',
)
