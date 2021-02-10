#!/usr/bin/python
# coding=utf-8
"""
The module of fetching FinMine data
More details in https://finmind.github.io/quickstart/.
"""

import requests

URLLOGIN = "https://api.finmindtrade.com/api/v4/login"


def get_token(max_try=10):
    """Get the token."""

    user_id = input('Enter the user id:')
    user_password = input('Enter the user passward:')
    parload = {"user_id": user_id, "password": user_password}
    for _ in range(max_try):
        data = requests.post(URLLOGIN, data=parload).json()
        if data['msg'] == "success":
            return data['token']
    raise Exception("Faild to get token.")


if __name__ == "__main__":
    token = get_token(max_try=10)
    print(token)
