# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='gener8',
    version='0.1',
    description='Generates a Dockerfile template based on user input',
    packages=[
        'gener8',
        'gener8.templates',
        'gener8.templates.docker'
    ],
    package_data={
        'gener8.templates': ['*.jinja2'],
        'gener8.templates.docker': ['*.jinja2']
    },
    scripts=['bin/gener8'],
    install_requires=[
        "certifi",
        "click",
        "click-log",
        "chardet",
        "Jinja2",
        "idna",
        "MarkupSafe",
        "pip",
        "requests",
        "setuptools",
        "urllib3",
        "wheel"
    ],
    extras_require={
        'test': [
            "mock",
            "pytest",
            "pytest-mock",
            "pytest-cov",
            "tzlocal"
        ]
    },
    zip_safe=False
)
