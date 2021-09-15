from setuptools import setup
import io
import os

here = os.path.abspath(os.path.dirname(__file__))

short_description = 'A star algorithm for finding shortest path from one to one in a graph'

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = short_description

setup(
    name='aStar',
    version='0.0.1',
    description=short_description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    authors=['A. Hoyby', 'M. Arhaug'],
    authors_email=['alex.hoeyby@gmail.com', 'mariusarhaug@hotmail.com'],
    url=['https://github.com/hoyby', 'https://github.com/MariusArhaug'],
    license='MIT',
    py_modules=['a_star', 'main', 'map'],
    install_requires=['PriorityQueue, Pillow, pandas']
)