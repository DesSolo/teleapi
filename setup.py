from setuptools import setup, find_packages


def read(file_name):
    with open(file_name, 'r') as file:
        return file.read()


setup(
    name='teleapi',
    version='0.1.3',
    author='DesSolo',
    author_email='dessolo@mail.ru',
    url='https://github.com/DesSolo/teleapi',
    description='Simple telegram api',
    license='GPLv3+',
    long_description=read('README.md'),
    keywords='telegram bot api',
    packages=find_packages(),
    install_requires=['requests', 'pysocks']
)
