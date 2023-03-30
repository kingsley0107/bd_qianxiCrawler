# -*- coding: utf-8 -*-
"""
Created on 27 Mar 2:30 PM

@Author: kingsley leung
@Email: kingsleyl0107@gmail.com

_description_: startup-script
"""

import os
PROXY_API_HOST = ""


scale = 'city'
city = '广州市'
direction = 'move_out'
date = '20230325'
FILE_ROOT_PATH = r'./data'


if not os.path.exists(FILE_ROOT_PATH):
    os.makedirs(FILE_ROOT_PATH)

# create a folder if not exist
if not os.path.exists(rf'{FILE_ROOT_PATH}/城市当日迁徙占比'):
    os.makedirs(rf'{FILE_ROOT_PATH}/城市当日迁徙占比/move_in')
    os.makedirs(rf'{FILE_ROOT_PATH}/城市当日迁徙占比/move_out')

if not os.path.exists(rf'{FILE_ROOT_PATH}/城市历史迁徙指数'):
    os.makedirs(rf'{FILE_ROOT_PATH}/城市历史迁徙指数/move_in')
    os.makedirs(rf'{FILE_ROOT_PATH}/城市历史迁徙指数/move_out')

if not os.path.exists(rf'{FILE_ROOT_PATH}/城市当日迁徙指数'):
    os.makedirs(rf'{FILE_ROOT_PATH}/城市当日迁徙指数/move_in')
    os.makedirs(rf'{FILE_ROOT_PATH}/城市当日迁徙指数/move_out')

if not os.path.exists(rf'{FILE_ROOT_PATH}/城内出行强度指数'):
    os.makedirs(rf'{FILE_ROOT_PATH}/城内出行强度指数')


if not os.path.exists(rf'{FILE_ROOT_PATH}/城市就餐休闲出行强度指数'):
    os.makedirs(rf'{FILE_ROOT_PATH}/城市就餐休闲出行强度指数')


if not os.path.exists(rf'{FILE_ROOT_PATH}/城市上班出行强度指数'):
    os.makedirs(rf'{FILE_ROOT_PATH}/城市上班出行强度指数')
