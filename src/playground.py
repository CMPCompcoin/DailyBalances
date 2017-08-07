import json
from pprint import pprint
from  __builtin__ import any as b_any


def main():
    example()

def example():
    data = {
        "nextDay_BUY_2552": {
            "Amount": 0.02,
            "Direction": "BUY",
            "Open price": 1.47145,
            "Close price": 1.47221,
            "Profit/Loss": 15.2,
            "Profit/Loss in pips": 7.6,
            "Open date": "2008-01-03 04:31:01",
            "Close date": "2008-01-03 16:11:08",
            "Comment": ""
        },
        "nextDay_SELL_25652": {
            "Amount": 0.02,
            "Direction": "BUY",
            "Open price": 1.47145,
            "Close price": 1.47221,
            "Profit/Loss": 15.2,
            "Profit/Loss in pips": 7.6,
            "Open date": "2008-01-03 04:31:01",
            "Close date": "2008-01-03 16:11:08",
            "Comment": ""
        },
        "nextDay_SELL_26552": {
            "Amount": 0.02,
            "Direction": "BUY",
            "Open price": 1.47145,
            "Close price": 1.47221,
            "Profit/Loss": 15.2,
            "Profit/Loss in pips": 7.6,
            "Open date": "2008-01-03 04:31:01",
            "Close date": "2008-01-03 16:11:08",
            "Comment": ""
        },
        "nextDay_SELL_25592": {
            "Amount": 0.02,
            "Direction": "BUY",
            "Open price": 1.47145,
            "Close price": 1.47221,
            "Profit/Loss": 15.2,
            "Profit/Loss in pips": 7.6,
            "Open date": "2008-01-03 04:31:01",
            "Close date": "2008-01-03 16:11:08",
            "Comment": ""
        }
    }
    data_keys = data.keys()
    search = "SELL"
    result = [keys for keys in data_keys if search in keys]

    nextDaySELL = []

    for i in result:
        nextDaySELL.append(i)
    # print(result.__class__)

    print nextDaySELL.__class__
    print nextDaySELL
if __name__ == "__main__": main()