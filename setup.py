# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '0.7.0'
REPOSITORY = 'https://github.com/JuxhinDB/gw2-api-interface'

with open('README.rst', 'r') as f:
    README = f.read()


setup(
    name='GuildWars2-API-Client',
    version=__version__,
    description='Library that interfaces with the Guild Wars 2 API that supports v1 and v2',
    long_description=README,
    author='JDB',
    author_email='JuxhinBox@gmail.com',
    url=REPOSITORY,
    packages=find_packages(exclude=['test', 'res']),
    install_requires=[
        'requests',
    ],
    extras_require={
        'dev': [
            'ruff'
        ]
    },
    license='MIT',
    keywords=['guildwars 2', 'api', 'gw2']
)
