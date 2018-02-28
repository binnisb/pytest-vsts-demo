import Demo.Simple
import Demo
import datetime
import sys
import pandas as pd
from io import StringIO

def test_add():
    assert Demo.Simple.add(1, 1) == 2


def test_stock():
    df = Demo.Simple.read_stock("GOOGL", datetime.date(2017, 1, 1), datetime.date(2017, 1, 31))
    assert df.shape == (20, 6)


def test_cli_add(capsys):
    sys.argv = ["file", "2", "3"]
    Demo.__cli_add()
    out, err = capsys.readouterr()
    assert out == "5\n"
    assert err == ""


def test_stock_fetch(capsys):
    sys.argv = ["file", "GOOGL","2017-01-01", "2017-01-31"]
    Demo.__stock_fetch()
    out, err = capsys.readouterr()
    df = pd.read_csv(StringIO(out), index_col=0)
    assert df.shape == (20,6)
