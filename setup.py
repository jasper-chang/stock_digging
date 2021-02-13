#!/usr/bin/python
# coding:utf-8
"""The installation of packages."""

import setuptools

NAMESPACE = 'stockmining'
PKG_NAME = 'datautils'

setuptools.setup(
    name=f'{NAMESPACE}',
    version='1.0',
    description='The stock process library tool setup',
    packages=setuptools.find_namespace_packages(include=[f'{NAMESPACE}.*']))
