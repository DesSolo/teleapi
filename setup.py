from os import path
from setuptools import setup, find_packages


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='teleapi',
    version='0.1.6',
    author='DesSolo',
    author_email='dessolo@mail.ru',
    url='https://github.com/DesSolo/teleapi',
    description='Simple telegram api',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='BSD',
    keywords='telegram bot api',
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=['requests', 'pysocks']
)
