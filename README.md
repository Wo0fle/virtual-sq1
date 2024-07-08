# virtual-sq1

### `pip install virtual-sq1`

<br>

## Python module that simulates a [Square-1 twisty puzzle](https://ruwix.com/twisty-puzzles/square-1-back-to-square-one/)

[![Build](https://github.com/Wo0fle/virtual-sq1/actions/workflows/main.yml/badge.svg)](https://github.com/Wo0fle/virtual-sq1/actions/workflows/main.yml)
[![Coverage Status](https://coveralls.io/repos/github/Wo0fle/virtual-sq1/badge.svg?branch=main)](https://coveralls.io/github/Wo0fle/virtual-sq1?branch=main)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/virtual_sq1)](https://pypi.org/project/virtual_sq1/)

## Usage

### Import and create `Square1` object

*Solved by default.*

```python
from virtual_sq1 import Square1


my_square_1 = Square1()
```

### View `Square1`'s current state

*`virtual_sq1` uses (almost) the same position notation as [Jaap's Square-1 optimiser](https://www.jaapsch.net/puzzles/square1.htm#progs).*

*Don't know how to read it? [Click here 🔗](./docs/jared19.md)*

```python
my_square_1 = Square1()

print(my_square_1)
# A1B2C3D4-5E6F7G8H
```

### Apply an algorithm to `Square1`

```python
my_square_1 = Square1()

my_square_1.apply_alg("/ (3,0) / (-3,-3) / (0,3) /")

print(my_square_1)
# A1C3B2D4-5E7G6F8H
```

### Apply a case to `Square1`

*Changes the Square1's state so that the input algorithm brings it to its current state.*

```python
my_square_1 = Square1()

my_square_1.apply_alg("/ (3,0) / (1,0) / (0,-3) / (-1,0) / (-3,0) / (1,0) / (0,3) / (-1,0)", True)

print(my_square_1)
# A2B3C1D4-5E6F7G8H
```

*The distinction between a "case" and an "algorithm" was made by [Tyson Decker's puzzle-gen](https://tdecker91.github.io/puzzlegen-demo/)*

### Apply a specific state to `Square1`

```python
my_square_1 = Square1()

my_square_1.apply_state("ABCDEF GH12345678 /")

print(my_square_1)
# ABCDEF/GH12345678
```

### Apply a individual moves to `Square1`

*Not sure why you'd do this when you could just use `apply_alg` but... it's an option.*

```python
my_square_1 = Square1()

my_square_1.slash()  # a slice/slash move
my_square_1.top.turn(-3)  # turn the top layer -3
my_square_1.bottom.turn(3)  # turn the bottom layer 3
my_square_1.slash()  # a slice/slash move
my_square_1.top.turn(3)  # turn the top layer 3
my_square_1.bottom.turn(-3)  # turn the bottom layer -3
my_square_1.slash()  # a slice/slash move

print(my_square_1)
# C3B2A1D4/5E8H7G6F
```

## Credits

This module was highly inspired by the following:
- Tyson Decker's puzzle-gen: https://tdecker91.github.io/puzzlegen-demo/
- Jaap's Square-1 optimiser: https://www.jaapsch.net/puzzles/square1.htm#progs
