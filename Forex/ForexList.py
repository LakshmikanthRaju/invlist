
from datetime import datetime
from threading import Thread

from Forex.MyForex import Value_Currency
from Forex.Forex import Forex


class Forex_List:
    def __init__(self):
        self.my_forex = Value_Currency
        self.threadPool = []

    def display_details(self):
        print("============== Forex list ===============")
        #print("Forex: " + str(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")))
        for forex_name in self.my_forex:
            forex = Forex(forex_name)
            t = Thread(forex.display())
            self.threadPool.append(t)
            t.start()
        #print("Forex: " + str(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")))

        for t in self.threadPool:
            t.join()

