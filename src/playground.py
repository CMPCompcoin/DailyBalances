#!/usr/bin/python
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
    determine_buy_or_sell()


def dynamic_converter():
    csv_file = \
        'http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3_en.php?block_no=47401&view=1'

    html = urllib2.urlopen(csv_file).read()
    soup = BeautifulSoup(html)
    table = soup.select_one('table.data2_s')

    headers = [th.text.encode('utf-8') for th in table.select('tr th')]

    for x in range(1):
        file_number = random.randint(1, 4000)

    file_name = 'converted_csv_%r.csv' % file_number
    with open(file_name, 'w') as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows([[td.text.encode('utf-8') for td in
                       row.find_all('td')] for row in
                      table.select('tr + tr')])


def determine_buy_or_sell():
    data_keys = data.keys()


    next_day_sell = []
    next_day_buy = []
    last_four_numbers = []

    labels = {'nextDayBUY': 'BUY', 'nextDaySELL': 'SELL'}

    sell_result = [keys for keys in data_keys if labels['nextDaySELL']
                   in keys]
    buy_result = [keys for keys in data_keys if labels['nextDayBUY']
                  in keys]

    for i in sell_result:
        next_day_sell.append(i)
    for i in buy_result:
        next_day_buy.append(i)

    last_four_numbers_edit = [x[-4:] for x in next_day_sell]

    for i in last_four_numbers_edit:
        last_four_numbers.append(i)

    standard_amount = 50000

    last_four_numbers_edit = (map(str, last_four_numbers_edit))
    next_day_buy = (map(str, next_day_buy))
    next_day_sell = (map(str, next_day_sell))

    for i in data:
        print i




if __name__ == '__main__':
    main()

