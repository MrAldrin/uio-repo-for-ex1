import calculator

def test_add_integer_exercise_1():
    a = 1
    b = 2
    assert calculator.add(a,b) == 3, 'should be 3'

def test_add_float_exercise_2():
    a = .1
    b = .2
    assert abs(calculator.add(a,b) - .3) < 1e-6, 'should be < 1e-6'