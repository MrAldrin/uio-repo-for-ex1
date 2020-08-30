import calculator
import pytest
from math import factorial, sin

@pytest.mark.parametrize('arg, answ', [[(1, 2), 3], [(1, -2), -1], [(-1, -1), -2]])
def test_add_integer_exercise_1(arg, answ):
    assert calculator.add(arg[0], arg[1]) == answ

@pytest.mark.parametrize('arg, answ', [[(.1, .2), .3], [(.1, -.1), 0], [(-.1, -.9), -1]])
def test_add_float_exercise_2(arg, answ):
    assert abs(calculator.add(arg[0], arg[1]) - answ) < 1e-10, 'should be < 1e-10'

@pytest.mark.parametrize('arg, answ', [[('Hello ', 'World'), 'Hello World'], [('No', 'Space'), 'NoSpace'], [('3rd', ' test'), '3rd test']])
def test_add_string_exercise_3(arg, answ):
    assert calculator.add(arg[0], arg[1]) == answ

@pytest.mark.parametrize('arg', [1, 2, 3])
def test_factorial_exercise_4(arg):
    assert calculator.factorial(arg) == factorial(arg)

@pytest.mark.parametrize('arg', [[0, 0], [1, 5], [6, 13]])
def test_sin_exercise_4(arg):
    assert abs(calculator.sin(arg[0], arg[1]) - sin(arg[0])) < 1e-6

@pytest.mark.parametrize('arg, answ', [[(1, 1), 1], [(4, 2), 2], [(6, 4), 1.5]])
def test_divide_exercise_4(arg, answ):
    assert calculator.devide(arg[0], arg[1]) == answ

@pytest.mark.parametrize('arg, answ', [[(1, 1), 0], [(2, -3), 5], [(6.5, -6), 12.5]])
def test_subtract_exercise_4(arg, answ):
    assert calculator.subtract(arg[0], arg[1]) == answ

@pytest.mark.parametrize('arg, answ', [[(1, 1), 1], [(2, -3), -6], [(1.5, -2), -3]])
def test_multiply_exercise_4(arg, answ):
    assert calculator.multiply(arg[0], arg[1]) == answ

@pytest.mark.parametrize('arg', [['hello', 0], [[1,2,3], 5], [2.3, (3, 5)]])
def test_add_typeError_exercise_5(arg):
    with pytest.raises(TypeError):
        calculator.add(arg[0], arg[1])

@pytest.mark.parametrize('arg', [[2, 0], [0, 0]])
def test_devide_ZeroDivisionError_exercise_5(arg):
    with pytest.raises(ZeroDivisionError):
        calculator.devide(arg[0], arg[1])

