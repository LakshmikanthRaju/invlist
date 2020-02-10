
import sys
import json
import requests
from datetime import datetime

from Forex.MyForex import INR_Currency, Forex_URL


DATE_FORMAT = "%d-%m-%Y"
CURRENT_DATE_FORMAT = "%d-%b-%Y"


class Forex:
    def __init__(self, name):
        self.name = name
        self.price = ""
        self.date = ""
        self.obj = None
        self.__fetch_obj__()

    def __fetch_obj__(self):
        url = Forex_URL.format(self.name, INR_Currency)

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
        self.date = self.obj["Meta Data"]["5. Last Refreshed"]
        dates = list(self.obj["Time Series FX (Daily)"].keys())
        self.price = self.obj["Time Series FX (Daily)"][dates[0]]["4. close"]

        diff = float(self.price) - float(self.obj["Time Series FX (Daily)"][dates[1]]["4. close"])
        print(self.name, self.price, self.date, diff)

