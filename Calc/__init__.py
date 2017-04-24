"""
Usage:
    calc_add <x> <y>
"""


def __cli_add():
    from docopt import docopt
    from .Calculator import add
    args = docopt(__doc__)
    x,y = int(args["<x>"]), int(args["<y>"])
    res = add(x, y)
    print(res)
    return 0
