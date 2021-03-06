#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    #Check Correct
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Paper", "Paper") == 0
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Paper", "Scissors") == 2
    #Check Incorrect
    assert decide_rps(1, 2) == 0
    assert decide_rps("Pi","Scu") == 2

   # other tests

