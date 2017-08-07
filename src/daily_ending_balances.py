# -*- coding: utf-8 -*-
import sys
import json
from pprint import pprint
from bs4 import BeautifulSoup
import urllib2
import csv
import random

fname = sys.argv[1]
flocation = 'docs/json/'
complete = flocation + fname
with open(complete) as data_file:
    data = json.load(data_file)

def main():
    print "Please be sure you are running the .py file from the same directory where you are working."
    print "*************************************"
    print "This will convert your HTML table to CSV.\n Static means you have the file saved to the computer.\n Dynamic means you have it on the internet. Where you access via URL"
    choose = input("Static [1] or Dynamic[2]")
    if choose == 1:
        determine_buy_or_sell()

def dynamic_converter():
    csv_file = 'http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3_en.php?block_no=47401&view=1'

    html = urllib2.urlopen(csv_file).read()
    soup = BeautifulSoup(html)
    table = soup.select_one("table.data2_s")

    headers = [th.text.encode("utf-8") for th in table.select("tr th")]

    for x in range(1):
        file_number = random.randint(1,4000)

    file_name = "converted_csv_%r.csv" %file_number
    with open(file_name, "w") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])

# TODO the buy and sell methods can be one with a little more logic. It's 12 am I am just  tired. I haven't slept in so long.
def determine_buy_or_sell():
    data_keys = data.keys()

    next_day_sell = []
    next_day_buy = []
    last_four_numbers = []

    labels = {'nextDayBUY': 'BUY', 'nextDaySELL': 'SELL'}

    # json_parse = {
    #     'next_day_sell': [],
    #     'next_day_buy': [],
    #     'last_four_numbers': [],
    #     'labels': {
    #         'nextDayBUY': 'BUY', 'nextDaySELL': 'SELL'
    #     },
    # }
    sell_result = [keys for keys in data_keys if labels['nextDaySELL'] in keys]
    buy_result = [keys for keys in data_keys if labels['nextDayBUY'] in keys]

    for i in sell_result:
        next_day_sell.append(i)
    for i in buy_result:
        next_day_buy.append(i)

    last_four_numbers_edit = [x[-4:] for x in next_day_sell]

    for i in last_four_numbers_edit:
        last_four_numbers.append(i)

    pprint(next_day_sell)
    pprint(next_day_buy)
    # pprint(data[next_day_sell[0]])

def static_converter():
    pass


def ending_balance():
    pass


def inital_ending_balance():
    i = range(2552, 2759)

    for num in i:
        pprint(data["nextDay_BUY_%r" %num])

    pprint(data["nextDay_SELL_2701"])
if __name__ ==  "__main__": main()