# -*- coding: utf-8 -*-
"""
Created on 27 Mar 2:30 PM

@Author: kingsley leung
@Email: kingsleyl0107@gmail.com

_description_: startup-script
"""

import requests
import pandas as pd
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
# from middlewares.proxy import gen_new_ip
import re
from cities.ChineseAdminiDivisionsDict import get_city_code, get_province_code
import time


def crawl_body(url, params, type='default'):
    pattern = r"^cb\((.*)\)"
    retry_times = 5
    retry_delay = 1

    session = requests.Session()
    retry = Retry(total=retry_times, backoff_factor=retry_delay)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    response = session.get(url, params=params)
    if response.status_code == 200:
        data = json.loads(re.search(pattern, response.text.strip()).group(1))
        if type == 'default':
            return data['data']['list']
        elif type == 'work':
            return data['data']['list']['work']
        elif type == 'entertainment':
            return data['data']['list']['entertainment']
    else:
        print("request failed...")


def crawl_cityrank(city, scale, direction, date):
    base_url = "https://huiyan.baidu.com/migration/cityrank.jsonp"
    if scale == 'province':
        id = get_province_code(city)
    elif scale == 'city':
        id = get_city_code(city)
    params = {"dt": scale, "id": id, "type": direction, 'date': date}
    data = crawl_body(base_url, params)
    result = pd.DataFrame.from_dict(data).rename(
        columns={'value': 'percentage'})
    return result


def crawl_historycurve(city, scale, direction):
    base_url = "https://huiyan.baidu.com/migration/historycurve.jsonp"
    if scale == 'province':
        id = get_province_code(city)
    elif scale == 'city':
        id = get_city_code(city)
    params = {"dt": scale, "id": id, "type": direction}
    data = crawl_body(base_url, params)
    result = pd.DataFrame.from_dict(data,
                                    orient='index',
                                    columns=[f'{direction}_values'
                                             ]).sort_index()
    return result


def calculate_index(history_curve, city_rank, date):
    comparable_curve_index = history_curve[history_curve.columns[0]].loc[date]
    curve_index = city_rank.copy()
    curve_index['迁徙指数'] = curve_index['percentage'] * comparable_curve_index
    return curve_index.drop(['percentage'], axis=1)


def crawl_internalflow(city):
    base_url = "https://huiyan.baidu.com/migration/internalflowhistory.jsonp"
    params = {
        "dt": "city",
        "id": get_city_code(city),
        "date": time.strftime("%Y%m%d", time.localtime())
    }
    data = crawl_body(base_url, params)
    result = pd.DataFrame.from_dict(data,
                                    orient='index',
                                    columns=[f'{city}_internalflow_values'
                                             ]).sort_index()
    return result


def crawl_work(city):
    base_url = "https://huiyan.baidu.com/migration/odsemantic.jsonp"
    params = {
        "dt": "city",
        "id": get_city_code(city),
        'date': time.strftime("%Y%m%d", time.localtime())
    }
    data = crawl_body(base_url, params, type='work')
    result = pd.DataFrame.from_dict(data, orient='index',
                                    columns=[f'OD_work']).sort_index()
    return result


def crawl_entertainment(city):
    base_url = "https://huiyan.baidu.com/migration/odsemantic.jsonp"
    params = {
        "dt": "city",
        "id": get_city_code(city),
        'date': time.strftime("%Y%m%d", time.localtime())
    }
    data = crawl_body(base_url, params, type='entertainment')
    result = pd.DataFrame.from_dict(data,
                                    orient='index',
                                    columns=[f'OD_entertainment'
                                             ]).sort_index()
    return result


if __name__ == '__main__':
    pass
