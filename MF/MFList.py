import sys
import requests

from MF.MyMF import My_MFs, MF_List_URL
from MF.MF import MF

class MF_List:
    def __init__(self):
        self.url = MF_List_URL
        self.my_mf = []

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

    def __process_mf_list__(self, mf_list):
        mf_array = mf_list.split('\n')
        my_mf = []
        for mf in mf_array:
            mf_info = mf.split(';')
            if len(mf_info) != 6: continue

            mf_name = mf_info[3]
            if mf_name not in My_MFs: continue

            mf_code, mf_price, mf_date = mf_info[0], mf_info[4], mf_info[5]
            mf_obj = MF(mf_name, mf_code, mf_price, mf_date)
            my_mf.append(mf_obj)
        return my_mf

    def get_my_mf_list(self):
        mf_list = self.__fetch_mf_list__()
        my_mf = self.__process_mf_list__(mf_list)
        return my_mf

    def display_mf_details(self):
        my_mf_list = self.get_my_mf_list()
        for mf in my_mf_list:
            mf.display()
        