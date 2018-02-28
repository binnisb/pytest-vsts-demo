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

def __stock_fetch():
    """
    Usage:
        stock_fetch <stock> <start_date> <end_date>
    """
    parse_date = lambda date_str: datetime.datetime.strptime(date_str,"%Y-%m-%d").date()
    args = docopt(__stock_fetch.__doc__)
    stock, start_date, end_date = args["<stock>"], parse_date(args["<start_date>"]), parse_date(args["<end_date>"])

    df = read_stock(stock,start_date,end_date)
    df.to_csv("./{stock}-{start}-{end}.csv".format(stock=stock,start=start_date,end=end_date))
    print(df.to_csv())
