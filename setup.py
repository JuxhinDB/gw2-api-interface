# -*- coding: utf-8 -*-

from setuptools import setup

__version__ = '0.5.5'
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
    packages=['gw2api'],
    package_dir={
        'gw2api': 'gw2api'
    },
    download_url='{}/tarball/{}'.format(REPOSITORY, __version__),
    install_requires=[
        'requests',
    ],
    license='MIT',
    keywords=['guildwars 2', 'api', 'gw2']
)