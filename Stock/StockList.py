import sys
import requests

from Stock.MyStock import My_Stock
from Stock.Stock import Stock


class Stock_List:
    def __init__(self):
        self.my_stock = My_Stock

    def display_stock_details(self):
        for stock_name in self.my_stock:
            stock = Stock(stock_name)
            stock.display()
