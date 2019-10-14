#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-sftp",
    version="0.0.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_sftp"],
    install_requires=[
        "singer-python==5.5.1",
    ],
    extras_require={
        'dev': [
            'ipdb==0.11',
            'pylint==2.1.1',
        ]
    },
    entry_points="""
    [console_scripts]
    tap-sftp=tap_sftp:main
    """,
    packages=["tap_sftp"],
    package_data = {
        "schemas": ["tap_sftp/schemas/*.json"]
    },
    include_package_data=True,
)
