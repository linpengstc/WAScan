#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/m4ll0k/Wascan
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from plugins.audit.xst import *
from plugins.audit.apache import *
from plugins.audit.dav import *
from plugins.audit.phpinfo import *
from plugins.audit.robots import *
from lib.utils.printer import *
from lib.utils.exception import *


def Audit(kwargs, url, data):
    try:
        info("Starting audit module...")
        xst(kwargs, url, data).run()
        apache(kwargs, url, data).run()
        # dav(kwargs, url, data).run()
        phpinfo(kwargs, url, data).run()
        robots(kwargs, url, data).run()
        null()
    except HTTPConnectionException,e:
        warn(str(e))
    except ReadTimeoutException,e:
        warn(str(e))