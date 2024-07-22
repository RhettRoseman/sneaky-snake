# we import pytest to use it in def test_str()
import pytest
# we import the funcion we want to test
from calculator import square

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(0) == 0
#     assert square(-3) == 9
   


# this is another way to write tests in pytest
# we split the above into 3 functions to test positive, negative, and zero numbers
# all 3 will be ran with pytest                                                                                         
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

# tests for strings instead of integers from the user input 
def test_str():
    with pytest.raises(TypeError):
        square('spirit')


# pytest will run all the tests in the current file that start with test_ 
# tests help us catch bugs and errors in our code