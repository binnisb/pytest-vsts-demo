import Demo.Simple
import Demo
import datetime
import sys
from io import StringIO

def test_add():
    assert Demo.Simple.add(1, 1) == 2


def test_cli_add(capsys):
    sys.argv = ["file", "2", "3"]
    Demo.__cli_add()
    out, err = capsys.readouterr()
    assert out == "5\n"
    assert err == ""
