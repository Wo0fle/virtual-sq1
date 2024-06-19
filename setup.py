from setuptools import setup
from virtual_sq1 import __version__

setup(
    name='virtual_sq1',
    description='Python module that simulates a Square-1 twisty puzzle',
    url='https://github.com/Wo0fle/virtual-sq1',
    author='Seby Amador',

    version=__version__,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Programming Language :: Python',
    ],

    py_modules=['virtual_sq1'],

    extras_require={'dev': ['pytest', 'coverage']}
)
