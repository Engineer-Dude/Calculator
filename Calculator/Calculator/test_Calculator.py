import pytest
from Calculator import Calculator

def test_add_0_0() :
    calculator = Calculator()
    answer = calculator.add(0,0)
    assert answer == 0

def test_add_0_1() :
    calculator = Calculator()
    answer = calculator.add(0,1)
    assert answer == 1