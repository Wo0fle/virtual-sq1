"""
A Python representation of the Square-1 twisty puzzle.

Classes:
    Square1: A virtual Square-1 object.
        flip_equator():
            Directly changes the equator state `equator_flipped` of the Square1 from flipped (True) to not flipped (False) (and vice-versa) without affecting other pieces.
        slash():
            Does a slice/slash move to the Square1. 
        apply_alg(alg, for_case):
            If `for_case = False` (default): Applies an input algorithm `alg` to the Square1, starting from a solved state.
            If `for_case = True`: Changes the Square1's state so that the input algorithm `alg` solves it.
        invert_alg(simplified_alg):
            Inverts the input simplified algorithm `simplified_alg` and returns it.
        apply_state(state):
            Changes the Square1's state to match the input state `state`.
        error_detected(input_type, errored_input, error_turns, error_turns_index):
            Prints an error message depending on the input type `input_type`.
            If `input_type = 0` or `input_type = 1`: `error_turns` and `error_turns_index` are the specifics of where the error occurred in `errored_input`.
        
    Layer: An arbitrary layer of the Square1.
        is_sliceable():
            Determines whether or not the Layer can slice/slash at the current position and returns True if possible (False otherwise).
        turn(amount):
            Rotates the Layer by an input amount `amount` and returns True if successful (False if Layer becomes unsliceable).

Author: Seby Amador
License: GNU GPLv3
"""

__version__ = '1.0.dev'

class Square1:
    """A virtual Square-1 object."""

    def __init__(self) -> None:
        """Initializes the Square1. Solved by default."""

        self.top = Layer("A1B2C3D4")
        self.equator_flipped = False
        self.bottom = Layer("5E6F7G8H")

    def __str__(self) -> str:
        """Converts the Square1's state to a string."""
        
        if self.equator_flipped:
            return f"{self.top}/{self.bottom}"
        else:
            return f"{self.top}-{self.bottom}"
    
    def flip_equator(self) -> None:
        """Directly changes the equator state `equator_flipped` of the Square1 from flipped (True) to not flipped (False) (and vice-versa) without affecting other pieces."""

        self.equator_flipped = not self.equator_flipped

    def slash(self) -> None: # lol "slice" is taken by Python already
        """Does a slice/slash move to the Square1."""

        value = 0

        for i in range(len(self.top.current_state)):
            if self.top.current_state[i] in "12345678":
                value += 1
            elif self.top.current_state[i] in "ABCDEFGH":
                value += 2

            if value == 6:
                left_side_U = self.top.current_state[:i+1]
                right_side_U = self.top.current_state[i+1:]
        
        value = 0

        for i in range(len(self.bottom.current_state)):
            if self.bottom.current_state[i] in "12345678":
                value += 1
            elif self.bottom.current_state[i] in "ABCDEFGH":
                value += 2

            if value == 6:
                right_side_D = self.bottom.current_state[:i+1]
                left_side_D = self.bottom.current_state[i+1:]
        
        self.top.current_state = left_side_U + right_side_D
        self.bottom.current_state =  right_side_U + left_side_D
        self.flip_equator()
    
    def apply_alg(self, alg:str, for_case:bool=False) -> None:
        """
        If `for_case = False` (default): Applies an input algorithm `alg` to the Square1.

        If `for_case = True`: Changes the Square1's state so that the input algorithm `alg` solves it (by inverting the input algorithm and then applying it).

        Resets the Square1 to its previous state if unsuccessful.

        Notes:
            The distinction between a "case" and an "algorithm" was made by Tyson Decker's puzzle-gen (https://tdecker91.github.io/puzzlegen-demo/), which highly inspired this module.
        """

        initial_state = self.__str__()
        simplfied_alg = list(alg)

        for char in alg:
            if not char.isnumeric() and ((char != '/') and (char != ',') and (char != '-')):
                simplfied_alg.remove(char)

        simplfied_alg = [slash.split(',') for slash in (''.join(simplfied_alg)).split('/')]

        if for_case:
            simplfied_alg = self.invert_alg(simplfied_alg)

        legal = True

        for i in range(len(simplfied_alg)):
            try:
                turn_amount = int(simplfied_alg[i][0])

                while abs(turn_amount) > 6:
                    if turn_amount > 0:
                        turn_amount -= 12
                    else:
                        turn_amount += 12

                if not self.top.turn(turn_amount):
                    self.apply_state(initial_state)
                    legal = False
                    break
            except:
                if simplfied_alg[i][0] != '':
                    print('\nSYNTAX ERROR involving "-" detected!')
                    self.apply_state(initial_state)
                    legal = False
                    break
            
            try:
                turn_amount = int(simplfied_alg[i][1])

                while abs(turn_amount) > 6:
                    if turn_amount > 0:
                        turn_amount -= 12
                    else:
                        turn_amount += 12

                if not self.bottom.turn(turn_amount):
                    self.apply_state(initial_state)
                    legal = False
                    break
            except ValueError:
                if simplfied_alg[i][1] != '':
                    print('\nSYNTAX ERROR involving "-" detected!')
                    self.apply_state(initial_state)
                    legal = False
                    break
            except:
                pass # assume 0 for bottom turn if there's only one input
            
            if len(simplfied_alg[i]) > 2:
                print('\nSYNTAX ERROR involving "," detected!')
                self.apply_state(initial_state)
                legal = False
                break

            self.slash()

        if legal:
            self.slash()
        else:
            if for_case:
                self.error_detected(0, simplfied_alg, simplfied_alg[i], i)
            else:
                self.error_detected(1, simplfied_alg, simplfied_alg[i], i)
    
    def invert_alg(self, simplified_alg:list) -> list:
        """
        Inverts the input simplified algorithm `simplified_alg`.
        
        Notes:
            An "inversion" in this context refers to manipulating an algorithm in such a way that applying the normal algorithm followed by the inverted algorithm (or vice-versa) would result in zero net effect on the Square-1.
        """
        
        simplified_alg = simplified_alg[::-1]

        for i in range(len(simplified_alg)):
            for j in range(len(simplified_alg[i])):
                if "-" in simplified_alg[i][j]:
                    simplified_alg[i][j] = simplified_alg[i][j].replace('-', '', 1)
                else:
                    if simplified_alg[i][j] != '0' and simplified_alg[i][j] != '':
                        simplified_alg[i][j] = "-" + simplified_alg[i][j]

        return simplified_alg

    def apply_state(self, state:str) -> None:
        """
        Changes the Square1's state to match the input state `state` (resets the Square1 to its previous state if unsuccessful).
        
        Notes:
            This module uses the same position notation as Jaap's Square-1 optimiser: https://www.jaapsch.net/puzzles/square1.htm#progs.
        """

        initial_state = self.__str__()
        req_pieces = "ABCDEFGH12345678"
        state = state.upper()
        state_list = list(state)
        
        for piece in req_pieces:
            if len(state_list) == 0:
                print('\nSYNTAX ERROR involving missing pieces detected!')
                self.apply_state(initial_state)
                self.error_detected(2, state)
                break
            
            if piece in state_list:
                state_list.remove(piece)
        
        if len(state_list) > 1:
            print('\nSYNTAX ERROR involving extra/nonexistent pieces detected!')
            self.apply_state(initial_state)
            self.error_detected(2, state)
        else:
            value = 0

            if len(state_list) == 1:
                state_list = list(state)

                if "/" in state:
                    self.flip_equator()
                    state_list = list(state)
                    state_list.remove("/")
                elif "-" in state:
                    state_list = list(state)
                    state_list.remove("-")
            else:
                state_list = list(state)
            
            for i in range(len(state)):
                if state[i] in "12345678":
                    value += 1
                elif state[i] in "ABCDEFGH":
                    value += 2

                if value == 12:
                    new_top = ''.join(state_list[:i+1])
                    new_bottom = ''.join(state_list[i+1:])

                    self.top = Layer(new_top)
                    self.bottom = Layer(new_bottom)

                    break
                elif value > 12:
                    print('\nSYNTAX ERROR involving impossible layer state detected!')
                    self.apply_state(initial_state)
                    self.error_detected(2, state)
                    break
        
    def error_detected(self, input_type:int, errored_input, error_turns:list=[], error_turns_index:int=0) -> None:
        """
        Prints an error message depending on the input type `input_type` (where 0 is "Case", 1 is "Algorithm", and 2 is "State").

        `errored_input` can be either an errored simplified algorithm (for Algorithm or Case) or an errored state (for State).
        
        For Case and Algorithm:
            `error_turns` is the set of top/bottom layer rotations where the error was detected.
            `error_turns_index` is the index of `error_turns` in the simplified algorithm `errored_input`.
        """

        if input_type == 0: # case
            self.invert_alg(errored_input)

            print(f'Error at "{','.join(error_turns)}" (move #{len(errored_input) - error_turns_index}).\nSquare-1 reset to previous state.\n')
        elif input_type == 1: # alg
            print(f'Error at "{','.join(error_turns)}" (move #{error_turns_index + 1}).\nSquare-1 reset to previous state.\n')
        elif input_type == 2: # state
            print(f'Error with "{errored_input}".\nSquare-1 reset to previous state.\n')

#########################################################

class Layer:
    """An arbitrary layer of the Square1."""

    def __init__(self, initial_state:str) -> None:
        """Initializes the Layer. Initial state `initial_state` is input."""

        self.current_state = initial_state
    
    def __str__(self) -> str:
        """Converts the Layer's state to a string."""

        return str(self.current_state)
    
    def is_sliceable(self):
        """Determines whether or not the Layer can slice/slash at the current position and returns True if possible (returns False otherwise)."""

        value = 0

        for piece in self.current_state:
            if piece in "12345678":
                value += 1
            elif piece in "ABCDEFGH":
                value += 2

            if value == 6:
                return True
            elif value > 6:
                return False            

    def turn(self, amount:int):
        """
        Rotates the Layer by an input amount `amount` and returns True (if successful).
        
        If the rotation leaves the Layer in an unsliceable position, it resets the Layer to its previous state and returns False.
        """

        if amount > 0:
            initial_state = self.current_state[::-1]

            for piece in initial_state:
                if piece in "12345678":
                    value = 1
                elif piece in "ABCDEFGH":
                    value = 2

                if amount >= value:
                    amount -= value
                    self.current_state = piece + self.current_state[:-1]
                else:
                    if amount != 0 or not self.is_sliceable():
                        print('\nLOGIC ERROR involving an incomplete turn detected!\n')
                        self.current_state = initial_state[::-1]
                        return False

                    return True
        elif amount < 0:
            amount *= -1
            initial_state = self.current_state

            for piece in initial_state:
                if piece in "12345678":
                    value = 1
                elif piece in "ABCDEFGH":
                    value = 2
                
                if amount >= value:
                    amount -= value
                    self.current_state = self.current_state[1:] + piece
                else:
                    if amount != 0 or not self.is_sliceable():
                        print('\nLOGIC ERROR involving an incomplete turn detected!\n')
                        self.current_state = initial_state
                        return False

                    return True
        else:
            return True
