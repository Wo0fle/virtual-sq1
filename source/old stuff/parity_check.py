""" Count the amount of swaps it has to make to get to the initial solved state for each layer """

from layer import Layer

solved_pieces = [
    (2, "FL"),
    (1, "L"),
    (2, "BL"),
    (1, "B"),
    (2, "BR"),
    (1, "R"),
    (2, "FR"),
    (1, "F"),
]


def swap_count(top_layer=Layer, bottom_layer=Layer):
    """Returns the amount of swaps that have been done from a solved state to the inputted state."""
    # idk how i will make a distinguish from top and bottom but ehhh
    return 0


def has_parity_problem(top_layer=Layer, bottom_layer=Layer):
    """Returns True or False depending on if there is a parity problem."""
    if swap_count(top_layer, bottom_layer) % 2 == 0:
        return False  # No parity :)

    return True  # Parity :(
