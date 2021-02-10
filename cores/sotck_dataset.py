#!/usr/bin/python
# coding=utf-8
"""
The modules of collecting Taiwan stock dataset
More details in https://finmind.github.io/tutor/TaiwanMarket/DataList/.
"""
import pandas as pd
import requests

URLSTOCK = "https://api.finmindtrade.com/api/v4/data"


class StockTWDatset():
    """ The methods are used to fetch Taiwan stock dataset."""
    def __init__(self, token, **cfgs):
        if not isinstance(token, str):
            raise "token is string type"
        self.__token = token

    def stock_price(self, stock_id, start_date, end_date):
        """Fetch the stock price."""
        parameter = {
            "dataset": "TaiwanStockPrice",
            "data_id": stock_id,
            "start_date": start_date,
            "end_date": end_date,
            "token": self.__token
        }
        data = requests.get(URLSTOCK, params=parameter).json()
        if data["msg"] == "success":
            data = pd.DataFrame(data["data"])
            return data
        raise "Fail to fetch the TaiwanStockPrice"
