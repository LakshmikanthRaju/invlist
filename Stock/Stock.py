
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
