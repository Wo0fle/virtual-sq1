"""
    Since what i *really* want is a "solver",
    I instead am opting to basically create a list of all possible states for the Squan
    Then gonna get to the correct one.

    Idk how to do this but I will figure it out
"""

import itertools

test_squan = [
    (2, "FL", "top"),
    (1, "L", "top"),
    (2, "BL", "top"),
    (1, "B", "top"),
    (2, "BR", "top"),
    (1, "R", "top"),
    (2, "FR", "top"),
    (1, "F", "top"),
    (1, "F", "bottom"),
    (2, "FR", "bottom"),
    (1, "R", "bottom"),
    (2, "BR", "bottom"),
    (1, "B", "bottom"),
    (2, "BL", "bottom"),
    (1, "L", "bottom"),
    (2, "FL", "bottom"),
]

# print(list(itertools.permutations(list of whatever)))
