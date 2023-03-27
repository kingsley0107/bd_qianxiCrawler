# -*- coding: utf-8 -*-
"""
Created on 27 Mar 2:30 PM

@Author: kingsley leung
@Email: kingsleyl0107@gmail.com

_description_: startup-script
"""

import requests
from settings import PROXY_API_HOST


def gen_new_ip():
    ip = requests.get(PROXY_API_HOST).json()
    print (f"Refresh Proxy:{ip}")
    return ip


if __name__ == '__main__':
    print(gen_new_ip())
