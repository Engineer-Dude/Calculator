import pytest
from Calculator import Calculator

# addition

def test_add_0_0() :
    calculator = Calculator()
    answer = calculator.add(0,0)
    assert answer == 0

def test_add_0_1() :
    calculator = Calculator()
    answer = calculator.add(0,1)
    assert answer == 1

def test_add_0_None() :
    calculator = Calculator()

    answer = None
    try :
        answer = calculator.add(0,None)
    except TypeError :
        assert True
    assert answer == None

def test_add_None_0() :
    calculator = Calculator()

    answer = None
    try :
        answer = calculator.add(None, 0)
    except TypeError :
        assert True
    assert answer == None

def test_add_a_0() :
    calculator = Calculator()

    answer = None
    try :
        answer = calculator.add('a', 0)
    except TypeError :
        assert True
    assert answer == None
    
# subtraction
def test_subtract_0_0() :
    calculator = Calculator()
    answer = calculator.subtract(0,0)
    assert answer == 0

def test_subtract_0_1() :
    calculator = Calculator()
    answer = calculator.subtract(0,1)
    assert answer == -1

def test_subtract_0_None() :
    calculator = Calculator()

    answer = None
    try :
        answer = calculator.subtract(0,None)
    except TypeError :
        assert True
    assert answer == None

def test_subtract_None_0() :
    calculator = Calculator()

    answer = None
    try :
        answer = calculator.subtract(None, 0)
    except TypeError :
        assert True
    assert answer == None

def test_subtract_a_0() :
    calculator = Calculator()

    answer = None
    try :
        answer = calculator.subtract('a', 0)
    except TypeError :
        assert True
    assert answer == None