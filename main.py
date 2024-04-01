# -*- coding: utf-8 -*-
"""
Created on 27 Mar 2:30 PM

@Author: kingsley leung
@Email: kingsleyl0107@gmail.com

_description_: startup-script
"""

from spider.qianxi import *
from settings import *
import shutil


def crawl(scale):
    if scale == 'city':
        try:
            city_date_curve_rank = crawl_cityrank(city, scale, direction, date)
            city_history_curve = crawl_historycurve(city, scale, direction)
            city_date_curve_index = calculate_index(city_history_curve,
                                                    city_date_curve_rank, date)
            city_internal_flow = crawl_internalflow(city)
            city_work_index = crawl_work(city)
            city_entertainment_index = crawl_entertainment(city)

            city_date_curve_rank.to_csv(
                rf'{FILE_ROOT_PATH}/城市当日迁徙占比/{direction}/{city}_{date}.csv',
                encoding='utf-8_sig')
            city_history_curve.to_csv(
                rf'{FILE_ROOT_PATH}/城市历史迁徙指数/{direction}/{city}.csv',
                encoding='utf-8_sig')
            city_date_curve_index.to_csv(
                rf'{FILE_ROOT_PATH}/城市当日迁徙指数/{direction}/{city}.csv',
                encoding='utf-8_sig')
            city_internal_flow.to_csv(
                rf'{FILE_ROOT_PATH}/城内出行强度指数//{city}_{time.strftime("%Y%m%d", time.localtime())}.csv',
                encoding='utf-8_sig')

            city_work_index.to_csv(
                rf'{FILE_ROOT_PATH}/城市上班出行强度指数//{city}_{time.strftime("%Y%m%d", time.localtime())}.csv',
                encoding='utf-8_sig')

            city_entertainment_index.to_csv(
                rf'{FILE_ROOT_PATH}/城市就餐休闲出行强度指数//{city}_{time.strftime("%Y%m%d", time.localtime())}.csv',
                encoding='utf-8_sig')
        except:
            # delete a root folder
            if os.path.exists(FILE_ROOT_PATH):
                shutil.rmtree(FILE_ROOT_PATH)

            raise ValueError("crawl failed")
    elif scale == 'province':
        city_date_curve_rank = crawl_cityrank(city, scale, direction, date)
        city_history_curve = crawl_historycurve(city, scale, direction)
        city_date_curve_index = calculate_index(city_history_curve,
                                                city_date_curve_rank, date)


if __name__ == '__main__':
    crawl(scale)
