from calculator import square

def main(): 
    test_square()

# we need to test a function that returns a value
# proper way to write this is test_function name 
def test_square():
    # we use the try and except operators to catch the AssertionError
    # we assert that the function square(2) returns 4
    # if not print the error message
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try: 
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
if __name__ == "__main__":
    main()

# assert definition : assert is a statement that helps you test if your code is working as expected. If the condition is True, the program continues to run. If the condition is False, the program stops and raises an AssertionError.