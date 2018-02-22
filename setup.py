# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='gener8',
    version='0.1',
    description='  A little tool to generate commonly used ci/cd templates like Dockerfiles and kubernetes service definitions.',
    packages=[
        'gener8',
        'gener8.templates',
        'gener8.templates.docker',
        'gener8.scripts'
    ],
    package_data={
        'gener8.templates': ['*.jinja2'],
        'gener8.templates.docker': ['*.jinja2'],
        'gener8.scripts': ['*.sh']
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
