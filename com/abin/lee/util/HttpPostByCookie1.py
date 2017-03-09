#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "abin"

import urllib2

cookies = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookies)
f = opener.open('http://172.16.2.145:9100/login/login?username=admin@heika.com&password=d1xqqOOj23Dve6AskgwkDtl8yZqVEKrBmMgpVhWxSl9yqG/ZyTJ6O/XfQMvXWRJvdvshRAxGLYGYzjzVoS9/5pF2/YU4Ptmyx4YPlZSDKtl90T5PpRqj4UCPqpMle2vm8Z5sO2BOi0g1EJR6CAN4cOX/mpl1TbCzcNHTHuHcl6U=')
# f = opener.open('http://172.16.2.145:9100/rrd-verify-web/login/login?username=admin@heika.com&password=d1xqqOOj23Dve6AskgwkDtl8yZqVEKrBmMgpVhWxSl9yqG/ZyTJ6O/XfQMvXWRJvdvshRAxGLYGYzjzVoS9/5pF2/YU4Ptmyx4YPlZSDKtl90T5PpRqj4UCPqpMle2vm8Z5sO2BOi0g1EJR6CAN4cOX/mpl1TbCzcNHTHuHcl6U=')

data = ''
request = urllib2.Request(
        url     = 'http://172.16.2.145:9100/thirdparty/sendReject?applicationId=RRD_407887hb_17',
        headers = {'Content-Type' : 'text/xml'},
        data    = data)
opener.open(request)













