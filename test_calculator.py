import calculator
from math import factorial, sin

def test_add_integer_exercise_1():
    a = 1
    b = 2
    assert calculator.add(a,b) == 3, 'should equal 3'

def test_add_float_exercise_2():
    a = .1
    b = .2
    assert abs(calculator.add(a,b) - .3) < 1e-10, 'should be < 1e-10'

def test_add_string_exercise_3():
    a = 'Hello '
    b = 'World'
    assert calculator.add(a,b) == 'Hello World', 'should equal "Hello World"'

def test_factorial_exercise_4():
    n = 3
    assert calculator.factorial(n) == factorial(n), 'should equal factorial(n) (n = 3 -> 6)'

def test_sin_exercise_4():
    x = 1
    N = 5
    # print (f'calculator value: {calculator.sin(x,N)}')        #Needed to see this in action during testing
    # print (f'math value: {sin(x)}')
    assert abs(calculator.sin(x,N) - sin(x)) < 1e-8, 'should be < 1e-8'

def test_divide_exercise_4():
    a = 4
    b = 2
    assert calculator.devide(a, b) == 2, 'should equal 2'
    a = .1
    b = .3
    # print(calculator.devide(c, d))                        #Needed to see this in action during testing
    # print(abs(calculator.devide(c, d) - 1/3))
    assert abs(calculator.devide(a, b) - 1/3) < 1e10, 'should be < 1e10'


def test_subtract_exercise_4():
    assert calculator.subtract(5, 3) == 2 , 'should equal 2'
    assert abs(calculator.subtract(1, 2/3) - 1/3) < 1e10 , 'should equal < 1e10'


def test_multiply_exercise_4():
    assert calculator.multiply(2,3) == 6 , 'should equal 6'

if __name__ == "__main__":
    test_sin_exercise_4()
    test_divide_exercise_4()
