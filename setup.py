from setuptools import setup
from virtual_sq1 import __version__
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='virtual_sq1',
    description='Python module that simulates a Square-1 twisty puzzle',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Wo0fle/virtual-sq1',
    author='Seby Amador',
    readme="README.md",

    version=__version__,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],

    py_modules=['virtual_sq1'],

    extras_require={'dev': ['pytest', 'coverage']}
)
