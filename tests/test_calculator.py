import Calc.Calculator

def test_add():
    assert Calc.Calculator.add(1,1) == 2
def test_pass():
    assert True == True
def test_fail():
    assert True == False
