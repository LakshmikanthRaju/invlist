import sys
import requests
from datetime import datetime
from threading import Thread

from MF.MyMF import Watch_Equity, My_Debt, My_ELSS, My_Equity, MF_List_URL
from MF.MF import MF

class MF_List:
    def __init__(self):
        self.url = MF_List_URL
        self.my_mf = []
        self.mf_list = self.__fetch_mf_list__()

    def __fetch_mf_list__(self):
        try:
            r = requests.get(self.url)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        if r.status_code is not requests.codes.ok:
            print("Error: API Failed - %s" % (str(r.status_code)))
            sys.exit(1)
        else:
            return r.text

    def __process_mf_list__(self, my_mfs):
        mf_array = self.mf_list.split('\n')
        my_mf = []
        for mf in mf_array:
            mf_info = mf.split(';')
            if len(mf_info) != 6: continue

            mf_name = mf_info[3]
            if mf_name not in my_mfs: continue

            mf_code, mf_price, mf_date = mf_info[0], mf_info[4], mf_info[5]
            mf_obj = MF(mf_name, mf_code, mf_price, mf_date)
            my_mf.append(mf_obj)
        return my_mf

    def get_mf_list(self, mfs_list):
        my_mf = self.__process_mf_list__(mfs_list)
        return my_mf

    def process_mf_list(self, my_mf_list):
        threadPool = []
        for mf in my_mf_list:
            t = Thread(mf.display())
            threadPool.append(t)
            t.start()
        for t in threadPool:
            t.join()

    def display_details(self):
        # print("MF: " + str(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")))
        #my_mf_list = self.get_my_mf_list()
        #print("============== Debt List ================")
        #self.process_mf_list(self.get_mf_list(My_Debt))
        #print("MF: " + str(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")))

        print("============== ELSS List ================")
        self.process_mf_list(self.get_mf_list(My_ELSS))
        print("============= Equity List ===============")
        self.process_mf_list(self.get_mf_list(My_Equity))
        #print("============== Watch List ===============")
        #self.process_mf_list(self.get_mf_list(Watch_Equity))
