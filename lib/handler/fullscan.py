#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/m4ll0k/Wascan
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt


from lib.utils.printer import *
from lib.handler.audit import *
from lib.handler.brute import *
from lib.handler.attacks import *
from lib.handler.disclosure import *
from lib.handler.fingerprint import *

def FullScan(kwargs,url,data):
    # 如果是非post格式，并且get请求中不带参数
    # if '?' in url and 'data' not in kargs:
    Attacks(kwargs,url,data)
    Disclosure(kwargs,url,data)
