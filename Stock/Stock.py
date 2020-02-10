
import sys
import json
import requests
from datetime import datetime

from Stock.MyStock import Stock_URL

DATE_FORMAT = "%Y-%m-%d"


class Stock:
    def __init__(self, name):
        self.name = name
        self.price = ""
        self.date = ""
        self.obj = None
        self.__fetch_obj__()

    def __fetch_obj__(self):
        url = Stock_URL.format(self.name)

        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        if r.status_code is not requests.codes.ok:
            print("Error: API Failed - %s" % (str(r.status_code)))
            sys.exit(1)
        else:
            self.obj = json.loads(r.text)
            #print(self.obj['meta']['scheme_name'])

    def display(self):
        self.date = self.obj["Meta Data"]["3. Last Refreshed"]
        dates = list(self.obj["Time Series (Daily)"].keys())
        self.price = self.obj["Time Series (Daily)"][dates[0]]["4. close"]

        diff = float(self.price) - float(self.obj["Time Series (Daily)"][dates[1]]["4. close"])
        print(self.name, self.price, self.date, diff)

