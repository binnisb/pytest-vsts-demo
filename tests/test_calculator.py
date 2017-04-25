import Calc.Calculator
import Calc
import datetime

def test_add():
    assert Calc.Calculator.add(1,1) == 2
def test_pass():
    assert True == True

def test_failNot():
    assert False == False

def test_stock():
    df = Calc.Calculator.read_stock("GOOGL", datetime.date(2017,1,1), datetime.date(2017,1,31))
    assert df.shape == (20,6)

def test_cli_add():
    a = Calc.__cli_add()