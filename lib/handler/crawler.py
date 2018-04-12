#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/m4ll0k/Wascan
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from lib.utils.printer import info
from lib.request.crawler import SCrawler
from lib.utils.exception import *
from lib.utils.printer import *

class Crawler:
    """ cralwer """
    def run(self, kwargs, url, data):
        links = []
        try:
            info("Starting crawler...")
            links.append(url)
            # for link in links:
            for k in SCrawler(kwargs, url, data).run():
                if k not in links:
                    # 判断link是否重复，以及是否和扫描url是否相同
                    links.append(k)
            return links
        except HTTPConnectionException,e:
            warn(str(e))
        except ReadTimeoutException,e:
            warn(str(e))
        return []