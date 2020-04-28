from setuptools import setup, find_packages
from teleapi import __version__

setup(
    name='teleapi',
    version=__version__,
    author='DesSolo',
    author_email='dessolo@mail.ru',
    long_description='Simple telegram api',
    packages=find_packages(),
    install_requires=['requests', 'pysocks'],
)
