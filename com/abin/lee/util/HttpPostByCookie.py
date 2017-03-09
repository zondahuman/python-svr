#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "abin"
### pip install requests ##
import requests

r1 = requests.get('http://172.16.2.145:9100/login/login?username=admin@heika.com&password=d1xqqOOj23Dve6AskgwkDtl8yZqVEKrBmMgpVhWxSl9yqG/ZyTJ6O/XfQMvXWRJvdvshRAxGLYGYzjzVoS9/5pF2/YU4Ptmyx4YPlZSDKtl90T5PpRqj4UCPqpMle2vm8Z5sO2BOi0g1EJR6CAN4cOX/mpl1TbCzcNHTHuHcl6U=')

# r2 = requests.post('http://172.16.2.145:9100/thirdparty/sendReject?applicationId=RRD_407887hb_17',cookies=r1.cookies)


r2 = requests.post('http://172.16.2.145:9100/thirdparty/sendReject',data={'applicationId':'RRD_407887hb_17'},cookies=r1.cookies)














