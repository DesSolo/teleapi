from setuptools import setup, find_packages

setup(
    name='teleapi',
    version='0.1.3',
    author='DesSolo',
    author_email='dessolo@mail.ru',
    url='https://github.com/DesSolo/teleapi',
    description='Simple telegram api',
    license='GPLv3+',
    keywords='telegram bot api',
    packages=find_packages(),
    install_requires=['requests', 'pysocks']
)
