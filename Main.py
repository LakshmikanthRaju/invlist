
import time
from threading import Thread

from MF.MFList import MF_List
from Stock.StockList import Stock_List
from Forex.ForexList import Forex_List


def add_to_thread_pool(thread_pool, inv_obj):
    t = Thread(inv_obj.display_details())
    thread_pool.append(t)
    t.start()

if __name__ == '__main__':
    #mf_list_obj = MF_List()
    thread_pool = []
    start = time.time()

    add_to_thread_pool(thread_pool, MF_List())
    add_to_thread_pool(thread_pool, Stock_List())
    add_to_thread_pool(thread_pool, Forex_List())

    for t in thread_pool:
        t.join()

    print("Time take (seconds): {}".format(round(time.time()-start, 2)))


#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=VMW&apikey=50TGXNDTSOUF0HH6
#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=VMW&outputsize=full&apikey=50TGXNDTSOUF0HH6

#https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=USD&to_symbol=INR&apikey=50TGXNDTSOUF0HH6
#https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=QAR&to_symbol=INR&apikey=50TGXNDTSOUF0HH6