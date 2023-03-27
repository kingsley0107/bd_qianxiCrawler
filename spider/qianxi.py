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
from cities.ChineseAdminiDivisionsDict import get_city_code,get_province_code


def crawl_body(url,params):
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
        return data['data']['list']
    else:
        print("request failed...")
def crawl_cityrank(city,scale,direction,date):
    base_url = "https://huiyan.baidu.com/migration/cityrank.jsonp"
    params = {
        "dt": scale,
        "id": get_city_code(city),
        "type": direction,
        'date':date
    }
    data = crawl_body(base_url,params,city,direction,'city')
    result = pd.DataFrame.from_dict(data).rename(columns = {'value':'percentage'})
    return result

def crawl_historycurve(city,scale,direction):
    base_url = "https://huiyan.baidu.com/migration/historycurve.jsonp"
    params = {
        "dt": scale,
        "id": get_city_code(city),
        "type": direction
    }
    data = crawl_body(base_url,params,city,direction,'city')
    result = pd.DataFrame.from_dict(data, orient='index', columns=[f'{direction}_values'])
    return result

def calculate_index(history_curve,city_rank,date):
    comparable_curve_index = history_curve[history_curve.columns[0]].loc[date]
    curve_index = city_rank.copy()
    curve_index['迁徙指数'] = curve_index['percentage'] * comparable_curve_index
    return curve_index.drop(['percentage'],axis = 1)