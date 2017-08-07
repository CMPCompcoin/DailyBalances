import sys
import json
from pprint import pprint
from bs4 import BeautifulSoup
import urllib2
import csv
import random

def main():
    print "Please be sure you are running the .py file from the same directory where you are working."
    print "*************************************"
    print "This will convert your HTML table to CSV.\n Static means you have the file saved to the computer.\n Dynamic means you have it on the internet. Where you access via URL"
    choose = input("Static [1] or Dynamic[2]")
    if choose == 1:
        # inital_ending_balance()
        determine_buy_or_sell()

def dynamic_converter():
    csv_file = 'http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3_en.php?block_no=47401&view=1'
    # csv_file = 'file:///C:/Users/bryan/Documents/Developer/Python/Compcoin/parse/example_one.html'
    # something = sys.argv[1]
    # csv_file = something
    html = urllib2.urlopen(csv_file).read()
    soup = BeautifulSoup(html)
    table = soup.select_one("table.data2_s")
    # python3 just use th.text
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
    with open('html_json_converted.json') as data_file:
        data = json.load(data_file)

    data_keys = data.keys()
    sub_str_sell = "SELL"
    sub_str_buy = "BUY"

    sell_result = [keys for keys in data_keys if sub_str_sell in keys]
    buy_result = [keys for keys in data_keys if sub_str_buy in keys]

    nextDaySELL = []
    nextDAYBUY = []

    for i in sell_result:
        nextDaySELL.append(i)

    for i in buy_result:
        nextDAYBUY.append(i)

    pprint (nextDaySELL.__class__)
    pprint (nextDaySELL)
    pprint (nextDAYBUY.__class__)
    pprint (nextDAYBUY)

def static_converter():
    pass


def ending_balance():
    pass


def inital_ending_balance():
    with open('html_json_converted.json') as data_file:
        data = json.load(data_file)
    i = range(2552, 2759)

    for num in i:
        pprint(data["nextDay_BUY_%r" %num])

    pprint(data["nextDay_SELL_2701"])
if __name__ ==  "__main__": main()