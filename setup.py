"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the test_bundle project.
"""
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

import open_commerce_data_pipelines.version

setup(
    name="open_commerce_data_pipelines",
    version=open_commerce_data_pipelines.version.version,
    url="https://stuzo.com",
    author="jordan.yaker@stuzo.com",
    description="wheel file based on test-bundle/src",
    packages=find_packages(where='./src'),
    package_dir={'': 'src'},
    install_requires=[
        # Dependencies in case the output wheel file is used as a library dependency.
        # For defining dependencies, when this package is used in Databricks, see:
        # https://docs.databricks.com/dev-tools/bundles/library-dependencies.html
        "setuptools"
    ],
)
