"""Virtual Square-1 logic"""

from copy import deepcopy


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

    def __str__(self):
        top_layer_statement = f"Top Layer:\n{str(self.top_layer)}"
        middle_layer_statement = f"\nMiddle Layer Flipped? {self.middle_layer_flipped}"
        bottom_layer_statement = f"\nBottom Layer:\n{str(self.bottom_layer)}"

        return top_layer_statement + middle_layer_statement + bottom_layer_statement

    def slice(self):
        """Executes a slice move, if possible"""

        def remove_slice_pieces(pieces_list=list):
            value = 0
            total_pieces_values = 0

            for i, piece in enumerate(pieces_list):
                if total_pieces_values < 6:
                    total_pieces_values += piece[value]
                elif total_pieces_values == 6:
                    sliced_pieces = pieces_list[i:]
                    remaining_pieces = pieces_list[:i]

                    return remaining_pieces, sliced_pieces
                else:
                    return "Illegal slice", "Illegal slice"

        def add_slice_pieces(orig_list=list, pieces_to_add=list):
            pieces_to_add.reverse()
            orig_list += pieces_to_add
            return orig_list

        top_copy = deepcopy(self.top_layer)
        bottom_copy = deepcopy(self.bottom_layer)

        remaining_top_pieces, removed_top_pieces = remove_slice_pieces(top_copy)
        remaining_bottom_pieces, removed_bottom_pieces = remove_slice_pieces(
            bottom_copy
        )
        if (
            removed_top_pieces != "Illegal slice"
            and removed_bottom_pieces != "Illegal slice"
        ):
            sliced_top = add_slice_pieces(remaining_top_pieces, removed_bottom_pieces)
            sliced_bottom = add_slice_pieces(
                remaining_bottom_pieces, removed_top_pieces
            )

            self.middle_layer_flipped = not self.middle_layer_flipped

            self.top_layer = sliced_top
            self.bottom_layer = sliced_bottom

    def move(self, instructions=str):
        """Reads the inputted instructions and moves accordingly."""

        # do tick clock and tick prime in here

        def turn_top(top_layer=list, turn_amount=int):
            total_value = 0
            tick_clock_amount = 0

            if turn_amount > 0:
                for piece in top_layer:
                    if total_value < turn_amount:
                        total_value += piece[0]
                        tick_clock_amount += 1
                    if total_value == turn_amount:
                        pass

                        # tickclock by tick_clock_amount
                    else:
                        raise SyntaxError("Error in instructions")
            elif turn_amount < 0:
                pass  # same but other way

        def turn_bottom(bottom_layer=list, turn_amount=int):
            pass

            # raise SyntaxError("Error in instructions") # if imposible

        for i in range(len(instructions)):
            # ik range len is cringe but it makes it more readable here imo
            if instructions[i].isdigit():
                if instructions[i + 1] == ",":
                    if instructions[i + 2].isdigit():
                        turn_top(self.top_layer, instructions[i])
                        turn_bottom(self.bottom_layer, instructions[i + 2])
            elif instructions[i] == "/":
                self.slice()

    def check_for_parity(self):
        """Checks parity count, returns if is odd or even."""
