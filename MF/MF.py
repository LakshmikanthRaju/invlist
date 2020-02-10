
import sys
import json
import requests
from datetime import datetime

from MF.MyMF import MF_URL

DATE_FORMAT = "%d-%m-%Y"
CURRENT_DATE_FORMAT = "%d-%b-%Y"


class MF:
    def __init__(self, name, code, price, date):
        self.name = name
        self.code = code
        self.price = price
        self.date = date.strip()
        self.obj = None
        self.__fetch_obj__()

    def __fetch_obj__(self):
        url = MF_URL + self.code

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
        print(self.name, self.price, self.date)
        current_date = datetime.strptime(self.date, CURRENT_DATE_FORMAT)
        diff = round(float(self.price)-float(self.obj['data'][1]['nav']), 4)
        price_list = [ float(obj['nav']) for obj in self.obj['data'] ]
        #price_list = price_list[:35]

        if diff > 0:
            days_index = next((x for x, val in enumerate(price_list) if val > float(self.price)), 'all')
            if days_index != 'all':
                mark_date = datetime.strptime(self.obj['data'][days_index]['date'], DATE_FORMAT)
                days_index = (current_date - mark_date).days
            print("+{0}. Highest in last {1} days".format(str(diff), days_index))
        else:
            days_index = next((x for x, val in enumerate(price_list) if val < float(self.price)), 'all')
            if days_index != 'all':
                mark_date = datetime.strptime(self.obj['data'][days_index]['date'], DATE_FORMAT)
                days_index = (current_date - mark_date).days
            print("{0}. Lowest in last {1} days".format(str(diff), days_index))

