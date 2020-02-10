import sys
import requests

from Forex.MyForex import Value_Currency
from Forex.Forex import Forex


class Forex_List:
    def __init__(self):
        self.my_forex = Value_Currency

    def display_forex_details(self):
        for forex_name in self.my_forex:
            forex = Forex(forex_name)
            forex.display()
