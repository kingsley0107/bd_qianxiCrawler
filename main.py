# -*- coding: utf-8 -*-
"""
Created on 27 Mar 2:30 PM

@Author: kingsley leung
@Email: kingsleyl0107@gmail.com

_description_: startup-script
"""

from spider.qianxi import *
from settings import *

def crawl():
    city_date_curve_rank = crawl_cityrank(city, scale, direction, date)
    city_history_curve = crawl_historycurve(city, scale, direction)
    city_date_curve_index = calculate_index(city_history_curve, city_date_curve_rank, date)

    city_date_curve_rank.to_csv(rf'./data/城市当日迁徙占比/{direction}/{city}_{date}.csv', encoding='utf-8_sig')
    city_history_curve.to_csv(rf'./data/城市历史迁徙指数/{direction}/{city}.csv', encoding='utf-8_sig')
    city_date_curve_index.to_csv(rf'./data/城市当日迁徙指数/{direction}/{city}.csv', encoding='utf-8_sig')

if __name__ == '__main__':
    crawl()







