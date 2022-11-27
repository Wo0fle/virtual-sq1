"""Virtual Square-1 logic"""


class Squan:
    """A Virtual Square-1 object."""

    top_layer = [
        [2, "FL", "top"],
        [1, "L", "top"],
        [2, "BL", "top"],
        [1, "B", "top"],
        [2, "BR", "top"],
        [1, "R", "top"],
        [2, "FR", "top"],
        [1, "F", "top"],
    ]
    bottom_layer = [
        [2, "FL", "bottom"],
        [1, "L", "bottom"],
        [2, "BL", "bottom"],
        [1, "B", "bottom"],
        [2, "BR", "bottom"],
        [1, "R", "bottom"],
        [2, "FR", "bottom"],
        [1, "F", "bottom"],
    ]
    middle_layer_flipped = False

    def __init__(self):
        pass

    def __str__(self) -> str:
        top_layer_statement = f"Top Layer:\n{str(self.top_layer)}"
        middle_layer_statement = f"\nMiddle Layer Flipped? {self.middle_layer_flipped}"
        bottom_layer_statement = f"\nBottom Layer:\n{str(self.bottom_layer)}"

        return top_layer_statement + middle_layer_statement + bottom_layer_statement

    def slice(self):
        """Executes a slice move."""

    def move(self, instructions=str):
        """Reads the inputted instructions and moves accordingly"""
