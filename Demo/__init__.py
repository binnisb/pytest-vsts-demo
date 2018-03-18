import datetime
from docopt import docopt
from .Simple import *

def __cli_add():
    """
    Usage:
        cli_add <x> <y>
    """
    args = docopt(__cli_add.__doc__)
    
    x,y = int(args["<x>"]), int(args["<y>"])
    res = add(x, y)
    print(res)
    return 0
