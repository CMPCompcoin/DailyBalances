import sys
import json
from pprint import pprint
from bs4 import BeautifulSoup
import urllib2
import csv
import random

with open('docs/html_json_converted.json') as data_file:
    data = json.load(data_file)

def main():
    example()


def example():
    data_keys = data.keys()

    next_day_sell = []
    next_day_buy = []

    labels = {'nextDayBUY': 'BUY', 'nextDaySELL': 'SELL'}

    sell_result = [keys for keys in data_keys if labels['nextDaySELL'] in keys]
    buy_result = [keys for keys in data_keys if labels['nextDayBUY'] in keys]

    for i in sell_result:
        next_day_sell.append(i)

    for i in buy_result:
        next_day_buy.append(i)

    # pprint(next_day_sell[-4:])

    last_four_numbers = [x[-4:] for x in next_day_sell]
    pprint(last_four_numbers)
    # pprint(data[next_day_sell[0]])

if __name__ == "__main__":
    main()
