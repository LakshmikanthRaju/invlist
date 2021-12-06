from datetime import datetime
from threading import Thread

from Stock.MyStock import My_Stock
from Stock.Stock import Stock


class Stock_List:
    def __init__(self):
        self.my_stock = My_Stock
        self.threadPool = []

    def display_details(self):
        print("============== Stock List ===============")
        #print("Stock: " + str(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")))
        for stock_name in self.my_stock:
            stock = Stock(stock_name)
            t = Thread(stock.display())
            self.threadPool.append(t)
            t.start()
        #print("Stock: " + str(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")))

        for t in self.threadPool:
            t.join()
