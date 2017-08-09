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


fname = sys.argv[1]
flocation = 'docs/json/'
complete = flocation + fname
with open(complete) as data_file:
    data = json.load(data_file)


def main():
    print 'MAKE SURE YOU READ THE README.MD'
    print 'Please be sure you are running the .py file from the same directory where you are working.'
    print '*************************************'
    print '''This will convert your HTML table to CSV.
 Static means you have the file saved to the computer.
 Dynamic means you have it on the Internet. Where you access via URL'''
    choose = input('Static [1] or Dynamic [2]: ')
    if choose == 1:
       ending_balances()
        # play()


def set_up():
    daily_data = {
        'next_day_buy': [],
        'next_day_sell': [],
        'num_id_sell': [],
        'num_id_buy': [],
        'labels': {'nextDayBUY': 'BUY','nextDaySELL': 'SELL'},
        'data': [],
        'keys': []
    }

    return daily_data


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


def uni_str():
    daily_data = set_up()

    daily_data['data'] = convert(data)
    daily_data['keys'] = convert(data.keys())

    return daily_data


def buy_or_sell():
    daily_data = uni_str()
    sell_result = [keys for keys in daily_data['keys'] if daily_data['labels']['nextDaySELL']
                   in keys]
    buy_result = [keys for keys in daily_data['keys'] if daily_data['labels']['nextDayBUY']
                  in keys]

    for i in sell_result:
        daily_data['next_day_sell'].append(i)
    for i in buy_result:
        daily_data['next_day_buy'].append(i)


    return daily_data


def get_num_id():
    daily_data = buy_or_sell()

    num_id_edit_sell = [x[-4:] for x in daily_data['next_day_sell']]
    num_id_edit_buy = [x[-4:] for x in daily_data['next_day_buy']]
    for i in num_id_edit_sell:
        daily_data['num_id_sell'].append(i)
    for i in num_id_edit_buy:
        daily_data['num_id_buy'].append(i)

    daily_data['num_id_buy'] = sorted(daily_data['num_id_buy'])
    daily_data['num_id_sell'] = sorted(daily_data['num_id_sell'])
    daily_data['keys'] = sorted(daily_data['keys'])
    return daily_data


def ending_balance():
    pass


def play():
    daily_data = get_num_id()
    something = daily_data['keys'][0]
    bryan = (daily_data['data'][something])
    pprint(something)
    pprint(bryan)
    pprint(bryan['Profit/Loss'])


def initial_ending_balance():
    daily_ending_balances = {
        'initial': [],
        'others': []
    }
    daily_data = get_num_id()
    initial_amount = 50000
    first_key = daily_data['keys'][0]
    f_attributes = (daily_data['data'][first_key])
    p_l = f_attributes['Profit/Loss']
    daily_ending_balances['initial'].append(initial_amount + p_l)
    return daily_ending_balances


def ending_balances():
    daily_ending_balances = initial_ending_balance()


if __name__ == '__main__':
    main()