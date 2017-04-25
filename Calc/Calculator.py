import pandas_datareader.data as web
import datetime    


def add(x,y):
    return x+y

def read_stock(stock, start_date, end_date):
    df = web.DataReader(stock,'yahoo', start_date, end_date)
    return df