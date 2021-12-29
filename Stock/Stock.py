
import sys
import json
import requests
import time
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

    def __fetch_api(self, url):
        try:
            r = requests.get(url)
            self.obj = json.loads(r.text)
            if "Note" in self.obj:
                time.sleep(60)
            r = requests.get(url)
            return r
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)


    def __fetch_obj__(self):
        url = Stock_URL.format(self.name)
        r = self.__fetch_api(url)

        if r.status_code is not requests.codes.ok:
            print("Error: API Failed - %s" % (str(r.status_code)))
            sys.exit(1)
        self.obj = json.loads(r.text)


    def display(self):
        if "Note" in self.obj:
            print("ERROR: " + self.obj["Note"])
            return
        self.date = self.obj["Meta Data"]["3. Last Refreshed"]
        dates = list(self.obj["Time Series (Daily)"].keys())
        self.price = self.obj["Time Series (Daily)"][dates[0]]["4. close"]
        current_date = datetime.strptime(self.date.split()[0], DATE_FORMAT)

        diff = round(float(self.price) - float(self.obj["Time Series (Daily)"][dates[1]]["4. close"]), 4)
        print(self.name, self.price, self.date)

        dates.pop(0)
        if diff > 0:
            for date in dates:
                if float(self.obj["Time Series (Daily)"][date]["2. high"]) > float(self.price):
                    mark_date = datetime.strptime(date, DATE_FORMAT)
                    days_index = (current_date - mark_date).days
                    print("+{0}. Highest in last {1} days".format(str(diff), days_index))
                    return
            print("+{0}. Highest in all days".format(str(diff)))
        else:
            for date in dates:
                if float(self.obj["Time Series (Daily)"][date]["3. low"]) >= float(self.price):
                    mark_date = datetime.strptime(date, DATE_FORMAT)
                    days_index = (current_date - mark_date).days
                    print("{0}. Lowest in last {1} days".format(str(diff), days_index))
                    return
            print("{0}. Lowest in all days".format(str(diff)))
