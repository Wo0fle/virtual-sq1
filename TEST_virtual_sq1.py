from virtual_sq1 import Square1
import pytest


# im pretty sure i tested every typical case
# soooo basically if something fails then thats a skill issue :)

@pytest.fixture
def sq1():
    return Square1()


def test_apply_alg(sq1):
    sq1.apply_alg("13/0,9/ -1,0)/ ignore this text (3,0)/ 1/ 0,3/-1,0 / (-3,/")
    assert sq1.__str__() == "A2B3C1D4-5E6F7G8H"


def test_apply_case(sq1):
    sq1.apply_alg("/ (-9,0) / (1,0) / (0,9) / (-1,0) / (-3,0) / (1,0) / (0,3) / (-1,0)", True)
    assert sq1.__str__() == "A2B3C1D4-5E6F7G8H"


def test_apply_state_with_slash(sq1):
    sq1.apply_state("ABCDEF GH12345678 /")
    assert sq1.__str__() == "ABCDEF/GH12345678"


def test_apply_state_with_dash(sq1):
    sq1.apply_state("ABCDEF GH12345678 -")
    assert sq1.__str__() == "ABCDEF-GH12345678"


def test_apply_illegal_alg_too_many_dashes_top(sq1):
    sq1.apply_alg("--3/")
    assert sq1.error_message == 'Error at "--3" (move #1).\nSquare-1 reset to previous state.\n'


def test_apply_illegal_alg_too_many_dashes_bottom(sq1):
    sq1.apply_alg("0,-3/0,--3")
    assert sq1.error_message == 'Error at "0,--3" (move #2).\nSquare-1 reset to previous state.\n'


def test_apply_illegal_alg_too_many_commas(sq1):
    sq1.apply_alg("3,4,5,6")
    assert sq1.error_message == 'Error at "3,4,5,6" (move #1).\nSquare-1 reset to previous state.\n'


def test_apply_illegal_alg_impossible_top_turn(sq1):
    sq1.apply_alg("2 oh hello there! you should IGNORE THIS TEXT BRUH")
    assert sq1.error_message == 'Error at "2" (move #1).\nSquare-1 reset to previous state.\n'


def test_apply_illegal_alg_impossible_bottom_turn(sq1):
    sq1.apply_alg("0,2/3/0,2")
    assert sq1.error_message == 'Error at "0,2" (move #3).\nSquare-1 reset to previous state.\n'


def test_apply_illegal_case(sq1):
    sq1.apply_alg("/ (3,0) / (1,0) / (0,-3) / (-1,0) / (-3,0) / (1,0) / (0,3) /", True)
    # in case you don't see why this is an issue, it's missing the top layer realignment at the end to make the sq1 back into a square, which makes the alg inversion fail
    assert sq1.error_message == 'Error at "1,0" (move #7).\nCheck that your input starts and ends in fully-aligned cubeshape.\nSquare-1 reset to previous state.\n'


def test_apply_illegal_state_extra_pieces(sq1):
    sq1.apply_state("ABCDEFGHI123456789")
    assert sq1.error_message == 'Error with "ABCDEFGHI123456789".\nCheck your input isn\'t missing any or contains any extra symbols.\nSquare-1 reset to previous state.\n'


def test_apply_illegal_state_missing_pieces(sq1):
    sq1.apply_state("ABCDEF1234567")
    assert sq1.error_message == 'Error with "ABCDEF1234567".\nCheck your input isn\'t missing any or contains any extra symbols.\nSquare-1 reset to previous state.\n'


def test_apply_illegal_state_impossible_state(sq1):
    sq1.apply_state("1ABCDEFG2345678")
    assert sq1.error_message == 'Error with "1ABCDEFG2345678".\nCheck your input isn\'t missing any or contains any extra symbols.\nSquare-1 reset to previous state.\n'
    # no need to include a "check that your input is actually possible" message IMO because... that's kind of implied

def test_apply_algs_from_different_initial_states(sq1):
    sq1.apply_state("CG216F5B/EHD4A837")
    sq1.apply_alg("(3,-1)/ (-2,1)/ (2,-4)/ (-2,-5)/ (0,-3)/ (3,-1)/ (0,-3)/ (3,0)/ (4,-4)/ (6,-2)", True)
    assert sq1.__str__() == "A1B2C3D4-5E6F7G8H"

def test_error_message_reset_from_bad_alg(sq1):
    sq1.apply_alg("2/")
    assert sq1.error_message == 'Error at "2" (move #1).\nSquare-1 reset to previous state.\n'
    sq1.apply_alg("//")
    assert sq1.error_message == ''

def test_error_message_reset_from_bad_case(sq1):
    sq1.apply_alg("-2/", True)
    assert sq1.error_message == 'Error at "-2" (move #1).\nCheck that your input starts and ends in fully-aligned cubeshape.\nSquare-1 reset to previous state.\n'
    sq1.apply_alg("//")
    assert sq1.error_message == ''

def test_error_message_reset_from_bad_state(sq1):
    sq1.apply_state("1ABCDEFG2345678")
    assert sq1.error_message == 'Error with "1ABCDEFG2345678".\nCheck your input isn\'t missing any or contains any extra symbols.\nSquare-1 reset to previous state.\n'
    sq1.apply_alg("//")
    assert sq1.error_message == ''
