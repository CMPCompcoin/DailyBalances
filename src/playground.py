#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import with_statement
import sys
import json
from pprint import pprint
from bs4 import BeautifulSoup
import urllib2
import csv
import random
import collections
from collections import defaultdict


fname = sys.argv[1]
flocation = 'docs/json/'
complete = flocation + fname
with open(complete) as data_file:
    data = json.load(data_file)


def main():
    determine_buy_or_sell()
    # example()
    # something_print()


def convert(d):
    if isinstance(d, basestring):
        return str(d)
    elif isinstance(d, collections.Mapping):
        return dict(map(convert, d.iteritems()))
    elif isinstance(d, collections.Iterable):
        return type(d)(map(convert, d))
    else:
        return d

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
    data_converted = convert(data)
    data_keys_converted = convert(data.keys())


    some_dict = {
        'next_day_buy': [],
        'next_day_sell': [],
        'last_four_numbers': [],
        'labels': {
                    'nextDayBUY': 'BUY',
                    'nextDaySELL': 'SELL'
                    }
    }
    next_day_sell = []
    next_day_buy = []
    last_four_numbers = []

    labels = {'nextDayBUY': 'BUY', 'nextDaySELL': 'SELL'}

    # sell_result = [keys for keys in data_keys_converted if labels['nextDaySELL']
    sell_result = [keys for keys in data_keys_converted if some_dict['labels']['nextDaySELL']
                   in keys]
    # buy_result = [keys for keys in data_keys_converted if labels['nextDayBUY']
    buy_result = [keys for keys in data_keys_converted if some_dict['labels']['nextDayBUY']
                  in keys]

    for i in sell_result:
        # next_day_sell.append(i)
        some_dict['next_day_sell'].append(i)
    for i in buy_result:
        # next_day_buy.append(i)
        some_dict['next_day_buy'].append(i)

    last_four_numbers_edit_sell = [x[-4:] for x in some_dict['next_day_sell']]

    for i in last_four_numbers_edit_sell:
        # last_four_numbers.append(i)
        some_dict['last_four_numbers'].append(i)


    # last_four_numbers_edit_sell = (map(str, last_four_numbers_edit_sell))
    # next_day_buy = (map(str, next_day_buy))
    # next_day_sell = (map(str, next_day_sell))

    # for i in next_day_buy:
    #     print i
    #     pprint(data_converted[i])
    # for i in next_day_sell:
    #     print i
    #     pprint(data_converted[i])

    # pprint(some_dict)

    pprint(data_keys_converted.__class__)

    return some_dict

def last_four_numbers(buy_list = [], sell_list = [], *args):
    # last_four_numbers_edit_sell = [x[-4:] for x in next_day_sell]
    # last_four_numbers_edit_buy = [x[-4:] for x in next_day_buy]
    last_four_numbers_edit_sell = [x[-4:] for x in buy_list]
    last_four_numbers_edit_buy = [x[-4:] for x in sell_list]
    return last_four_numbers_edit_sell

def example():
    daily_ending_balances = []

    data_converted = convert(data)
    data_keys_converted = convert(data.keys())

    data_store = (data_converted['nextDay_BUY_2552'])
    profit_loss =  some_var['Profit/Loss']

    std = 50000
    d_eb = standard + profit_loss
    daily_ending_balances.append(d_eb)

    print daily_ending_balances
    # for i in data_converted:
    #     print data_converted[i]
    # pprint(data_keys_converted)

def something_print():
    pprint(determine_buy_or_sell())


if __name__ == '__main__':
    main()

